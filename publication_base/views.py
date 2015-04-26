# -*- coding: utf-8 -

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import activate
# from django.http import HttpResponse
from model.models import Rubric, Article, Issue, Edition, Edition_Locale, \
    Article_Locale, Author, Author_Locale, Article_Authors
import model.models as models
import model.data as data
# from django.contrib import auth
from django.conf import settings
# from django.views.static import serve
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.http import is_safe_url
# from django.shortcuts import resolve_url
from django.contrib.auth import REDIRECT_FIELD_NAME, \
    login as auth_login, logout as auth_logout
from django.contrib.sites.models import get_current_site
from django.template.response import TemplateResponse
from publ_forms import EditorAuthenticationForm, ALLOWED_ED_PREFIX, NewIssueForm, \
     PublMsg, ArticleForm
# from django.core.context_processors import request
from django.conf import settings
import os
from publication_base import publ_forms
from django.db.models import Q
import shutil
import math
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import messages
from thumbnail import create_pdf_thumbnail, create_pdf_thumbnail2
# from django.conf import settings
# import os.path
from django.template import Template
from collections import OrderedDict


lng_code_ukr = 'uk'
lng_code_en = 'en'
def_lng = lng_code_ukr  # default laguage
def_edition = data.edt_phys_math  # models.phys_math

ARTICLE_CODE_PREFIX = u'artcl_'

class PublViewError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)


def view_wrapper(view):
    def new_view(request, *args, **kwargs):
        cur_lng_code = kwargs["cur_lng_code"]
        if not cur_lng_code:
            cur_lng_code = lng_code_en
        activate(cur_lng_code)
        # edition_list = Edition.objects.all_locale(cur_lng_code)

        kwargs["cur_lng_code"] = cur_lng_code
        # kwargs["edition_list"] = edition_list
        return view(request, *args, **kwargs)
    return new_view

def edition_view_wrapper(view):
    def new_view(request, *args, **kwargs):
        cur_lng_code = kwargs["cur_lng_code"]
        if not cur_lng_code:
            cur_lng_code = lng_code_en
        activate(cur_lng_code)
        # edition_list = Edition.objects.all_locale(cur_lng_code)
        kwargs["cur_lng_code"] = cur_lng_code
        edition_alias = kwargs["edition"]
        edition_locale_obj = Edition_Locale.objects.get(lang_code = cur_lng_code,
                                            edition__edition_alias__iexact = edition_alias)
        edition_name = edition_locale_obj.edition_name
        kwargs["edition_name"] = edition_name
        return view(request, *args, **kwargs)
    return new_view

def editor_wrapper(view):
    def new_view(request, *args, **kwargs):
        cur_lng = get_lang_code()  # lng_code_ukr
        activate(cur_lng)
        if request.user.is_authenticated():
            # permissions_list = request.user.get_all_permissions()
            # allowed_editions = [item[len(ALLOWED_ED_PREFIX):] for item in permissions_list if item.startswith(ALLOWED_ED_PREFIX) ]
            user_id = request.user.id
            allowed_editions = Edition.objects.user_editions(cur_lng, user_id)
            cur_edition_alias = kwargs['edition']
            cur_edition = [item for item in allowed_editions if item.edition_alias == cur_edition_alias]
            if not cur_edition:
                return HttpResponseRedirect('/login/')

#             if len(editions_allowed) == 1:
#                 edit_permission = editions_allowed[0]
#                 edition_alias = edit_permission[len(ALLOWED_ED_PREFIX):]
#                 if edition_alias != kwargs['edition']:
#                     return HttpResponseRedirect('/login/')
#             if len(editions_allowed) >= 1:
#                 cur_edition = kwargs['edition']
#
#                 edit_permission = editions_allowed[0]
#                 edition_alias = edit_permission[len(ALLOWED_ED_PREFIX):]
#                 if edition_alias != kwargs['edition']:
#                     return HttpResponseRedirect('/login/')
#             else:
#                 return HttpResponseRedirect('/login/')
#            edition_alias = kwargs["edition"]

