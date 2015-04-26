# -*- coding: utf-8 -*-

# from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, include, url
from publication_base import views
from views import def_lng, view_wrapper, edition_view_wrapper, editor_wrapper
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from model.data import cat_herald, cat_journal, cat_conference
# import django.contrib.auth.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

url_page_patterns = patterns('',
      url(r'^$', view_wrapper(views.edition_list),
           {'edition_list_root_url': 'editionlist', 'category': cat_herald}),
      url(r'^editionlist$', view_wrapper(views.edition_list),
           {'edition_list_root_url': 'editionlist', 'category': cat_herald}),
      url(r'^editionlist/herald$', view_wrapper(views.edition_list),
          {'edition_list_root_url': 'editionlist', 'category': cat_herald}),
      url(r'^editionlist/journal$', view_wrapper(views.edition_list),
          {'edition_list_root_url': 'editionlist', 'category': cat_journal}),
      url(r'^editionlist/conference$', view_wrapper(views.edition_list),
          {'edition_list_root_url': 'editionlist', 'category': cat_conference}),

      url(r'^(?P<edition_root_url>edition)/(?P<category>\w+)/(?P<edition>\w+)/$',
          edition_view_wrapper(views.publication),
          {"action": "publication",
          "issue_year": "0",
          "issue_number": "0"}),
      url(r'^(?P<edition_root_url>edition)/(?P<category>\w+)/(?P<edition>\w+)/(?P<action>about)/$',
          edition_view_wrapper(views.about)),
      url(r'^(?P<edition_root_url>edition)/(?P<category>\w+)/(?P<edition>\w+)/(?P<action>staff)/$',
          edition_view_wrapper(views.staff)),
      url(r'^(?P<edition_root_url>edition)/(?P<category>\w+)/(?P<edition>\w+)/(?P<action>publication)/(?P<issue_year>\d{1,4})/(?P<issue_number>\d{1,4})/$',
          edition_view_wrapper(views.publication)),
      url(r'^(?P<edition_root_url>edition)/(?P<category>\w+)/(?P<edition>\w+)/(?P<action>publication)/$',
          edition_view_wrapper(views.publication),
          {"issue_year": "0", "issue_number": "0"}),
)

urlpatterns = patterns('',
         url(r'^login/$', views.user_login),
         url(r'^logout/$', views.user_logout),
         # url(r'^logout/by/$', views.display_goodby),

        # new issue
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/new_issue/$',
             editor_wrapper(views.new_issue)),

        # new article
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/new_article/$',
             editor_wrapper(views.new_article)),
        # update article
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>edit_article)/$',
             editor_wrapper(views.select_artcl_edit),
             {"issue_year": "0", "issue_number": "0"}),
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>edit_article)/'
             '(?P<issue_year>\d{1,4})/(?P<issue_number>\d{1,4})/$',
             editor_wrapper(views.select_artcl_edit),
             ),
          url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>edit_article)/'
              '(?P<issue_year>\d{1,4})/(?P<issue_number>\d{1,4})/(?P<article_id>\d+)/$',
              editor_wrapper(views.edit_article)),
        # delete
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>delete_article)/$',
             editor_wrapper(views.check_artcl_del),
             {"issue_year": "0", "issue_number": "0"}),
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>delete_article)/'
             '(?P<issue_year>\d{1,4})/(?P<issue_number>\d{1,4})/$',
             editor_wrapper(views.check_artcl_del),
             ),
         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>delete_article)/execute/'
             '(?P<issue_year>\d{1,4})/(?P<issue_number>\d{1,4})/$',
             editor_wrapper(views.delete_artcl_exec),
             ),

         url(r'^(?P<editor_root>editor)/(?P<category>\w+)/(?P<edition>\w+)/(?P<menu_action>\w+)/display_msg/(?P<msg>\w+)/$',
              editor_wrapper(views.display_msg)),

         url(r'^(?P<cur_lng_code>en)/', include(url_page_patterns)),
         url(r'^(?P<cur_lng_code>uk)/', include(url_page_patterns)),
         url(r'', include(url_page_patterns), {'cur_lng_code': def_lng}),
         )

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)


urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
 )

# urlpatterns += staticfiles_urlpatterns()

# urlpatterns = patterns('',
#                       (r"^$", hello),
#                       (r"^hello/$", hello),
#    # Examples:
#    # url(r'^$', 'herald_knu.views.home', name='home'),
#    # url(r'^herald_knu/', include('herald_knu.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
# )

