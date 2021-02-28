###############################################################################################################################
# Author : Haripriyan.R
###############################################################################################################################
# Import required libraries
import datetime,time,os
from platform import system
from modules.playsound import playsound as ps
if system() == 'Windows':
    clsr='cls'
    cfile='contacts.txt'
    greetings='files\\greetings.mp3'
    ex='files\\ex.mp3'
    oops='files\\oops.mp3'
    aborted='files\\aborted.mp3'
    general='files\\general.mp3'
    fr='files\\fr.mp3'
    confirmation='files\\confirmation.mp3'
else:
    x=str(os.getcwd())	
    cfile=x+'/API/contacts.txt'
    clsr='clear'
    greetings=x+'/API/files/greetings.mp3'
    ex=x+'/API/files/ex.mp3'
    oops=x+'/API/files/oops.mp3'
    aborted=x+'/API/files/aborted.mp3'
    general=x+'/API/files/general.mp3' 
    fr=x+'/API/files/fr.mp3'
    confirmation=x+'/API/files/confirmation.mp3' 
###################################################################################################################################
# Class to create database
class Createdatabase:
    # Define required variables
    list,contactsdatabase=[],[]
    def __init__(self, name, dob, number, emailid):
      self.name,self.dob,self.number,self.emailid=name,dob,number,emailid
    ###############################################################################################################################
    # Function to create contact
    def cc():
      fm,ln,dob,number,emailid=input("Enter contact's first name : "),input("Enter contact's last name : "),input("Enter contact's DOB : "),input("Enter contact's number : "),input("Enter contact's Email ID : ")
      try: 
          int(number)
      except ValueError:
          print("Incorrect phone number!\tIt should be a number not characters!\nINFO : Don't include Dialing code...\n")
          number=input("Enter phone number in correct format : ")
      try:
          datetime.datetime.strptime(dob, "%d/%m/%Y")
      except:
          print("Incorrect DOB!\tIt should be in format dd/mm/yyyy")
          dob=input("Enter DOB in Correct format! : ")
      x=('{},{},{},{},{}'.format(fm,ln,dob,number,emailid))
      with open(cfile,'a+') as f:
          print("\n"+x,file=f,end="")
    ###############################################################################################################################
    # Function to display contact
    def dc():
      print("-"*103+"\n| First Name"," "*(10)+"|","Last Name"," "*(11)+"|","DOB"," "*(10-len("DOB"))+"|","Number"," "*(7)+"|"+"EMAIL ID"," "*(17)+"|","\n"+"-"*103)
      try:
        f = open(cfile, "r").readlines()
        for i in range(len(f)):
          lines = f[i]
          try:
            for item in [lines.split(",")]:           
              print("|",item[0]," "*(20-len(item[0]))+"|",item[1]," "*(20-len(item[1]))+"|",item[2]," "*(10-len(item[2]))+"|",item[3][0:len(item[3])]," "*(13-len(item[3]))+"|",item[4][0:len(item[4])].replace("\n","")," "*(23-len(item[4].replace("\n",""))),"|")
              print("-"*103)
          except:
            pass
      except:
        print("|"," "*31,"Unexpected error occured !"," "*41+"|\n"+"-"*103)
    ###############################################################################################################################
    # Function to find contact
    def fc(name):
        cn,cfi=[],[]
        f = open(cfile, "r").readlines()
        for i in range(len(f)):
          lines = f[i]
          for item in [lines.split(",")]:
              cn.append(item[0].strip())
              cfi.append(item)
        found=False
        for k in range(len(cn)):
            if  name==cn[k]:
                found=True
                print("-"*103+"\n| First Name"," "*(10)+"|","Last Name"," "*(11)+"|","DOB"," "*(10-len("DOB"))+"|","Number"," "*(7)+"|"+"EMAIL ID"," "*(17)+"|","\n"+"-"*103)
                print("|",cn[k]," "*(20-len(cn[k]))+"|",cfi[k][1]," "*(20-len(cfi[k][1]))+"|",cfi[k][2]," "*(10-len(cfi[k][2]))+"|",cfi[k][3][0:len(cfi[k][3])]," "*(13-len(cfi[k][3]))+"|",cfi[k][4][0:len(cfi[k][4])].replace("\n","")," "*(23-len(cfi[k][4].replace("\n",""))),"|")
                print("-"*103)
        if not found:
            print("Contact name "+name+" is not found in Database...")
    ################################################################################################################################
    # Function to delete contact
    def dl(name):
        f = open(cfile, "r")
        output = []
        for line in f:
           if not line.startswith(name):
              output.append(line+"\n")
        f.close()
        with open(cfile,'w') as f:
          print(*output,file=f,end="")
    #################################################################################################################################
    # Function to factory reset database
    def fr():
      with open(cfile,'w') as f:
          print("Database reseted at "+time.asctime(time.localtime(time.time()))+"\nFirst name,Last name,01/01/2021,0123456789,example@example.com",file=f,end="")
          print("Database successfully reseted at "+time.asctime(time.localtime(time.time())))
###############################################################################################################################
# Greetings
ps(greetings)
while True:
    print("-"*50,"\n| Use these short codes:"," "*(47-len("| Use these short codes:")),"|\n"+"-"*50,"\n|\tcc - To create a new contact"," "*(12)+"|\n|\tdc - display contacts"," "*(18),"|","\n|\tfr - Factory Reset"," "*(21),"|","\n|\tdl - delete contacts"," "*(19),"|\n|\tfc - find a contact"," "*(20),"|","\n|\tex - exit the contact list"," "*(13),"|\n"+"-"*50,"\n")
    scode = input(">").lower().strip()
    if scode == 'cc':
            print('New Contact')
            print("-"*30)
            Createdatabase.cc()        
    elif scode == 'dc':
            Createdatabase.dc()
            ps(general)
    elif scode == 'fr':
           ps(confirmation)
           ch=input("Are you sure to reset (y/n): ")
           if ch.lower()=='y':
             Createdatabase.fr()
             ps(fr)
           else:
             print("\nTask aborted!")
             ps(aborted)
    elif scode == 'fc':
            name=input("Enter contact name to find : ")
            if name!='':
              try:
                Createdatabase.fc(name)
              except:
                pass
            else:
              ps(aborted) 
            ps(general)
    elif scode == 'dl':
           name=input("Enter contact name to delete from database : ")
           print("Are you sure to delete",name,"from your contacts database (y/n): ")
           ps(confirmation)
           ch=input('>>>')
           if ch.lower()=='y':
             Createdatabase.dl(name)
           else:
             print("\nTask aborted!")
             ps(aborted)
    elif scode == 'ex':
            print('Bye.......')
            ps(ex) 
            break
    else:
        print("Unknown shortcut... Use  the shortcut ")
        ps(oops)
    input("PRESS ENTER TO CONTINUE....")
    os.system(clsr)
###############################################################################################################################
# END OF PROGRAM
###############################################################################################################################
