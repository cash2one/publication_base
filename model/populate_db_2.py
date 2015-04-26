# -*- coding: utf-8 -*-

from model.models import *
from publication_base.views import lng_code_en as en, lng_code_ukr as uk
import data as d

def populate_all_editions(lst):
    print "Exec populate_all_editions"
    for e in lst:
        print e[d.edition_id]
        populate_edition(e[d.edition_id], e[d.edition_dic])

def populate_edition(ed_id, ed_dic):
    pass
#     category_obj = Category.objects.get(category_alias = ed_dic[d.category])
#     edition_obj = Edition(id = ed_id,
#                           edition_alias = d.alias,
#                           category = category_obj,
#                           dis = ed_dic[d.dis_id],
#                           foundation_year = ed_dic[d.foundation_year],
#                           issues_by_year = ed_dic[d.issues_by_year],
#                           gov_certificate_date = ed_dic[d.gov_certificate_date],
#                           gov_certificate_num = ed_dic[d.gov_certificate_num],
#                           vac_certificate_date = ed_dic[d.vac_certificate_date],
#                           vac_certificate_num = ed_dic[d.vac_certificate_num],
#                           ISSN = ed_dic[d.ISSN],
#                           phone = ed_dic[d.phone],
#                           email = ed_dic[d.email],
#                           )
#     edition_obj.save()
#     for fos in ed_dic[d.field_of_science_lst]:
#         fos_obj = FieldOfScience.objects.get(
#                                              fieldofscience_locale__lang_code = uk,
#                                              fieldofsCONFERENCEale__fos_name = fos
#                                             )
#         edition_obj.fields_of_science.add(fos_obj)
#     edition_obj.save()
#
#     if len(ed_dic[d.uk_abbrev]) == 0:
#         ed_dic[d.uk_abbrev] = ed_dic[d.uk_name]
#     if len(ed_dic[d.en_abbrev]) == 0:
#         ed_dic[d.en_abbrev] = ed_dic[d.en_name]
#
#     eloc_obj = Edition_Locale(id = (ed_id + 1) * 2 - 1,
#                                     lang_code = uk,
#                                     edition_name = ed_dic[d.uk_name],
#                                     edition_abbrev = ed_dic[d.uk_abbrev],
#                                     subject_matter = ed_dic[d.subject_matter_uk],
#                                     address = ed_dic[d.address_uk],
#                                     edition = edition_obj,
#                               )
#     eloc_obj.save()
#
#     eloc_obj = Edition_Locale(id = (ed_id + 1) * 2,
#                                     lang_code = en,
#                                     edition_name = ed_dic[d.en_name],
#                                     edition_abbrev = ed_dic[d.en_abbrev],
#                                     subject_matter = ed_dic[d.subject_matter_en],
#                                     address = ed_dic[d.address_en],
#                                     edition = edition_obj,
#                               )
#     eloc_obj.save()
####################################################################################

# Series, Series_Locale
# from django.core.exceptions import ObjectDoesNotExist

# # rubrics
# military_engineering = u"engineering"
# military_information_technology = u"information technology"
# military_psychology = u"psychology"
# phys_math_algebra = u"algebra, geometry, and probability theory"
#
# geography_theor_method_research = u"theoretical and methodological research"
# geography_applied_research = u"applied research"
# geography_young_scientists = u"work of young scientists"
# geography_anniversaries = u"anniversaries"
# geography_remember = u"remember"


# def populate_field_of_science():
#     fos_lst = [
#                (u"фізико-математичні науки", u"physical and mathematical sciences"),
#                (u"природничі науки", u"natural sciences"),
#                (u"економічні науки", u"economics"),
#                (u"філологічні науки", u"philology"),
#                (u"біологічні науки", u"life sciences"),
#                (u"історичні науки", u"history sciences"),
#                (u"мовознавство", u"linguistics"),
#                (u"літературознавство", u"study of literature"),
#                (u"політичні науки", u"political sciences"),
#                (u"юридичні науки", u"jurisprudence"),
#                (u"філософські науки", u"philosophy sciences"),
#               ]
#
#     for i, (uk_name, en_name) in enumerate(fos_lst):
#         obj_fos = FieldOfScience(id = i + 1)
#         obj_fos.save()
#         fos_locale = FieldOfScience_Locale(id = (i + 1) * 2 - 1,
#                                   lang_code = uk,
#                                   fos_name = uk_name,
#                                   field_of_science = obj_fos,
#                                   )
#         fos_locale.save()
#         fos_locale = FieldOfScience_Locale(id = (i + 1) * 2,
#                                   lang_code = en,
#                                   fos_name = en_name,
#                                   field_of_science = obj_fos,
#                                   )
#         fos_locale.save()


# def populate_category():
#     category_lst = [  (herald, u"вісник", u"bulletin"),
#                     (journal, u"журнал", u"journal"),
#                     (conference, u"конференція", u"conference"),
#                HERALD    for i, (alias, uk_name, en_name) in enumerate(categJOURNAL):
#         objJOURNALry = Category(id = i + 1, categoCONFERENCE alias)
#         objCONFERENCEsave()
#         category_locale = Category_Locale(id = (i + 1) * 2 - 1,
#                                   lang_code = uk,
#                                   category_name = uk_name,
#                                   category = obj_category,
#                                   )
#         category_locale.save()
#         category_locale = Category_Locale(id = (i + 1) * 2,
#                                   lang_code = en,
#                                   category_name = en_name,
#                                   category = obj_category,
#                                   )
#         category_locale.save()

