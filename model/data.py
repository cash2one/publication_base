# -*- coding: utf-8 -*-

# from model.models import *
# from publication_base.views import lng_code_en as en, lng_code_ukr as uk


# ALTER TABLE `publication_db`.`publ_edition` CHANGE COLUMN `gov_certificate_date` `gov_certificate_date` DATE NULL  , CHANGE COLUMN `vac_certificate_date` `vac_certificate_date` DATE NULL  ;


# category
cat_herald = u"herald"
cat_journal = u"journal"
cat_conference = u"conference"

catid_herald = 1
catid_journal = 2
catid_conference = 3

category_lst = [(catid_herald, cat_herald, u"вісник", u"herald"),
                (catid_journal, cat_journal, u"журнал", u"journal"),
                (catid_conference, cat_conference, u"конференція", u"conference"),
               ]


# INSERT INTO auth_permission
# (name, content_type_id, codename)
# VALUES('User can edit Bulletin of KNU, Sci. science', 12, 'edit_phys_math')
# ON DUPLICATE KEY UPDATE
# name = 'User can edit Bulletin of KNU, Sci. science',
# content_type_id = 12,
# codename = 'edit_phys_math';


# from django.db import models
#
# class Permission(models.Model):
#     name = models.CharField(max_length = 50)
#     content_type_id = models.IntegerField()
#     codename = models.CharField(max_length = 100)
#
#     class Meta:
#         db_table = 'auth_permission'


# class FieldDefShort(object):
#     def __init__(self, attname):
#         self.attname = attname
#
# permission_lst = [FieldDefShort("codename"), FieldDefShort("name"), FieldDefShort("content_type_id"), ]

content_edition_id = 12

permissions_lst = (
            ("edit_phys_math", "Bul phys-math sciences", content_edition_id),
            ("edit_cybernetics", "Bul cybernetics", content_edition_id),
            ("edit_opm", "Jor Jour. of Num. and Appl. Math.", content_edition_id),
            ("edit_taapsd", "Con TAAPSD", content_edition_id),
        )

# department, institute, subdivision,
disid_geography = 1
disid_geology = 2
disid_economics = 3
disid_history = 4
disid_mechmath = 5
disid_preparatory = 6
disid_radiophysics = 7
disid_cybernetics = 8
disid_interstudents = 9
disid_psychology = 10
disid_sociology = 11
disid_physics = 12
disid_philosophy = 13
disid_chemistry = 14
disid_law = 15
disid_linguistics = 16
disid_journalism = 17
disid_biology = 18
disid_conteducation = 19
disid_interrelations = 20
disid_military = 21
disid_technologies = 22

dis_geography = u"geography"
dis_geology = u"geology"
dis_economics = u"economics"
dis_history = u"history"
dis_mechmath = u"mechmath"
dis_preparatory = u"preparatory"
dis_radiophysics = u"radiophysics"
dis_cybernetics = u"cybernetics"
dis_interstudents = u"interstudents"
dis_psychology = u"psychology"
dis_sociology = u"sociology"
dis_physics = u"physics"
dis_philosophy = u"philosophy"
dis_chemistry = u"chemistry"
dis_law = u"law"
dis_linguistics = u"linguistics"
dis_journalism = u"journalism"
dis_biology = u"biology"
dis_conteducation = u"conteducation"
dis_interrelations = u"interrelations"
dis_military = u"military"
dis_technologies = u"technologies"