#             edition_locale_obj = Edition_Locale.objects.get(lang_code = cur_lng,
#                                                 edition__edition_alias__iexact = cur_edition_alias)
#             edition_name = edition_locale_obj.edition_name
            edition_name = cur_edition[0].edition_name
            kwargs["edition_name"] = edition_name
            kwargs["allowed_editions_lst"] = allowed_editions

            return view(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return new_view

def new_issue(request, editor_root, category, edition, edition_name, allowed_editions_lst):
    html_page = 'editor/new_issue.html'
    if request.method == 'POST':
        form = NewIssueForm(request.POST)
        if form.is_valid():
            edition_obj = Edition.objects.get(edition_alias = edition)
            issue_num = form.cleaned_data["issue_num"]
            issue_year = form.cleaned_data["issue_year"]
            issue_obj = Issue(issue_year = issue_year,
                             issue_num = issue_num,
                             edition = edition_obj)
            issue_obj.save()
            msg = "new_issue_created"

            folder_name = get_issue_folder_path(edition, issue_obj)
            if not os.path.isdir(folder_name):
                os.makedirs(folder_name)
            else:
                msg = "new_issue_created_but_dir_exists"


            return HttpResponseRedirect("/editor/" + category + "/" + edition + "/new_issue/display_msg/" + msg + "/")
    else:
        form = NewIssueForm()


    return render_to_response(html_page,
                              {"action": "new_issue",
                               "edition_alias": edition,
                               "form": form,
                                "edition_name": edition_name,
                                "category": category,
                                "allowed_editions_lst": allowed_editions_lst,
                                },
                              context_instance = RequestContext(request))

def new_article(request, editor_root, category, edition, edition_name, allowed_editions_lst):
    html_page = 'editor/article_form.html'

    caption = _(u"New Article")
    err_warning = ""
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, edition_alias = edition, article_file_required = True)
        if form.is_valid():
            data = {}
            data["file_name"] = request.FILES['article_file'].name
            data['issue_obj'] = form.cleaned_data['issue_year_num']
            data['rubric_obj'] = form.cleaned_data['rubric']
            data['caption_uk'] = form.cleaned_data['caption_uk']
            data['caption_en'] = form.cleaned_data['caption_en']
            data['abstract_uk'] = form.cleaned_data['abstract_uk']
            data['abstract_en'] = form.cleaned_data['abstract_en']
            author_uk = []
            author_en = []
            for i in xrange(1, 6):
                author_first_name_uk = "author_first_name_uk_" + str(i)
                author_first_name_en = "author_first_name_en_" + str(i)
                author_middle_name_uk = "author_middle_name_uk_" + str(i)
                author_middle_name_en = "author_middle_name_en_" + str(i)
                author_last_name_uk = "author_last_name_uk_" + str(i)
                author_last_name_en = "author_last_name_en_" + str(i)

                if form.cleaned_data[author_last_name_uk] != "":
                    author_uk.append((form.cleaned_data[author_last_name_uk],
                                      form.cleaned_data[author_first_name_uk],
                                      form.cleaned_data[author_middle_name_uk],
                                      ),)
                if form.cleaned_data[author_last_name_en] != "":
                    author_en.append((form.cleaned_data[author_last_name_en],
                                      form.cleaned_data[author_first_name_en],
                                      form.cleaned_data[author_middle_name_en],
                                      ),)

            data['author_uk'] = author_uk
            data['author_en'] = author_en

            issue_year = form.cleaned_data['issue_year_num'].issue_year
            issue_num = form.cleaned_data['issue_year_num'].issue_num
            handle_uploaded_file(request.FILES['article_file'], edition, issue_year, issue_num)

            add_article_to_db(data)

            # return HttpResponseRedirect("/editor/" + category + "/" + edition + "/new_article/display_msg/new_article_created/")
            messages.success(request, _(u"Article was added"))
            # clear data
            form = ArticleForm(edition_alias = edition, article_file_required = True)
        else:
            err_warning = _(u"There are errors")
    else:
        form = ArticleForm(edition_alias = edition, article_file_required = True)

    issue_cnt = Issue.objects.filter(edition__edition_alias = edition).count()
    if issue_cnt > 0:
        return render_to_response(html_page, {"action": "new_article",
                                          "edition_alias": edition,
                                          "err_warning": err_warning,
                                          "caption": caption,
                                          "form": form,
                                          "edition_name": edition_name,
                                          "category": category,
                                          "allowed_editions_lst": allowed_editions_lst, },
                    context_instance = RequestContext(request))
    else:
        return render_to_response('editor/article_form_no_issue.html', {"action": "new_article",
                                          "edition_alias": edition,
                                          "err_warning": err_warning,
                                          "caption": caption,
                                          "form": form,
                                          "edition_name": edition_name,
                                          "category": category,
                                          "allowed_editions_lst": allowed_editions_lst,
                                          },
                    context_instance = RequestContext(request))


