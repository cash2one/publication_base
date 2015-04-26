# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms
from django.core import validators
from model.models import Issue, Rubric, Category, FieldOfScience
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.utils.translation import get_language
from django.utils.encoding import smart_text, force_text
# from views import lng_code_ukr, lng_code_en

lng_code_ukr = 'uk'
lng_code_en = 'en'



ALLOWED_ED_PREFIX = 'model.edit_'
MAX_AUTHORS = 12

class PublMsg(object):
    """
    Form to create new issue 
    """

    _messages_ = {
        'new_issue_created': _("New issue has been created"),
        'issue_exists': _("Issue already exists"),
        'new_issue_created_but_dir_exists': _("New issue has been created. Warning: directory with same name exists"),
        'new_article_created': _("New article has been created"),
        'article_updated': _("Article has been updated"),
        'application_post_error': _("Only POST method can be used"),
        'article_deleted': _("Article(s) has been deleted"),
        'article_not_deleted': _("Article(s) deletion has been canceled"),
    }

    @staticmethod
    def get_msg(msg):
        return PublMsg._messages_[msg]

class ArticleForm(forms.Form):
    """
    Form to create new article 
    """

    na_error_messages = {
        'issue_exists': _(u"Issue already exists"),
        'too_many_issues': _(u"Too many issues")
    }

    issue_year_num = forms.ModelChoiceField(queryset = Issue.objects.none(), label = _(u"Issue"))
    rubric = forms.ModelChoiceField(queryset = Rubric.objects.none(), label = _(u"Rubric"))

    author_last_name_uk_1 = forms.CharField(max_length = 50, label = _(u"Last Name"))
#    author_first_name_uk_1 = forms.CharField(max_length = 50, label = force_text(_(u"First Name")))
    author_first_name_uk_1 = forms.CharField(max_length = 50,
                                             label = force_text(_(u"First Name")))
    author_middle_name_uk_1 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_1 = forms.CharField(max_length = 50, label = _(u"Last Name"))
    author_first_name_en_1 = forms.CharField(max_length = 50,
                                             label = force_text(_(u"First Name")))
    author_middle_name_en_1 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_2 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_2 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_2 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_2 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_2 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_2 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_3 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_3 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_3 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_3 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_3 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_3 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_4 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_4 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_4 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_4 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_4 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_4 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_5 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_5 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_5 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_5 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_5 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_5 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_6 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_6 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_6 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_6 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_6 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_6 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_7 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_7 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_7 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_7 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_7 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_7 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_8 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_8 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_8 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_8 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_8 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_8 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_9 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_9 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_9 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_9 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_9 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_9 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_10 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_10 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_10 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_10 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_10 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_10 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_11 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_11 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_11 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_11 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_11 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_11 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))

    author_last_name_uk_12 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_uk_12 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_uk_12 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))
    author_last_name_en_12 = forms.CharField(max_length = 50, required = False, label = _(u"Last Name"))
    author_first_name_en_12 = forms.CharField(max_length = 50, required = False, label = force_text(_(u"First Name")))
    author_middle_name_en_12 = forms.CharField(max_length = 50, required = False, label = _(u"Middle Name"))


    caption_uk = forms.CharField(max_length = 250, label = _(u"Caption ukr."))
    caption_en = forms.CharField(max_length = 250, label = _(u"Caption engl."))

    abstract_uk = forms.CharField(widget = forms.Textarea, label = _(u"Abstract ukr."))
    abstract_en = forms.CharField(widget = forms.Textarea, label = _(u"Abstract engl."))
    article_file = forms.FileField(label = _(u"File"))

    def __init__(self, *args, **kwargs):
        edition_alias = kwargs.pop('edition_alias')
        if 'article_file_required' in kwargs:
            article_file_required = kwargs.pop('article_file_required')
        else:
            article_file_required = True

        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields['issue_year_num'].queryset = Issue.objects.filter(edition__edition_alias = edition_alias)\
            .order_by("-issue_year", "-issue_num")
        if len(self.fields['issue_year_num'].queryset) > 0:
            self.fields["issue_year_num"].initial = self.fields['issue_year_num'].queryset[0].id

        self.fields['rubric'].queryset = Rubric.objects.filter(edition__edition_alias = edition_alias).\
            order_by('rubric_order')

        if len(self.fields['rubric'].queryset) == 1:
            self.fields["rubric"].initial = self.fields['rubric'].queryset[0].id

        self.fields['caption_uk'].widget.attrs['size'] = 100
        self.fields['caption_en'].widget.attrs['size'] = 100

        self.fields['abstract_uk'].widget.attrs['cols'] = 150
        self.fields['abstract_en'].widget.attrs['cols'] = 150
        self.fields['article_file'].required = article_file_required

        first_name = "First Name"
        if get_language() == lng_code_ukr:
            first_name = u"Ім'я"

        for i in xrange(1, MAX_AUTHORS + 1):
            self.fields["author_first_name_uk_" + str(i)].label = first_name
            self.fields["author_first_name_en_" + str(i)].label = first_name

        # self.fields['article_file'].widget.attrs['value'] = u"Load filw"

