#!/usr/bin/python
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
class timeRecord:
    """Default Time Item Class"""
    def __init__(self):
        d = datetime.datetime.now()
        self.year=getattr(d, 'year')
        self.month=d.strftime("%B")
        self.day=getattr(d, 'day')
        self.hour=getattr(d, 'hour')
        self.minute=getattr(d, 'minute')
        self.second=getattr(d, 'second')
        self.microsecond=getattr(d, 'microsecond')
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
    def __init__(self):
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
        elif self.hour>12:
           self.stimeFormatted=str(self.shour-12)+':'+str(self.sminute)+':'+str(self.ssecond)+' p.m'
        elif self.shour==12:
            self.stimeFormatted=str(12)+':'+str(self.sminute)+':'+str(self.ssecond)+' p.m'
        elif self.shour==0:
            self.stimeFormatted=str(12)+':'+str(self.sminute)+':'+str(self.ssecond)+' p.m'


    def endInterval(self):
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
class eventCategory:
    categoryName=''
   
    def __init__(self,catName,entriesArray):
        self.categoryName=catName
        for x in entriesArray:
            self.possibleEntries=[]
            self.possibleEntries.append(x)

    def reportOptions(self):
        for x in range(len(self.possibleEntries)):
            print (x,self.possibleEntries[x])
            input('Input index to selection option')
        
class trackedEvent:

    #Constructor
    def __init__(self,catName,defineType,possibleEntries):
 
        if defineType=='simple' or defineType=='Simple' or defineType=='s' or defineType=='S':
            self.category=eventCategory(catName,possibleEntries)
            print('New Simple Category '+name+' defined.')
        else:
            self.category=eventCategory(catName,possibleEntries)
            print('New Complex Category '+name+' defined.')
        
        self.eventTimeRecord=[]
  
    #Add New Event Time for Category
    def newEvent(self):
        time.sleep(1)
        new=timeRecord()
        self.eventTimeRecord.append(new)

    #Reports current state to console
    def report(self):
        print('----'+self.category+'----')
        y=1
        for x in self.eventTimeRecord:
            print (str(y)+'. '+x.timeFormatted)
            y=y+1
    

    
#####################################################################################
#####################################################################################
#INTERFACE
#####################################################################################
#####################################################################################
    # we open the file for readin

eventList=[]
vList=[]
try:
    fileObject = open( "testfile",'rb')  
            
    eventList = pickle.load(fileObject)
    print("testfile successfully loaded...")
except:
    traceback.print_exc()
    print("--exception--")
    eventList=[]
controlBoolean=True

print('Entering main loop...')
name = input('Virtue or Vice?')
while controlBoolean==True:
    if name=='Virtue' or name == 'virtue':
           
        name=input('Category, Entry, View, Destroy,Exit:')
        if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
            for x in range(len(eventList)):
                print(x,eventList[x].category.categoryName)
            destroyEventIndex=input('Input index to PERMENANTLY DELETE category')
            eventList.pop(int(destroyEventIndex))
        elif name=='Create' or name=='create' or name=='c' or name=='C':
            name=input('Input Category Name: ')
            defineType=input('Simple or Complex: ')
            if defineType=='simple' or defineType=='Simple' or defineType=='s' or defineType=='S':
                newSimpleType=trackedEvent(str(name),str(defineType),[1])
                eventList.append(newSimpleType)
            else:
                entryCount=int(input('How many entry types?'))
                y=1
                myEntries=[]
                for x in range(entryCount):
                    myEntries.append(input())
                    y=y+1
                    newComplexType=trackedEvent(name,defineType,myEntries)
                print('New Category '+name+' defined.')
                eventList.append(newSimpleType)
        elif name== 'Entry'or name=='entry' or name=='e' or name =='E':
            name=input('Create or Destroy?')
            if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                for x in range(len(eventList)):
                    print(x,eventList[x].category.categoryName)
                destroyEventIndex=input('Input index to delete an entry from a category')
                for x in range(len(eventList[int(destroyEventIndex)].eventTimeRecord)):
                    print(x,eventList[int(destroyEventIndex)].eventTimeRecord[x].timeFormatted)
                destroyEventIndex=input('Input indx to PERMENANTLY DELETE entry from category')
                eventList[int(destroyEventIndex)].eventTimeRecord.pop(int(destroyEventIndex))
            elif name=='Create' or name=='create' or name=='c' or name=='C':
                for x in range(len(eventList)):
                    print(x,eventList[x].category.categoryName)
                newEventIndex=input('Input index to track new event')
                eventList[int(newEventIndex)].newEvent()
        elif name=='View' or name=='view' or name == 'v' or name=='V':
            for x in eventList:
                print(x.category.categoryName)
                q=0
                for z in x.eventTimeRecord:
                    print(x.eventTimeRecord[q].timeFormatted)
                    q=q+1
        elif name=='ex':
            print('Serializing Event List, Leaving Main Loop')
           
            file_Name = "testfile"
            # open the file for writing
            fileObject = open(file_Name,'wb') 
            # this writes the object a to the
            # file named 'testfile'
            pickle.dump(eventList,fileObject)   
            #here we close the fileObject
            fileObject.close()
            controlBoolean=False
    else:
        name = input('Category, Entry, View, Exit: ')
        if name=='Category' or name=='category' or name=='c' or name=='C':

            name=input('Create or Destroy?')
      
            if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                for x in range(len(eventList)):
                    print(x,eventList[x].category.categoryName)
                destroyEventIndex=input('Input index to PERMENANTLY DELETE category')
                eventList.pop(int(destroyEventIndex))
            elif name=='Create' or name=='create' or name=='c' or name=='C':
                name=input('Input Category Name: ')
                defineType=input('Simple or Complex: ')
                if defineType=='simple' or defineType=='Simple' or defineType=='s' or defineType=='S':
                    newSimpleType=trackedEvent(str(name),str(defineType),[1])
                    eventList.append(newSimpleType)
                else:
                    entryCount=int(input('How many entry types?'))
                    y=1
                    myEntries=[]
                    for x in range(entryCount):
                        myEntries.append(input())
                        y=y+1
                    newComplexType=trackedEvent(name,defineType,myEntries)
                    print('New Category '+name+' defined.')
                    eventList.append(newComplexType)
                    
        elif name== 'Entry'or name=='entry' or name=='e' or name =='E':
            
            name=input('Create or Destroy?')
      
            if name=='Destroy' or name=='destroy' or name=='d' or name=='D':
                for x in range(len(eventList)):
                    print(x,eventList[x].category.categoryName)
                destroyEventIndex=input('Input index to delete an entry from a category')

                for x in range(len(eventList[int(destroyEventIndex)].eventTimeRecord)):
                    print(x,eventList[int(destroyEventIndex)].eventTimeRecord[x].timeFormatted)
                destroyEventIndex=input('Input indx to PERMENANTLY DELETE entry from category')
                eventList[int(destroyEventIndex)].eventTimeRecord.pop(int(destroyEventIndex))
            elif name=='Create' or name=='create' or name=='c' or name=='C':
             for x in range(len(eventList)):
                print(x,eventList[x].category.categoryName)
             newEventIndex=input('Input index to track new event')
             eventList[int(newEventIndex)].newEvent()
        elif name=='View' or name=='view' or name == 'v' or name=='V':
            for x in eventList:
                print(x.category.categoryName,end='')
                for x in x.category.possibleEntries:
                    print(x)
                q=0
                for z in x.eventTimeRecord:
                    print(x.eventTimeRecord[q].timeFormatted)
                    q=q+1
        elif name=='ex':
            print('Serializing Event List, Leaving Main Loop')
            controlBoolean=False
            file_Name = "testfile"
                # open the file for writing
            fileObject = open(file_Name,'wb') 

                # this writes the object a to the
                # file named 'testfile'
            pickle.dump(eventList,fileObject)   

                # here we close the fileObject
            fileObject.close()
            controlBoolean=False
          
            
      

