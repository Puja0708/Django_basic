from xlrd import open_workbook ,cellname ,sys
import os
sys.path.append("/Users/harshkothari/Dropbox/quoteme/aniweb/linteltest")  #Project file path
#Give Settings file (entry gateway in our Django modual) path
os.environ["DJANGO_SETTINGS_MODULE"] = "linteltest.settings"
from lintel.models import DateData,stockdata

file_to_import = 'database/j.xls'

column_count=14

book = open_workbook(file_to_import)

sheet = book.sheet_by_index(0)

dateList = ['02072014','01072014','30062014','29062014','28062014','27062014','26062014','25062014','24062014','23062014']

dateCount = 6
print "Workbook sheet name:%s" % sheet.name
print "Number of rows in sheet: %s" % sheet.nrows
d = DateData.objects.create(date = dateList[dateCount])
for row_index in range(1,sheet.nrows):
	d.stockdata_set.create(SC_CODE=sheet.cell(row_index,0).value,SC_NAME=sheet.cell(row_index,1).value,SC_GROUP=sheet.cell(row_index,2).value,SC_TYPE=sheet.cell(row_index,3).value,OPEN=sheet.cell(row_index,4).value,HIGH=sheet.cell(row_index,5).value,LOW=sheet.cell(row_index,6).value,CLOSE=sheet.cell(row_index,7).value,LAST=sheet.cell(row_index,8).value,PREVCLOSE=sheet.cell(row_index,9).value,NO_TRADES=sheet.cell(row_index,10).value,NO_OF_SHRS=sheet.cell(row_index,11).value,NET_TURNOV=sheet.cell(row_index,12).value,TDCLOINDI=sheet.cell(row_index,13).value)
