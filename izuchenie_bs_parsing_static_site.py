import re

import requests
import lxml
from bs4 import BeautifulSoup as bs
import codecs
import html5lib
import html

# __________вариант нажатия на кнопку при работе с сайтом_
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('http://yo.ur/pretty-and-cool/url')
# element = driver.find_element_by_css_selector('button.with-class#or-id')
# element.click()
# ___________________________________________________


#url = "https://www.avito.ru/"
url = "https://m1.top/ru/"
# url = "https://izhevsk.hh.ru"
# url = "https://www.radiorecord.ru/"


# ________раскрывет библиотеку в бутефал суп ______________
file_requests = requests.get(url)


# __________ сами прарсеры через которую открывется  суп ______
soup_html_parser = bs(file_requests.text, 'html.parser')# встроеный в питон парсер
soup_lxml = bs(file_requests.text, 'lxml')
soup_html5lib = bs(file_requests.text, 'html5lib')


# ______________ печатает всю страницу __________-
# print(soup_lxml) #парсит практический без отсупов
# print(soup_html_parser) #парсит практический без отсупов
# print(soup_html5lib) #парсит с отступами как в html


# _____________ печатет титульный тег ___________
# title_lxml = soup_lxml.title
#print(1 ,title_lxml) # целый с тегом
# print(2, title_lxml.text) # только текст
# print(3 , title_lxml.string, 'job is  metod strong') # только строка


# ______________методы работы с .find _______________
# .find() показывает только первый искомый тег
# .find_all() все теги

# page_h1_xlml = soup_lxml.find("div")# format strong i teg
# for i in page_h1_xlml:
#     print( i, "hello word", type (i) )
# print(page_h1_xlml)
# page_all_h1_xlml = soup_lxml.find_all("div")
# save v formate list # можно перебирать черз for
# print(page_all_h1_xlml)


# _________ искать через  class find ___________
# container_class = soup_lxml.find("div", class_="container")
# container_class_plus = soup_lxml.find("div", class_="container").find("span").text
# # может не открыть если имяя контейнера указоно не полностью
# # пример на сайте радидио рекорд есть container-fluid и если
# # не полностью то не откроет
# container_class_plus_id = soup_lxml.find("div", {"class": "container"}).find("span").text
#можно в фигурные скобки добовлять искомое пример "id" : "aaa" словарь с ключом и значением
# print(container_class_plus) #
# print(container_class.text.strip())#obect soup job metod .text na .find
# print(container_class_plus_id)


# _________ искать через  class find_all  _______
# find_all_teg = soup_lxml.find(class_="container").find_all("span")
# print(find_all_teg)
# можно перебирать черз for
# for i in find_all_teg:
#     print(i.text)
#можно выводить по индексу
# print(find_all_teg[0])
# #можно выводить по тексту
# print(find_all_teg[0].text)


# ____________________parsin silok na site________________
# если знаешь класс и теги в которых он находится
# social_liks = soup_lxml(class_ = "bloko-column bloko-column_xs-1 bloko-column_s-1 bloko-column_m-1 bloko-column_l-1")#.find("ul").find_all
# парсин всег тегов


# ______общий парсинг сайта по тегам (здесь по сылкам) ________________
# all_teg_href_src = soup_lxml.find_all("a")
# # print(all_teg_href_src)
#
# for i in all_teg_href_src:
#     i_text = i.text # name silka
#     i_url = i.get("href") #sbor silok c sita
#     print(f"{i_text}: {i_url}")


# ____методы для парсинга классасодежащего
# несколько вложений парсит во внуторь и верх____
# .find_parent() .find.parents()

# # принт выше пост идет по одному значению в верх по сайту
# post_div = soup_lxml.find(class_="menu__btn-close").find_parent()
# print(post_div) #принт выше пост идет по одному значению в верх по сайту

# post_divs = soup_lxml.find(class_="menu__btn-close")\
#     .find_parents(class_="row align-items-center")\
#     # job s classom i ("div", "row align-items-center")
# # .find_parents() если в скобки ставим данные до них\
# # идет поиск, если огронечения нет ищет до конца \
# # списка ввверх
# print(post_divs)