dis_lst = [
            (disid_geography, dis_geography, u"Географічний факультет", u"Faculty of Geography"),
            (disid_geology, dis_geology, u"Геологічний факультет", u"Faculty of Geology"),
            (disid_economics, dis_economics, u"Економічний факультет", u"Faculty of Economics"),
            (disid_history, dis_history, u"Історичний факультет", u"Faculty of History"),
            (disid_mechmath, dis_mechmath, u"Механіко-математичний факультет", u"Faculty of Mechanics and Mathematics"),
            (disid_preparatory, dis_preparatory, u"Підготовчий факультет", u"Faculty of Preparatory Studies"),
            (disid_radiophysics, dis_radiophysics, u"Радіофізичний факультет", u"Faculty of Radiophysics"),
            (disid_cybernetics, dis_cybernetics, u"Факультет кібернетики", u"Faculty of Cybernetics"),
            (disid_interstudents, dis_interstudents, u"Факультет навчання іноземних громадян", u"Faculty for International Students"),
            (disid_psychology, dis_psychology, u"Факультет психології", u"Faculty of Psychology"),
            (disid_sociology, dis_sociology, u"Факультет соціології", u"Faculty of Sociology"),
            (disid_physics, dis_physics, u"Фізичний факультет", "Faculty of Physics"),
            (disid_philosophy, dis_philosophy, u"Філософський факультет", u"Faculty of Philosophy"),
            (disid_chemistry, dis_chemistry, u"Хімічний факультет", u"Faculty of Chemistry"),
            (disid_law, dis_law, u"Юридичний факультет", u"Faculty of Law"),
            (disid_linguistics, dis_linguistics, u"Інститут філології", u"Institute of Linguistics"),
            (disid_journalism, dis_journalism, u"Інститут журналістики", u"Institute of Journalism"),
            (disid_biology, dis_biology, u"Навчально-науковий центр \"Інститут біології\"", u"Institute of Biology"),
            (disid_interrelations, dis_interrelations, u"Інститут міжнародних відносин", u"Institute of International Relations"),
            (disid_conteducation, dis_conteducation, u"Інститут післядипломної освіти", u"Institute of Continuing Education"),
            (disid_military, dis_military, u"Військовий інститут", u"Military Academy"),
            (disid_technologies, dis_technologies, u"Інститут високих технологій", u"Institute of High Technologies"),
        ]

# field of science
fos_physical_mathematical = u"фізико-математичні науки"
fos_natural_sciences = u"природничі науки"
fos_economics = u"економічні науки"
fos_philology = u"філологічні науки"
fos_life_sciences = u"біологічні науки"
fos_history_sciences = u"історичні науки"
fos_linguistics = u"мовознавство"
fos_study_of_literature = u"літературознавство"
fos_political_sciences = u"політичні науки"
fos_jurisprudence = u"юридичні науки"
fos_philosophy_sciences = u"філософські науки"

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

# edition

edition_id = 'edition_id'
edition_dic = 'edition_dic'
alias = 'alias'
dis_id = "dis_id"
uk_name = 'uk_name'
en_name = 'en_name'
uk_abbrev = 'uk_abbrev'
en_abbrev = 'en_abbrev'
category = 'category'
subject_matter_uk = 'subject_matter_uk'
subject_matter_en = 'subject_matter_en'
foundation_year = 'foundation_year'
issues_by_year = 'issues_by_year'
gov_certificate_date = 'gov_certificate_date'
gov_certificate_num = 'gov_certificate_num'
vac_certificate_date = 'vac_certificate_date'
vac_certificate_num = 'vac_certificate_num'
ISSN = 'ISSN'
field_of_science_lst = 'field_of_science_lst'
phone = 'phone'
email = 'email'
address_uk = 'address_uk'
address_en = 'address_en'
rubric_lst = 'rubric_lst'

# edition aliases
# als_astronomy = u"astronomy"
# als_biology = u"biology"
# als_military = u"military"
# als_geography = u"geography"
# als_geology = u"geology"
# als_economics = u"economics"
# als_journalism = u"journalism"
# als_philology = u"philology"
# als_plant = u"plant"
# als_history = u"history"
# als_cybernetics = u"cybernetics"
# als_literature = u"literature"
# als_math_mech = u"math_mech"
# als_relations = u"relations"


edtid_phys_math = 1
edtid_taapsd = 2
edtid_opm = 3
edtid_cybernetics = 4
edtid_astr_space_phys = 5
edtid_mech_math = 6
edtid_world_of_mathematics = 7
edtid_probability_and_statistics = 8

edt_phys_math = u"phys_math"
edt_taapsd = u"taapsd"
edt_opm = u"opm"
edt_cybernetics = u"cybernetics"
edt_astr_space_phys = u"astr_space_phys"
edt_mech_math = u"mech_math"
edt_world_of_mathematics = u"iwom"
edt_probability_and_statistics = u"tps"

######################## кибернетика ########################