def edit_article(request, editor_root, category, edition, edition_name, menu_action,
                 issue_year, issue_number, article_id, allowed_editions_lst):

    html_page = 'editor/article_form.html'
    err_warning = ""

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, edition_alias = edition, article_file_required = False)
        if form.is_valid():
            article_file_obj = request.FILES.get('article_file')
            old_article = Article.objects.get(id = article_id)
            old_issue = old_article.issue
            file_name = old_article.file_name

            new_issue = form.cleaned_data['issue_year_num']
            issue_was_changed = False
            if old_issue.issue_year != new_issue.issue_year or\
                    old_issue.issue_num != new_issue.issue_num:
                issue_was_changed = True

            data = {}
            data["article_id"] = article_id
            # article_file_obj.size - the size of the uploaded file
            if not (article_file_obj is None):
                data["file_name"] = article_file_obj.name
            data['issue_obj'] = new_issue
            data['rubric_obj'] = form.cleaned_data['rubric']
            data['caption_uk'] = form.cleaned_data['caption_uk']
            data['caption_en'] = form.cleaned_data['caption_en']
            data['abstract_uk'] = form.cleaned_data['abstract_uk']
            data['abstract_en'] = form.cleaned_data['abstract_en']
            author_uk = []
            author_en = []
            for i in xrange(1, publ_forms.MAX_AUTHORS + 1):
                author_first_name_uk = "author_first_name_uk_" + str(i)
                author_first_name_en = "author_first_name_en_" + str(i)
                author_middle_name_uk = "author_middle_name_uk_" + str(i)
                author_middle_name_en = "author_middle_name_en_" + str(i)
                author_last_name_uk = "author_last_name_uk_" + str(i)
                author_last_name_en = "author_last_name_en_" + str(i)

                if form.cleaned_data[author_last_name_uk] != "":
                    author_uk.append((form.cleaned_data[author_last_name_uk],
                                      form.cleaned_data[author_first_name_uk],
                                      form.cleaned_data[author_middle_name_uk],
                                      ),)
                if form.cleaned_data[author_last_name_en] != "":
                    author_en.append((form.cleaned_data[author_last_name_en],
                                      form.cleaned_data[author_first_name_en],
                                      form.cleaned_data[author_middle_name_en],
                                      ),)

            data['author_uk'] = author_uk
            data['author_en'] = author_en

            file_full_path = get_full_file_path(edition, old_issue, file_name)
            dest_path = get_issue_folder_path(edition, new_issue)
            dest_thumbnail_full_path = get_thumbnail_full_path(edition, new_issue, file_name)
            src_thumbnail_full_path = get_thumbnail_full_path(edition, old_issue, file_name)

            article_file_exists = bool(article_file_obj)
            if article_file_exists and issue_was_changed:
                # delete file in old folder and upload new file into new folder
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                    # raise PublViewError("Destination Folder Does Not Exists")

                if len(file_name) != 0:
                    file_cnt = Article.objects.filter(~Q(id = article_id),
                                    issue = old_issue,
                                    file_name = file_name).count()
                    if file_cnt == 0:  # there are no other references to the file
                        delete_article_files(edition, old_issue, file_name)
                issue_year = new_issue.issue_year
                issue_num = new_issue.issue_num
                handle_uploaded_file(article_file_obj, edition, issue_year, issue_num)
            elif not article_file_exists and issue_was_changed:
                # move file to new location

                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                if len(file_name) != 0 and os.path.isfile(file_full_path):
                    file_cnt = Article.objects.filter(~Q(id = article_id),
                                    issue = old_issue,
                                    file_name = file_name).count()
                    source = file_full_path
                    destination = get_full_file_path(edition, new_issue, file_name)
                    new_file_exists = os.path.isfile(destination)
                    if file_cnt == 0 and not new_file_exists:
                        # move file
                        os.rename(source, destination)
                        if os.path.isfile(src_thumbnail_full_path):
                            os.rename(src_thumbnail_full_path, dest_thumbnail_full_path)
                        else:
                            # thumbnail does not exist by some reason. Create new one.
                            create_pdf_thumbnail2(destination)
                    elif file_cnt > 0 and not new_file_exists:
                        # copy file
                        shutil.copy2(source, destination)
                        if os.path.isfile(src_thumbnail_full_path):
                            shutil.copy2(src_thumbnail_full_path, dest_thumbnail_full_path)
                        else:
                            # thumbnail does not exist by some reason. Create new one.
                            create_pdf_thumbnail2(destination)
                    elif file_cnt == 0 and new_file_exists:
                        # delete file in new folder and move file from old folder
                        os.remove(destination)
                        if os.path.isfile(dest_thumbnail_full_path):
                            os.remove(dest_thumbnail_full_path)
                        os.rename(source, destination)
                        if os.path.isfile(src_thumbnail_full_path):
                            os.rename(src_thumbnail_full_path, dest_thumbnail_full_path)
                        else:
                            # thumbnail does not exist by some reason. Create new one.
                            create_pdf_thumbnail2(destination)
                    elif file_cnt > 0 and new_file_exists:
                        # delete file in new folder and copy file from old folder
                        os.remove(destination)
                        if os.path.isfile(dest_thumbnail_full_path):
                            os.remove(dest_thumbnail_full_path)
                        shutil.copy2(source, destination)
                        if os.path.isfile(src_thumbnail_full_path):
                            shutil.copy2(src_thumbnail_full_path, dest_thumbnail_full_path)
                        else:
                            # thumbnail does not exist by some reason. Create new one.
                            create_pdf_thumbnail2(destination)
                    else:
                        raise PublViewError("Edit Article Error")
                else:
                    # pdf file does not exist
                    # check thumbnail and delete it
                    if os.path.isfile(src_thumbnail_full_path):
                        os.remove(src_thumbnail_full_path)

            elif article_file_exists and not issue_was_changed:
                # replace file
                if len(file_name) != 0:
                    file_cnt = Article.objects.filter(~Q(id = article_id),
                                    issue = old_issue,
                                    file_name = file_name).count()
                    if file_cnt == 0:  # there are no other references to the file
                        delete_article_files(edition, old_issue, file_name)
                        # os.remove(file_full_path)
                issue_year = new_issue.issue_year
                issue_num = new_issue.issue_num
                handle_uploaded_file(article_file_obj, edition, issue_year, issue_num)
            elif not article_file_exists and not issue_was_changed:
                # Nothing to do. Only check does thumbnail exist
                if not os.path.isfile(src_thumbnail_full_path):
                    create_pdf_thumbnail2(file_full_path)
            else:
                raise PublViewError("Edit Article Error")

            update_article_in_db(data)
            messages.success(request, _(u"Article was updated"))
            return HttpResponseRedirect("/" + editor_root + "/" + category + "/" + edition + "/"
                                        + menu_action + "/" + issue_year + "/" + issue_number + "/")
        else:
            # form is not valid
            err_warning = _(u"There are errors")
    else:
        # request.method is not 'POST'
        default_data = get_article_form_data(article_id)
        form = ArticleForm(edition_alias = edition, initial = default_data,
                           article_file_required = False)

    caption = _(u"Article editing")
    return render_to_response(html_page, {"action": menu_action,
                                          "edition_alias": edition,
                                          "err_warning": err_warning,
                                          "caption": caption,
                                          "form": form,
                                          "edition_name": edition_name,
                                          "category": category,
                                          "allowed_editions_lst": allowed_editions_lst,
                                           },
                    context_instance = RequestContext(request))

