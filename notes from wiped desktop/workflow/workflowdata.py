
import sys
import tkinter
import time
import datetime
import pickle
import traceback

#####################################################################################
#####################################################################################
#DATA
#####################################################################################
#####################################################################################
class user:
    def __init__(self,name,password,vList,eventList):
        print('new user defined')
    def newDay(self):
        newDayRecord=dayRecord()
        dayArray.append(newDayRecord)

class dayRecord:
    def __init__(self):
        now=timeRecord('Day Record Instantiation')
        now.manualFix()
        self.created=now
        self.month=now.month
        self.year=now.year
        self.day=now.day
        print('dayRecord created for '+str(self.month),str(self.day),str(self.year)+'.')

class database:
    def __init__(self):
        pass

    def newUser(self,name,password,vList,eventList):
        self.users=[]
        newUser=user(name,password,vList,eventList)
        users.append(newUser)
    def login(self,name,password):
        uniqueFound=0
        for x in self.users:
            pass



class timeRecord:
    """Default Time Item Class"""
    def __init__(self,_comment):
        self.comment=str(_comment)
        d = datetime.datetime.now()
        self.year=getattr(d, 'year')
        self.month=d.strftime("%B")
        self.day=getattr(d, 'day')
        self.hour=getattr(d, 'hour')
        self.minute=getattr(d, 'minute')
        self.second=getattr(d, 'second')
        self.microsecond=getattr(d, 'microsecond')
        if self.hour<12:
           self.timeFormatted=str(self.hour)+':'+str(self.minute)+':'+str(self.second)+' a.m'
        elif self.hour>12:
           self.timeFormatted=str(self.hour-12)+':'+str(self.minute)+':'+str(self.second)+' p.m'
        elif self.hour==12:
            self.timeFormatted=str(12)+':'+str(self.minute)+':'+str(self.second)+' p.m'
        elif self.hour==0:
            self.timeFormatted=str(12)+':'+str(self.minute)+':'+str(self.second)+' p.m'

    def compare(self,other):
        #same day situation
        if self.day==other.day and self.month==other.month and self.year == other.year:
            finalMins= int(other.hour*60) + int(other.minute) - int(self.hour*60) -int(self.minute)
            minutesPlace=int(finalMins%60)
            hoursPlace=int(finalMins/60)
            return str(hoursPlace)+':'+str(self.minuteFix(minutesPlace))

    def minuteFix(self,fixMe):
        if fixMe<10:
            fixMe=str(0)+str(fixMe)
            return int(fixMe)
        else:
            return fixMe
    def hourFix(self,fixMe):
        if fixMe==0:
            return 12
        else:
            return fixMe


    def manualFix(self):
        print('Setting year, month and day to today\'s values.')
        print('Congrats you woke up at 10:00 a.m. You didn\'t? Too bad.')
        d = datetime.datetime.now()
        self.year=getattr(d, 'year')
        self.month=d.strftime("%B")
        self.day=getattr(d, 'day')
        self.hour=10
        self.minute=0
        if self.hour<12:
           self.timeFormatted=str(self.hour)+':,'+str(self.minute)+':'+str(self.second)+' a.m'
        elif self.hour>12:
           self.timeFormatted=str(self.hour-12)+':'+str(self.minute)+':'+str(self.second)+' p.m'
        elif self.hour==12:
            self.timeFormatted=str(12)+':'+str(self.minute)+':'+str(self.second)+' p.m'
        elif self.hour==0:
            self.timeFormatted=str(12)+':'+str(self.minute)+':'+str(self.second)+' p.m'


class intervalRecord:
    """Default Interval"""
    def __init__(self,_begincomment):

        self.endStatus='started'
        st = datetime.datetime.now()
        self.syear=getattr(st, 'year')
        self.smonth=st.strftime("%B")
        self.sday=getattr(st, 'day')
        self.shour=getattr(st, 'hour')
        self.sminute=getattr(st, 'minute')
        self.ssecond=getattr(st, 'second')
        self.smicrosecond=getattr(st, 'microsecond')
        if self.shour<12:
           self.stimeFormatted=str(self.shour)+':,'+str(self.sminute)+':'+str(self.ssecond)+' a.m'
        elif self.shour>12:
           self.stimeFormatted=str(self.shour-12)+':'+str(self.sminute)+':'+str(self.ssecond)+' p.m'
        elif self.shour==12:
            self.stimeFormatted=str(12)+':'+str(self.sminute)+':'+str(self.ssecond)+' p.m'
        elif self.shour==0:
            self.stimeFormatted=str(12)+':'+str(self.sminute)+':'+str(self.ssecond)+' p.m'
        self.begincomment=_begincomment


    def endInterval(self,_endcomment):
        self.endStatus='ended'
        et = datetime.datetime.now()
        self.eyear=getattr(et, 'year')
        self.emonth=et.strftime("%B")
        self.eday=getattr(et, 'day')
        self.ehour=getattr(et, 'hour')
        self.eminute=getattr(et, 'minute')
        self.esecond=getattr(et, 'second')
        self.emicrosecond=getattr(et, 'microsecond')
        if self.ehour<12:
           self.etimeFormatted=str(self.ehour)+':,'+str(self.eminute)+':'+str(self.esecond)+' a.m'
        elif self.ehour>12:
           self.etimeFormatted=str(self.ehour-12)+':'+str(self.eminute)+':'+str(self.esecond)+' p.m'
        elif self.ehour==12:
            self.etimeFormatted=str(12)+':'+str(self.eminute)+':'+str(self.esecond)+' p.m'
        elif self.ehour==0:
            self.etimeFormatted=str(12)+':'+str(self.eminute)+':'+str(self.esecond)+' p.m'
        self.endcomment=_endcomment
        self.duration=self.ehour*60+self.eminute-self.shour*60-self.sminute


class eventCategory:

    def __init__(self,catName):
        self.categoryName=catName


class trackedEvent:

    #Constructor
    def __init__(self,catName):
        self.category=eventCategory(catName)
        print('New Simple Category '+catName+' defined.')
        self.eventTimeRecord=[]

    #Add New Event Time for Category
    def newEvent(self,_comment):
        new=timeRecord(_comment)
        self.eventTimeRecord.append(new)

    #Reports current state to console
    def report(self):
        print('----'+self.category+'----')
        y=1
        for x in self.eventTimeRecord:
            print (str(y)+'. '+x.timeFormatted)
            y=y+1

class dailyEvent:

    #Constructor
    def __init__(self,catName):
        self.category=eventCategory(catName)
        print('New Daily '+catName+' defined.')
        self.eventTimeRecord=[]

    #Add New Event Time for Category
    def newEvent(self,_comment):
        new=timeRecord(_comment)
        self.eventTimeRecord.append(new)

    #Reports current state to console
    def report(self):
        print('----'+self.category+'----')
        y=1
        for x in self.eventTimeRecord:
            print (str(y)+'. '+x.timeFormatted)
            y=y+1


class intervalCategory:

    def __init__(self,catName):
        self.categoryName=catName


class trackedInterval:

    def __init__(self,catName):
            self.category=intervalCategory(catName)
            print('New Interval Category '+catName+' defined.')
            self.eventTimeRecord=[]
            self.finished=False
        #Add New Event Time for Category
    def newEvent(self,_begincomment):
        new=intervalRecord(_begincomment)
        self.eventTimeRecord.append(new)
    def report(self):
        print('----'+self.category+'----')
        y=1
        for x in self.eventTimeRecord:
            print (str(y)+'. '+x.timeFormatted,end=' ')
            print(self.comment)
            y=y+1