# ______шагает по одному или несколько
# элементов вниз или верх __________________
# .next_element .previous_element.find_next()

# next_el = \
#     soup_lxml.find\
#         (class_="lang-change col-3 col-md-2 col-lg-1 text-end font-expanded-i")\
#         .next_element.next_element
# выводит следующий элемент в этом случие требуется повтоить/
# два раза чтобы увидить следующий элемет ходит по одному шагу \
#     вниз
# print(next_el)

# find_next_el = \
#     soup_lxml.find\
#         (class_="lang-change col-3 col-md-2 col-lg-1 text-end font-expanded-i")\
#         .find_next().text\
# пропускае пробелы и переходит на следующую строку где есть \
#     элемент
# print(find_next_el)


# _____ парсинг тега __________
# .find_next_sibing()\
# только первый из них:
# .find_previous_sibings()\
# возвращает все подходящие одноуровневые элемент
# par_fin_nex_sib = soup_lxml.find(class_="pt-2 pt-lg-0 mv-4")\
#     .find_next_sibling()
# print(par_fin_nex_sib)

soup_find = soup_lxml.find()

# par_fin_pre_sib = soup_find.find_previous_siblings() #(class_="pt-2 pt-lg-0 mv-4")
# print(par_fin_pre_sib)

# ___ parsing po tegs ________
# "a", "href", "div", "h1, h2, h3", "form", "img", "li"\
# "input",  "batton", "script", "nav", "ul", "header"
# par_kus_zaprosa = soup_lxml.find_all()#можно вставить тег\
# для сужения запросов по отбору с парсеного
#
# #print(par_kus_zaprosa)
# list_i_re = []
# list_teg = [ "a", "div", "h1", "h2", "h3", "form", \
#              "img", "li", "input", "batton", "script",\
#              "nav", "ul", "header", "href", "class","span"\
#              ,"name", "style", "src"]
#
# def par_prov_list():
#     for i in par_kus_zaprosa:
#         i_re = i.get("href")
#         for teg_i in list_teg:
#             i_re_text = i.get(teg_i)
#             if i_re_text not in list_i_re:
#                 list_i_re.append(i_re_text)
#     print(list_i_re, len(list_i_re))
#     return list_i_re
#
# # par_prov_list()

# ___ парсинг по обрвыку слова ________
# parsing one strong .find
# par_find_text = soup_lxml.find(text=re.compile("Оффе"))
# # сильно зависит от регистра искомого
# print(par_find_text)

# par_find_all_text = soup_lxml.find_all\
#     (text=re.compile("([Оо]ффе)"))
# # собирает не зависит от регистра искомого
# print(par_find_all_text)


# # ___ парсинг по методики стической строницы ресурс\
# # https://www.youtube.com/watch?v=os5ig-EekMs&t=0s_________
# url_2 = "https://en.soccerwiki.org/league.php?leagueid=28"
# # 1. получение html кода
# html2 = requests.get(url_2).text
# # 2. присоеденения bs и вкладка аргумента html2 и определения \
# #     черз какой парсер будем использовать "html.parser"
# parser_soup_metod2 = bs(html2, "html.parser")
# # print(parser_soup_metod2.prettify())
# # class_="row mt-3 mb-3" table clubs
# # 3. через .find_all собираем данные со всей доступной страницы\
# # сужаем поиск через "div" аргумент и еще сужаем\
# #  уточняем какой класс class_="table-custom-responsive mb-3"\
# # так как отсеивает строчный метод сужаем индексом поиск [0]
# div_1 = parser_soup_metod2.find_all\
#     ("div", class_="table-custom-responsive mb-3")[0]
# и к томужее таблици 2 шт выбераем [0]
# # 4. для сужения поиска применяем div_1.find котрый\
# #  и собираем данные под тегом "table" , чтобы увиличить \
# #     коли-во принимаемых классов применяем \
# #     attrs = {'class': ["table-custom", "table-roster"]}
# table = div_1.find\
#      ("table",  attrs={'class':["table-custom", "table-roster"]})
# # 5. собирем полученые данные  table.select \
# #     аргументом задаем ('td')
# td_s = table.select('td')#.team:text-left')
#
# # отсеваем даные через for td in td_s:\
# # через count_club подбираем нужные
# count_club = 3
# for td in td_s:
#     count_club +=1
#     td_ob = td#.text.strip()
#     if count_club ==5:
#     # if td_ob != None:
#          print(td_ob)
#          count_club = 0