def get_full_file_path(edition, issue_obj, file_name):
#     full_path = os.path.join(settings.MEDIA_ROOT, "docs", edition,
#                  str(issue_obj.issue_year) + '_' + str(issue_obj.issue_num), file_name)
    full_path = os.path.join(get_issue_folder_path(edition, issue_obj), file_name)
    return full_path

def get_thumbnail_full_path(edition, issue_obj, file_name):
#     full_path = os.path.join(settings.MEDIA_ROOT, "docs", edition,
#                  str(issue_obj.issue_year) + '_' + str(issue_obj.issue_num), file_name)
    thumbnail_name = file_name_to_thumbnail(file_name)
    full_path = os.path.join(get_issue_folder_path(edition, issue_obj), thumbnail_name)
    return full_path

def file_name_to_thumbnail(file_name):
    file_without_ext, ext = os.path.splitext(file_name)
    thumbnail_name = file_without_ext + ".jpg"
    return thumbnail_name

def get_issue_folder_path(edition, issue_obj):
    full_path = get_issue_folder_path2(edition, issue_obj.issue_year, issue_obj.issue_num)
#    full_path = os.path.join(settings.MEDIA_ROOT, "docs", edition,
#                 str(issue_obj.issue_year) + '_' + str(issue_obj.issue_num))
    return full_path

def get_issue_folder_path2(edition, issue_year, issue_num):
    if type(issue_year) is not str:
        issue_year = str(issue_year)

    if type(issue_num) is not str:
        issue_num = str(issue_num)

    full_path = os.path.join(settings.MEDIA_ROOT, "docs", edition,
                 issue_year + '_' + issue_num)
    return full_path


def check_artcl_del(request, editor_root, category, edition, edition_name,
                        menu_action, issue_year, issue_number, allowed_editions_lst):
    '''
    check on articles to delete them
    '''
    # article_list = []
#    html_del_confirm_page = 'editor/delete_confirm.html'

    non_field_errors = []
    if request.method == 'POST':
        artcl_code_list = [value for key, value in request.POST.iteritems() if (unicode(key)).startswith(ARTICLE_CODE_PREFIX)]
        if artcl_code_list:
            if issue_year == "0":
                issue_list = Issue.objects.filter(edition__edition_alias = edition)\
                    .order_by("-issue_year", "-issue_num")
                if issue_list:
                    first_issue = issue_list[0]
                    issue_year = str(first_issue.issue_year)
                    issue_number = str(first_issue.issue_num)
            codes_list = "-".join(artcl_code_list)

            return HttpResponseRedirect(
                    "/" + editor_root + "/" + category + "/" + edition + "/" +
                    menu_action + "/execute/" + issue_year + "/" + issue_number +
                    "/?codes=" + codes_list)

        else:
            non_field_errors.append(_(u"There is/are no article(s) selected. Select an article(s) for deletion."))

            issue_list = Issue.objects.filter(edition__edition_alias = edition)\
                .order_by("-issue_year", "-issue_num")

            try:
                cur_issue = Issue.objects.get(edition__edition_alias = edition,
                                        issue_year = issue_year, issue_num = issue_number)
            except Issue.DoesNotExist:
                issue_year = "0"
                issue_number = "0"

            if issue_year == "0":
                if issue_list:
                    first_issue = issue_list[0]
                    issue_year = str(first_issue.issue_year)
                    issue_number = str(first_issue.issue_num)

            article_list = Article.objects.one_issue(get_lang_code(), edition, issue_year, issue_number)

            return render_to_response("editor/issue_content_del.html",
                              {"non_field_errors": non_field_errors,
                               "issue_year": issue_year,
                               "issue_number": issue_number,
                               "root_url": editor_root,
                               "active_url": editor_root + "/" + category + "/" + edition + "/" + menu_action
                                        + "/%s/%s" % (issue_year, issue_number),
                               "edition_alias": edition,
                               "action": menu_action,
                               "issue_list": issue_list,
                               "article_list": article_list,
                               "edition_name": edition_name,
                               "category": category,
                               "allowed_editions_lst": allowed_editions_lst,
                               },
                               context_instance = RequestContext(request))
    else:
        redirect_msg(editor_root, category, edition, menu_action, "application_post_error")

    # display selection form
    issue_list = Issue.objects.filter(edition__edition_alias = edition)\
        .order_by("-issue_year", "-issue_num")

    try:
        cur_issue = Issue.objects.get(edition__edition_alias = edition,
                                issue_year = issue_year, issue_num = issue_number)
    except Issue.DoesNotExist:
        issue_year = "0"
        issue_number = "0"

    if issue_year == "0":
        if issue_list:
            first_issue = issue_list[0]
            issue_year = str(first_issue.issue_year)
            issue_number = str(first_issue.issue_num)

    article_list = Article.objects.one_issue(get_lang_code(), edition, issue_year, issue_number)

    return render_to_response("editor/issue_content_del.html",
                              {"non_field_errors": non_field_errors,
                               "issue_year": issue_year,
                               "issue_number": issue_number,
                               "root_url": editor_root,
                               "active_url": editor_root + "/" + category + "/" + edition + "/" + menu_action
                                        + "/%s/%s" % (issue_year, issue_number),
                               "edition_alias": edition,
                               "action": menu_action,
                               "issue_list": issue_list,
                               "article_list": article_list,
                               "edition_name": edition_name,
                               "category": category,
                               "allowed_editions_lst": allowed_editions_lst,
                                },
                               context_instance = RequestContext(request))


