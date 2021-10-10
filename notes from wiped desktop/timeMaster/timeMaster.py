#!/usr/bin/python
import sys
import tkinter
import time
import datetime
import pickle
import traceback
from timeData import *

class timeMaster:

    def downTime(self):
        if self.downList[len(self.downList)].endstatus=='started':
            pass

        else:
            pass



    def sleepModule(self):

        if False==False:
            now=timeRecord('comparion dummy')
            now=timeRecord('dummy')
            now.manualFix()
            self.sleepList.append(now)
            self.awokeAt=str(now.timeFormatted)
            self.loggedin=True
            print('Print loggedin value has changed, this marks the beginning of a new day.')
            print('Resetting Virtues.')
            for x in self.vList:
                x.finished=False
                self.save()
        else:
            pass

    def final(self):
        ##called at end of day to reset virtues
        self.loggedoff=True
        print('loggedoff value has changed. This marks the end of today.')
    def load(self):
        print('load method called...')
        try:
            fileObject = open( "viceList",'rb')
            self.eventList = pickle.load(fileObject)
            print("viceList successfully loaded...")
        except:
                traceback.print_exc()
                print("--exception--")

        try:
            fileObject2 = open( "virtueList",'rb')
            self.vList = pickle.load(fileObject2)
            print("virtueList successfully loaded...")
        except:
            traceback.print_exc()
            print("--exception--")

        try:
            fileObject3 = open( "sleepList",'rb')
            self.sleepList = pickle.load(fileObject3)
            print("sleepList successfully loaded...")
        except:
            traceback.print_exc()
            print("--exception--")
        try:
            fileObject4 = open( "downList",'rb')
            self.sleepList = pickle.load(fileObject4)
            print("List successfully loaded...")
        except:
            traceback.print_exc()
            print("--exception--")

        for x in self.vList:
            if x.category.categoryName=='Downtime':
                self.downList=x
        print('testing downlist transfer contents...')

        #for x in self.vList:
        #    if x.category.categoryName=='Downtime':
        #        self.vList.pop(x)

        self.save()
    def save(self):


        file_Name = 'viceList'
        fileObject = open(file_Name,'wb')
        pickle.dump(self.eventList,fileObject)
        fileObject.close()

        file_Name2 = 'virtueList'
        fileObject2 = open(file_Name2,'wb')
        pickle.dump(self.vList,fileObject2)
        fileObject2.close()

        file_Name3 = 'sleepList'
        fileObject3 = open(file_Name3,'wb')
        pickle.dump(self.sleepList,fileObject3)
        fileObject3.close()

        file_Name4= 'downList'
        fileObject4 = open(file_Name4,'wb')
        pickle.dump(self.downList,fileObject4)
        fileObject4.close()

    def categoryEdit(self):
        self.master=tkinter.Tk()
        vcLabel=tkinter.Label(self.master,text='Vice')
        vrLabel=tkinter.Label(self.master,text='Virtue')
        def editVirtue():
            name=input('Create or Destroy?')
            if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                for x in range(len(self.vList)):
                    print(x,self.vList[x].category.categoryName)
                destroyEventIndex=input('Input index to PERMENANTLY DELETE Virtue category')
                self.vList.pop(int(destroyEventIndex))
            elif name=='Create' or name=='create' or name=='c' or name=='C':
                catName=input('Input new Interval category name:')
                newSimpleType=trackedInterval(str(catName))
                self.vList.append(newSimpleType)
                self.save()
        def editVice():
                name=input('Create or Destroy?')

                if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                    for x in range(len(self.eventList)):
                        print(x,self.eventList[x].category.categoryName)
                    destroyEventIndex=input('Input index to PERMENANTLY DELETE Vice category')
                    self.eventList.pop(int(destroyEventIndex))
                elif name=='Create' or name=='create' or name=='c' or name=='C':
                    catName=input('Input new Vice category name:')
                    newSimpleType=trackedEvent(str(catName))
                    self.eventList.append(newSimpleType)
        vcb1=tkinter.Button(self.master,text='Edit Vice Category',command=editVice)
        vcb2=tkinter.Button(self.master,text='Edit Virtue Entries',command=None)
        vrb1=tkinter.Button(self.master,text='Edit Virtue Category',command=editVirtue)
        vrb2=tkinter.Button(self.master,text='Edit Virtue Entries',command=None)
        vcLabel.pack()
        vcb1.pack()
        vcb2.pack()
        vrLabel.pack()
        vrb1.pack()
        vrb2.pack()
        tkinter.mainloop()


    def editMode(self):

        self.master = tkinter.Tk()
        self.master.wm_title('TimeMaster')
        #adding a menu widget to the root
        bar = tkinter.Menu(self.master)
        self.myInt=0
        self.myString=''
        #creating a menu widget
        fileMenu = tkinter.Menu(bar, tearoff=0)

        fileMenu.add_command(label='Edit',command=self.categoryEdit)
        bar.add_cascade(label='File',menu=fileMenu)

        self.master.config(menu=bar)
        e = tkinter.Entry(self.master)
        e2 = tkinter.Entry(self.master)
        self.vicOptions=[]
        self.virOptions=['']
        self.variable=tkinter.StringVar(self.master)

        def resetMenus():
            for x in self.eventList:
                self.vicOptions.append(str(x.category.categoryName))
            self.variable = tkinter.StringVar(self.master)
            self.viceMenu = tkinter.OptionMenu(self.master, self.variable, *tuple(self.vicOptions))
            self.viceMenu.config(width=20)

        def newVice():

            q=0
            comment=str(e.get())
            myKey=str(self.variable.get())
            for x in self.eventList:
                if x.category.categoryName==myKey:
                    self.eventList[int(q)].newEvent(comment)
                q=q+1
            e.delete(0,999)
            self.variable.set('')
            resetMenus()



        def virtueGUI():
            self.currentVirtue=None

            for x in self.vList:
                for z in x.eventTimeRecord:
                    if z.endStatus=='started'and x.category.categoryName!='Downtime':
                        self.currentVirtue=x
            self.master2=tkinter.Tk()
            self.master2.wm_title('VirtueEntry')
            self.master1=tkinter.Frame(self.master2,bg='red')
            self.w=tkinter.Label(self.master1, text='')
            self.virtueWidgetArray=[]
            self.var1=tkinter.IntVar(self.master1)
            self.var2=tkinter.IntVar(self.master1)
            self.virtueButton1=tkinter.Button(self.master1, text='Start Virtue')
            self.virtueButton2=tkinter.Button(self.master1,text='End Virtue')

            self.e3 = tkinter.Entry(self.master1)
            self.e4 = tkinter.Entry(self.master1)

            self.c1 = tkinter.Checkbutton(self.master1, text="Complete", variable=self.var1)
            self.c2 = tkinter.Checkbutton(self.master1, text="Finish(Delete)", variable=self.var2)

            def rebootGUI():
                for x in self.virtueWidgetArray:
                    try:
                        x.pack_forget()
                    except:
                        print('not packed, lol')
                if self.currentVirtue==None:
                    self.master2.wm_title('VirtueTracker')
                    self.master2.config(bg='red')
                    self.virtueMenu.pack()
                    self.e3.pack()
                    self.virtueButton1.pack()
                else:
                    self.master2.config(bg='green')
                    self.master2.wm_title(str(self.currentVirtue.category.categoryName))
                    self.w.pack()
                    self.e4.pack()
                    self.virtueButton2.pack()
                    self.c1.pack()
                    self.c2.pack()
                self.master1.pack()

            self.variable2 = tkinter.StringVar(self.master1)
            def newVirtueEntry():
                self.downTime()
                myKey=str(self.variable2.get())
                for x in self.vList:
                    if myKey==x.category.categoryName:
                        myString=str(self.variable2.get())+'---'+str(self.e3.get())
                        self.w.config(text=str(myString))
                        x.newEvent(str(self.e3.get()))
                        self.currentVirtue=x
                        self.save()
                        rebootGUI()
            self.virtueButton1.config(command=newVirtueEntry)



            for x in self.vList:
                try:
                    if x.finished==False:
                        self.virOptions.append(str(x.category.categoryName))
                except:
                    traceback.print_exc()

            self.virtueMenu = tkinter.OptionMenu(self.master1, self.variable2, *tuple(self.virOptions))
            self.virtueMenu.config(width=20)


            def stopCurrentVirtue():
                if self.var1.get()==1:
                    #Complete
                    for x in range(len(self.vList)):
                        for z in self.vList[x].eventTimeRecord:
                            if z.endStatus=='started':
                                print('The checkbox works')
                                self.vList[x].finished=True
                                print(self.vList[x].finished)
                elif self.var2.get()==1:
                    #Finish(Delete)
                    print('Delete Virtue called')
                    for x in range(len(self.vList)):
                        for z in self.vList[x].eventTimeRecord:
                            if z.endStatus=='started':
                                self.endList.append(x)
                                self.vList.pop(x)
                try:
                    for x in self.vList:
                        for z in x.eventTimeRecord:
                            if z.endStatus=='started'and x.category.categoryName!='Downtime':
                                z.endInterval(str(self.e4.get()))
                                self.e4.delete(0,999)
                except:
                    traceback.print_exc()
                    print('Current Virtue Not Found.')
                    return None
                self.currentVirtue=None
                self.downTime()
                self.save()
                rebootGUI()
            self.virtueButton2.config(command=stopCurrentVirtue)





            self.virtueWidgetArray.append(self.virtueMenu)
            self.virtueWidgetArray.append(self.c2)
            self.virtueWidgetArray.append(self.c1)
            self.virtueWidgetArray.append(self.e4)
            self.virtueWidgetArray.append(self.e3)
            self.virtueWidgetArray.append(self.virtueButton2)
            self.virtueWidgetArray.append(self.virtueButton1)
            self.virtueWidgetArray.append(self.w)



            rebootGUI()

        b1 = tkinter.Button(self.master, text ="Print Vice", command = self.viewVice)
        bb1 = tkinter.Button(self.master, text ="Input Vice", command = newVice)
        b2 = tkinter.Button(self.master, text ="Print Virtue", command = self.viewTodayVirtue)
        bb2 = tkinter.Button(self.master, text ="Virtue", command=virtueGUI)


        e.insert(0, "")
        e2.insert(0, "")
        resetMenus()

        self.viceMenu.pack()
        e.pack()
        b1.pack()
        bb1.pack()

        b2.pack()
        bb2.pack()




        tkinter.mainloop()

    def timerMeth(self):
        if self.myInt<10:
            self.myString='0:0'+str(self.myInt)
        self.w.config(text=self.myString)
        self.w.pack()
        self.master.after(1000, self.timerMeth)
        self.myInt=self.myInt+1
    def openInterval(self):
        myString=None
        for x in self.vList:
            try:
                for z in x.eventTimeRecord:
                    if z.endStatus=='started':
                        myString=str(x.category.categoryName)
                        return myString
            except:
                return 'None'

    def viewVice(self):
        self.sleepModule()
        self.save()
        for x in self.eventList:
            print(x.category.categoryName,end='(')
            print('Last: ',end='')
            now=timeRecord('Comparison Dummy')
            if len(x.eventTimeRecord)>0:
                print(x.eventTimeRecord[len(x.eventTimeRecord)-1].compare(now),end='')
            else:
                print('None.',end='')
            print(')')
            q=0
            for z in x.eventTimeRecord:
                if z.day== now.day and z.month== now.month and z.year== now.year:
                    print(x.eventTimeRecord[q].timeFormatted,end=' | ')
                    print(x.eventTimeRecord[q].comment)
                q=q+1

    def viewTodayVirtue(self):
        self.sleepModule()
        self.save()
        print('---Active---')
        totalTimeTracked=0
        todayTotals=[]
        for x in self.vList:
            if x.finished==False:
                q=0
                now=timeRecord('Comparison Dummy')
                print(x.category.categoryName,end='')
                print('(',end='')
                print(' Total: ',end='')
                minuteHolder=0
                if len(x.eventTimeRecord)>=1:
                    for d in range(len(x.eventTimeRecord)):
                        try:
                            if x.eventTimeRecord[d].sday==now.day and x.eventTimeRecord[d].smonth==now.month and x.eventTimeRecord[d].syear==now.year:
                                minuteHolder=minuteHolder+x.eventTimeRecord[d].duration
                                totalTimeTracked=totalTimeTracked+x.eventTimeRecord[d].duration
                        except:
                            pass
                    print(str(minuteHolder)+' minute(s).',end='')
                    todayTotals.append(minuteHolder)
                else:
                    print('None.',end='')
                print(')')
            q=0
            for z in x.eventTimeRecord:
                try:
                    if x.finished==False and z.sday== now.day and z.smonth== now.month and z.syear== now.year and z.duration>2:
                        print(x.eventTimeRecord[q].stimeFormatted,end=' ')
                        print(x.eventTimeRecord[q].begincomment,end=' ')
                        try:
                            print(x.eventTimeRecord[q].etimeFormatted,end=' ')
                            print(x.eventTimeRecord[q].endcomment,end=' ')
                            print(str(x.eventTimeRecord[q].duration)+' minute(s)')
                        except:
                            print('Ongoing')


                    q=q+1
                except:
                    pass

        print('---Dead---')
        for x in self.vList:
            if x.finished==True:
                for z in range(len(x.eventTimeRecord)):
                    print(x.category.categoryName+' '+str(x.eventTimeRecord[z].duration)+' minute(s).')
        print('---Percentage Report---')
        for x in range(len(self.vList)):
            try:
                if todayTotals[x]>0:
                    myString=int(totalTimeTracked/todayTotals[x])
                    print(self.vList[x].category.categoryName, str(myString))
            except:
                pass
    def eventTimeMath(self,index):
        q=self.eventList[index].eventTimeRecord[len(self.eventList[index].eventTimeRecord)-1]
        try:
            now=timeRecord('Current Time Comparison Entry')
            print(str(q.compare(now)))

        except:
            traceback.print_exc()
            print('Time since last ',end='')
            q.hour

    def intervalTimeMath(self):
        pass
    def viewUserData(self):
        now=timeRecord('comparison dummy variable')
        for x in self.sleepList:
            if x.day==now.day and x.year== now.year and x.month==now.month:
                print('You woke up at '+str(x.timeFormatted)+' today.')
