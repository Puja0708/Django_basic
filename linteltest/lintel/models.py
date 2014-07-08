from django.db import models
from django.contrib.auth.models import User

def dateFormate(in_date):
	date_full = in_date
	date = date_full[0]+date_full[1]
	month = date_full[2]+date_full[3]
	year = date_full[4]+date_full[5]+date_full[6]+date_full[7]
	d_list = year+month+date
	return d_list

class DateData(models.Model):
	date  				= models.CharField(max_length=20)

	def getDate(self):
		date_full = self.date
		date = date_full[0]+date_full[1]
		month = date_full[2]+date_full[3]
		year = date_full[4]+date_full[5]+date_full[6]+date_full[7]
		d_list = year+month+date
		return d_list

	def btwDates(self,start_d,end_d):
		start = dateFormate(start_d)
		end = dateFormate(end_d)
		curr = self.getDate()
		return curr >= start and curr <= end

	def __unicode__(self):
		date = self.date
		final_date = date[:2] + '-' + date[2:4] + '-' + date[4:]
		return final_date

class stockdata(models.Model):
	"""docstring for stockdata"""
	creator 			= models.ForeignKey(DateData)
	SC_CODE 			= models.IntegerField()
	SC_NAME 			= models.CharField(max_length=255)
	SC_GROUP 			= models.CharField(max_length=2)
	SC_TYPE 			= models.CharField(max_length=2)
	OPEN 				= models.FloatField()
	HIGH 				= models.FloatField()
	LOW 				= models.FloatField()
	CLOSE 				= models.FloatField()
	LAST 				= models.FloatField()
	PREVCLOSE 			= models.FloatField()
	NO_TRADES			= models.IntegerField()
	NO_OF_SHRS			= models.IntegerField()
	NET_TURNOV			= models.IntegerField()
	TDCLOINDI			= models.CharField(max_length=255,blank=True,null=True)

	def __unicode__(self):
		return self.SC_NAME

