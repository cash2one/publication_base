# -*- coding: utf-8 -*-

from django.db import connection, models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.translation import get_language
# from django.db.backends.mysql.base import DatabaseError
# import MySQLdb


# BEGIN;
# ALTER TABLE publ_edition
# ADD `dis_id` integer NOT NULL;
#
# ALTER TABLE `publ_edition`
# ADD CONSTRAINT `dis_id_refs_id_daf9326d`
# FOREIGN KEY (`dis_id`) REFERENCES `publ_dis` (`id`);
# COMMIT;


# department, institute, subdivision,
class DIS_Manager_Locale(models.Manager):
    def all_locale(self, language_code):
        cursor = connection.cursor()
        cursor.execute('''
             SELECT publ_dis.id,
                 publ_dis.dis_alias,
                 publ_dis_locale.dis_name
             FROM publ_dis LEFT JOIN publ_dis_locale 
                        ON publ_dis.id = publ_dis_locale.dis_id
             WHERE publ_dis_locale.lang_code = %s 
             ORDER BY publ_dis_locale.dis_name;
             ''', [language_code])
        result_list = []
        for raw in cursor.fetchall():
            p = self.model(id = raw[0], dis_alias = raw[1],)
            p.dis_name = raw[2]
            result_list.append(p)
        return result_list

class DIS(models.Model):
    dis_alias = models.CharField(max_length = 25, unique = True)

    objects = DIS_Manager_Locale()

    def __unicode__(self):
        return self.dis_alias

    class Meta:
        db_table = 'publ_dis'

class DIS_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    dis = ForeignKey(DIS)
    dis_name = models.CharField(max_length = 100, unique = True)

    def __unicode__(self):
        return self.dis_name

    class Meta:
        db_table = 'publ_dis_locale'
        unique_together = (("lang_code", "dis"),)


class Category_Manager_Locale(models.Manager):
    def all_locale(self, language_code):
        cursor = connection.cursor()
        cursor.execute('''
             SELECT publ_category.id,
                 publ_category.category_alias,
                 publ_category_locale.category_name
             FROM publ_category LEFT JOIN publ_category_locale 
                        ON publ_category.id = publ_category_locale.category_id
             WHERE publ_category_locale.lang_code = %s 
             ORDER BY publ_category_locale.category_name;
             ''', [language_code])
        result_list = []
        for raw in cursor.fetchall():
            p = self.model(id = raw[0], category_alias = raw[1],)
            p.category_name = raw[2]
            result_list.append(p)
        return result_list

class Category(models.Model):
    category_alias = models.CharField(max_length = 25, unique = True)

    objects = Category_Manager_Locale()

    def __unicode__(self):
        return self.category_alias

    class Meta:
        db_table = 'publ_category'

class Category_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    category = ForeignKey(Category)
    category_name = models.CharField(max_length = 200, unique = True)

    def __unicode__(self):
        return self.category_name

    class Meta:
        db_table = 'publ_category_locale'
        unique_together = (("lang_code", "category"),)

class FieldOfScience(models.Model):
    def __unicode__(self):
        fos_name = self.field_of_science_locale_set.model.objects.get(# field_of_science_id=self.id,
                    lang_code = get_language()).fos_name
        return fos_name
    class Meta:
        db_table = 'publ_field_of_science'

class FieldOfScience_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    field_of_science = ForeignKey(FieldOfScience)  # Field of science; Галузь науки
    fos_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.fos_name

    class Meta:
        db_table = 'publ_field_of_science_locale'
        unique_together = (("lang_code", "field_name"),)
        unique_together = (("lang_code", "field_of_science"),)