##CONSTRUCTOR####
##CONSTRUCTOR####
##CONSTRUCTOR####
##CONSTRUCTOR####
    def __init__(self):
        self.eventList=[]
        self.vList=[]
        self.endList=[]
        self.downList=[]
        self.sleepList=[]
        self.load()

        controlBoolean=False
        #while self.loggedin==False:

        self.editMode()

######TEST TUESDAY DEC 22 WHEN YOU WAKE UP######


################################################

        while controlBoolean==True:
            self.save()
            print('Entering main loop...')
            name = input('Virtue or Vice?')
        ###############################################################################
        #VIRTUE#############################################################################
        ###############################################################################
            if name=='Virtue' or name == 'virtue':
                self.viewVirtue()
                name=input('Category, Entry, Destroy')
                if name=='Category' or name=='category' or name=='c' or name=='C':
                    name=input('Create or Destroy?')
                    if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                        for x in range(len(self.vList)):
                            print(x,self.vList[x].category.categoryName)
                        destroyEventIndex=input('Input index to PERMENANTLY DELETE Virtue category')
                        self.vList.pop(int(destroyEventIndex))
                    elif name=='Create' or name=='create' or name=='c' or name=='C':
                        catName=input('Input new Interval category name:')
                        newSimpleType=trackedInterval(str(catName))
                        self.vList.append(newSimpleType)
                        self.save()
                elif name== 'Entry'or name=='entry' or name=='e' or name =='E':
                    entryCommand=input('Create or Destroy?')
                    if name=='Create' or name=='create' or name=='c' or name=='C':
                        print('to be implemented')

            else:
        ###############################################################################
        #VICE#############################################################################
        ###############################################################################
                self.viewVice()
                name = input('Category, Entry')
                if name=='Category' or name=='category' or name=='c' or name=='C':

                    name=input('Create or Destroy?')

                    if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                        for x in range(len(self.eventList)):
                            print(x,self.eventList[x].category.categoryName)
                        destroyEventIndex=input('Input index to PERMENANTLY DELETE Vice category')
                        self.eventList.pop(int(destroyEventIndex))
                    elif name=='Create' or name=='create' or name=='c' or name=='C':
                        catName=input('Input new Vice category name:')
                        newSimpleType=trackedEvent(str(catName))
                        self.eventList.append(newSimpleType)
                elif name== 'Entry'or name=='entry' or name=='e' or name =='E':
                    name=input('New,Delete,Edit')
                    if name=='Delete' or name=='delete' or name=='d' or name=='D':
                        for x in range(len(self.eventList)):
                            print(x,self.eventList[x].category.categoryName)
                        categoryIndex=input('Input index to delete an entry from a category')
                        for x in range(len(self.eventList[int(categoryIndex)].eventTimeRecord)):
                            print(x,self.eventList[int(categoryIndex)].eventTimeRecord[x].timeFormatted)
                        destroyEventIndex=input('Input indx to PERMENANTLY DELETE entry from category')
                        self.eventList[int(categoryIndex)].eventTimeRecord.pop(int(destroyEventIndex))
                    elif name=='New' or name=='new' or name=='n' or name=='N':
                        for x in range(len(self.eventList)):
                            print(x,self.eventList[x].category.categoryName)
                        newEventIndex=input('Input index to track new event')
                        comment=str(input('Comment:'))
                        self.eventList[int(newEventIndex)].newEvent(comment)
                    elif name=='Edit' or name=='Edit' or name=='e' or name=='e':
                        print('to be implemented')



        print('While Loop Exiting')
