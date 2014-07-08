from django.shortcuts import render,redirect,render_to_response
from lintel.models import DateData,stockdata
from django.http import HttpResponseRedirect,HttpResponse
import json
import json as simplejson
import datetime
import mycharts

def home(request):
	context = {'title':'Lintel Test'}
	return render(request,'index.html',context)

def get_data(request,comp_name,date):
	date_obj = DateData.objects.get(date=date)
	company = date_obj.stockdata_set.get(SC_CODE=comp_name)
	data = {'SC_NAME':company.SC_NAME,'SC_CODE':company.SC_CODE,'OPEN':company.OPEN,'CLOSE':company.CLOSE}
	jsondata = simplejson.dumps(data,indent=4)
	return HttpResponse(jsondata, mimetype='application/json')

def get_alldata(request,comp_name,start_date,end_date):
	d_list = DateData.objects.all()
	c = d_list[0].stockdata_set.get(SC_CODE=comp_name)
	data = {'SC_NAME':c.SC_NAME,'SC_CODE':c.SC_CODE}
	for dates in d_list:
		if dates.btwDates(start_date,end_date):
			company = dates.stockdata_set.get(SC_CODE=comp_name)
			temp_dict = {'OPEN':company.OPEN,'CLOSE':company.CLOSE}
			data[str(dates)] = temp_dict
	jsondata = simplejson.dumps(data,indent=4)
	return HttpResponse(jsondata, mimetype='application/json')


def draw_graph(request,comp_name,start_date,end_date):
	d_list = datedata.objects.all()
	c = d_list[0].stockdata_set.get(SC_CODE=comp_name)
	data = {'SC_NAME':c.SC_NAME,'SC_CODE':c.SC_CODE}
	for dates in d_list:
		if dates.btwDates(start_date,end_date):
			company = dates.stockdata_set.get(SC_CODE=comp_name)
			temp_dict = {'OPEN':company.OPEN,'CLOSE':company.CLOSE}
			data[str(dates)] = temp_dict
			Chart = LineChart(SimpleDataSource(data=data),c,start_date,end_date)
		return HttpResponse(chart,graph.html)


def barchart(request):

    #instantiate a drawing object
    d = mycharts.MyBarChartDrawing()

    #extract the request params of interest.
    #I suggest having a default for everything.
    if 'height' in request:
        d.height = int(request['height'])
    if 'width' in request:
        d.width = int(request['width'])
    
    if 'numbers' in request:
        strNumbers = request['numbers']
        numbers = map(int, strNumbers.split(','))    
        d.chart.data = [numbers]   #bar charts take a list-of-lists for data

    if 'title' in request:
        d.title.text = request['title']
  

    #get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')