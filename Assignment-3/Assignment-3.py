# Luke Coddington
# 9/19/22
# Assignment 3 - AI
# Assumed Time: 1hr
# Actual Time: 1hr
# Reasoning: The UI can take a bit to look right

from tkinter import *
from tkinter import messagebox
from textblob import TextBlob


def info_ButtonClick():
    popup = Tk()
    popup.wm_title("Test pop up")
    label = Label(popup, text="You clicked the more info button")
    label.pack(fill="both", pady=20, padx=20)
    entry1 = Entry (popup)
    entry1.pack(fill="both", pady=20, padx=20) 
    B1 = Button(popup, text="Continue", command = lambda:(messagebox.showinfo("Value from box", entry1.get())))
    B1.pack(fill="both", pady=20, padx=20)
    popup.mainloop()

def validateText(text):
    if(len(text)>0):
        return True
    else:
        messagebox.showinfo("Input Error", "No text entered for blob text".format(text))
        return False

def CorrectSpelling(entryBox):
    boxText = entryBox.get()
    if(validateText(boxText)):
        blob=TextBlob(boxText)
        correctedText = str(blob.correct())
        showText = "Original Text : {0}\nCorrected Text : {1}".format(boxText, correctedText)
        messagebox.showinfo("Corrected Spelling",showText)
        entryBox.delete(0,END)
        entryBox.insert(0,correctedText)

def TranslateToSpanish(boxText):
    if(validateText(boxText)):
        blob=TextBlob(boxText)
        showText = "English : {0}\nSpanish : {1}".format(boxText, str(blob.translate(from_lang='en',to='fr')))
        messagebox.showinfo("English to Spanish", showText)

def GetUnique(boxText):
    if(validateText(boxText)):
        blob=TextBlob(boxText)
        unique_words = blob.word_counts
        showText = "Unique words in '{0}' : {1}".format(boxText,str(len(unique_words)))
        messagebox.showinfo("Unique Text",showText)

def sentiment(boxText):
    if(validateText(boxText)):
        blob=TextBlob(boxText)
        messagebox.showinfo("Nouns", "Nouns {0}".format(blob.sentiment))

    

form = Tk()
(form.winfo_toplevel()).title("GUI Example")

canvas1 = Canvas(form, width = 400, height = 400)

entry1 = Entry (form) 
canvas1.create_window(160, 50, window=entry1)

label1 = Label(form, text="Enter Text for Text Blob")
canvas1.create_window(30, 50, window= label1)

b = Button(form, text="Correct Spelling", command=lambda:CorrectSpelling(entry1))
canvas1.create_window(70, 100, window = b)

b1 = Button(form, text="Translate to Spanish", command=lambda:TranslateToSpanish(entry1.get()))
canvas1.create_window(70, 150, window = b1)

b2 = Button(form, text="Get Unique", command=lambda:GetUnique(entry1.get()))
canvas1.create_window(70, 200, window = b2)

b3 = Button(form, text="Analyse Text for Sentiment", command=lambda:sentiment(entry1.get()))
canvas1.create_window(70, 250, window = b3)

canvas1.pack()

mainloop()

