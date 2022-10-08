# Luke Coddington
# 9/16/22
# Assignment 2 - AI
# Assumed Time: 1hr
# Actual Time: 1hr
# Reasoning: The classes took a minute. Wasn't sure how they would be usefull in this program. 


from textblob import TextBlob



def log(text):
    f = open("Assignment2-output.txt", "a")
    f.write(text)
    print(text)
    f.close()

class Menu:
    def printMenu(self):
        print("1) Text Blob")
        print("2) Correct Spelling")
        print("3) Translate to Spanish")
        print("4) Exit")

class TextBlobFunctions(Menu):
    blob = TextBlob("")
    def enterText(self):
        text = input("Enter Text for Text Blob :: ")
        self.blob=TextBlob(text)
        log(text)

    def correctedText(self):
        log("\nCorrected Text :: "+str(self.blob.correct()))

    def translateToSpanish(self):
        log("\nText in Spanish :: "+str(self.blob.translate(from_lang='en',to='fr')))

class userInput(TextBlobFunctions):
    usrInput = -1
    def getInput(self):
        usrInput = input("Enter Selection :: ")
        usrInput = int(usrInput)
        if(usrInput == 1):
            self.enterText()
        elif(usrInput == 2):
            self.correctedText()
        elif(usrInput == 3):
            self.translateToSpanish()
        elif(usrInput == 4):
            log("Exiting")
            quit()
        else:
            print("Invalid Input")


f = open("Assignment2-output.txt", "w")
f.close()

menu = Menu()
userinput = userInput()
while(userinput.usrInput != 4) :
    menu.printMenu()
    userinput.getInput()