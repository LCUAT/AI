# Luke Coddington
# 10/1/22
# Assignment 4 - AI
# Assumed Time: 1hr
# Actual Time: 3hr
# Reasoning: The items I selected in the previous assignment didn't work the way they were expected to and 
# I ended up writting most of the functionality from scratch.

# imports
import wikipedia
import re
from textblob import TextBlob

# header
print("\n")
print("="*50)
print("AI Initial Reseach Paper Example Generator")
print("="*50)
print("")

# get topic
user_topic = input("Reasearch Topic :: ")
print("")

# get number of results pages
numResults = input("How many pages to list :: ")
print("")
print("Searching for pages [--", end="")
wiki_page = wikipedia.search(user_topic, results=numResults)
print("---] Done!\n")

# show pages and get input
print("Pages Found for " + user_topic)
print("-"*50)
num =0
usrInput = ""
if(int(numResults) < 1):
    numResults = 3
if(int(numResults) > 1):
    for res in wiki_page:
        print("{0}) {1}".format(num, res))
        num +=1
    usrInput=input("\nSelect page to use :: ")
print("")

#get page
print("Gathering intial data [", end="")
wiki_page = wikipedia.page(wiki_page[int(usrInput)])
print("--", end="")

#get content of selected page
content = wiki_page.content
print("--", end="")

#get references of selected page
references = wiki_page.references

#get headings of selected page
headings=re.findall('===? .* ===?',content)
print("--] DONE!\n")

#get number of references to list
numReferences = int(input("Number of references to list (max: {0}) : ".format(len(references))))
print("")

#show topics to include and get input
print("Topics to Include")
print("-"*50)
num = 0
for heading in headings:
    tmp=heading.replace("==","")
    tmp=tmp.replace("=","")
    tmp.strip()
    print("{0}) {1}".format(num, tmp))
    num +=1
usrInput=input("Select topics to include separated by a comma :: ")
splitInput = usrInput.split(',')

#compile the paper content
print("\nCompiling Example Paper [", end="")
body = []
for selection in splitInput:
    bodyContent = re.findall(rf"{headings[int(selection)]}\n?\n?(.*?)\n", content)[0]
    blob = TextBlob(bodyContent)
    body.append({"title": headings[int(selection)], "body": str(blob.correct())})
    print("--", end="")

print("--] - DONE!")

#write to file
def log(text):
    try:
        f = open("{0}-Example.doc".format(user_topic), "a", encoding="utf-8")
        f.write(text)
        f.write('\n')
        f.close()
    except Exception as e:
        print(e)
        print("Unable to append text :: ", text) 
    
#log paper
def logPaper():
    print("writing content to file [--", end='')

    #title
    log("_"*50)
    log(wiki_page.title)
    log("_"*50)
    log("")
    log("")
    print("--", end="")

    #summary
    log("Sumary")
    log("-"*50)
    log("\t"+wiki_page.summary)
    log("")
    log("")
    print("--", end="")

    #body
    for element in body:
        log(element["title"])
        log("-"*50)
        log("\t"+element["body"])
        log("")
        log("")
        print("--", end="")

    #references
    log("References")
    log("-"*50)
    for ref in range(numReferences):
        log("\t"+str(references[ref]))
    print("--] Done!")
    print("Output File :: {0}-Example.doc".format(user_topic))

#print paper
def printPaper():
    #title
    print(wiki_page.title)
    print("-"*50)
    print("\n\n")

    #summary
    print("Sumary")
    print("-"*50)
    print("\t"+wiki_page.summary)
    print("\n\n")

    #body
    for element in body:
        print(element["title"])
        print("-"*50)
        print("\t"+element["body"])
        print("\n\n")

    #references
    print("References")
    print("-"*50)
    for ref in range(numReferences):
        print("\t"+str(references[ref]))

#get input on what the user wants to do with the content
usrInput = -1
while(usrInput <1 and usrInput <3):
    print("")
    print("Actions")
    print("-"*50)
    print("1) Print Paper to Console")
    print("2) Write Paper to File")
    print("3) Exit")
    usrInput = int(input("Select Action ::"))

print("")
if(usrInput == 1):
    printPaper()
if(usrInput == 2):
    logPaper()
else:
    quit()