class Edition_Manager_Locale(models.Manager):
    def user_editions(self, language_code, user_id):
        cursor = connection.cursor()
        cursor.execute(
            """    
            SELECT
            publ_edition.id,
            auth_user.username,
            auth_user_user_permissions.user_id,
            auth_user_user_permissions.permission_id,
            auth_permission.name,
            auth_permission.codename,
            publ_edition.edition_alias,
            publ_edition.category_id,
            publ_edition_locale.lang_code,
            publ_edition_locale.edition_name,
            publ_edition_locale.edition_abbrev
            FROM 
            auth_permission
            JOIN auth_user_user_permissions
            ON auth_user_user_permissions.permission_id = auth_permission.id
            JOIN auth_user
            ON auth_user.id = auth_user_user_permissions.user_id
            JOIN publication_db.publ_edition
            ON auth_permission.codename = CONCAT('edit_' , publ_edition.edition_alias)
            JOIN publ_edition_locale 
            ON publ_edition_locale.edition_id = publ_edition.id
            WHERE publ_edition_locale.lang_code = %s AND auth_user.id = %s
            ORDER BY publ_edition_locale.edition_abbrev
            """
             , [language_code, user_id])
        result_list = []
        columns = tuple([d[0].decode('utf8') for d in cursor.description])
        for row in cursor.fetchall():
            dict_row = dict(zip(columns, row))
            p = self.model(id = dict_row["id"], edition_alias = dict_row["edition_alias"],)
            p.edition_abbrev = dict_row["edition_abbrev"]
            p.edition_name = dict_row["edition_name"]
            result_list.append(p)
        return result_list


    def all_locale(self, language_code):
        cursor = connection.cursor()
        cursor.execute('''
             SELECT publ_edition.id,
                 publ_edition.edition_alias,
                 publ_edition_locale.edition_name
             FROM publ_edition LEFT JOIN publ_edition_locale 
                        ON publ_edition.id = publ_edition_locale.edition_id
             WHERE publ_edition_locale.lang_code = %s 
             ORDER BY publ_edition_locale.edition_name
             ''', [language_code])
        result_list = []
        for raw in cursor.fetchall():
            p = self.model(id = raw[0], edition_alias = raw[1],)
            p.edition_name = raw[2]
            result_list.append(p)
        return result_list

    def category_locale(self, language_code, category):
        cursor = connection.cursor()
        cursor.execute('''
             SELECT publ_edition.id,
                 publ_edition.edition_alias,
                 publ_edition_locale.edition_name,
                publ_category.category_alias,
                (SELECT COUNT(*) 
                    FROM publ_issue
                    WHERE publ_issue.edition_id = publ_edition.id)
                    AS issue_cnt,
                (SELECT COUNT(*) 
                    FROM publ_article JOIN publ_issue 
                    ON publ_article.issue_id = publ_issue.id
                    WHERE publ_issue.edition_id = publ_edition.id
                ) AS artcl_cnt
             FROM publ_edition LEFT JOIN publ_edition_locale 
                            ON publ_edition.id = publ_edition_locale.edition_id
                        LEFT JOIN publ_category
                            ON publ_category.id = publ_edition.category_id
             WHERE publ_edition_locale.lang_code = %s 
                        AND publ_category.category_alias = %s
             ORDER BY publ_edition_locale.edition_name
             ''', [language_code, category])
        result_list = []
        for raw in cursor.fetchall():
            p = self.model(id = raw[0], edition_alias = raw[1],)
            p.edition_name = raw[2]
            p.issue_cnt = raw[4]
            p.artcl_cnt = raw[5]
            result_list.append(p)
        return result_list