def delete_artcl_exec(request, editor_root, category, edition, menu_action, edition_name,
                       issue_year, issue_number, allowed_editions_lst):
    '''
    delete articles from list
    '''

    if request.method == 'POST':
        if "confirm_yes" in request.POST:
            artcl_code_list = [value for key, value in request.POST.iteritems() if (unicode(key)).startswith(ARTICLE_CODE_PREFIX)]
            for artcl_id in artcl_code_list:
                artcl_obj = Article.objects.get(id = artcl_id)
                issue_obj = artcl_obj.issue
                file_name = artcl_obj.file_name
                if len(file_name) != 0:
                    file_cnt = Article.objects.filter(~Q(id = artcl_id),
                                        issue = issue_obj,
                                        file_name = file_name).count()
                    if file_cnt == 0:  # there are no other references to the file
                        delete_article_files(edition, issue_obj, file_name)
                artcl_obj.delete()

            messages.success(request, _(u"Article(s) was/were deleted"))
            return HttpResponseRedirect("/" + editor_root + "/" + category + "/" + edition + "/"
                                    + menu_action + "/" + issue_year + "/" + issue_number + "/")

#                return HttpResponseRedirect("/" + editor_root + "/" +
#                    category + "/" + edition + "/" + menu_action + "/display_msg/article_deleted/")
        else:
            messages.success(request, _(u"Article(s) deleting was/were cancelled"))
            return HttpResponseRedirect("/" + editor_root + "/" + category + "/" + edition + "/"
                                        + menu_action + "/" + issue_year + "/" + issue_number + "/")
#             return HttpResponseRedirect(
#                 "/" + editor_root + "/" + category + "/" + edition + "/" + menu_action +
#                 "/display_msg/article_not_deleted/")
    # display list of articles
    data = request.GET
    artcl_code_list = data["codes"].split("-")
    article_list = []
    for artcl_id in artcl_code_list:
        artcl_obj = Article_Locale.objects.get(article__id = artcl_id, lang_code = get_lang_code())
        authors_obj = Author.objects.article_authors_locale(get_lang_code(), int(artcl_id))
        authors_list = [item.full_name for item in authors_obj]
        article_list.append({'id': artcl_obj.article_id, 'caption': artcl_obj.caption, "authors": authors_list})

    return render_to_response("editor/delete_artcl_exec.html",
                          {"issue_year": issue_year,
                           "issue_number": issue_number,
                           "root_url": editor_root,
                           "active_url": editor_root + "/" + category + "/" + edition + "/deletion",
                           "edition_alias": edition,
                           "action": menu_action,
                           "article_list": article_list,
                           "edition_name": edition_name,
                           "category": category,
                           "allowed_editions_lst": allowed_editions_lst,
                           },
                           context_instance = RequestContext(request))