print('Program Exiting')


'''def main():

    #opening a root window
    #you can open many windows, but the main window is called the root window
    root = tkinter.Tk()
    root.title('Placeholder™')

    #defining a local function
    def quit():
        root.destroy()

    #adding a menu widget to the root    
    bar = tkinter.Menu(root)

    #creating a menu widget 
    fileMenu = tkinter.Menu(bar, tearoff=0)
    
    fileMenu.add_command(label='Exit',command=quit)
    fileMenu.add_command(label='Party',command=quit)
    bar.add_cascade(label='File',menu=fileMenu)
    root.config(menu=bar)

    #defing data
    notes=[]
    reminders=[]

    #frames
    #<frameName>=tkinter.Frame(TargetWindow., etc..)
    mainFrame = tkinter.Frame(root,borderwidth=1,padx=3,pady=3)
    mainFrame.pack()
    note= tkinter.Text(mainFrame,bg='yellow',width=100,height=1)
    note.pack()
    note1= tkinter.Text(mainFrame,bg='yellow',width=100,height=1)
    note1.pack()
    def reminder(text,x,y,notes,reminder):
        notewin=tkinter.Toplevel()
        notewin.resizable(width=False,height=False)
        notewin.geometry('+'+str(x)+'+'+str(y))
        reminder= tkinter.Text(notewin,bg='yellow', width=30,height=15)
        reminder.insert(tkinter.END,'hey')
        reminder.pack()
        notes.append(notewin)
        reminders.append(reminder)
        def deleteWindowHandler():
            print('Window Deleted')
            notewin.withdraw()
            notes.remove(notewin)
            reminders.remove(reminder)
        notewin.protocol('WM_DELETE_WINDOW',deleteWindowHandler)
        
    def post():
        print('Post')
        #creating a reminder window
        reminder('hi',10,10,notes,reminder)
    
    tkinter.Button(mainFrame,text='Button',command=post).pack()
    tkinter.mainloop()

if __name__ == '__main__':
    main()

#localtime = time.localtime(time.time())
#print("Local current time :", localtime)
#localtime = time.asctime( time.localtime(time.time()) )
#print(localtime)
#print ('Now    :', datetime.datetime.now())
#print ('Today  :', datetime.datetime.today())
#print ('UTC Now:', datetime.datetime.utcnow())
#for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
#    print (attr, ':', getattr(d, attr))
#tester=timeRecord()
#dateString=str(str(tester.month)+' '+str(tester.day)+', '+str(tester.year))
#print('It\'s',dateString+'.'+' '+tester.timeFormatted)
'''
