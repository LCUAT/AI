# Luke Coddington
# 9/7/22
# Assignment 1 - AI
# Assumed Time: 30mins
# Actual Time: 2hrs
# Reasoning: This look longer because I got distracted a couple times and also had to get my environment set up.


from textblob import TextBlob

usrInput = -1
blob = TextBlob("")
while(usrInput != 4) :
    print("1) Text Blob")
    print("2) Correct Spelling")
    print("3) Translate to Spanish")
    print("4) Exit")
    usrInput = input("Enter Selection :: ")
    usrInput = int(usrInput)
    if(usrInput == 1):
        text = input("Enter Text for Text Blob :: ")
        blob=TextBlob(text)
        print("Blob :: ", blob)
    elif(usrInput == 2):
        print("Corrected Text :: ",blob.correct())
    elif(usrInput == 3):
        print("Text in Spanish :: ",blob.translate(from_lang='en',to='fr'))
    else:
        print("Invalid Input")
    