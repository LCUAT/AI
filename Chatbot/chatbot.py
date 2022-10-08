# Luke Coddington
# 10/11/22
# Assignment: Chatbod
# Assumed Time: 1hr
# Actual Time: 3hr
# Reasoning: I got distracted with some of the dialog and references. If you have never seen red vs blue I would recomend it

#dependencies
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#create chatbot
chatbot=ChatBot('Gary')


#train chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
			"chatterbot.corpus.english.conversations" )
greeting = "THIS IS THE HOUSING FACILITY FOR THE GREAT WEAPON. I AM THE KEEPER OF THE GREAT WEAPON. YOU ARE THE GREAT DESTROYER. YOU WILL DEMOLISH THIS FACILITY, KILL ME, STEAL THE GREAT WEAPON, AND BRING ABOUT THE GREAT DOOM FOR BILLIONS OF PEOPLE. ...WELCOME! HOW MAY I BE OF ASSISTANCE?"
trainingPrases = [
    "Hello my name is ",
    greeting,
    "What is the great weapon?",
    "I don't know. I was programed by an advanced alien race who forgot to tell me"
    "What is your name?",
    "My name is Gary",
    "What is your favorit movie?",
    "Red vs Blue is my favorite tv show",
    "Hello",
    greeting,
    "Hi",
    greeting,
    "Can computers lie?",
    "Lying is such a shisno concept. I mean human concept.",
    "How are you?",
    "I'm good but my ION submatrix is a little itchy.",
    "Who made you?",
    "I was made my an advanced alien race.",
    "What alien race?",
    "I don't know anything about those creatures. Instead they filled my memory banks with knowledge about the shisnos. I mean humans.",
    "What is a shisno?",
    "Shisno is what you are called by the aliens that built me.",
    "What?",
    "Your coming has been fortold by the great prophecy",
    "Do you know any jokes?",
    "Knock Knock",
    "Who's there?",
    "Hard Drive",
    "Hard Drive who?",
    "01001001 00100000 01101000 01100001 01100100 00100000 01100001 00100000 01101000 01100001 01110010 01100100 00100000 01100100 01110010 01101001 01110110 01100101 00101100 00100000 01101100 01100101 01110100 00100000 01101101 01100101 00100000 01101001 01101110 00100000 01110011 01101111 00100000 01001001 00100000 01100011\n hahaha I love that one"
    ]
listTrainer = ListTrainer(chatbot)
listTrainer.train(trainingPrases)

#intro
print("\n\n\n\n")
print("="*100)
print("GARY: YOU ARE EARLY. YOU ARE NOT SUPPOSED TO BE HERE FOR ANOTHER 1,856 YEARS. MY NAME IS GARY. WHAT IS YOUR NAME?")
name = input ("response :: ")
usrInput = "Hello my name is " + name

#get user input and run program
while(usrInput.lower() != "bye" or usrInput.lower() != "good bye" or usrInput.lower() != "exit"):
    response = chatbot.get_response(usrInput)
    print("GARY: {0}".format(str(response).upper()))
    usrInput=input("{0}: ".format(name.upper()))
print("GOOD BYE")
