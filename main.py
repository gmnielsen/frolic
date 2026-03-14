# IMPORTS

import random as R
import tkinter as T
import argparse

# METHODS

def getStudent():
    return R.choice(students)

def removeStudent(who):
    students.remove(who)

def absentStudent(who):
    global  students
    count = students.count(who)
    for i in range(count):
        students.remove(who)

def timesUp():
    # big red stop
    biglabel.config(text="STOP",bg='red')
    # drop the student from the list
    removeStudent(student['text'])
    # set the button states
    pause['state'] = 'disabled'

def timesIn():
    # clear stop
    biglabel.config(text="",bg=BGCOLOR)#,bg='normal')

def updateRemainingTimeForAll(label):
    # countdown for observing the question
    global counter, observe
    if counter == 0:
        observe = False
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    label['text'] = f"{minutes:02}:{seconds:02}"
    if observe:
        label.after(1000, updateRemainingTimeForAll, label)
        counter = counter - 1

def updateRemainingTimeForStudent(label):
    # countdown for answering the question
    global answer, running
    if answer == 0:
        running = False
        timesUp()
    seconds = answer % 60
    minutes = int(answer / 60) % 60
    label['text'] = f"{minutes:02}:{seconds:02}"
    if running:
        label.after(1000,updateRemainingTimeForStudent, label)
        answer = answer - 1

def timeLoop(label):
    # clock program
    global counter, running, observe,answer
    # countdown for all
    updateRemainingTimeForAll(label)
    while running and observe:
        # rotate through student after student
        student['text'] = getStudent()
        top.update()
    # countdown for one
    updateRemainingTimeForStudent(label)
    while running and not observe:
        # countdown clock for selected student
        top.update()
    reset['state'] = 'normal'
    quit['state'] = 'normal'
    # end timeLoop

def Start(label):
    global running, observe, counter, answer
    # prep the loop variables
    running = True
    observe = True
    # set button states
    start['state'] = 'disabled'
    pause['state'] = 'normal'
    quit['state'] = 'disabled'
    # get non-default times
    c = lookTime.get()
    a = answerTime.get()
    if c : counter = int(c)
    if a : answer = int(a)
    # get missing peeps
    e = removePerson.get()
    if e : absentStudent(e)
    # start the clock
    timeLoop(label)
    # end Start
    print(students.count("maggie"))

def Reset(label):
    global counter, COUNTERDEFAULT, answer, ANSWERDEFAULT
    if not running:
        # default time value
        counter = COUNTERDEFAULT
        answer = ANSWERDEFAULT
        # clear stop
        timesIn()
        # reset labels and buttons
        student['text'] = 'hi everyone'
        reset['state'] = 'disabled'
        start['state'] = 'normal'
        pause['state'] = 'disabled'
        # reset time entries
        lookTime.delete(0,T.END)
        lookTime.insert(0,str(COUNTERDEFAULT))
        answerTime.delete(0,T.END)
        answerTime.insert(0,str(ANSWERDEFAULT))

def Pause(label):
    global running, observe
    # flip the times
    running = not running
    observe = not observe
    timeLoop(label)

# WORKING PROGRAM

top = T.Tk()

# constants

WIDE = 250
HIGH = 800
GEOMETRY = ('%dx%d+%d+%d' % (WIDE, HIGH, top.winfo_screenwidth()-WIDE-10, 10))
COUNTERDEFAULT = 20
ANSWERDEFAULT = 3
BGCOLOR = "yellow green"

# the class of kids
students = ["josei","avery","alphy","riley","josei","avery","alphy","riley","josei","avery","alphy","riley"]

# parse the arguements with the program
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # two unnecessary arguments
    parser.add_argument("a", nargs='?', default=COUNTERDEFAULT)
    parser.add_argument("b", nargs='?', default=ANSWERDEFAULT)
    # get all the arguments
    args = parser.parse_args()
    # set the constants to the arguments
    COUNTERDEFAULT = int(args.a)
    ANSWERDEFAULT = int(args.b)

# starting values
counter = COUNTERDEFAULT
answer = ANSWERDEFAULT
running = False
observe = False


# setting up the window
# top = T.Tk()
top.title("frolic")
top.geometry(GEOMETRY)
top.config(bg=BGCOLOR)
label = T.Label(top, text="Frolic frenzy!", fg="black", bg=BGCOLOR, font="Verdana 30 bold")
label.pack()

# first frame, stopwatch and student
s = T.Frame(top)
student = T.Label(s,text='hi everyone',width=50, fg="black", bg=BGCOLOR, font="Verdana 30 bold")
# pack first frame
s.pack(anchor='center', pady=10)
student.pack(side = 'left')

# second frame, four buttons
f = T.Frame(top)
f.config(bg=BGCOLOR)
start = T.Button(f, text='New Question', width=10,  bg=BGCOLOR, command=lambda: Start(label))
reset = T.Button(f, text='Reset', width=6, state='disabled',  bg=BGCOLOR, command=lambda: Reset(label))
pause = T.Button(f, text='Pause', width=6, state='disabled',  bg=BGCOLOR, command=lambda: Pause(label))
quit = T.Button(f, text='Exit', width=6,  bg=BGCOLOR, command=top.quit)
# pack second frame
f.pack(anchor='center', pady=5)
start.pack(side='top')
reset.pack(side='top')
pause.pack(side='top')
quit.pack(side='top')
# third frame, 3 time entries
e = T.Frame(top)
lookTime = T.Entry(e,width=3, fg=BGCOLOR)
answerTime = T.Entry(e,width=3, fg=BGCOLOR)
removePerson = T.Entry(e,width=8, fg=BGCOLOR)
# pack third frame
e.pack(anchor='center', pady=5)
lookTime.grid(row=1,column=1,padx=10)
answerTime.grid(row=1,column=2)
removePerson.grid(row=1,column=3)

# fourth frame, the big STOP
a = T.Frame(top)
a.config(bg=BGCOLOR)
biglabel = T.Label(a, text='', fg='white', bg=BGCOLOR, font="Verdana 64 bold")
# pack third frame
a.pack(anchor='center', pady=10, fill=T.BOTH, expand=True)
biglabel.pack(fill=T.BOTH, expand=True)

top.mainloop()