#     def clean(self):
#         pass
#         super(NewIssueForm, self).clean()
#         issue_year = self.cleaned_data.get('issue_year')
#         issue_num = self.cleaned_data.get('issue_num')
#         try:
#             issue_obj = Issue.objects.get(issue_year = issue_year, issue_num = issue_num)
#             raise forms.ValidationError(self.ni_error_messages['issue_exists'] %
#                                         {'number': issue_num, 'year': issue_year})
#         except Issue.DoesNotExist:
#             pass
#         except Issue.MultipleObjectsReturned:
#             raise forms.ValidationError(self.ni_error_messages['too_many_issues'] %
#                                         {'number': issue_num, 'year': issue_year})
#         return self.cleaned_data


class NewIssueForm(forms.Form):
    """
    Form to create new issue 
    """

    ni_error_messages = {
        'issue_exists': _("Issue number %(number)d for %(year)d already exists"),
        'too_many_issues': _("System error. There are more than one issue number %(number)d for %(year)d.")
    }

    issue_year = forms.IntegerField(label = _(u"Year"),
                                    min_value = 1950, max_value = 2050)
    issue_num = forms.IntegerField(label = _(u"Number"),
                                   min_value = 1, max_value = 200)

    def clean(self):
        super(NewIssueForm, self).clean()
        issue_year = self.cleaned_data.get('issue_year')
        issue_num = self.cleaned_data.get('issue_num')
        try:
            issue_obj = Issue.objects.get(issue_year = issue_year, issue_num = issue_num)
            raise forms.ValidationError(self.ni_error_messages['issue_exists'] %
                                        {'number': issue_num, 'year': issue_year})
        except Issue.DoesNotExist:
            pass
        except Issue.MultipleObjectsReturned:
            raise forms.ValidationError(self.ni_error_messages['too_many_issues'] %
                                        {'number': issue_num, 'year': issue_year})
        return self.cleaned_data


class EditorAuthenticationForm(AuthenticationForm):
    """
    Класс для аутентификации редакторов изданий 
    """
    ed_error_messages = {
        'not_pass_authorization': _("User has not pass authorization"),
        'too_much_authorities': _("System Error: user has rights to edit more than one edition"),
    }

    def __init__(self, *args, **kwargs):
        super(EditorAuthenticationForm, self).__init__(*args, **kwargs)
        self.edition = ""

    def clean(self):
        super(EditorAuthenticationForm, self).clean()
        if self.get_user():  # not bool(self.errors):
            permissions_list = self.get_user().get_all_permissions()  # user.user_permissions.all()
            allowed_editions = [item[len(ALLOWED_ED_PREFIX):] for item in permissions_list if item.startswith(ALLOWED_ED_PREFIX) ]
            if len(allowed_editions) >= 1:
                self.edition = allowed_editions[0]
                # self.edition = edit_permission
            else:  # len(allowed_editions) == 0:
                raise forms.ValidationError(self.ed_error_messages['not_pass_authorization'])
        return self.cleaned_data

    def get_user_edition(self):
        return self.edition