class Edition(models.Model):
    edition_alias = models.CharField(max_length = 25, unique = True)
    category = ForeignKey(Category)
    dis = ForeignKey(DIS)
    # subject_matter = models.CharField(max_length = 500)  # subject matter; проблематика
    fields_of_science = models.ManyToManyField(FieldOfScience)  # Fields of science; Галузь науки
    foundation_year = models.PositiveIntegerField()  # Year of foundation; Рік заснування
    issues_by_year = models.PositiveSmallIntegerField()  # periodicity; periodicity
    # Certificate of registration; Свідоцтво про державну реєстрацію
    gov_certificate_date = models.DateField(null = True)
    gov_certificate_num = models.SlugField(max_length = 17)
    # professional registration in Ukraine VAC; Фахова реєстрація у ВАК України
    vac_certificate_date = models.DateField(null = True)
    vac_certificate_num = models.SlugField(max_length = 10)
    ISSN = models.SlugField(max_length = 9)
    # address = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 20)
    email = models.EmailField()

    objects = Edition_Manager_Locale()

    def __unicode__(self):
        return self.edition_alias

    class Meta:
        db_table = 'publ_edition'
#         permissions = (
#             ("edit_astronomy", "User can edit Astronomy edition"),
#             ("edit_biology", "User can edit Biology edition"),
#             ("edit_military", "User can edit Military edition"),
#             ("edit_geography", "User can edit Geography edition"),
#             ("edit_geology", "User can edit Geology edition"),
#             ("edit_economics", "User can edit Economics edition"),
#             ("edit_journalism", "User can edit Journalism edition"),
#             ("edit_philology", "User can edit Philology edition"),
#             ("edit_plant", "User can edit Plant edition"),
#             ("edit_history", "User can edit History edition"),
#             ("edit_cybernetics", "User can edit Cybernetics edition"),
#             ("edit_literature", "User can edit Literature edition"),
#             ("edit_math_mech", "User can edit Math_mech edition"),
#             ("edit_relations", "User can edit Relations edition"),
#             ("edit_phys_math", "User can edit Phys_math edition"),
#         )

class Edition_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    edition = ForeignKey(Edition)
    edition_name = models.CharField(max_length = 200, unique = True)
    edition_abbrev = models.CharField(max_length = 40)
    subject_matter = models.CharField(max_length = 500)  # subject matter; проблематика
    address = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.edition_abbrev

    class Meta:
        db_table = 'publ_edition_locale'
        unique_together = (("lang_code", "edition"), ("lang_code", "edition_abbrev"),)

class Issue(models.Model):
    issue_year = models.IntegerField()
    issue_num = models.IntegerField()  # year relative number
    edition = ForeignKey(Edition)

    def __unicode__(self):
        return _(u"number %d for %d year") % (self.issue_num, self.issue_year)

    class Meta:
        db_table = 'publ_issue'
        unique_together = (("issue_year", "issue_num", "edition"),)


class Rubric_Manager_Locale(models.Manager):
    def all_locale(self, language_code, series_alias):
        cursor = connection.cursor()
        cursor.execute('''
            SELECT publ_rubric.id,
                publ_rubric_locale.rubric_name,
                publ_rubric.rubric_order
            FROM publ_rubric LEFT JOIN publ_rubric_locale 
                    ON publ_rubric.id = publ_rubric_locale.rubric_id
                LEFT JOIN publ_edition
                    ON publ_edition.id = publ_rubric.edition_id
            WHERE publ_rubric_locale.lang_code = %s 
                    AND publ_edition.edition_alias = %s
            ORDER BY publ_rubric.rubric_order
            ''', [language_code, series_alias])
        result_list = []
        for raw in cursor.fetchall():
            p = self.model(id = raw[0], rubric_order = raw[2])
            p.locale_name = raw[1]
            result_list.append(p)
        return result_list

class Rubric(models.Model):
    edition = ForeignKey(Edition)
    rubric_order = models.IntegerField()
    objects = Rubric_Manager_Locale()

    def __unicode__(self):
        # rubric_locale
        name = self.rubric_locale_set.model.objects.get(rubric_id = self.id, lang_code = get_language()).rubric_name
        if name == '':
            name = _(u"There are no rubrics")
        return name  # str(self.id)

    class Meta:
        db_table = 'publ_rubric'
        unique_together = (("edition", "rubric_order"),)

