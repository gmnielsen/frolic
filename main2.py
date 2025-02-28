import tkinter as T

# a variable to help with testing the destruction and opening of a window frame
x = True
# a variable to show data saving outside the tkinter interface
mydata = ""

 # the parameter win is the window with the button
 # sending it here allows it to be destroyed here
def swapX(win):
    global x
    x = not x
    win.destroy()
    if x: open1()
    else: open2()

# since x starts as True, swapping between window 1 and 2 is confused if 2 is opened first
# so this corrects that
def setXFalse():
    global x
    x = False

# saves the data in an entrybox to a global variable
def saveme(entrybox):
    global mydata
    mydata = entrybox.get()
    print(mydata)

# this opens a new window, technically a sub window of myframe
# in other words
# window1 creation and options and packing
def open1():
    # toplevel creates a separate window frame
    window1 = T.Toplevel(myframe, bg="blue")
    # num x num is the width and height, + num + num is the starting x and y position
    window1.geometry("200x200+10+10")
    window1.title("me 1")
    # command=   only allows one command and no parameters
    # command=lambda: allows parameters and more than one command
    # this allows us to test the .get() outside the window
    button1 = T.Button(window1, bg="red", text="close me 1, open me not 1", command=lambda: swapX(window1))
    entry1 = T.Entry(window1, bg="orange", width=50)
    button2 = T.Button(window1, bg="orange", text="save this entry", command=lambda: saveme(entry1))
    button1.pack(side="top")
    entry1.pack(side="top")
    button2.pack(side="top")

# opens a different subwindow of myframe
# in other words:
# window2 creation and options and packing
def open2():
    window2 = T.Toplevel(myframe, bg="green")
    window2.geometry("200x200+10+10")
    window2.title("me not 1")
    button1 = T.Button(window2, bg="yellow", text="close me not 1, open me 1", command=lambda: swapX(window2))
    button1.pack(side="top")

# myframe creation and options
myframe = T.Tk()
myframe.title("hi")
myframe.geometry("400x400")
# buttons and packing for myframe
buttonopen1 = T.Button(myframe, text="open 1", command=open1)
buttonopen2 = T.Button(myframe, text="open 2", command=lambda: [open2(), setXFalse()])
buttonopen1.pack(side="top")
buttonopen2.pack(side="top")

myframe.mainloop()