# url_page_patterns = patterns('',
#       url(r'^$', view_wrapper(views.home)),
#       url(r'^home/$', view_wrapper(views.home)),
#       url(r'^staff/$', view_wrapper(views.editorial_staff)),
#       url(r'^rubrics/$', view_wrapper(views.rubrics)),
#       url(r'^requirements/$', view_wrapper(views.requirements)),
#       url(r'^address/$', view_wrapper(views.address)),
#       url(r'^archive/(?P<issue_year>\d{1,4})/(?P<issue_number>\d{1,4})/$', view_wrapper(views.load_issue)),
#       url(r'^archive/$', view_wrapper(views.load_issue), {"issue_year": "0", "issue_number": "0"}),
# )
#
# urlpatterns = patterns('',
#                        url(r'^(?P<cur_lng_code>en)/', include(url_page_patterns), {'edition': def_edition}),
#                        url(r'^(?P<cur_lng_code>uk)/', include(url_page_patterns), {'edition': def_edition}),
#                        url(r'', include(url_page_patterns), {'cur_lng_code': def_lng, 'edition': def_edition}),
#
#                        url(r'^(?P<cur_lng_code>en)/-(?P<edition>\w+)/', include(url_page_patterns)),
#                        url(r'^(?P<cur_lng_code>uk)/-(?P<edition>\w+)/', include(url_page_patterns)),
#                        url(r'^-(?P<edition>\w+)/', include(url_page_patterns), {'cur_lng_code': def_lng}),
#
#                        )


# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.STATIC_ROOT,
#         }),
# )

# urlpatterns = patterns('',
#                        url('^en/', include(url_page_patterns), {'cur_lng_code': lng_code_en}),
#                        url('^en-us/', include(url_page_patterns), {'cur_lng_code': lng_code_en}),
#                        url('^uk/', include(url_page_patterns), {'cur_lng_code': lng_code_ukr}),
#                        url('', include(url_page_patterns), {'cur_lng_code': def_lng}),)

# from django.conf.urls import patterns, include, url
# from bulletin_knu import views
# from archive.views import load_issue
# #from django.conf.urls import i18n
#
# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#
# url_page_patterns = patterns('',
#      url(r'^$', views.home),
#      url('^home/$', views.home),
#      url('^staff/$', views.editorial_staff),
#      url('^rubrics/$', views.rubrics),
#      url('^requirements/$', views.requirements),
#      url('^adress/$', views.adress),
#      url(r'^archive/(\d{4,4})/(\d)/$', load_issue),
# )
#
# lng_code_ukr = 'uk'
# lng_code_en = 'en'
# def_lng = lng_code_ukr #default laguage
#
# urlpatterns = patterns('',
#      url(r'^$', views.home, {'cur_lng_code': def_lng}),
#      url('^home/$', views.home, {'cur_lng_code': def_lng}),
#      url('^staff/$', views.editorial_staff, {'cur_lng_code': def_lng}),
#      url('^rubrics/$', views.rubrics, {'cur_lng_code': def_lng}),
#      url('^requirements/$', views.requirements, {'cur_lng_code': def_lng}),
#      url('^adress/$', views.adress, {'cur_lng_code': def_lng}),
#      url(r'^archive/(\d{4,4})/(\d)/$', load_issue, {'cur_lng_code': def_lng}),
#      url(r'docs/(\d{4,4})/(\d)/(.+)/$', views.load_document),
#      url(r'images/(.+)/$', views.load_image),
#      url('^en/', include(url_page_patterns), {'cur_lng_code': lng_code_en}),
#      url('^uk/', include(url_page_patterns), {'cur_lng_code': def_lng}),
#
#    # Examples:
#    # url(r'^$', 'bulletin_knu.views.home', name='home'),
#    # url(r'^bulletin_knu/', include('bulletin_knu.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    # Uncomment the next line to enable the admin:
#    url(r'^admin/', include(admin.site.urls)),
# )
#
# #urlpatterns = patterns('',
# #          url(r'^$', home),
# #          url('^home/$', home),
# #          url('^staff/$', editorial_staff),
# #          url('^rubrics/$', rubrics),
# #          url('^requirements/$', requirements),
# #          url('^adress/$', adress),
# #          url(r'^archive/(\d{4,4})/(\d)/$', load_issue),
# #          url(r'docs/(\d{4,4})/(\d)/(.+)/$', load_document),
# #          url(r'images/(.+)/$', load_image),
# #          url(r'^i18n/', include('django.conf.urls.i18n')),
#