# # # ___ парсинг по методики динамический строницы ресурс\
# # # https://www.youtube.com/watch?v=sjq8KSMWxQ4_________
#
# # урл сосотит из 2 частей икать придется на двух частях
# base_url = "https://en.soccerwiki.org/"
# extra_url = "league.php?leagueid=28"
#
# html_2 = requests.get(base_url+extra_url).text
# soup = bs(html_2, "html.parser")
# # на первом урл выяляем extra_url всех команд
# div = soup.find_all\
#     ("div", class_="table-custom-responsive mb-3")[0]
# # table = div.find("table", class_="table-roster")
# # "text-left text-dark font-weight-normal"#, class_="pt-0 pb-0 pr-0 pl-2 text-center")
# # собираем класс в таблице где лежат "href"
# table_td_all = div.find_all("td", class_="text-left")
#
#
# clubs = []
# count_comand=0
# # for table_td in table_td_all:
# for index in range(1, len(table_td_all)):
#     count_comand+=1
#     if count_comand == 4:
# # особеность достать html cod надо открыть тег "а"
#         td = table_td_all[index].find("a")
# # достоем даные в теге где нет классов через .get
#         td_href = td.get("href")
# # собираем "href" которые будут сотовляющей адреса сбора инфы
#         clubs.append(td_href)
#         count_comand=0
#
#
#
# natin_gamers_list = []
# # переход в клубы и поиск стрну игрока
# for club_url in clubs:
#     html_3 = requests.get(base_url+club_url).text
#     soup_3 = bs(html_3, "html.parser")
# #     собираем нужный класс ищем на странице подобрать индекс
#     div_table_gamers = soup_3.find_all\
#         ("div", class_="table-custom-responsive mb-3")[0]
#     # сужаем классом поиск нужного названия
#     natin_gamers = div_table_gamers.find_all \
#         ('div', class_='d-inline')
#     for raskl_list in natin_gamers: #soup_3.find(id="datatable").previous_siblings:
#         for raskl_html in raskl_list:
#     # искомое находится в "title" вытаскиваем через .get
#             i_2 = raskl_html.get("title")#.pre(vious_siblings
#             natin_gamers_list.append(i_2)
#     # ('td', class_='text-center')[6]
#
#
# # print(natin_gamers_list)
# # собрал данные для того чтобы их перебрать если выпадет\
# #     ошибка или заблочит сайт
# natin_gamers_list_copy = ['Brazil', 'Ireland', 'England', \
#     'Argentina', 'England', 'Wales', 'England', 'England', \
#     'Zimbabwe', 'Colombia', 'England', 'England', 'England', \
#     'England', 'England', 'Denmark', 'England', 'Denmark', \
#     'England', 'Scotland', 'England', 'England', 'Wales', \
#     'Wales', 'England', 'Jamaica', 'Scotland', 'England', \
#     'United States', 'Estonia', 'France', 'Brazil', 'England', \
#     'England', 'England', 'Japan', 'England', 'England', 'England',\
#     'Scotland', 'England', 'Ghana', 'Switzerland', 'Egypt', \
#     'Belgium', 'England', 'England', 'England', 'Portugal', \
#     'England', 'England', 'Romania', 'England', 'Ukraine', \
#     'Netherlands', 'Norway', 'England', 'Portugal', 'England',\
#     'England', 'England', 'England', 'Brazil', 'Brazil', \
#     'Brazil', 'Norway', 'England', 'Argentina', 'Sweden', \
#     'England', 'Finland', 'Poland', 'Poland', 'Brazil', 'Poland',\
#     'England', 'Netherlands', 'Scotland', 'England', 'England',\
#     'England', 'England', 'Netherlands', 'England', 'England', \
#     'France', 'Sweden', 'Brazil', 'Zimbabwe', 'France', 'Belgium',\
#     'Northern Ireland', 'Poland', 'France', 'France', 'England',\
#     'England', 'Scotland', 'England', 'England', 'England', \
#     'England', 'England', 'England', 'Brazil', 'England',\
#     'Scotland', 'England', 'Jamaica', 'Bermuda', 'Argentina', \
#     'England', 'England', 'England', 'Albania', 'Spain', 'England',\
#     'England', 'England', 'Jamaica', 'Sweden', 'Denmark', 'England',\
#     'Ireland', 'Norway', 'England', 'Denmark', 'Wales', 'England',\
#     'Ireland', 'Grenada', 'Germany', 'England', 'Denmark', 'Denmark',\
#     'Scotland', 'England', 'Denmark', 'Nigeria', 'Ireland', 'Spain',\
#     'Ukraine', 'Denmark', 'England', 'England', 'Congo DR', \
#     'Germany', 'Cameroon', 'Iran', 'England', 'Spain', 'England',\
#     'England', 'England', 'England', 'Netherlands', 'England', \
#     'Wales', 'Belgium', 'England', 'England', 'Ecuador', 'England',\
#     'Ecuador', 'Scotland', 'England', 'Ghana', 'Netherlands', \
#     'Japan', 'Ireland', 'Argentina', 'Poland', 'Germany', 'Ecuador',\
#     'Ireland', 'England', 'Australia', 'England', 'Argentina', \
#     'Turkey', 'England', 'Ireland', 'Paraguay', 'Belgium', \
#     'Senegal', 'Spain', 'England', 'United States', 'England',
#     'Senegal', 'Brazil', 'France', 'France', 'England', 'England',\
#     'Spain', 'England', 'Netherlands', 'Spain', 'France', 'Croatia',\
#     'Italy', 'Brazil', 'Switzerland', 'England', 'England', \
#     'England', 'England', 'England', 'Italy', 'England', 'England',\
#     'Jamaica', 'England', 'England', 'Albania', 'England', \
#     'England', 'Morocco', 'Germany', 'England', 'Gabon', \
#     'Ivory Coast', 'United States', 'Spain', 'England', 'Denmark', \
#     'England', 'United States', 'Northern Ireland', 'Ireland', \
#     'England', 'England', 'England', 'England', 'Ireland', \
#     'Scotland', 'Mali', 'Serbia', 'Netherlands', 'Ghana', 'England',\
#     'France', 'England', 'England', 'France', 'France', \
#     'Ivory Coast', 'Ghana', 'England', 'England', \
#     'Bosnia & Herzegovina', 'England', 'Switzerland', 'England', \
#     'Slovenia', 'Northern Ireland', 'England', 'England', 'Colombia',\
#     'England', 'England', 'England', 'England', 'Portugal', 'Ukraine',\
#     'Northern Ireland', 'Senegal', 'England', 'Belgium', 'Ireland', \
#     'Scotland', 'Mali', 'England', 'Northern Ireland', 'England', \
#     'England', 'Nigeria', 'England', 'France', 'England', 'Ireland', \
#     'England', 'England', 'England', 'Wales', 'Germany', 'Slovakia', \
#     'England', 'France', 'Ireland', 'United States', 'England', \
#     'Netherlands', 'France', 'United States', 'Portugal', 'England', \
#     'Switzerland', 'England', 'Scotland', 'Wales', 'Brazil', 'England',\
#     'Ireland', 'Serbia', 'Brazil', 'Finland', 'Brazil', 'Wales',\
#     'Israel', 'Congo DR', 'Wales', 'Jamaica', 'France', 'Spain',\
#     'Norway', 'Spain', 'Scotland', 'Austria', 'Norway', 'Germany',\
#     'Netherlands', 'Spain', 'Spain', 'England', 'Northern Ireland',\
#     'Denmark', 'England', 'England', 'United States', \
#     'Northern Ireland', 'England', 'England', 'England', 'England',\
#     'United States', 'England', 'Spain', 'England', 'England', \
#     'Netherlands', 'Colombia', 'Italy', 'Northern Ireland', 'Spain',\
#     'England', 'England', 'Denmark', 'Wales', 'England',\
#     'United States', 'Turkey', 'Northern Ireland', 'Denmark', \
#     'Belgium', 'Guyana', 'Netherlands', 'England', 'Ghana', \
#     'England', 'England', 'France', 'Senegal', 'England', 'Nigeria',\
#     'Belgium', 'Portugal', 'England', 'Thailand', 'England', \
#     'Belgium', 'England', 'England', 'Belgium', 'England', \
#     'England', 'England', 'England', 'Zambia', 'Nigeria', 'Spain', \
#     'Brazil', 'Spain', 'Ireland', 'England', 'Netherlands', \
#     'Cameroon', 'France', 'England', 'England', 'England', \
#     'England', 'Scotland', 'Greece', 'England', 'Spain', 'Brazil',\
#     'England', 'Brazil', 'England', 'United States', 'Spain', \
#     'England', 'Scotland', 'England', 'England', 'England', \
#     'England', 'Guinea', 'England', 'England', 'Scotland', \
#     'England', 'Poland', 'Portugal', 'England', 'Germany', \
#     'England', 'England', 'England', 'Brazil', 'Uruguay', \
#     'Colombia', 'England', 'Egypt', 'Portugal', 'Netherlands', \
#     'Brazil', 'Germany', 'England', 'Netherlands', 'Portugal', \
#     'England', 'Spain', 'Netherlands', 'England', 'Switzerland', \
#     'Venezuela', 'Northern Ireland', 'France', 'England', 'Spain',\
#     'Spain', 'England', 'England', 'England', 'Portugal', 'Germany',\
#     'England', 'Portugal', 'England', 'Spain', 'England', 'Norway',\
#     'Belgium', 'Algeria', 'Scotland', 'England', 'Argentina', \
#     'England', 'Portugal', 'Norway', 'Argentina', 'England',\
#     'Spain', 'England', 'England', 'England', 'Czech Republic', \
#     'Czech Republic', 'Northern Ireland', 'France', 'England', \
#     'England', 'England', 'England', 'Netherlands', 'Sweden', \
#     'England', 'England', 'Argentina', 'Spain', 'Netherlands', \
#     'England', 'England', 'Brazil', 'Brazil', 'England', 'Wales', \
#     'Poland', 'Scotland', 'England', 'England', 'Portugal', \
#     'Netherlands', 'England', 'Norway', 'England', 'Iraq', \
#     'Portugal', 'England', 'Denmark', 'England', 'England', \
#     'Brazil', 'Uruguay', 'Argentina', 'France', 'England', \
#     'England', 'England', 'England', 'France', 'Sweden', 'England',\
#     'Slovakia', 'England', 'Germany', 'England', 'Scotland',\
#     'Netherlands', 'Switzerland', 'England', 'England', 'Wales',\
#     'Ireland', 'England', 'Scotland', 'England', 'England', \
#     'Northern Ireland', 'England', 'Brazil', 'England', 'England', \
#     'Sweden', 'Spain', 'Scotland', 'England', 'England', 'England',\
#     'England', 'England', 'Scotland', 'Scotland', 'England', 'Peru',\
#     'Sweden', 'England', 'New Zealand', 'Mexico', 'England', \
#     'Australia', 'France', 'Paraguay', 'Brazil', 'England', 'Wales', \
#     'England', 'Bosnia & Herzegovina', 'England', 'Ivory Coast', \
#     'England', 'England', 'Scotland', 'France', 'Senegal', 'England',\
#     'Brazil', 'England', 'England', 'Switzerland', 'Belgium', \
#     'England', 'Ireland', 'Wales', 'Senegal', 'England', 'Ivory Coast',\
#     'Wales', 'France', 'Costa Rica', 'Portugal', 'England', 'England',\
#     'France', 'Brazil', 'Nigeria', 'England', 'Montserrat', \
#     'Northern Ireland', 'England', 'Nigeria', 'Wales', 'England', \
#     'Ireland', 'Argentina', 'Croatia', 'Ghana', 'Brazil', 'England', \
#     'Germany', 'France', 'Spain', 'France', 'England', 'Belgium',\
#     'England', 'England', 'England', 'England', 'Scotland', \
#     'Scotland', 'France', 'England', 'Mali', 'England', 'Norway',\
#     'England', 'England', 'Nigeria', 'France', 'England', 'England',\
#     'England', 'Ireland', 'Argentina', 'France', 'Colombia', \
#     'Estonia', 'England', 'England', 'Wales', 'England', 'England',\
#     'England', 'England', 'Uruguay', 'Denmark', 'England', 'Ireland',\
#     'Brazil', 'England', 'Ireland', 'England', 'England', 'England',\
#     'Mali', 'Senegal', 'Spain', 'Croatia', 'England', 'England', \
#     'England', 'England', 'Spain', 'Sweden', 'Brazil', \
#     'Korea Republic', 'Brazil', 'Poland', 'France', 'Ireland',\
#     'Morocco', 'Italy', 'England', 'Brazil', 'England', 'England',\
#     'France', 'Germany', 'Italy', 'England', 'Czech Republic', \
#     'Ireland', 'England', 'England', 'France', 'England', \
#     'England', 'Czech Republic', 'Scotland', 'England', \
#     'England', 'Bermuda', 'Spain', 'Argentina', 'Italy', 'England',\
#     'Brazil', 'Northern Ireland', 'Ivory Coast', 'Algeria', \
#     'England', 'Jamaica', 'England', 'Portugal', 'Montenegro', \
#     'Denmark', 'England', 'England', 'Iceland', 'Ireland', \
#     'Colombia', 'England', 'Portugal', 'England', 'Algeria', \
#     'Spain', 'Portugal', 'Mali', 'Ireland', 'England', 'Portugal', \
#     'Spain', 'Jamaica', 'Portugal', 'Portugal', 'Ireland', 'China',\
#     'Wales', 'Mexico', 'Austria', 'Spain', 'Portugal', \
#     'Korea Republic', 'Spain', 'Canada', 'Portugal', 'Brazil', \
#     'Portugal', 'Portugal']
# all_nations = {}
#
# for natin in natin_gamers_list:
# # если разбираем копию
# # for natin in natin_gamers_list_copy:
#     if natin in all_nations:
#         all_nations[natin] +=1
#     else:
#         all_nations[natin] = 1
# print(sorted(all_nations.items(),\
#              key=lambda item: item[1], reverse=True))
#
# print(all_nations, len(natin_gamers_list))


#_____________________  parsing privat site clouse code_______

url_strnica_1 =\
    "https://www.transfermarkt.com"
url_strnica_2 = \
    "/schnellsuche/ergebnis/schnellsuche?query=uefa"
# strano pohozi



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'}
html_2 = requests.get(url_strnica_1+url_strnica_2, headers=headers)
html_izmen_headers = html_2.text
soup_headers = bs(html_izmen_headers, "lxml")
# 1./open table na site SEARCH RESULTS: CLUBS - 199 HITS
# 2. с учетом их 10 стр.
# 3. открываем каждый клуб
# 4. в таблице SQUAD OF BAYERN MUNICH UEFA U19 раскрываем игрока и
# и считаем голы
# 5. результат сколько голов забила данный игрок на момент парсинга

print(soup_headers)



# # на первом урл выяляем extra_url всех команд
# div = soup.find_all\
#     ("div", class_="table-custom-responsive mb-3")[0]
# # table = div.find("table", class_="table-roster")
# # "text-left text-dark font-weight-normal"#, class_="pt-0 pb-0 pr-0 pl-2 text-center")
# # собираем класс в таблице где лежат "href"
# table_td_all = div.find_all("td", class_="text-left")

