class Rubric_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    rubric = ForeignKey(Rubric)
    rubric_name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.rubric_name

    class Meta:
        db_table = 'publ_rubric_locale'
        unique_together = (("rubric", "lang_code", "rubric_name"),)

class Author_Manager_Locale(models.Manager):
#     tuple_factory = tuple
#     def row_to_dict(self, rowdata):
#             try:
#                 desc = self.description
#                 to_python = self._connection.converter.to_python
#                 gen = (to_python(desc[i], v) for i, v in enumerate(rowdata))
#                 return self.tuple_factory(gen)
#             except StandardError, e:
#                 raise DatabaseError("Failed converting row to Python types; %s" % e)

    def article_authors_locale(self, language_code, article_id):
        cursor = connection.cursor()
#         sql_text = '''
#              SELECT publ_author.id,
#                          publ_author_locale.first_name,
#                          publ_author_locale.middle_name,
#                          publ_author_locale.last_name,
#
#                          CONCAT(
#                             UPPER(LEFT(publ_author_locale.last_name,1)),
#                                             RIGHT(publ_author_locale.last_name,
#                                             CHAR_LENGTH(publ_author_locale.last_name)-1),
#                             ' ',
#                             UPPER(LEFT(publ_author_locale.first_name,1)), '.',
#
#                             IF(CHAR_LENGTH(publ_author_locale.middle_name) > 0,
#                                 CONCAT(UPPER(LEFT(publ_author_locale.middle_name,1)), '.'),
#                                 ''
#                                 )
#                          )AS full_name
#              FROM publ_author
#                         LEFT JOIN publ_author_locale
#                              ON publ_author.id = publ_author_locale.author_id
#                         LEFT JOIN publ_article_authors
#                              ON publ_article_authors.author_id = publ_author.id
#              WHERE publ_author_locale.lang_code = %(lang_code)s
#                              AND publ_article_authors.article_id = %(article_id)d
#             ORDER BY publ_article_authors. author_order
#              '''
#         sql_parms = {"lang_code": language_code, "article_id": article_id}
#         cursor.execute(sql_text, sql_parms)
        sql_string = """
                     SELECT publ_author.id,
                         publ_author_locale.first_name,
                         publ_author_locale.middle_name,
                         publ_author_locale.last_name,

                         CONCAT(
                            UPPER(LEFT(publ_author_locale.last_name,1)),
                                            RIGHT(publ_author_locale.last_name,
                                            CHAR_LENGTH(publ_author_locale.last_name)-1),
                            ' ',
                            UPPER(LEFT(publ_author_locale.first_name,1)), '.',
                        
                            IF(CHAR_LENGTH(publ_author_locale.middle_name) > 0,
                                CONCAT(UPPER(LEFT(publ_author_locale.middle_name,1)), '.'), 
                                ''
                                )
                         )AS full_name
             FROM publ_author 
                        LEFT JOIN publ_author_locale
                             ON publ_author.id = publ_author_locale.author_id
                        LEFT JOIN publ_article_authors
                             ON publ_article_authors.author_id = publ_author.id
             WHERE publ_author_locale.lang_code = '%(lang_code)s' 
                             AND publ_article_authors.article_id = %(article_id)d
             ORDER BY publ_article_authors. author_order

        """ % {"lang_code": language_code, "article_id": article_id}
        # sql_parms = {"lang_code": language_code, "article_id": article_id}
        # sql_parms = {"article_id": article_id}

        cursor.execute(sql_string)

        result_list = []
        columns = tuple([d[0].decode('utf8') for d in cursor.description])
#        field_names = tuple(d.attname for d in self.model._meta.fields)
        for row in cursor.fetchall():
            dict_row = dict(zip(columns, row))
            p = self.model(id = dict_row["id"],)
            p.first_name = dict_row["first_name"]
            p.middle_name = dict_row["middle_name"]
            p.last_name = dict_row["last_name"]
            p.full_name = dict_row["full_name"]
            result_list.append(p)
        return result_list