class EditionForm(forms.Form):
    """
    Form to input edititon info 
    """

    na_error_messages = {
        'issue_exists': _(u"Issue already exists"),
        'too_many_issues': _(u"Too many issues")
    }


    category = forms.ModelChoiceField(queryset = Category.objects.none(), label = _(u"Category"))

    subject_matter = forms.CharField(widget = forms.Textarea, max_length = 500,
                                     label = _(u"Subject Matter"))  # subject matter; проблематика
    fields_of_science = forms.ModelMultipleChoiceField(queryset = FieldOfScience.objects.none(),
                                                       label = _(u"Fields of science"))  # Fields of science; Галузь науки
    foundation_year = forms.IntegerField()  # Year of foundation; Рік заснування
    issues_by_year = forms.IntegerField()  # periodicity; periodicity
    # Certificate of registration; Свідоцтво про державну реєстрацію
    gov_certificate_date = forms.DateField()
    gov_certificate_num = forms.SlugField(max_length = 10)
    # professional registration in Ukraine VAC; Фахова реєстрація у ВАК України
    vac_certificate_date = forms.DateField()
    vac_certificate_num = forms.SlugField(max_length = 10)
    ISSN = forms.SlugField(max_length = 9)
    address = forms.CharField(max_length = 500)
    phone = forms.CharField(max_length = 10)
    email = forms.EmailField()


    def __init__(self, *args, **kwargs):
        pass
#         edition_alias = kwargs.pop('edition_alias')
#         if 'article_file_required' in kwargs:
#             article_file_required = kwargs.pop('article_file_required')
#         else:
#             article_file_required = True
#
#         super(ArticleForm, self).__init__(*args, **kwargs)
#
#         self.fields['issue_year_num'].queryset = Issue.objects.filter(edition__edition_alias = edition_alias)\
#             .order_by("-issue_year", "-issue_num")
#         if len(self.fields['issue_year_num'].queryset) > 0:
#             self.fields["issue_year_num"].initial = self.fields['issue_year_num'].queryset[0].id
#
#         self.fields['rubric'].queryset = Rubric.objects.filter(edition__edition_alias = edition_alias).\
#             order_by('rubric_order')
#
#         if len(self.fields['rubric'].queryset) == 1:
#             self.fields["rubric"].initial = self.fields['rubric'].queryset[0].id
#
#         self.fields['caption_uk'].widget.attrs['size'] = 100
#         self.fields['caption_en'].widget.attrs['size'] = 100
#
#         self.fields['abstract_uk'].widget.attrs['cols'] = 150
#         self.fields['abstract_en'].widget.attrs['cols'] = 150
#         self.fields['article_file'].required = article_file_required
#
#         first_name = "First Name"
#         if get_language() == lng_code_ukr:
#             first_name = u"Ім'я"
#
#         for i in xrange(1, MAX_AUTHORS + 1):
#             self.fields["author_first_name_uk_" + str(i)].label = first_name
#             self.fields["author_first_name_en_" + str(i)].label = first_name
#
#         # self.fields['article_file'].widget.attrs['value'] = u"Load filw"

#     def clean(self):
#         pass
#         super(NewIssueForm, self).clean()
#         issue_year = self.cleaned_data.get('issue_year')
#         issue_num = self.cleaned_data.get('issue_num')
#         try:
#             issue_obj = Issue.objects.get(issue_year = issue_year, issue_num = issue_num)
#             raise forms.ValidationError(self.ni_error_messages['issue_exists'] %
#                                         {'number': issue_num, 'year': issue_year})
#         except Issue.DoesNotExist:
#             pass
#         except Issue.MultipleObjectsReturned:
#             raise forms.ValidationError(self.ni_error_messages['too_many_issues'] %
#                                         {'number': issue_num, 'year': issue_year})
#         return self.cleaned_data