edtnm_phys_math = {edition_id: edtid_phys_math,
             edition_dic: { alias: edt_phys_math,
                      dis_id: disid_cybernetics,
                      uk_name: u"Вісник КНУ серія фіз.-мат. науки",
                      en_name: u"Bulletin of KNU Series Sci. science",
                      uk_abbrev: u"Фіз.-мат. науки",
                      en_abbrev: u"Sci. science",
                      category: cat_journal,
                      subject_matter_uk: u"висвітлення результатів досліджень у різних галузях математики, "
                        u"інформатики, механіки, фізики та радіофізики",
                      subject_matter_en: u"coverage of research in various fields of mathematics,"
                            u"computer science, mechanics, physics and radio physics",
                      foundation_year: 1991,
                      issues_by_year: 4,
                      gov_certificate_date: u'2009-12-11',
                      gov_certificate_num: u"КВ № 16299-4771 Р",
                      vac_certificate_date: u"1999-06-09",
                      vac_certificate_num: u"1-05/7",
                      ISSN: u"1812-5409",
                      field_of_science_lst: [fos_physical_mathematical, ],
                      phone: u"(044) 259-01-49",
                      email: u"",
                      address_uk: u"Київський національний університет імені Тараса Шевченка, "
                            u"Факультет кібернетики, "
                            u"просп. акад. Глушкова, 2, корп. 6, кімн. 23, Київ-127, Україна, 03127",
                      address_en: u"Kyiv National Taras Shevchenko, "
                                u"Department of Cybernetics, "
                                u"ave. Acad. Glushkov, 2, Bldg. 6 BR. 23, Kyiv-127, Ukraine, 03127",
                      rubric_lst:[(1,
                                 u"алгебра, геометрія та теорія ймовірностей",
                                 u"algebra, geometry, and probability theory"),
                                (2,
                                 u"диференціальні рівняння, математична фізика та механіка",
                                 u"differential equation, mathematical physics, mechanics"),
                                (3,
                                 u"комп'ютерні науки та інформатика",
                                 u"computer science and informatics"),
                                (4,
                                 u"радіофізика",
                                 u"radiophysics"),
                                (5,
                                 u"сучасна фізика",
                                 u"modern physics"),
                               ]
                     }
             }

