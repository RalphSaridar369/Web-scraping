from bs4 import BeautifulSoup
import requests
from xlrd import open_workbook
import xlwt
import xlrd
from datetime import datetime
from xlutils.copy import copy


#scraping the data

url = requests.get('https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?')
page = BeautifulSoup(url.content, 'html.parser')

TotalCases = page.findAll(id="maincounter-wrap")[0].find(class_="maincounter-number").find('span').get_text()
TotalDeaths = page.findAll(id="maincounter-wrap")[1].find(class_="maincounter-number").find('span').get_text()
TotalRecovered = page.findAll(id="maincounter-wrap")[2].find(class_="maincounter-number").find('span').get_text()

ActiveCases = page.find(class_="panel_flip").find(class_="panel_front").find(class_="number-table-main").get_text()
ACMild = page.find(class_="panel_flip").find(class_="panel_front").findAll('div')[2].findAll('div')[0].find('span').get_text()
ACCritical = page.find(class_="panel_flip").find(class_="panel_front").findAll('div')[2].find('div').findNextSibling().find(class_="number-table").get_text()

ClosedCases = page.findAll(class_="panel_flip")[1].find(class_="panel_front").find(class_="number-table-main").get_text()
CCRecovered = page.findAll(class_="panel_flip")[1].find(class_="panel_front").findAll('div')[2].findChild().findChild().get_text()
CCDeaths = page.findAll(class_="panel_flip")[1].find(class_="panel_front").findAll('div')[2].findAll('div')[2].findChild().get_text()

print(TotalCases, "\n", TotalDeaths , "\n", TotalRecovered, "\n", ActiveCases, "\n", ACMild,
      "\n", ACCritical, "\n", ClosedCases, "\n", CCRecovered, "\n", CCDeaths)

# styling the sheets

style= xlwt.XFStyle()
style.num_format_str="D-MMMM-YY"

#inserting the data

def saveWorkSpace():

    rb = xlrd.open_workbook('test.xls',formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(r, 0, datetime.now(), style)
    sheet.write(r, 1, TotalCases)
    sheet.write(r, 2, TotalDeaths)
    sheet.write(r, 3, TotalRecovered)
    sheet.write(r, 4, ActiveCases)
    sheet.write(r, 5, ACMild)
    sheet.write(r, 6, ACCritical)
    sheet.write(r, 7, ClosedCases)
    sheet.write(r, 8, CCRecovered)
    sheet.write(r, 9, CCDeaths)
    sheet.write(r, 10, )
    wb.save('test.xls')
    print('Wrote accounts.xls')
    print(r)

saveWorkSpace()

# if you want to automate the program daily
# write all this code in a while(true): loop
# and try to request from the server 4-5 times max
# so that you don't get banned
# watch this youtube video https://www.youtube.com/watch?v=0fQjA8w1woQ