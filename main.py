from tkinter import *
import tkinter.filedialog as fd
import pyttsx3

app1 = Tk()
def openfile():
    path = fd.askopenfile(mode ='r')
    none = path.read()
    print(none)
    speak(none)
    app1.destroy()
#screen
app1.configure(bg="Black")
btn1 = Button(text="Import File",font=("", 80), fg="green", bg="black", command=openfile)
btn1.pack(side="top")

def speak(text):
    robot = pyttsx3.init()
    robot.say(text)
    robot.runAndWait()
#END
mainloop()