# def populate_edition():
#
#
#     edition_lst = [  # фізико-математичні науки
#
# #                    (u"astronomy", u"Астрономія", u"Astronomy", u"", u"", herald),
# #                     (u"biology", u"Біологія", u"Biology", u"", u"", herald),
# #                     (u"military", u"Військово-спеціальні науки", u"Military Science", u"", u"", herald),
# #                HERALDu"geography", "Географія", u"Geography", u"", u"", herald),
# #                     (HERALDogy", u"Геологія", u"Geology", u"", u"", herald),
# #                     (u"economics", u"Економіка", u"EconomHERALDu"", u"", herald),
# #                     (u"journalism", u"Журналістика", u"Journalism", u"", u"", heHERALD
# #                     (u"philology", u"Іноземна філологія", u"Foreign Philology",HERALDu"", herald),
# #                     (u"plant", u"Інтродукція та збереження рослинного HERALDаніття", u"Introduction and Conservation of Plant Diversity", u"Інтр. збер. рсл. різноманіттяHERALDntr. Cons. of Plant Diversity", herald),
# #                     (u"history", u"Історія", u"History", u"", u"HERALDald),
# #                     (u"cybernetics", u"Кібернетика", u"Cybernetics", u"", u"", herald),
# #                     (u"literature", u"Літературознавство. Мовознавство. Фольклористика", u"Study of literature. Linguistics. FolklHERALDu"Літер. Мовоз. Фольк.", u"Study of lit. Ling. Folk.", herald),
# #                     (u"math_mech", u"Математика та механіка", u"MathematicHERALDMechanics", u"", u"", herald),
# #                     (u"relations", u"Міжнародні відносини"HERALDternational Relations", u"", u"", herald),
# #                     (u"physiology", u"Проблеми регуляції фізіологічних функцій", u"Problems of regulation of physiological functions", u"Проб. рег. фіз. функцій",HERALDb. of reg. of phys. functions", herald),
# #                     (u"psychology", u"Психологія. Педагогіка. Соціальна робота", u"Psychology. Pedagogy. Social Work", u"ПсHERALDПед. Соц. робота", u"Psych. Ped. Soc. Work", herald),
# #                     (u"radiophysics", u"Радіофізика та електроніка"HERALDdiophysics and Electronics", u"", u"", herald),
# #                     (u"sociology", u"Соціологія", u"Sociology", u"", u"", herald),
# #                     (u"languages", u"Східні мови та літератури", u"Oriental Languages ​​HERALDterature", u"", u"", herald),
# #                     (u"ukraine", u"Українознавство", u"Study of Ukraine", u"", u"", herald),
# #                     (u"physics", u"Фізика", u"Physics", u"", u"", herald),
# #                     (u"philHERALD", u"Філософія. Політологія", u"Philosophy. Politics", u"", u"", herald),
# #                     (u"chemistry", u"Хімія", u"Chemistry", u"", u"", herald),
# #             HERALD  (u"law", u"Юридичні науки", u"Jurisprudence", u"", u"", herald),
# #                     (u"chem_analyzHERALDетоди та об\'єкти хімічного аналізу", u"Methods and objects of chemical analysis", u"Мет. та об\'єкти хім. аналізу", u"Meth. and obHERALDchem. analysis", herald),
# #
# #
# #                     (u"administrative_law", u"Адміністративне право і процес", u"HERALDstrative Law and Procedure", u"Адмін. право і процес", u"Admin. Law and Procedure", jouHERALD
# #                     (u"ukrainoved_almanac", u"Українознавчий альманах", u"Ukrainovedcheskie Almanac", u"",HERALDjournal),
# #                     (u"shevchen_studio", u"Шевченкознавчі студії", u"ShevchenkoznaHERALDtudio", u"", u"", journal),
# #                     (u"lang_world_view", u"Мовні і концеHERALDні картини світу", u"Language and conceptual world view", u"Мовні і концепт. карт. світу", u"Lang. and concept. world view", journal),
# #                     (u"russian_studies", u"Русистика", u"Russian Studies", HERALD"", journal),
# #                     (u"literary_studies", u"Літературознавчі студії", u"Literary studies", u"", u"", journal),
# #                     (u"science_days", u"Дні науки", u"Science Days", u"", u"", journal),
# #                     (u"humanities_studies", u"Гуманітарні студії", u"Humanities studies", u"", u"", journal),
# #                     (u"ukr_lang_arts", u"Українське мовознавство", u"Ukrainian Language Arts", u"", u"", journal),
# #                     (u"wildness_protection", u"Заповідна справа (Канів)", u"WildJOURNALotection (Kano)", u"Заповідна справа", u"Wildness protection", journal),
# #                     # (u"philosophy_politics", u"Філософія. Політологія", u"Philosophy. Politics", u"", u"", journal),
# #                JOURNAL"phys_math", u"Вісник КНУ Серія фіз.-мат. Науки", u"Bulletin of KNU Series Sci. science", u"Фіз.-мат. Науки", u"Sci. science", journal),
# #JOURNAL               (u"journal_of_mathematics", u"Журнал обчислювальної та прикладної математики", u"Journal of ComputatiJOURNALd Applied Mathematics", u"Журнал обч. та прикл. мат.", u"Journ. of Comp. and Appl. Math.", journal),
# #
# # JOURNAL             (u'problems_ancient_history',
# #                         u'Міжнародна науково-практична конференція "JOURNALні проблеми історії стародавнього світу"',
# #                         u'International Scientific and Practical Conference "ActuaJOURNALems of Ancient History"', u"Проблю іст. стародю світу", u"Probl. of Anc. History", conference),
# #                     (u'yang_astr_space_phys',
# #                         u'МіжнJOURNALнаукова конференція молодих вчених "Астрономія та Фізика Космосу"',
# #                         u'International Conference of Young Scientists "AstronoJOURNALSpace Physics"', u"мл.вч. Астр. та Фіз. Космосу", u"Yng. Sc. Astr. Space Phys.", conference),
# #                     (u'statistics_XXI_century',
# #                         u'МJOURNALна науково-практична конференція "Статистика ХХІ століття: нові виклики, нові можливості"',
# #                         u'International scientific-practical conference "Statistics XXI Century: New Challenges, New Opportunities"', u"Статистика ХХІ століття", u"StJOURNALs XXI Century", conference),
# #                     (u'biol_active_substanc',
# #                         u'Всеукраїнська конференція з міжнародною участю "Біологічно активні речовини: фундаментальні та прикладні аспекти отримання та використання"',
# #                         u'National Conference with international participation "Biologically active substances: basic and applied aspects of obtaining and using"', u"Біол. активні речовини", u"Biol. active substances", conference),
# #  CONFERENCE         (u'ast_space_phys',
# #                         u'Міжнародна наукова конференція "Астрономія та фізика космосу в Київському університеті"',
# #                         u'International Conference "Astronomy and Space Physics at the University of Kiev"', u"Астр. та фіз. космосу", u"Astr. and Space Phys.", conference),
# #                     (u'recent_devel_chemistry',
# #                         u'МіжнарCONFERENCEренція студентів та аспірантів "Сучасні проблеми хімії"',
# #                         u'International Students and Postgraduates "Recent developments in chemistry"', u"Сучасні пробл. хімії", u"Recent devel. in chemistry", conference),
# #                     (u'modern_cell_tech',
# #                         u'Весняна школа "Сучасні клітинні техCONFERENCEундаментальні та прикладні аспекти"',
# #                         u'Spring School "Modern cell technology: basic and apCONFERENCEcts"', u"Сучасні клітинні технології", u"Modern cell technology", conference),
# #                     (u'ukr_participation_model',
# #                         u'Науково-практична конференція "Основні моделі участі України в інтеграційних процесах на теренах СНД"',
# #                         u'Scientific conference "Ukraine\'s participation model in the integration processes in the CIS"', u"Моделі участі Укр. в інтегр. проц.", u"Ukr. part. model in the integ. proc.", conference),
# #                     (u'phys_chem_cond_matter',
# #                         u'Конференція "Фізико-хімія CONFERENCEних систем і міжфазних границь"',
# #                         u'Conference "Physics and chemistry of condensed matter systems and interfaces"', u"Фізико-хімія конд. систем", u"Physics and chem. of cond. systems", conference),
# #                     (u'yang_lng_awareness',
# #                         u'Всеукраїнська наукова конференція за участю молодих учених "Мова, свідомість, художня творчість, інтернет у дзеркалі сучаснCONFERENCEічних студій"',
# #                         u'National Conference with the participation of young scientists "Language awareness, artistic creativity, the Internet in a mirror modern philological studies "', u"Мова, свідомість, ...", u"Language awareness,...", conference),
# #                     (u'rd_civil_landmarks',
# #                         u'"RUTHENIA DIVIDA: цивілізаційні орієнтири та поліCONFERENCEиріччя козацьких еліт другої половини XVII ст."',
# #                         u'"RUTHENIA DIVIDA: civilizational landmarks and political contradictions Cossack elite second half of XVII century."', u"RUTHENIA DIVIDA", u"RUTHENIA DIVIDA", conference),
# #                     (u'shevchenko_spring',
# #                         u'Міжнародна наукова конференція студентів, аспірантів та молодих вчених "ШевчеCONFERENCEесна"',
# #                         u'International Conference of Students and Young Scientists "Shevchenko Spring"', u"Шевченківська Весна", u"Shevchenko Spring", conference),
# #                     (u'modern_probl_geol',
# #                         u'Всеукраїнська молодіжна конференція-школа "Сучасні проблеми геологічних наук"',
# #       CONFERENCE        u'All-School Youth Conference "Modern Problems of Geological Sciences"', u"Пробл. геол. наук", u"Probl. of Geol. Scienc.", conference),
# #          CONFERENCE (u'lang_society_journ',
# #                         u'міжнародна науково-практична конференція з проблем функціонування і розвитку української мови "Мова. Суспільство. Журналістика"',
# #                         u'International scientific-practical conference on the operation and development of the Ukrainian language "Language. Society. journalism"', u"Мова. Сусп. Журн.", u"Lange. Soc. jour.", conference),
# #   CONFERENCE        (u'field_social_commun',
# #                         u'Всеукраїнська науково-практична конференція "Актуальні дослідження українських наукових шкіл у галузі соціальних комунікацій"',
# #                         u'National Scientific and Practical Conference "Ukrainian scientific research schools in the field of social communications"', u"Досл. у соц. ком.", u"Sci. res. in the field of soc. comm.", conference),
# #                     (u'human_rights',
# #                         u'Міжнародна науково-практична конференція Права людини в сучасному світі"',
# #                         u'International ScientificCONFERENCEe of Human Rights in the Modern World "', u"Права людини в світі", u"Human Rights in the World", conference),
# #                     (u'study_media_content',
# #                         u'Всеукраїнська студентська науково-практична конференція "Прикладні аспекти дослідження медійного контенту"',
# #                         u'Ukrainian Student Scientific Conference "Applications of the study of media content"', u"Прикл. асп. досл. мед. конт.", u"Study of med. CONFERENCEnference),
# #                     (u'spatial_transf_proc',
# #                         u'Міжнародна наукова конференція "Просторові трансформаційні процеси в Центральній Європі в ХХІ столітті"',
# #                         u'International Scientific Conference "Spatial transformation processes in Central Europe in the twentieth century"', u"Проц. в Центр. Євр. в ХХІ ст.", u"Proc. in Centr. Eur. in the XXI cCONFERENCEence),
# #                     (u'neovulkanizm_alpine',
# #                         u'Міжнародна науково-практичнаконференція "Континентальний неовулканізм альпійської складчастої зони Східної Європи"',
# #                         u'International Scientific praktychnakonferentsiya "Continental neovulkanizm Alpine folded zone of Eastern Europe"', u"Неовулк. Східної Європи", u"Neovulkanizm of EasCONFERENCEe", conference),
#
#                       {'alias': u"phys_math",
#                       'uk_name': u"Вісник КНУ Серія фіз.-мат. Науки",
#                       'en_name': u"Bulletin of KNU Series Sci. science",
#                       'uk_abbrev': u"Фіз.-мат. Науки",
#                       'en_abbrev': u"Sci. science",
#                       'category': journal,
#                       'subject_CONFERENCE: u"висвітлення результатів досліджень у різних галузях математики, "
#                         "інформатики, механіки, фізики та радіофізиCONFERENCE                  'subject_matter_en': u"coverage of research in various fields of mathematics,"
#                             "computer science, mechanics, physics and radio physics",
#                       'foundation_year': 1991,
#                       'issues_by_year': 4,
#                       'gov_certificate_date': u'2009-12-11',
#                       'gov_certificate_num': u"КВ № 16299-4771 Р",
#                       'vac_certificate_date': u"1999-06-09",
#                       'vac_certificate_num': u"1-05/7",
#                       CONFERENCE1812-5409",
#                       'phone': u"(044) 259-01-49",
#                       'email': u"",
#                       'address_uk': u"Київський національний університет імені Тараса Шевченка"
#                             "Факультет кібернетики"
#                             "просп. акад. Глушкова, 2, корп. 6, кімн. 23, Київ-127, Україна, 03127",
#                       'addreCONFERENCEyiv National Taras Shevchenko"
#                                 "Department of Cybernetics"
#                                 "ave. Acad. Glushkov, 2, Bldg. 6 BR. 23, Kyiv-127, Ukraine, 03127",
#                       },
#
#
#                   ]
#
#     for i, edition_dic in enumerate(edition_lst):
#         obj_category = Category.objects.get(category_alias = edition_dic["category"])
#         obj_edition = Edition(id = i + 1,
#                               edition_alias = CONFERENCEc["alias"],
#                               category = obj_category,
#                               foundation_year = edition_dic["foundation_year"],
#                               issues_by_year = edition_dic["issues_by_year"],
#                               gov_certificate_date = edition_dic["gov_certificate_date"],
#                               gov_certificate_num = edition_dic["gov_certificate_num"],
#                               vac_certificate_date = edition_dic["vac_certificate_date"],
#              CONFERENCE       vac_certificate_num = edition_dic["vac_certificate_num"],
#                               ISSN = edition_dic["ISSN"],
#                               phone = edition_dic["phone"],
#                               email = edition_dic["email"],
#                               )
#         # print alias
#         obj_edition.save()
#
#
#         fos_obj = FieldOfScience.objects.get(
#                                                 fieldofscience_locale__lang_code = uk,
#                                                 fieldofsCONFERENCEale__fos_name = u"фізико-математичні науки"
#                                                 )
#
#
#
#         obj_edition.fields_of_science.add(fos_obj)
#         obj_edition.save()
#
#         if len(edition_dic["uk_abbrev"]) == 0:
#             edition_dic["uk_abbrev"] = edition_dic["uk_name"]
#         if len(edition_dic["en_abbrev"]) == 0:
#             edition_dic["en_abbrev"] = edition_dic["en_name"]
#
#         eJOURNALlocale = Edition_Locale(id = (i + 1) * 2 - 1,
#                                   lang_code = uk,
#                                   edition_name = edition_dic["uk_name"],
#                                   edition_abbrev = edition_dic["uk_abbrev"],
#                                   subject_matter = edition_dic["subject_matter_uk"],
#                                   address = edition_dic["address_uk"],
#                                   edition = obj_edition,
#                                   )
#
#         edition_locale.save()
#
#         edition_locale = Edition_Locale(id = (i + 1) * 2,
#                                   lang_code = en,
#                                   edition_name = edition_dic["en_name"],
#                                   edition_abbrev = edition_dic["en_abbrev"],
#                                   subject_matter = edition_dic["subject_matter_en"],
#                                   address = edition_dic["address_en"],
#                                   edition = obj_edition,
#                                   )
#         edition_locale.save()
#
#
# #     for i, (alias, uk_name, en_name, uk_abbrev, en_abbrev, category) in enumerate(edition_lst):
# #         obj_category = Category.objects.get(category_alias = category)
# #         obj_edition = Edition(id = i + 1, edition_alias = alias, category = obj_category)
# #         # print alias
# #         obj_edition.save()
# #         if len(uk_abbrev) == 0:
# #             uk_abbrev = uk_name
# #         if len(en_abbrev) == 0:
# #             en_abbrev = en_name
# #
# #         edition_locale = Edition_Locale(id = (i + 1) * 2 - 1,
# #                                   lang_code = uk,
# #                                   edition_name = uk_name,
# #                                   edition_abbrev = uk_abbrev,
# #                                   edition = obj_edition,
# #                                   )
# #
# #         edition_locale.save()
# #
# #         edition_locale = Edition_Locale(id = (i + 1) * 2,
# #                                   lang_code = en,
# #                                   edition_name = en_name,
# #                                   edition_abbrev = en_abbrev,
# #                                   edition = obj_edition,
# #                                   )
# #         edition_locale.save()