class Author(models.Model):
    objects = Author_Manager_Locale()

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'publ_author'

class Author_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    author = ForeignKey(Author)
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    def _get_full_name(self):
        return '%s. %s. %s' % (self.first_name[:1], self.middle_name[:1], self.last_name)
    full_name = property(_get_full_name)
    def __unicode__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    class Meta:
        db_table = 'publ_author_locale'
        unique_together = (("lang_code", "author"),)

class Article_Manager_Locale(models.Manager):
    def one_issue(self, language_code, edition_alias, issue_year, issue_num):
        cursor = connection.cursor()
        sql_text = """
             SELECT publ_edition.edition_alias, 
                             publ_article.id,
                             publ_article.issue_id,
                             publ_article.rubric_id,
                             publ_article.file_name,
                             publ_issue.issue_year,
                             publ_issue.issue_num,
                             publ_rubric_locale.rubric_name,
                             publ_article_locale.caption,
                             publ_article_locale.abstract
             FROM publ_article 
                            LEFT JOIN publ_article_locale 
                                    ON publ_article.id = publ_article_locale.article_id
                            LEFT JOIN publ_issue 
                                    ON publ_article.issue_id = publ_issue.id
                            LEFT JOIN publ_edition
                                    ON publ_edition.id = publ_issue.edition_id
                            LEFT JOIN publ_rubric 
                                    ON publ_rubric.id = publ_article.rubric_id
                            LEFT JOIN publ_rubric_locale 
                                    ON publ_rubric.id = publ_rubric_locale.rubric_id
             WHERE publ_article_locale.lang_code = %(lang_code)s
                        AND publ_edition.edition_alias = %(edition)s 
                        AND publ_rubric_locale.lang_code = %(lang_code)s
                        AND publ_issue.issue_year = %(issue_year)s
                        AND publ_issue.issue_num = %(issue_num)s
             ORDER BY publ_rubric.rubric_order, publ_article_locale.caption
         """
        sql_parms = {"lang_code": language_code,
                "edition": edition_alias,
                "issue_year": issue_year,
                "issue_num": issue_num}
        cursor.execute(sql_text, sql_parms)
        result_list = []
        columns = tuple([d[0].decode('utf8') for d in cursor.description])
        for row in cursor.fetchall():
            dict_row = dict(zip(columns, row))
            p = self.model(id = dict_row["id"],
                issue_id = dict_row["issue_id"],
                rubric_id = dict_row["rubric_id"],
                file_name = dict_row["file_name"],
            )
            p.edition_alias = dict_row["edition_alias"]
            p.issue_year = dict_row["issue_year"]
            p.issue_num = dict_row["issue_num"]
            p.rubric_name = dict_row["rubric_name"]
            p.caption = dict_row["caption"]
            p.abstract = dict_row["abstract"]
            p.authors_list = Author.objects.article_authors_locale(language_code, p.id)
            result_list.append(p)
        return result_list

class Article(models.Model):
    authors = models.ManyToManyField(Author, through = "Article_Authors")
    issue = models.ForeignKey(Issue)
    rubric = models.ForeignKey(Rubric)
    file_name = models.CharField(max_length = 250)

    objects = Article_Manager_Locale()

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'publ_article'


class Article_Authors(models.Model):
    article = ForeignKey(Article)
    author = ForeignKey(Author)
    author_order = models.IntegerField()

    def __unicode__(self):
        return 'article: %s author: %s' % (self.article, self.author)

    class Meta:
        db_table = 'publ_article_authors'
        unique_together = (("article", "author_order"),
                           ("article", "author"),
                           )

class Article_Locale(models.Model):
    lang_code = models.CharField(max_length = 2)
    article = ForeignKey(Article)
    caption = models.CharField(max_length = 250)
    abstract = models.TextField()

    def __unicode__(self):
        return self.caption

    class Meta:
        db_table = 'publ_article_locale'
        unique_together = (("lang_code", "article"),)