def select_artcl_edit(request, editor_root, category, edition, menu_action,
                        issue_year, issue_number, edition_name, allowed_editions_lst):
    html_page = 'editor/issue_content_edt.html'

    issue_list = Issue.objects.filter(edition__edition_alias = edition)\
        .order_by("-issue_year", "-issue_num")

    try:
        cur_issue = Issue.objects.get(edition__edition_alias = edition,
                                issue_year = issue_year, issue_num = issue_number)
    except Issue.DoesNotExist:
        issue_year = "0"
        issue_number = "0"

    if issue_year == "0":
        if issue_list:
            first_issue = issue_list[0]
            issue_year = str(first_issue.issue_year)
            issue_number = str(first_issue.issue_num)

    article_list = Article.objects.one_issue(get_lang_code(), edition, issue_year, issue_number)

    return render_to_response(html_page,
                              {"issue_year": issue_year,
                               "issue_number": issue_number,
                               "root_url": editor_root,
                               "active_url": editor_root + "/" + edition + "/" + menu_action
                                        + "/%s/%s" % (issue_year, issue_number),
                               "edition_alias": edition,
                               "action": menu_action,
                               "issue_list": issue_list,
                               "article_list": article_list,
                               "edition_name": edition_name,
                               "category": category,
                               "allowed_editions_lst": allowed_editions_lst,
                               },
                               context_instance = RequestContext(request))


def user_login(request, template_name = 'editor/login.html',
          authentication_form = EditorAuthenticationForm,
          current_app = None, extra_context = None):
    """
    Displays the login form and handles the login action.
    """
    cur_lng = get_lang_code()  # lng_code_ukr
    activate(cur_lng)

    if request.method == "POST":
        form = authentication_form(data = request.POST)
        if form.is_valid():
            # Ensure the user-originating redirection url is safe.
            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            category_alias = Edition.objects.get(edition_alias = form.get_user_edition()).category.category_alias
            redirect_to = "/editor/" + category_alias + "/" + form.get_user_edition() + "/new_issue/"
            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)
        request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        "next": "",
        'site': current_site,
        'site_name': current_site.name,
    }

    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app = current_app)

def user_logout(request, template_name = '/login/'):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    cur_lng = get_lang_code()  # lng_code_ukr
    activate(cur_lng)

    auth_logout(request)
    return HttpResponseRedirect(template_name)

def display_goodby(request):
    return HttpResponse('<h1>До побачення</h1>')

def edition_list(request, edition_list_root_url, category, cur_lng_code = None):
#    request.session["fav_color"] = "blue"
    html_page = 'edition_list.html'

    # user = auth.authenticate(username = u"astronomy", password = "astronomy")
    # perm = user.has_perm("model.edit_astronomy")
    edition_list_rs = Edition.objects.category_locale(cur_lng_code, category)

    if category == data.cat_conference:
        column_size = len(edition_list_rs)
    else:
        column_size = math.ceil(len(edition_list_rs) / 3.0)

    return render_to_response(html_page, {"root_url": edition_list_root_url,
                                          "active_url": edition_list_root_url + '/' + category,
                                          "category": category,
                                          "edition_list": edition_list_rs,
                                          "column_size": column_size},
                    context_instance = RequestContext(request))


def about(request, edition_root_url, category, edition, action, edition_name, cur_lng_code = None):

# category
# edition name
# division (department, institute, subdivision)
# * field of science
# foundation year
# issues by year
# subject_matter
# government certificate date
# government certificate number
# VAC certificate date
# VAC certificate number
# ISSN
# phone
# email
# address


    edition_data = Edition_Locale.objects.select_related("edition").\
            extra(select = OrderedDict([('dis_name',
                        "SELECT dis_name FROM publ_dis_locale WHERE publ_dis_locale.dis_id = publ_edition.dis_id "
                        "AND lang_code = %s")]),
                  select_params = (cur_lng_code,)).\
            get(edition__edition_alias = edition, lang_code = cur_lng_code)


    fos_set = edition_data.edition.fields_of_science.extra(select = OrderedDict([("fos_name", "SELECT fos_name FROM publ_field_of_science_locale"
                                                        " WHERE publ_field_of_science_locale.field_of_science_id = "
                                                        " publ_field_of_science.id AND publ_field_of_science_locale."
                                                        "lang_code = %s"), ]),
                                                select_params = (cur_lng_code,)
                                                )

    return render_to_response("about.html",
                              {"root_url": edition_root_url,
                              "active_url": edition_root_url + "/"
                                         + category + "/" + edition + "/" + action,
                              "edition_alias": edition,
                              "action": action,
                              "category": category,
                              "edition_name": edition_name,
                              "ed": edition_data,
                              "fos_set": fos_set},
                    context_instance = RequestContext(request))

def staff(request, edition_root_url, category, edition, action, edition_name, cur_lng_code = None):

    return render_to_response('staff.html',
                              {"root_url": edition_root_url,
                              "active_url": edition_root_url + "/"
                                         + category + "/" + edition + "/" + action,
                              "edition_alias": edition,
                              "action": action,
                              "category": category,
                              "edition_name": edition_name},
                              context_instance = RequestContext(request))


def publication(request, edition_root_url, category, edition, action, issue_year,
                issue_number, edition_name, cur_lng_code = None):

    issue_list = Issue.objects.filter(edition__edition_alias = edition)\
        .order_by("-issue_year", "-issue_num")
#    article_list = []

    try:
        cur_issue = Issue.objects.get(edition__edition_alias = edition,
                                issue_year = issue_year, issue_num = issue_number)
    except Issue.DoesNotExist:
        issue_year = "0"
        issue_number = "0"

    if issue_year == "0":
        if issue_list:
            first_issue = issue_list[0]
            issue_year = str(first_issue.issue_year)
            issue_number = str(first_issue.issue_num)