# def populate_rubric():
#     rubric_lst = [(phys_math, 1,
#                    u"алгебра, геометрія та теорія ймовірностей",
#                    u"algebra, geometry, and probability theory"),
#
#                   (phys_math, 2,
#                    u"диференціальні рівняння, математична фізика та механіка",
#                    u"differential equation, mathematical physics, mechanics"),
#
#                   (phys_math, 3,
#                    u"комп'ютерні науки та інформатика",
#                    u"computer science and informatics"),
#
#                   (phys_math, 4,
#                    u"радіофізика",
#                    u"radiophysics"),
#
#                   (phys_math, 5,
#                    u"сучасна фізика",
#                    u"modern physics"),
#
# #                   (astronomy, 1, "", ""),
# #
# #                   (biology, 1, "", ""),
# #
# #                   (military, 1, u"техніка", military_engineering),
# #                   (military, 2, u"інформаційні технології", military_information_technology),
# #                   (military, 3, u"психологія", military_psychology),
# #
# #                   (geography, 1, u"теоретико-методичні дослідження", geography_theor_method_research),
# #                   (geography, 2, u"прикладні дослідження", geography_applied_research),
# #                   (geography, 3, u"праці молодих вчених", geography_young_scientists),
# #                   (geography, 4, u"ювілеї", geography_anniversaries),
# #                   (geography, 5, u"пам'ятаємо", geography_remember),
# #
# #                   (geology, 1, "загальна та історична геологія, геотектоніка та геологія родовищ корисних копалин",
# #                    "general and historical geology, geotectonics and mineral resources"),
# #                   (geology, 2, "мінералогія, геохімія та петрографія",
# #                    "mineralogy, geochemistry and petrography"),
# #                   (geology, 3, "геофізика", "geophysics"),
# #                   (geology, 4, "геологічна інформатика", "geological informatics"),
# #                   (geology, 5, "екологічна геологія", "ecological geology"),
# #                   (geology, 6, "колекції геологічного музею", "the geological museum collections"),
# #
# #                   (economics, 1, u"", u""),
# #
# #                   (journalism, 1, u"теорія і практика журналістики", u"the theory and practice of journalism"),
# #                   (journalism, 2, u"історя журналістики", u"the history of journalism"),
# #                   (journalism, 3, u"історія видавничої справи", u"the history of publishing"),
# #                   (journalism, 4, u"видавнича справа", u"the publishing"),
# #                   (journalism, 5, u"редагування", u"the editing"),
# #                   (journalism, 6, u"електронні видання", u"the electronic editions"),
# #
# #                   (philology, 1, u"мовознавство", u"linguistics"),
# #                   (philology, 2, u"перекладознавство", u"translation studies"),
# #                   (philology, 3, u"літературознавство", u"literature studies"),
# #                   (philology, 4, u"сторінки історії", u"pages of history"),
# #
# #                   (plant, 1, u"інтродукція та збереження рослинного різноманіття в природі та культурі",
# #                     u"introduction and conservation of plant diversity in nature and culture contents"),
# #                   (plant, 2, u"фізіологія, біохімія та анатомія рослин",
# #                     u"plant physiology, biochemistri and anatomi"),
# #                   (plant, 3, u"захист рослин від шкідників і хвороб",
# #                     u"plant protection from vermin and diseases"),
# #
# #                   (history, 1, u"", u""),
# #
# #                   (cybernetics, 1, u"", u""),
# #
# #                   (literature, 1, u"літературознавство", u"literary studies"),
# #                   (literature, 2, u"мовознавство", u"language studies"),
# #                   (literature, 3, u"фольклористика", u"folklore studies"),
# #
# #                   (math_mech, 1, u"", u""),
# #
# #                   (relations, 1, u"актуальні проблеми міжнародних відносин",
# #                     u"actual problems of international relations"),
# #                   (relations, 2, u"особливості розвитку світового господарства та міжнародних економічних відносин",
# #                     u"special features of the world economy and international economic relation's development"),
# #                   (relations, 3, u"сучасна система міжнародного права",
# #                     u"modern system of international law"),
#
#                   ]
#
#     for i, (edition_alias, order, uk_name, en_name) in enumerate(rubric_lst):
#         obj_edition = Edition.objects.get(edition_alias = edition_alias)
#         obj_rubric = Rubric(id = i + 1, edition = obj_edition, rubric_order = order)
#         obj_rubric.save()
#         rubric_locale = Rubric_Locale(id = (i + 1) * 2 - 1,
#                                    lang_code = uk,
#                                    rubric_name = uk_name,
#                                    rubric = obj_rubric,
#                                    )
#         rubric_locale.save()
#         rubric_locale = Rubric_Locale(id = (i + 1) * 2,
#                                    lang_code = en,
#                                    rubric_name = en_name,
#                                    rubric = obj_rubric,
#                                    )
#         rubric_locale.save()
#
#
# def populate_articles():
#     articles_lst = [
#                     {"edition": astronomy,
#                      "issue_num": 47,
#                      "issue_year": 2011,
#                      "rubric":u"",
#                      "file_name": u"Mapping_the_total_matter_density_in_the_Local_Universe_with_POTENT_12878.pdf",
#                      "title_ua": u"Картографування повної густини матерії у Місцевому Всесвіті за методом POTENT",
#                      "title_en": u"Mapping the total matter density in the Local Universe with POTENT",
#                      "author_ua":[(u"Парновський", u"С", u""), (u"Шаров", u"П", u""), (u"Парновський", u"О", u"")],
#                      "author_en":[(u"Parnovsky", u"S", u""), (u"Sharov", u"P", u""), (u"Parnovsky", u"O", u"")],
#                      "abstract_ua": u"""
#                          Ми застосували метод POTENT до останньої версії вибірки RFGC-галактик для відновлення поля
#                          швидкостей великомасштабного колективного руху галактик а відповідного просторового розподілу
#                          повної густини матерії на масштабах близько 100 h-1 Мпк. Отримані мапи містять усі основні
#                          спостережувані об'єкти, включаючи Великий Атрактор, надскупчення Персей-Риби, скупчення Кома,
#                          стіну Кита та порожнечу Скульптора.
#                      """,
#                      "abstract_en": u"""
#                          We applied POTENT method to the latest sample of RFGC galaxies to reconstruct the velocity field of
#                          large-scale collective motions  of galaxies and the corresponding spatial distribution of total
#                          matter density on the scale of about 100 h-1 Mpc. The resulting maps reveal all of the major
#                          observed features including Great Attractor, Perseus-Pisces supercluster, Coma cluster, Cetus wall
#                          and Sculptor void.
#                      """,
#                     },
#
#                     {"edition": astronomy,
#                      "issue_num": 47,
#                      "issue_year": 2011,
#                      "rubric":u"",
#                      "file_name": u"X_ray_properties_of_the_gravitational_lens_system_Q0957_561_with_XMM_Newton_observations_12879.pdf",
#                      "title_ua": u"Рентгенівські властивості гравітаційно-лінзової системи Q0957+561 за даними спостережень XMM-Newton",
#                      "title_en": u"X-ray properties of the gravitational lens system Q0957+561 with XMM-Newton observations",
#                      "author_ua":[(u"Федорова", u"Е", u"")],
#                      "author_en":[(u"Fedorova", u"E", u"")],
#                      "abstract_ua": u"""
#                          Оброблено результати двох спостережень гравітаційно-лінзової системи (ГЛС) Q0957+561 "Перша Лінза"
#                          космічною місією XMM-Newton. Отримані спектри та очищені криві блиску зображень А та В квазара в
#                          ГЛС, відтворене припасування спектрів степеневою моделлю (фотонний індекс перевищує 2 і співпадає
#                          в межах похибок для обох спостережень, для обох зображень). Ані на кривих блиску під час окремих
#                          спостережень, ані між двома спостереженнями не помічено змінності потоку.
#                      """,
#                      "abstract_en": u"""
#                         The results of two XMM-Newton observations of the gravitational lens system
#                         (GLS) Q0957+561 "First Lens" is analyzed. The individual spectra of both
#                         images A and B of the quasar in this GLS were extracted and modeled with a
#                         power-law model. The lightcurves obtained after background subtraction show
#                         no significant variability neither during the time of the two observations
#                         nor between them. Fitting the background-subtracted source spectra yields
#                         the power-law photon index above.
#                      """,
#                     },
#
#                     {"edition": astronomy,
#                      "issue_num": 45,
#                      "issue_year": 2009,
#                      "rubric":u"",
#                      "file_name": u"Brightness_magnification_factor_for_small_Gaussian_source_near_caustic_of_gravitation_lens_13323.pdf",
#                      "title_ua": u"Коефіцієнт підсилення блиску малого гаусівського джерела поблизу каустики гравітаційної лінзи",
#                      "title_en": u"Brightness magnification factor for small Gaussian source near caustic of gravitation lens",
#                      "author_ua":[(u"Александров", u"О", u""), (u"Жданов", u"В", u"")],
#                      "author_en":[(u"Alexandrov", u"A", u""), (u"Zhdanov", u"V", u"")],
#                      "abstract_ua": u"""
#                         В околі регулярної точки каустики для протяжного джерела з гаусівським
#                         розподілом поверхневої яскравості знайдено уточнену формулу залежності
#                         коефіцієнта підсилення від координат центра. Порівняно з добре відомим
#                         "нульовим наближенням" нова формула враховує поправки, пропорційні до розміру
#                         джерела, і містить три додаткові параметри гравітаційно-лінзової системи.
#                         Шляхом граничного переходу знайдено формулу коефіцієнта підсилення точкового
#                         джерела.
#                      """,
#                      "abstract_en": u"""
#                         For a small Gaussian source near a fold the improved formulae for the
#                         brightness magnification factor is found as a function of the centre
#                         coordinates. As compared with the well-known leading approximation the new
#                         formula takes into account correction terms proportional to the source size
#                         and contains three additional parameters of the gravitational lens system.
#                         By means of the limit process a formula for point source magnification is
#                         derived.
#                      """,
#                     },
#
#                     {"edition": biology,
#                      "issue_num": 59,
#                      "issue_year": 2011,
#                      "rubric":u"",
#                      "file_name": u"Viral_diseases_of_tomatoes_and_cucumbers_in_greenhouses_of_Belarus_13196.pdf",
#                      "title_ua": u"Вірусні хвороби томату та огірка захищеного ґрунту в Білорусі",
#                      "title_en": u"Viral diseases of tomatoes and cucumbers in greenhouses of Belarus",
#                      "author_ua":[(u"Блоцька", u"Ж", u""), (u"Вабищевич", u"В", u"")],
#                      "author_en":[(u"Blotskaya", u"Zh", u""), (u"Vabishchevich", u"V", u"")],
#                      "abstract_ua": u"""
#                         В статті наведено інформацію про випадки вірусних захворювань томатів та
#                         огірків, що вирощуються в умовах закритого ґрунту. Показано, що при
#                         інтенсивному розвитку вірусних захворювань огірків, їх шкодочинність
#                         становить 14,7-46,2 %, в залежності від гібриду. На основі біологічного
#                         тестування та ІФА ідентифіковані віруси ВТМ, ВОМ, ВМТ, ВЗКМО. Доведена
#                         можливість використання біологічно активних речовин для обмеження експресії
#                         ВЗКМО на ранніх стадіях розвитку огірків.
#                      """,
#                      "abstract_en": u"""
#                          In the article the information on virus diseases incidence in tomato and
#                          cucumber cultivated under protected ground conditions is presented. It is
#                          shown that at the intensive virus diseases development in cucumber plants
#                          their harmfulness makes 14,7-46,2% depending on hybrid. Based on biological
#                          test and ELISA-test TMV, CMV, ToMV and CGMMV viruses are identified.
#                          A possibility of biologically active substances application for restriction
#                          the CGMMV expression and development at the early stage of cucumber plant
#                          development is determined.
#                      """,
#                     },
#
#                     {"edition": biology,
#                      "issue_num": 59,
#                      "issue_year": 2011,
#                      "rubric":u"",
#                      "file_name": u"Etiological_prognostication_of_influenza_epidemics_in_Ukraine_13200.pdf",
#                      "title_ua": u"Етіологічне прогнозування епідемій грипу в Україні",
#                      "title_en": u"Etiological prognostication of influenza epidemics in Ukraine",
#                      "author_ua":[(u"Міроненко", u"А", u""),
#                                   (u"Хмельницька", u"Г", u""),
#                                   (u"Лейбенко", u"Л", u""),
#                                   (u" Онищенко", u"О", u""),
#                                   (u"Костюк", u"О", u""),
#                                   (u"Курінько", u"Н", u""),
#                                   (u"Бабій", u"С", u""),
#                                   ],
#                      "author_en":[(u"Mironenko", u"A", u""),
#                                   (u"Khmelnitskaya", u"G", u""),
#                                   (u"Leibenko", u"L", u""),
#                                   (u"Onischenko", u"O", u""),
#                                   (u"Kostiyk", u"O", u""),
#                                   (u"Kurinko", u"N", u""),
#                                   (u"Babii", u"S", u""),
#
#                                   ],
#                      "abstract_ua": u"""
#                          Етіологічне прогнозування спалахів грипу використовується для передбачення
#                          епідемій, розрахунку очікуваних рівнів захворюваності та смертності, а також
#                          для вибору стратегії профілактики. Оскільки на Україні вакцини не
#                          виробляються, особливу увагу слід приділяти ідентифікації основних
#                          інфекційних агентів. В статті наведено аналіз етіологічних прогнозів
#                          епідемій грипу в Україні за останні 12 років.
#                      """,
#                      "abstract_en": u"""
#                          An etiological prognostication influenza outbreak is used for epidemic
#                          forecast, calculating expected morbidity and mortality and choosing
#                          preventive strategies. As influenza vaccines aren't produced in Ukraine,
#                          attention should be paid on identification leading infectious agent. It was
#                          analyzed etiological prognoses of influenza epidemics in Ukraine through
#                          last 12 years.
#                      """,
#                     },
#
#                     {"edition": biology,
#                      "issue_num": 58,
#                      "issue_year": 2011,
#                      "rubric":u"",
#                      "file_name": u"The_connection_of_seasonal_dynamics_of_quantity_of_the_females_thrips_Frankliniella_occidentalis_Pergande_with_morphology_of_antenna_13210.pdf",
#                      "title_ua": u"Зв'язок сезонної динаміки чисельності самок трипса Frankliniella occidentalis Pergande з  морфологією антен.",
#                      "title_en": u"The connection of seasonal dynamics of quantity of the females thrips Frankliniella occidentalis Pergande with morphology of antenna",
#                      "author_ua":[(u"Ларкі", u"Д", u""),
#                                   (u"Чумак", u"П", u""),
#                                   (u"Кілочицький", u"П", u"")],
#                      "author_en":[(u"Larki", u"J", u""),
#                                   (u"Chumak", u"P", u""),
#                                   (u"Kilochyckij", u"P", u"")],
#                      "abstract_ua": u"""
#                          Встановлено, що довжина переважної більшості члеників антен самок
#                          Frankliniella occidentalis зимової генерації (за винятком 2-о членика)
#                          значно перевищує довжину члеників антен самок літньої генерації. Найбільш
#                          тісний кореляційний зв'язок між розмірами окремих члеників антен та між
#                          розмірами члеників та загальною довжиною антен мають лише 3-й і 4-й
#                          членики, на яких є парні трихоми. Морфометричні характеристики 3-о та 4-о
#                          члеників антен трипсів можуть бути використані при аналізі стану популяцій
#                          та для прогнозу тенденції до масового розмноження цього небезпечного
#                          шкідника в умовах закритого грунту.
#                      """,
#                      "abstract_en": u"""
#                          It has been determined that overwhelming majority of winter generation antenna segments of
#                          females Frankliniella occidentalis (except for the 2-nd segment) considerably exceeds the
#                          length of antenna segments of females summer generation.The closest correlation between the
#                          sizes of individual Antenna segments and sizes of segments and total antenna length is found
#                          only for the 3-d and the 4-th segment, which is paired trichomes. The Morphological
#                          characteristics of 3-d and 4-th antenna segments of thrips can be used for analysis of
#                          population condition and for the prognosis of tendency to mass reproduction of this dangerous
#                          pest in greenhouse conditions.
#                      """,
#                     },
#
#                     {"edition": military,
#                      "issue_num": 24,
#                      "issue_year": 2010,
#                      "rubric": military_engineering,
#                      "file_name": u"Research_of_dynamics_of_the_Diesel_engine_with_power_regulation_switching_off_of_cycles_and_their_prospect_13379.pdf",
#                      "title_ua": u"Дослідження динаміки дизельного двигуна з регулюванням потужності відключенням циклів і їх перспектива",
#                      "title_en": u"Research of dynamics of the Diesel engine with power regulation, switching-off of cycles and their prospect",
#                      "author_ua":[(u"Бешун", u"О", u"А"),
#                                   (u"Лях", u"М", u"А"),
#                                   (u"Дем'янюк", u"О", u"С")],
#                      "author_en":[(u"Beshun", u"O", u"A"),
#                                    (u"Liakh", u"М", u"А"),
#                                    (u"Demianiuk", u"О", u"S")],
#                      "abstract_ua": u"""
#                          Наведено результати теоретичних досліджень показників динаміки 4-тактного
#                          8-циліндрового дизеля з V-подібним розміщенням циліндрів і регулюванням
#                          потужності відключенням окремих робочих циклів. Визначено нерівномірності
#                          індикаторного крутного моменту та кутової швидкості обертання колінчатого
#                          вала (ходу) двигуна. Дослідження виконані на оригінальній математичній
#                          моделі динаміки з використанням персонального комп'ютера. Приведено напрям
#                          заміни існуючого парку автомобільної техніки в Збройних Силах України.
#                      """,
#                      "abstract_en": u"""
#                         The article presents results of theoretical researches of dynamics for
#                         four-stroke 8-cylinder diesel engines, in which power is controlled by
#                         means of separate working cycles switching-off. It is definite to the
#                         unevenness of indicator moment and engine angular speed of rotation. The
#                         algorithm of working cycles displacement at cylinders of the engine were
#                         developed and investigated. Theoretical researches were performed on personal
#                         computer. Original mathematical model dynamics was developed. The direction
#                         of present-day automotive materiel fleet of the Armed Forces of Ukraine's
#                         replacement is presented.
#                      """,
#                     },
#
#                     {"edition": military,
#                      "issue_num": 24,
#                      "issue_year": 2010,
#                      "rubric": military_engineering,
#                      "file_name": u"The_block_diagramme_of_inbuilt_diagnostic_device_of_radio_electronic_means_of_armament_is_generalised_13381.pdf",
#                      "title_ua": u"Узагальнена структурна схема вмонтованого засобу діагностування радіоелектронних засобів озброєння",
#                      "title_en": u"The block diagramme of inbuilt diagnostic device of radio-electronic means of armament is generalised",
#                      "author_ua":[(u"Жердєв", u"М", u"К"),
#                                   (u"Вишнівський", u"В", u"В"),
#                                   ],
#                      "author_en":[(u"Zherdev", u"М", u"К"),
#                                   (u"Vyshnivskyi", u"V", u"V"), ],
#                      "abstract_ua": u"""
#                         Запропоновано раціональні варіанти структурних схем вмонтованих засобів
#                         діагностування аналогових і цифрових пристроїв об'єктів РЕЗО. Показано, що
#                         вони забезпечують необхідний рівень бойової готовності об'єктів РЕЗО
#                         наземного базування і суттєво менші витрати на їх відновлення.
#                      """,
#                      "abstract_en": u"""
#                         Rational alternatives of block diagrammes of inbuilt diagnostics of tools of
#                         analogue and digital devices of installations RECS are offered. It is shown
#                         that they provide necessary level of alertness of installations RECS of land
#                         basing and essentially smaller charges on their renewal.
#                      """,
#                     },
#
#                     {"edition": military,
#                      "issue_num": 24,
#                      "issue_year": 2010,
#                      "rubric": military_psychology,
#                      "file_name": u"Applications_of_separate_technicians_of_neurolinguistics_programming_in_vocational_training_of_law_enforcement_agencies_13390.pdf",
#                      "title_ua": u"Застосування окремих технік нейролінгвістичного програмування у професійній підготовці співробітників правоохоронних органів",
#                      "title_en": u"Applications of separate technicians of neurolinguistics programming in vocational training of lawenforcement agencies",
#                      "author_ua":[(u"Олексієнко", u"С", u"Б")],
#                      "author_en":[(u"Oleksienko", u"S", u"B")],
#                      "abstract_ua": u"""
#                         У статті автор акцентує увагу на проблемі професійного розвитку співробітників
#                         правоохоронних органів України. Автор розглядає можливості вживання окремої
#                         техніки нейро-лінгвістичного програмування в контексті оптимізації особового
#                         розвитку співробітників правоохоронних органів виходячи з розвитку
#                         комунікативних властивостей особи відповідно до вимог оперативно-розшукової
#                         діяльності.
#                      """,
#                      "abstract_en": u"""
#                         In the article the author draws his attention to the problem of professional
#                         development of employees of the law enforcement bodies of Ukraine. He
#                         considers possibility of applying separate techniques of neurolinguistic
#                         programming within the optimization of personal development of employees of
#                         the law enforcement bodies based on development of communicative characteristics
#                         of a personality according to requirements of real-time searching activities.
#                      """,
#                     },
#                     {"edition": geography,
#                      "issue_num": 58,
#                      "issue_year": 2011,
#                      "rubric": geography_applied_research,
#                      "file_name": u"landscape_architectural_complexes_of_Kiev_13520.pdf",
#                      "title_ua": u"Ландшафтно-архітектурні комплекси міста  Києва",
#                      "title_en": u"landscape-architectural complexes of Kiev",
#                      "author_ua":[(u"Дмитрук", u"О", u""),
#                                   (u"Олішевська", u"Ю", u""),
#                                   (u"Дем'яненко", u"С", u""),
#                                   (u"Купач", u"Т", u""), ],
#                      "author_en":[(u"Dmytruc", u"O", u""),
#                                   (u"Olishevsca", u"J", u""),
#                                   (u"Demyanenco", u"S", u""),
#                                   (u"Coupach", u"T", u""), ],
#                      "abstract_ua": u"""
#                          Проаналізовано ландшафтно-архітектурну структуру території міста Києва. Представлено карту ландшафтноархітектурних комплексів міста Києва із застосуванням новітніх інформаційних технологій.
#                      """,
#                      "abstract_en": u"""
#                         The landscape-architectural structure of territory of city of Kyiv is analysed. The map of landscape-architectural complexes of city of Kyiv is presented with application of the newest information technologies.
#                      """,
#                     },
#
#                     {"edition": geography,
#                      "issue_num": 58,
#                      "issue_year": 2011,
#                      "rubric": geography_applied_research,
#                      "file_name": u"Territorial_organization_of_Ukrainian_restaurant_industry_13521.pdf",
#                      "title_ua": u"Територіальна організація підприємств ресторанного господарства України",
#                      "title_en": u"Territorial organization of Ukrainian restaurant industry ",
#                      "author_ua":[(u"Дорошенко", u"В", u""),
#                                   (u"Дмитрієва", u"К", u""), ],
#                      "author_en":[(u"Doroshenko", u"V", u""),
#                                   (u"Dmytriieva", u"K", u""), ],
#                      "abstract_ua": u"""
#                          Проаналізовано регіональні відмінності територіальної організації ресторанного господарства України, визначено їх причини. Досліджено впровадження новітніх тенденцій територіальних форм ресторанного господарства.
#                      """,
#                      "abstract_en": u"""
#                         Regional differences of the territorial organization of restaurant facilities of Ukraine are analyzed, their reasons are researched. Introduction of the newest trends of territorial forms of restaurant facilities is researched
#                      """,
#                     },
#                     {"edition": geography,
#                      "issue_num": 58,
#                      "issue_year": 2011,
#                      "rubric": geography_applied_research,
#                      "file_name": u"Estimation_of_functioning_regional_labour_market_factors_in_Khmelnitsky_13522.pdf",
#                      "title_ua": u"Оцінка чинників функціонування Хмельницького регіонального ринку праці",
#                      "title_en": u"Estimation of functioning regional labour-market factors in Khmelnitsky",
#                      "author_ua":[(u"Мезенцев", u"К", u""),
#                                   (u"Сайчук", u"В", u""), ],
#                      "author_en":[(u"Mezentsev", u"C", u""),
#                                   (u"Saychouc", u"V", u""), ],
#                      "abstract_ua": u"""
#                          Визначено особливості суспільно-географічної оцінки чинників функціонування регіонального ринку праці та описано методичні аспекти застосування факторного аналізу при їх дослідженні. За допомогою факторного аналізу визначено найсуттєвіші чинники функціонування Хмельницького регіонального ринку праці, проведено їх інтерпретацію та аналіз. Проведено групування районів області за особливостями розподілу впливу основних чинників функціонування регіонального ринку праці.
#                      """,
#                      "abstract_en": u"""
#                         The specific features of the human-geographical assessment of the factors of regional labor market functioning are determined, and the technical aspects of factor analysis application are described. The most significant factors of Khmelnytsky regional labor market functioning are determined by factor analysis using, their interpretation and analysis are carried out. Districts grouping by distribution features of the basic factors influence on the regional labor market functioning is conducted.
#                      """,
#                     },
#
#                     {"edition": phys_math,
#                      "issue_num": 1,
#                      "issue_year": 2012,
#                      "rubric": phys_math_algebra,
#                      "file_name": u"p_009_012.pdf",
#                      "title_ua": u"Існування та єдиність розв'язку задачі Коші для рівняння теплопровідності із загальною стохастичною мірою",
#                      "title_en": u"Existence and uniqueness of the solution of Cauchy problem for a heat equation with general stochastic measure",
#                      "author_ua":[(u"Городня", u"Д", u"М")],
#                      "author_en":[(u"Gorodnya", u"D", u"M")],
#                      "abstract_ua": """
#                          Доведено iснування та єдинiсть слабкого розв'язку задачi Кошi для рiвняння
#                          теплопровiдностi, керованого загальною стохастичною мiрою.
#                      """,
#                      "abstract_en": """
#                         Existence and uniqueness of the weak solution of Cauchy problem for a heat
#                         equation driven by the general stochastic measure is proved.
#                      """,
#                     },
#
#                     {"edition": phys_math,
#                      "issue_num": 1,
#                      "issue_year": 2012,
#                      "rubric": phys_math_algebra,
#                      "file_name": u"p_013_017.pdf",
#                      "title_ua": u"Узагальнені розв'язки гіперболічного рівняння з Орлічевою правою частиною",
#                      "title_en": u"Generalized solutions of the hyperbolic equation with Orlicz right part",
#                      "author_ua":[(u"Довгай", u"Б", u"В")],
#                      "author_en":[(u"Dovgay", u"B", u"V")],
#                      "abstract_ua": u"""
#                         Розглядається гiперболiчне рiвняння з Орлiчевою правою частиною.
#                         Знайденi умови iснування узагальненого розв'язку цiєї задачi.
#                      """,
#                      "abstract_en": u"""
#                         A hyperbolic equation with Orlicz right side is considered. The conditions
#                         for existence of generalized solution of this problem are found.",
#                      """,
#                     },
#
#                     {"edition": phys_math,
#                      "issue_num": 1,
#                      "issue_year": 2012,
#                      "file_name": u"p_018_023.pdf",
#                      "rubric": phys_math_algebra,
#                      "title_ua": u"Робастні оцінки для сумішей з гауссовою компонентою",
#                      "title_en": u"Robust Estimates for Mixtures with Gaussian Component",
#                      "author_ua":[(u"Доронін", u"О", u"В")],
#                      "author_en":[(u"Doronin", u"A", u"V")],
#                      "abstract_ua": u"""
#                         Розглянута задача семiпараметричного оцiнювання для спостережень, якi
#                         описуються моделлю сумiшi кiлькох ймовiрнисних розподiлiв зi змiнними
#                         концентрацiями. Побудованi та дослiдженi оцiнки для параметрiв гаусcової
#                         компоненти.
#                      """,
#                      "abstract_en": u"""
#                          The paper is devoted to the problem of semiparametric estimation for
#                          observation, described by the model of mixture of some probability
#                          distributions with varying concentrations. Constructedand studied the
#                          estimators for parameters ofgaussian component.
#                      """,
#                     },
#
# #                     {"edition": phys_math,
# #                      "issue_num": 1,
# #                      "issue_year": 2012,
# #                      "rubric": phys_math_algebra,
# #                      "file_name": u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
#
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
# #                     {"edition":u"",
# #                      "issue_num": 0,
# #                      "issue_year":0,
# #                      "rubric":u"",
# #                      "title_ua": u"",
# #                      "title_en": u"",
# #                      "author_ua":[(u"", u"", u"")],
# #                      "author_en":[(u"", u"", u"")],
# #                      "abstract_ua": u"",
# #                      "abstract_en": u"",
# #                     },
#
#                     ]
#
#     for i, item in enumerate(articles_lst):
#         edition_obj = Edition.objects.get(edition_alias = item["edition"])
#
#         try:
#             issue_obj = Issue.objects.get(issue_year = item["issue_year"],
#                                          issue_num = item["issue_num"],
#                                          edition = edition_obj)
#         except Issue.DoesNotExist:
#             issue_obj = Issue(issue_year = item["issue_year"],
#                                          issue_num = item["issue_num"],
#                                          edition = edition_obj)
#             issue_obj.save()
#
#         rubric_obj = Rubric.objects.get(edition = edition_obj,
#                             rubric_locale__rubric_name = item["rubric"],
#                             rubric_locale__lang_code = en)
#
#         article_obj = Article(id = i + 1,
#                               issue = issue_obj,
#                               rubric = rubric_obj,
#                               file_name = item["file_name"],
#                               )
#
#         article_obj.save()
#
#         article_locale_obj = Article_Locale(id = (i + 1) * 2 - 1,
#                                    lang_code = uk,
#                                    caption = item["title_ua"],
#                                    abstract = item["abstract_ua"],
#                                    article = article_obj,
#                                    )
#         article_locale_obj.save()
#
#         article_locale_obj = Article_Locale(id = (i + 1) * 2,
#                                    lang_code = en,
#                                    caption = item["title_en"],
#                                    abstract = item["abstract_en"],
#                                    article = article_obj,
#                                    )
#         article_locale_obj.save()
#
#
#         for j, ((last_uk, first_uk, middle_uk), (last_en, first_en, middle_en)) in enumerate(zip(item["author_ua"], item["author_en"])):
#             try:
#                 author_obj = Author.objects.get(author_locale__lang_code = en,
#                         author_locale__first_name = first_en,
#                         author_locale__middle_name = middle_en,
#                         author_locale__last_name = last_en)
#             except Author.DoesNotExist:
#                 author_obj = Author.objects.create()
#                 Author_Locale.objects.create(
#                         lang_code = en,
#                         author = author_obj,
#                         first_name = first_en,
#                         middle_name = middle_en,
#                         last_name = last_en)
#
#                 Author_Locale.objects.create(
#                         lang_code = uk,
#                         author = author_obj,
#                         first_name = first_uk,
#                         middle_name = middle_uk,
#                         last_name = last_uk)
#
#
#             m = Article_Authors(article = article_obj,
#                                 author = author_obj,
#                                 author_order = j + 1)
#             m.save()
#
# #              print last_en, first_en, midle_en
# #              print last_uk, first_uk, midle_uk
#
# def populate_all():
# #    populate_category()
# #    populate_edition()
#     populate_rubric()
# #    populate_articles()
#
if __name__ == '__main__':
    populate_all_editions(d.edition_lst)
#     populate_rubric()
#     # populate_edition()
#     # populate_category()
#     # populate_field_of_science()
#     # populate_all()
