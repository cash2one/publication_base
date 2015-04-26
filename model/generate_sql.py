# -*- coding: utf-8 -*-

from django.db import models as m
import MySQLdb

from model.models import *
from publication_base.views import lng_code_en as en, lng_code_ukr as uk
import data

class sql_not_implemented(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def justify_number(num, width):
    """
    add trailing zeros to fit the width
    """
    assert type(num) is int or type(num) is long
    assert num >= 0
    # calc the current number size
    x = num
    size = 1
    while x > 9:
        x /= 10
        size += 1

    assert size <= width
    alig_num = num
    while size < width:
        alig_num *= 10
        size += 1

    return alig_num

def fos_lst():
    """
    field of science
    """

    fos_lst = [
               (u"фізико-математичні науки", u"physical and mathematical sciences"),
               (u"природничі науки", u"natural sciences"),
               (u"економічні науки", u"economics"),
               (u"філологічні науки", u"philology"),
               (u"біологічні науки", u"life sciences"),
               (u"історичні науки", u"history sciences"),
               (u"мовознавство", u"linguistics"),
               (u"літературознавство", u"study of literature"),
               (u"політичні науки", u"political sciences"),
               (u"юридичні науки", u"jurisprudence"),
               (u"філософські науки", u"philosophy sciences"),
              ]
    return fos_lst

def generate_field_of_science_sql():
    fos = fos_lst()
    for i, (uk_name, en_name) in enumerate(fos):
        obj_fos = FieldOfScience(id = i + 1)
        obj_fos.save()
        fos_locale = FieldOfScience_Locale(id = (i + 1) * 2 - 1,
                                  lang_code = uk,
                                  fos_name = uk_name,
                                  field_of_science = obj_fos,
                                  )
        fos_locale.save()
        fos_locale = FieldOfScience_Locale(id = (i + 1) * 2,
                                  lang_code = en,
                                  fos_name = en_name,
                                  field_of_science = obj_fos,
                                  )
        fos_locale.save()

def gen_insert_query(model_cls, **kw_attrib):
    tbl_name = model_cls._meta.db_table
    # print tbl_name
    # fld_names_ustr = u""
    # fld_vals_ustr = u""
    val_lst = []
    fld_lst = []
    for fld in model_cls._meta.fields:
        try:
            fld_val = kw_attrib[fld.attname]
            if fld_val is None:
                db_val = "NULL"
                val_lst.append(db_val)
                fld_lst.append(fld.attname)
            else:
                db_val = convert_to_sql_str(fld, fld_val)
                val_lst.append(db_val)
                fld_lst.append(fld.attname)
        except KeyError:
            pass
    # print val_lst
    # print fld_lst
    sql_txt_insert = u"INSERT INTO {0}\n({1})\nVALUES({2})\n".format(
                                                         tbl_name,
                                                         ", ".join(fld_lst),
                                                         ", ".join(val_lst)
                                                         )
    fv_lst = [ f + "=" + v for (f, v) in zip(fld_lst, val_lst)]

    sql_txt_update = u"ON DUPLICATE KEY UPDATE\n{0};\n".format(", \n".join(fv_lst))
#     s = \
#     """
# INSERT INTO publ_field_of_science_locale(
#         id,
#         lang_code,
#         field_of_science_id,
#         fos_name
#         )
# VALUES(1, "uk", 1, "фізико-математичні науки")
# ON DUPLICATE KEY UPDATE
#         lang_code = "uk",
#         field_of_science_id = 1,
#         fos_name = "фізико-математичні науки"
# ;
#     """

    return sql_txt_insert + sql_txt_update

def gen_insert_query2(tbl_name, tbl_fields, **kw_attrib):
    # print tbl_name
    # fld_names_ustr = u""
    # fld_vals_ustr = u""
    val_lst = []
    fld_lst = []
    for fld in tbl_fields:
        fld_val = kw_attrib[fld.attname]
        if fld_val is None:
            db_val = "NULL"
            val_lst.append(db_val)
            fld_lst.append(fld.attname)
        else:
            db_val = convert_to_sql_str(fld, fld_val)
            val_lst.append(db_val)
            fld_lst.append(fld.attname)
    # print val_lst
    # print fld_lst
    sql_txt_insert = u"INSERT INTO {0}\n({1})\nVALUES({2})\n".format(
                                                         tbl_name,
                                                         ", ".join(fld_lst),
                                                         ", ".join(val_lst)
                                                         )
    fv_lst = [ f + "=" + v for (f, v) in zip(fld_lst, val_lst)]

    sql_txt_update = u"ON DUPLICATE KEY UPDATE\n{0};\n".format(", \n".join(fv_lst))
    return sql_txt_insert + sql_txt_update


def convert_to_sql_str(fld, val):

    if val is None:
        return "NULL"
    if type(fld) is m.AutoField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.BooleanField:
        assert type(val) is bool
        if val:
            return u"1"
        else:
            return u"0"
    elif type(fld) is m.CharField:
        assert is_char_type(val)
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.CommaSeparatedIntegerField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.DateField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.DateTimeField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.DecimalField:
        assert type(val) is int or type(val) is long or type(val) is float
        return unicode(val)
    elif type(fld) is m.EmailField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.FileField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.FilePathField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.FloatField:
        assert type(val) is float
        return unicode(val)
    elif type(fld) is m.ImageField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.IntegerField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.IPAddressField:
        raise sql_not_implemented("Conversion of the IPAddressField is not implemented")
    elif type(fld) is m.NullBooleanField:
        assert val is None or type(val) is bool
        if val is None:
            return u"Null"
        elif val:
            return u"1"
        else:
            return u"0"
    elif type(fld) is m.PositiveIntegerField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.PositiveSmallIntegerField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.SlugField:
        assert type(val) is str or type(val) is unicode
        return unicode("'" + escape_sql_str(val) + "'")
    elif type(fld) is m.SmallIntegerField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.TextField:
        raise sql_not_implemented("Conversion of the TextField is not implemented")
    elif type(fld) is m.TimeField:
        raise sql_not_implemented("Conversion of the TimeField is not implemented")
    elif type(fld) is m.URLField:
        raise sql_not_implemented("Conversion of the URLField is not implemented")
    elif type(fld) is m.ForeignKey:
        assert type(val) is int or type(val) is long
        return unicode(val)
    elif type(fld) is m.ManyToManyField:
        raise sql_not_implemented("Conversion of the ManyToManyField is not implemented")
    elif type(fld) is m.OneToOneField:
        assert type(val) is int or type(val) is long
        return unicode(val)
    else:
        raise sql_not_implemented("undefined type")

def is_char_type(val):
    return (type(val) is str) or (type(val) is unicode)

def escape_sql_str(s):
    s = s.replace("\\", "\\\\'")
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    s = s.replace("%", "\\%")
#    s = s.replace("_", "\\_")

    return s

def generate_field_of_science():
    fos_lst = [
               (u"фізико-математичні науки", u"physical and mathematical sciences"),
               (u"природничі науки", u"natural sciences"),
               (u"економічні науки", u"economics"),
               (u"філологічні науки", u"philology"),
               (u"біологічні науки", u"life sciences"),
               (u"історичні науки", u"history sciences"),
               (u"мовознавство", u"linguistics"),
               (u"літературознавство", u"study of literature"),
               (u"політичні науки", u"political sciences"),
               (u"юридичні науки", u"jurisprudence"),
               (u"філософські науки", u"philosophy sciences"),
              ]

    for i, (uk_name, en_name) in enumerate(fos_lst):
        id = i + 1
        sql_txt = gen_insert_query(FieldOfScience, id = id)
        print sql_txt
        sql_locale_uk = gen_insert_query(FieldOfScience_Locale,
                                         id = (i + 1) * 2 - 1,
                                         lang_code = uk,
                                         fos_name = uk_name,
                                         field_of_science_id = id,)
        print sql_locale_uk
        sql_locale_en = gen_insert_query(FieldOfScience_Locale,
                                         id = (i + 1) * 2,
                                         lang_code = en,
                                         fos_name = en_name,
                                         field_of_science_id = id,)
        print sql_locale_en

# def generate_category():
#     category_lst = [  (data.HERALD, u"вісник", u"bulletin"),
#                     (data.JOURNAL, u"журнал", u"journal"),
#                     (data.CONFERENCE, u"конференція", u"conerence"),
#                   ]
#     for i, (alias, uk_name, en_name) in enumerate(category_lst):
#         cat_id = i + 1
#         sql_txt = gen_insert_query(Category, id = cat_id, category_alias = alias)
#         sql_locale_uk = gen_insert_query(Category_Locale,
#                                          id = (i + 1) * 2 - 1,
#                                          lang_code = uk,
#                                          category_name = uk_name,
#                                          category_id = cat_id,
#                                          )
#         sql_locale_en = gen_insert_query(Category_Locale,
#                                          id = (i + 1) * 2,
#                                          lang_code = en,
#                                          category_name = en_name,
#                                          category_id = cat_id,
#                                          )
#
#         print sql_txt
#         print sql_locale_uk
#         print sql_locale_en

def gen_mtom_query(table_name, id, **kwfields):

    name_lst = []
    val_lst = []
    attrib_lst = []
    for f_name, f_val in kwfields.iteritems():
        name_lst.append(f_name)
        val_lst.append(str(f_val))
        attrib_lst.append("{0}={1}".format(f_name, f_val))

    sql_txt_insert = u"INSERT INTO {0}\n(id, {1})\nVALUES({2}, {3})\n".format(
                                                         table_name,
                                                         ", ".join(name_lst),
                                                         id,
                                                         ", ".join(val_lst)
                                                         )


    sql_txt_update = u"ON DUPLICATE KEY UPDATE\n id={0}, {1};\n".format(id, ", \n".join(attrib_lst))
    sql_txt_full = sql_txt_insert + sql_txt_update
    return sql_txt_full

def generate_edition(edition):

    edtn_id = edition[data.edition_id]
    edition_dic = edition[data.edition_dic]

    obj_category = Category.objects.get(category_alias = edition_dic[data.category])

    id_base = justify_number(edtn_id, 5)
    sql_txt = gen_insert_query(Edition,
                               id = edtn_id,
                               edition_alias = edition_dic[data.alias],
                               dis_id = edition_dic[data.dis_id],
                               category_id = obj_category.id,
                               foundation_year = edition_dic[data.foundation_year],
                               issues_by_year = edition_dic[data.issues_by_year],
                               gov_certificate_date = edition_dic[data.gov_certificate_date],
                               gov_certificate_num = edition_dic[data.gov_certificate_num],
                               vac_certificate_date = edition_dic[data.vac_certificate_date],
                               vac_certificate_num = edition_dic[data.vac_certificate_num],
                               ISSN = edition_dic[data.ISSN],
                               phone = edition_dic[data.phone],
                               email = edition_dic[data.email],
                          )

    print sql_txt

    for f in edition_dic[data.field_of_science_lst]:
        fos_obj = fos_obj = FieldOfScience.objects.get(
                                                       fieldofscience_locale__lang_code = uk,
                                                       fieldofscience_locale__fos_name = f,
                                                       )
        assert fos_obj.id <= 99
        assert edtn_id <= 999
        edtn_fos_sql = gen_mtom_query(u"publ_edition_fields_of_science",
                                      id_base + fos_obj.id,
                                      edition_id = edtn_id,
                                      fieldofscience_id = fos_obj.id)
        print edtn_fos_sql



    if len(edition_dic[data.uk_abbrev]) == 0:
        edition_dic[data.uk_abbrev] = edition_dic[data.uk_name]
    if len(edition_dic[data.en_abbrev]) == 0:
        edition_dic[data.en_abbrev] = edition_dic[data.en_name]

    locale_uk_sql = gen_insert_query(Edition_Locale,
                                     id = (edtn_id + 1) * 2 - 1,
                                     lang_code = uk,
                                     edition_name = edition_dic[data.uk_name],
                                     edition_abbrev = edition_dic[data.uk_abbrev],
                                     subject_matter = edition_dic[data.subject_matter_uk],
                                     address = edition_dic[data.address_uk],
                                     edition_id = edtn_id,
                                     )


    locale_en_sql = gen_insert_query(Edition_Locale,
                                     id = (edtn_id + 1) * 2,
                                     lang_code = en,
                                     edition_name = edition_dic[data.en_name],
                                     edition_abbrev = edition_dic[data.en_abbrev],
                                     subject_matter = edition_dic[data.subject_matter_en],
                                     address = edition_dic[data.address_en],
                                     edition_id = edtn_id,
                                     )
    print locale_uk_sql
    print locale_en_sql
    generate_rubric(edtn_id, edition_dic[data.rubric_lst])

def generate_edition_list(edition_lst):
    for i, edition_dic in enumerate(edition_lst):
        obj_category = Category.objects.get(category_alias = edition_dic["category"])
        edtn_id = i + 1
        id_base = justify_number(edtn_id, 5)
        sql_txt = gen_insert_query(Edition,
                                   id = edtn_id,
                                   dis_id = edition_dic["dis_id"],
                                   edition_alias = edition_dic["alias"],
                                   category_id = obj_category.id,
                                   foundation_year = edition_dic["foundation_year"],
                                   issues_by_year = edition_dic["issues_by_year"],
                                   gov_certificate_date = edition_dic["gov_certificate_date"],
                                   gov_certificate_num = edition_dic["gov_certificate_num"],
                                   vac_certificate_date = edition_dic["vac_certificate_date"],
                                   vac_certificate_num = edition_dic["vac_certificate_num"],
                                   ISSN = edition_dic["ISSN"],
                                   phone = edition_dic["phone"],
                                   email = edition_dic["email"],
                              )

        print sql_txt

        for f in edition_dic["FieldOfScience"]:
            fos_obj = fos_obj = FieldOfScience.objects.get(
                                                           fieldofscience_locale__lang_code = uk,
                                                           fieldofscience_locale__fos_name = f,
                                                           )
            assert fos_obj.id <= 99
            assert edtn_id <= 999
            edtn_fos_sql = gen_mtom_query(u"publ_edition_fields_of_science",
                                          id_base + fos_obj.id,
                                          edition_id = edtn_id,
                                          fieldofscience_id = fos_obj.id)
            print edtn_fos_sql



        if len(edition_dic["uk_abbrev"]) == 0:
            edition_dic["uk_abbrev"] = edition_dic["uk_name"]
        if len(edition_dic["en_abbrev"]) == 0:
            edition_dic["en_abbrev"] = edition_dic["en_name"]

        locale_uk_sql = gen_insert_query(Edition_Locale,
                                         id = (i + 1) * 2 - 1,
                                         lang_code = uk,
                                         edition_name = edition_dic["uk_name"],
                                         edition_abbrev = edition_dic["uk_abbrev"],
                                         subject_matter = edition_dic["subject_matter_uk"],
                                         address = edition_dic["address_uk"],
                                         edition_id = edtn_id,
                                         )


        locale_en_sql = gen_insert_query(Edition_Locale,
                                         id = (i + 1) * 2,
                                         lang_code = en,
                                         edition_name = edition_dic["en_name"],
                                         edition_abbrev = edition_dic["en_abbrev"],
                                         subject_matter = edition_dic["subject_matter_en"],
                                         address = edition_dic["address_en"],
                                         edition_id = edtn_id,
                                         )
        print locale_uk_sql
        print locale_en_sql
        generate_rubric(edtn_id, edition_dic['rubric'])

def generate_rubric(edtn_id, rubric_lst):

    assert edtn_id <= 999
    id_base = justify_number(edtn_id, 5)
    for (order, uk_name, en_name) in rubric_lst:
        id = id_base + order
        rubric_sql = gen_insert_query(Rubric,
                                      id = id,
                                      edition_id = edtn_id,
                                      rubric_order = order)
        print rubric_sql
        locale_uk_sql = gen_insert_query(Rubric_Locale,
                                         id = (id + 1) * 2 - 1,
                                         lang_code = uk,
                                         rubric_name = uk_name,
                                         rubric_id = id,
                                   )
        locale_en_sql = gen_insert_query(Rubric_Locale,
                                         id = (id + 1) * 2,
                                         lang_code = en,
                                         rubric_name = en_name,
                                         rubric_id = id,
                                   )
        print locale_uk_sql
        print locale_en_sql

def generate_dis(dis_lst):

    for (dis_id, dis_alias, uk_name, en_name) in dis_lst:
        dis_sql = gen_insert_query(DIS,
                                  id = dis_id,
                                  dis_alias = dis_alias)
        print dis_sql
        locale_uk_sql = gen_insert_query(DIS_Locale,
                                         id = dis_id * 2 - 1,
                                         lang_code = uk,
                                         dis_name = uk_name,
                                         dis_id = dis_id,
                                   )
        locale_en_sql = gen_insert_query(DIS_Locale,
                                         id = dis_id * 2,
                                         lang_code = en,
                                         dis_name = en_name,
                                         dis_id = dis_id,
                                   )
        print locale_uk_sql
        print locale_en_sql


def generate_permission():
    class Permission(m.Model):
        name = models.CharField(max_length = 50)
        content_type_id = models.IntegerField()
        codename = models.CharField(max_length = 100)
        class Meta:
            db_table = 'auth_permission'
            app_label = 'generate.py'


    lst = data.permissions_lst
    for (codename, name, content_type_id) in lst:
        permission_sql = gen_insert_query(Permission,
                                  codename = codename,
                                  name = name,
                                  content_type_id = content_type_id)
        print permission_sql

def test_get_insert_query():
    sql_txtu = gen_insert_query(
                           FieldOfScience_Locale,
                           id = 1,
                           lang_code = uk,
                           fos_name = u"kkjjjj",
                           field_of_science_id = 1
                           )
    f = open("d:\\test.txt", "w")
    f.write(sql_txtu)
    f.close()

if __name__ == "__main__":
#    generate_permission()
#    generate_dis(data.dis_lst)
    generate_edition(data.edtnm_cybernetics)
#    print justify_number(99, 10)