#            article_list = Article.objects.one_issue(cur_lng_code, edition, issue_year, issue_number)
#    else:
#            article_list = Article.objects.one_issue(cur_lng_code, edition, issue_year, issue_number)

    article_list = Article.objects.one_issue(cur_lng_code, edition, issue_year, issue_number)

    return render_to_response("issue_content.html",
                              {"issue_year": issue_year,
                               "issue_number": issue_number,
                               "root_url": edition_root_url,
                               "active_url": edition_root_url + "/" + category + "/" + edition + "/" + action
                                        + "/%s/%s" % (issue_year, issue_number),
                               "edition_alias": edition,
                               "action": action,
                               "issue_list": issue_list,
                               "article_list": article_list,
                               "category": category,
                               "edition_name": edition_name},
                               context_instance = RequestContext(request))


def add_article_to_db(article_data):

        issue_obj = article_data['issue_obj']
        rubric_obj = article_data['rubric_obj']
        article_obj = Article(issue = issue_obj,
                              rubric = rubric_obj,
                              file_name = article_data["file_name"],
                              )
        article_obj.save()


        article_locale_obj = Article_Locale(lang_code = lng_code_ukr,
                                   caption = article_data["caption_uk"],
                                   abstract = article_data["abstract_uk"],
                                   article = article_obj,
                                   )
        article_locale_obj.save()

        article_locale_obj = Article_Locale(lang_code = lng_code_en,
                                   caption = article_data["caption_en"],
                                   abstract = article_data["abstract_en"],
                                   article = article_obj,
                                   )
        article_locale_obj.save()
        for j, ((last_uk, first_uk, middle_uk), (last_en, first_en, middle_en)) \
                in enumerate(zip(article_data["author_uk"], article_data["author_en"])):

            author_obj_lst = Author.objects.filter(
                    author_locale__lang_code__iexact = lng_code_ukr,
                    author_locale__first_name__iexact = first_uk,
                    author_locale__middle_name__iexact = middle_uk,
                    author_locale__last_name__iexact = last_uk).\
                    filter(
                    author_locale__lang_code__iexact = lng_code_en,
                    author_locale__first_name__iexact = first_en,
                    author_locale__middle_name__iexact = middle_en,
                    author_locale__last_name__iexact = last_en)
            if len(author_obj_lst) == 1:
                author_obj = author_obj_lst[0]
            elif len(author_obj_lst) == 0:
                author_obj = Author.objects.create()
                Author_Locale.objects.create(
                        lang_code = lng_code_ukr,
                        author = author_obj,
                        first_name = first_uk,
                        middle_name = middle_uk,
                        last_name = last_uk)

                Author_Locale.objects.create(
                        lang_code = lng_code_en,
                        author = author_obj,
                        first_name = first_en,
                        middle_name = middle_en,
                        last_name = last_en)
            else:
                # TODO: raise exception and show error message: database integrity violation or log and send email
                author_obj = author_obj_lst[0]

            m = Article_Authors(article = article_obj,
                                author = author_obj,
                                author_order = j + 1)
            m.save()


def update_article_in_db(article_data):

        article_id = article_data["article_id"]

        issue_obj = article_data['issue_obj']
        rubric_obj = article_data['rubric_obj']


        article_obj = Article.objects.get(id = article_id)
        article_obj.issue = issue_obj
        article_obj.rubric = rubric_obj
        file_name = article_data.get("file_name")
        if file_name:
            article_obj.file_name = file_name
        article_obj.save()

        # update article locale info
        article_locale_obj = Article_Locale.objects.get(article_id = article_id, lang_code = lng_code_ukr)
        article_locale_obj.caption = article_data["caption_uk"]
        article_locale_obj.abstract = article_data["abstract_uk"]
        article_locale_obj.save()

        article_locale_obj = Article_Locale.objects.get(article_id = article_id, lang_code = lng_code_en)
        article_locale_obj.caption = article_data["caption_en"]
        article_locale_obj.abstract = article_data["abstract_en"]
        article_locale_obj.save()

        # delete Article_Authors relationship
        Article_Authors.objects.filter(article = article_id).delete()

        # create new Artice_Authors relationship
        for j, ((last_uk, first_uk, middle_uk), (last_en, first_en, middle_en)) \
                in enumerate(zip(article_data["author_uk"], article_data["author_en"])):

            author_obj_lst = Author.objects.filter(
                    author_locale__lang_code__iexact = lng_code_ukr,
                    author_locale__first_name__iexact = first_uk,
                    author_locale__middle_name__iexact = middle_uk,
                    author_locale__last_name__iexact = last_uk).\
                    filter(
                    author_locale__lang_code__iexact = lng_code_en,
                    author_locale__first_name__iexact = first_en,
                    author_locale__middle_name__iexact = middle_en,
                    author_locale__last_name__iexact = last_en)
            if len(author_obj_lst) == 1:
                author_obj = author_obj_lst[0]
            elif len(author_obj_lst) == 0:
                author_obj = Author.objects.create()
                Author_Locale.objects.create(
                        lang_code = lng_code_ukr,
                        author = author_obj,
                        first_name = first_uk,
                        middle_name = middle_uk,
                        last_name = last_uk)

                Author_Locale.objects.create(
                        lang_code = lng_code_en,
                        author = author_obj,
                        first_name = first_en,
                        middle_name = middle_en,
                        last_name = last_en)
            else:
                # TODO: raise exception and show error message: database integrity violation or log and send email
                author_obj = author_obj_lst[0]

            m = Article_Authors(article = article_obj,
                                author = author_obj,
                                author_order = j + 1)
            m.save()