edtnm_taapsd = {edition_id: edtid_taapsd,
             edition_dic: { alias: edt_taapsd,
                      dis_id: disid_cybernetics,
                      uk_name: u"Теоретичні та прикладні аспекти побудови програмних систем",
                      en_name: u"Theoretical and applied aspects of program systems development",
                      uk_abbrev: u"TAAPSD",
                      en_abbrev: u"TAAPSD",
                      category: cat_conference,
                      subject_matter_uk: u"",
                      subject_matter_en: u"",
                      foundation_year: 0,
                      issues_by_year: 1,
                      gov_certificate_date: None,
                      gov_certificate_num: u"",
                      vac_certificate_date: None,
                      vac_certificate_num: u"",
                      ISSN: u"",
                      field_of_science_lst: [fos_physical_mathematical, ],
                      phone: u"(044) 259-01-49",
                      email: u"",
                      address_uk: u"Київський національний університет імені Тараса Шевченка, "
                            u"Факультет кібернетики, "
                            u"просп. акад. Глушкова, 2, корп. 6, кімн. 603, Київ-127, Україна, 03127",
                      address_en: u"Kyiv National Taras Shevchenko, "
                                u"Department of Cybernetics, "
                                u"ave. Acad. Glushkov, 2, Bldg. 6 BR. 603, Kyiv-127, Ukraine, 03127",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

edtnm_opm = {edition_id: edtid_opm,
             edition_dic: { alias: edt_opm,
                      dis_id: disid_cybernetics,
                      uk_name: u"Журнал обчислювальної та прикладної математики",
                      en_name: u"Journal of numerical and applied mathematics",
                      uk_abbrev: u"ОПМжурнал",
                      en_abbrev: u"OPMjournal",
                      category: cat_journal,
                      subject_matter_uk:
                      u"Проблематика журналу: диференціальні рівняння, математична фізика,"
                      u" теорія ймовірностей і математична статистика, обчислювальна математика,"
                      u" варіаційне числення та теорія оптимального керування, теоретичні основи інформатики"
                      u" та кібернетики, математичне моделювання та обчислювальні методи,"
                      u" математичне та програмне забезпечення машин та систем, системний аналіз та"
                      u" теорія оптимальних рішень.",
                      subject_matter_en:
                      u"Issues: differential equations, mathematical physics, theory of probability"
                      u"and mathematical statistics, numerical mathematics, variational calculation and"
                      u"optimal control theory, theoretical foundations of informatics and cybernetics,"
                      u"mathematical simulation and numerical methods, software, system analysis and"
                      u"theory of optimal decisions.",
                      foundation_year: 1965,
                      issues_by_year: 3,
                      gov_certificate_date: "2000-06-26",
                      gov_certificate_num: u"КВ 4246",
                      vac_certificate_date: "2010-07-01",
                      vac_certificate_num: u"",
                      ISSN: u"0868-6912",
                      field_of_science_lst: [fos_physical_mathematical, ],
                      phone: u"044-259-04-36",
                      email: u"opmjournal@gmail.com",
                      address_uk:
                      u"Київ, пр. Глушкова, 4д,"
                      u" Київський національний університет імені Тараса Шевченка,"
                      u" факультет кібернетики, кафедра обчислювальної математики, к. 218.",
                      address_en:
                      u"Kiev, prospekt Glushkova 4d,"
                      u" Kiev National Taras Shevchenko University,"
                      u" faculty of cybernetics, department of numerical mathematics, room 218.",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

edtnm_cybernetics = {edition_id: edtid_cybernetics,
             edition_dic: { alias: edt_cybernetics,
                      dis_id: disid_cybernetics,
                      uk_name: u"Вісник Київського національного університету імені Тараса Шевченка. КІБЕРНЕТИКА.",
                      en_name: u"Bulletin of Taras Shevchenko National university of Kyiv. Cybernetics.",
                      uk_abbrev: u"Вісник КНУ, Кібернетика.",
                      en_abbrev: u"Bulletin of KNU, Cybernetics",
                      category: cat_herald,
                      subject_matter_uk:
                      u"Наведено результати досліджень з аналізу, оцінки, керування й оптимізації"
                      u" динамічних систем, проблеми еколого-економічного аналізу та чисельних методів моделювання"
                      u" процесів. Для викладачів, наукових співробітників, аспірантів і студентів.",
                      subject_matter_en:
                      u"In this issue the results of researches in analysis, estimates, control and "
                      u"optimization of dynamical systems, problems of ecology-economic analysis and "
                      u"numerical methods of procwss are presented. For scientists, professors, "
                      u"aspirants and students.",
                      foundation_year: 2000,
                      issues_by_year: 1,
                      gov_certificate_date: "2002-10-31",
                      gov_certificate_num: u"КВ № 16271-4743Р",
                      vac_certificate_date: "2011-01-26",
                      vac_certificate_num: u"№1-05/1",
                      ISSN: u"1728-3817",
                      field_of_science_lst: [fos_physical_mathematical, fos_natural_sciences],
                      phone: u"+380 44 258 89 84",
                      email: u"dkh@unicyb.kiev.ua",
                      address_uk:
                      u"03680, Київ-680, Проспект Академіка Глушкова, 4 Д, факультет кібернетики",
                      address_en:
                      u"03680б Kyiv, Prospekt akademika Glushkova, 4 D, faculty of cybernetics",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

######################## мех-мат ########################

edtnm_astr_space_phys = {edition_id: edtid_astr_space_phys,
             edition_dic: { alias: edt_astr_space_phys,
                      dis_id: disid_mechmath,
                      uk_name: u"Здобутки астрономії та фізики космосу",
                      en_name: u"Advances in Astronomy and Space Physics",
                      uk_abbrev: u"ЗАФК",
                      en_abbrev: u"AASP",
                      category: cat_journal,
                      subject_matter_uk: u"Публікація оригінальних і оглядових робіт аспірантів"
                        u" та молодих науковців з основних проблем астрономії, космічної фізики, "
                        u"та суміжних областей: геофізики та інформаційних технологій"
                        ,
                      subject_matter_en: u"Publication of original and review manuscripts of "
                        u"doctoral students and young researchers on the main problems of "
                        u"Astronomy, Space Physics and related fields: Geophysics and "
                        u"Information Technology"
                        ,
                      foundation_year: 2011,
                      issues_by_year: 2,
                      gov_certificate_date: u"",
                      gov_certificate_num: u"КВ 18721-7521Р",
                      vac_certificate_date: u"",
                      vac_certificate_num: u"",
                      ISSN: u"2227-1481",
                      field_of_science_lst: [fos_physical_mathematical, fos_natural_sciences, ],
                      phone: u"(044)526-44-57",
                      email: u"aasp.editorial.board@gmail.com",
                      address_uk: u"Кафедра астрономії та фізики космосу, "
                            u"фізичний факультет КНУ імені Тараса Шевченка "
                            u"пр-т акад. Глушкова, 4 "
                            u"03127 Київ",
                      address_en: u"Astronomy and Space Physics Department "
                            u"Faculty of Physics of the Taras Shevchenko National Univesity "
                            u"of Kyiv"
                            u"Glushkova ave. 4, Kyiv 03127",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

edtnm_mech_math = {edition_id: edtid_mech_math,
             edition_dic: { alias: edt_mech_math,
                      dis_id: disid_mechmath,
                      uk_name: u"Вісник Київського національного університету імені Тараса "
                      u"Шевченка Математика. Механіка",
                      en_name: u"Visnyk Of Taras Shevchenko National University Of Kyiv, "
                        u"Mechanics And Mathematics",
                      uk_abbrev: u"Вісник КНУ, Математика. Механіка",
                      en_abbrev: u"Bulletin, Mechanics And Mathematics",
                      category: cat_herald,
                      subject_matter_uk: u"Публікуються оригінальні статті з актуальних питань "
                        u"математичного аналізу, теорії диференціальних рівнянь, математичної "
                        u"фізики, геометрії, топології, алгебри, теорії ймовірностей, теорії "
                        u"оптимального керування, теоретичної механіки, теорії пружності, "
                        u"механіки рідини та газу. Усі матеріали, які надходять до редколегії, "
                        u"рецензуються. Після виходу у світ усі матеріали реферуються в "
                        u"\"Zentralblatt MATH\" (http://www.emis.de/ZMATH). Для науковців, "
                        u"викладачів, студентів.",
                      subject_matter_en: u"The bulletin publishes original articles devoted to "
                        u"topical problems of mathematical analysis, theory of differential "
                        u"equations, mathematical physics, geometry, topology, algebra, "
                        u"probability theory, optimal control, theoretical mechanics, elasticity "
                        u"theory, fluid and gas mechanics. All articles submitted to the "
                        u"Editorial board are reviewed. After publication, each article is "
                        u"provided with an abstract in \"Zentralblatt MATH\" "
                        u"(http://www.emis.de/ZMATH). For scientist, professors, students.",
                      foundation_year: 1958,
                      issues_by_year: 2,
                      gov_certificate_date: u'2009-12-11',
                      gov_certificate_num: u"КВ № 16007-4479Р",
                      vac_certificate_date: u"2010-05-26",
                      vac_certificate_num: u"1-05/4",
                      ISSN: u"1728-3817",
                      field_of_science_lst: [fos_physical_mathematical, ],
                      phone: u"380 44 259 05 42",
                      email: u"alex_z_ua@univ.kiev.ua",
                      address_uk: u"03127, Київ-127, просп. акад. Глушкова, 4Е, "
                        u"механіко-математичний факультет",
                      address_en: u"The Faculty of Mechanics and Mathematics"
                        u"4E, Prospect Akademika Hlushkova"
                        u"03127, Kyiv-127",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

edtnm_world_of_mathematics = {edition_id: edtid_world_of_mathematics,
             edition_dic: { alias: edt_world_of_mathematics,
                      dis_id: disid_mechmath,
                      uk_name: u"У світі математики",
                      en_name: u"In the World of Mathematics",
                      uk_abbrev: u"У світі математики",
                      en_abbrev: u"In the World of Mathematics",
                      category: cat_journal,
                      subject_matter_uk: u"Журнал розрахований в першу чергу на школярів і "
                        u"студентів математичних спеціальностей коледжів, класичних, педагогічних "
                        u"і технічних університетів. Журнал може бути корисним викладачам "
                        u"математики, математикам-професіоналам та всім любителям математики. "
                        u"Зокрема, журнал друкує багато олімпіадних і конкурсних матеріалів з "
                        u"математики, а також матеріали для шкільних гуртків.",
                      subject_matter_en: u"The journal is addressed to schoolchildren and "
                        u"students of mathematical specialities of colleges and classical, "
                        u"pedagogical and technical universities. The journal can be useful for "
                        u"mathematics teachers, professional mathematicians and all amateurs of "
                        u"mathematics. In particular the journal publishes a lot of Olympic and "
                        "competitive materials in Mathematics, as well as materials for school "
                        "circles.",
                      foundation_year: 1995,
                      issues_by_year: 4,
                      gov_certificate_date: u"",
                      gov_certificate_num: u"КВ № 1564",
                      vac_certificate_date: u"",
                      vac_certificate_num: u"",
                      ISSN: u"1029-4171",
                      field_of_science_lst: [fos_physical_mathematical, ],
                      phone: u"044-259-05-91",
                      email: u"usm@univ.kiev.ua",
                      address_uk: u"01601 МСП, Київ, КНУ імені Тараса Шевченка, кафедра математичного аналізу",
                      address_en: u"01601 MSP, Kyiv, Taras Shevchenko National University, Board of Mathematical Analysis",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

edtnm_probability_and_statistics = {edition_id: edtid_probability_and_statistics,
             edition_dic: { alias: edt_probability_and_statistics,
                      dis_id: disid_mechmath,
                      uk_name: u"Теорія ймовірностей та математична статистика",
                      en_name: u"Theory of Probability and Mathematical Statistics",
                      uk_abbrev: u"Теорія ймовір. та матем. статист.",
                      en_abbrev: u"Theor. Probability and Math.Statist.",
                      category: cat_journal,
                      subject_matter_uk: u"У журналі публікуються оригінальні статті з теорії "
                        u"ймовірностей, теорії випадкових процесів та полів, математичної "
                        u"статистики та їх застосувань. Головні напрямки: випадкові процеси та "
                        u"поля, статистика випадкових процесів та полів, випадкові оператори, "
                        u"стохастичні диференціальні рівняння, стохастичний аналіз, теорія черг, "
                        u"теорія надійності, процеси ризику, фінансова та актуарна математика.",
                      subject_matter_en: u"The journal publishes original peer-reviewed research "
                        u"papers in probability theory, theory of random processes and fields, "
                        u"mathematical statistics and its applications. The main subjects covered "
                        u"by the journal are: random processes and fields; statistics of "
                        u"random processes and fields; random operators; stochastic differential "
                        u"equations; stochastic analysis; queiung theory; reliability theory; "
                        u"risk processes; financial and actuarial mathematics.",
                      foundation_year: 1970,
                      issues_by_year: 2,
                      gov_certificate_date: u"2000-05-23",
                      gov_certificate_num: u"КВ4229",
                      vac_certificate_date: u"2010-04-14",
                      vac_certificate_num: u"N 1-05/3",
                      ISSN: u"0868-6904",
                      field_of_science_lst: [fos_physical_mathematical, ],
                      phone: u"259-03-92",
                      email: u"tims@univ.kiev.ua",
                      address_uk: u"Україна, 01601, Київ, вул. Володимирська, 64/13, Київський "
                        u"національний університет імені Тараса Шевченка, механіко-математичний "
                        u"факультет, кафедра теорії ймовірностей, статистики та актуарної "
                        u"математики",
                      address_en: u"Ukraine, 01601, Kyiv, 64/13 Volodymyrska str., "
                        u"Kyiv National Taras Shevchenko University, Faculty of Mechanics "
                        u"and Mathematics, Department of Probability Theory, Statistics and "
                        u"Actuarial Mathematics",
                      rubric_lst:[(1,
                                 u"",
                                 u""),
                               ]
                     }
             }

edition_lst = [
# cybernetics
               edtnm_cybernetics, edtnm_phys_math, edtnm_opm, edtnm_taapsd,
# mech-math
               edtnm_astr_space_phys, edtnm_mech_math, edtnm_world_of_mathematics, edtnm_probability_and_statistics
               ]
