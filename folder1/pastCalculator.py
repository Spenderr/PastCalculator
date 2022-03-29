from tkinter import *
from datetime import datetime

#have set the colors into a variable for a cleaner implementation
bg = 'black'
fg = 'cyan'

App = Tk() #created my tkinter app
App.title('Past Calculator') #set the title of the app
App.geometry('300x200') #the size of the window when program is run
App['background']=bg #here the background of the window is set

msg=Label(App,text='Enter a memorable day',background=bg,foreground=fg) #a simple text message commanded to be printed in 'App'
msg.grid(row=0 , column=0 , columnspan=3) #the location and the space it will cover is set

dayL = Label(App, text='Day: ' ,background=bg,foreground=fg) # like on line 13, a message is printer and the color of background and text color is set
dayE = Entry(App, width=2) #an entry/input box is created and labeled where it will be used

monL = Label(App, text=' Month: ' ,background=bg,foreground=fg) #line 16
monE = Entry(App, width=2) # line 17

yrL=Label(App, text=' Year: ' ,background=bg,foreground=fg) #line 16
yrE=Entry(App, width=4) #line 17

#each one is gridded or pack inside the 'App' with the grid command and placed accordingly
dayL.grid(row = 1, column=0)
dayE.grid(row =  1, column=1)
monL.grid(row = 1, column =2)
monE.grid(row =1, column =3)
yrL.grid(row =1 ,column =4)
yrE.grid(row =1, column =5)

# a function to recieve the days months and years from the entry commands above
def find_days():
    days = int(dayE.get())
    month = int(monE.get())
    year = int(yrE.get())
    since = datetime(day=days , month = month, year = year)

    time_now = datetime.now() #to have a clear code, the datetime of current time is stored in a variable
    time_dif = time_now - since #the difference is then taken subtracting current time with the time set

    timeDifmsg = Label(App, text = 'Days since then: ' + str(time_dif.days),background=bg,foreground=fg) #then the time is prepared here to be printed
    timeDifmsg.grid(row=3,column=0,columnspan=4) #line25

#this is just like the find days function except we deal with the seconds parameter here in line 56
def find_sec():
    days = int(dayE.get())
    month = int(monE.get())
    year = int(yrE.get())
    since = datetime(day=days, month=month, year=year)

    time_now = datetime.now()
    time_dif = time_now - since

    scs = Label(App,text=' Seconds since then: ' +str(time_dif.total_seconds()),background=bg,foreground=fg) #total seconds is used here to represent time diff in seconds
    scs.grid(row=4 , column = 0, columnspan=6) #line 25

dayButton = Button(App, text = 'Total Days', command = find_days, relief = 'sunken')
#the button to print the time difference is created and has been given the command to execute the find_days func and print the line 43
secButton = Button(App, text = 'Total Seconds',command=find_sec, relief = 'sunken')
#same as line 60 but this one executes the find_sec function
dayButton.grid( row = 2, column = 0, columnspan = 3) #line 25
secButton.grid( row = 2, column = 3, columnspan = 4) #line 25

App.mainloop() #command used to run the whole program once it is run