def get_article_form_data(article_id):
    article_obj = Article.objects.get(id = article_id)
    issue_obj = article_obj.issue
    rubric_obj = article_obj.rubric

    data = {}
    data["issue_year_num"] = issue_obj.id
    data["rubric"] = rubric_obj.id

    article_locale_uk = Article_Locale.objects.get(article_id = article_id, lang_code__iexact = lng_code_ukr)
    data["caption_uk"] = article_locale_uk.caption
    data["abstract_uk"] = article_locale_uk.abstract

    article_locale_en = Article_Locale.objects.get(article_id = article_id, lang_code__iexact = lng_code_en)
    data["caption_en"] = article_locale_en.caption
    data["abstract_en"] = article_locale_en.abstract

    author_qs_uk = Author_Locale.objects.filter(lang_code__iexact = lng_code_ukr,
                                                  author__article_authors__article_id = article_id)\
                                                  .order_by("author__article_authors__author_order")

    for i, author in enumerate(author_qs_uk):
        data["author_first_name_uk_" + str(i + 1)] = author.first_name
        data["author_middle_name_uk_" + str(i + 1)] = author.middle_name
        data["author_last_name_uk_" + str(i + 1)] = author.last_name

    author_qs_en = Author_Locale.objects.filter(lang_code__iexact = lng_code_en,
                                                  author__article_authors__article_id = article_id)\
                                                  .order_by("author__article_authors__author_order")

    for i, author in enumerate(author_qs_en):
        data["author_first_name_en_" + str(i + 1)] = author.first_name
        data["author_middle_name_en_" + str(i + 1)] = author.middle_name
        data["author_last_name_en_" + str(i + 1)] = author.last_name


    return data

def handle_uploaded_file(upload_obj, edition, issue_year, issue_num):

#    upload_dir = os.path.join('docs', edition, str(issue_year) + '_' + str(issue_num))
#    upload_full_path = os.path.join(settings.MEDIA_ROOT, upload_dir)
    upload_full_path = get_issue_folder_path2(edition, issue_year, issue_num)
    if not os.path.exists(upload_full_path):
        os.makedirs(upload_full_path)

    dest = open(os.path.join(upload_full_path, upload_obj.name), 'wb+')
    for chunk in upload_obj.chunks():
        dest.write(chunk)
    dest.close()

    create_pdf_thumbnail(upload_full_path, upload_obj.name)


def get_lang_code():
    return settings.LANGUAGE_CODE

# TODO: replace HttpResponseRedirect with redirect_msg
def redirect_msg(editor_root, category, edition, menu_action, msg_id):
                return HttpResponseRedirect(
                    "/" + editor_root + "/" + category + "/" + edition + "/" +
                    menu_action + "/display_msg/" + msg_id + "/")

def display_msg(request, editor_root, category, edition, edition_name, menu_action, msg, allowed_editions_lst):
    msg_text = PublMsg.get_msg(msg)

    return render_to_response("editor/display_msg.html",
                              {"action": menu_action,
                               "edition_alias": edition,
                               "msg": msg_text,
                               "edition_name": edition_name,
                               "category": category,
                               "allowed_editions_lst": allowed_editions_lst,
                               },
                              context_instance = RequestContext(request))

def delete_article_files(edition, issue_obj, file_name):
    file_full_path = get_full_file_path(edition, issue_obj, file_name)
    if os.path.isfile(file_full_path):
        os.remove(file_full_path)
    thumbnail_full_path = get_thumbnail_full_path(edition, issue_obj, file_name)
    if os.path.isfile(thumbnail_full_path):  # there are no other references to the file
        os.remove(thumbnail_full_path)



# def load_document(request, document_year, document_number, document_full_name):
#    doc_items = document_full_name.split('.')
#    data = open(os.path.join(os.path.dirname(__file__), 'templates\\docs\\%s\\%s\\%s' % \
#                             (document_year, document_number, document_full_name))\
#                             .replace('\\','/'), "rb").read()
#    doc_type = doc_items[1]
#    if doc_type == "pdf":
#        return HttpResponse(data, mimetype="application/pdf")
#    elif doc_type == "doc":
#        return HttpResponse(data, mimetype="application/msword")
#    elif doc_type == "docx":
#        return HttpResponse(data, mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
#    else:
#        return HttpResponse(data, mimetype="application/text/plain") #or:  x-binary
#
