from tkinter import *
import pyttsx3


engine = pyttsx3.init()
# voices = engine.getProperty('voices')
engine.setProperty('voice', 10) # voices[0].id
engine.setProperty('rate', 100)
engine.setProperty('volume', 1.0)

root = Tk()
root.geometry("710x300")
root.resizable(False, False)
root.configure(bg='light grey')
root.title("Concepts.pk - Text to Speak")

Msg = StringVar()
Label(root, text="Enter Text to convert to Voice", font='Arial 15 bold',fg= "green", bg='light grey').place(x=20,y=60)

entry_field = Entry(root, fg='Blue', font='Calibri 18 bold', textvariable=Msg, width=50)
entry_field.place(x=20, y=100)


def Text_to_speech():
    Message = entry_field.get()
    engine.say(Message)
    engine.runAndWait()


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width='4').place(x=100,y=140)
Button(root, font ='arial 15 bold', text='EXIT', width='4', command=Exit, bg='OrangeRed1').place(x=200, y=140)
Button(root, font='arial 15 bold',text='RESET', width='6', command=Reset).place(x=300, y=140)
# photo = PhotoImage(file = 'logo.png')
# image_label = Label(image = photo).place(x=150, y = 280)

Label(text="Text to speech Converter", font = 'Perpetua 20 bold', fg = 'green', bg ='light grey' , width = '50', relief= SUNKEN).pack(side = 'top')

Label(text="Concepts Coding--www.concepts.pk--Farhan--03009665776", font='Times 15 bold', fg='Teal', bg='light grey' , width='70', relief=SUNKEN).pack(side='bottom')

Label(text="For feedback or suggestions email us : ENGR.FARHAN.92@gmail.com", font='Arial 10 italic', fg='green', bg='light grey', width = '70', relief=SUNKEN).pack(side='bottom')

root.mainloop()