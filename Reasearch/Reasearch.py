# Luke Coddington
# 10/1/22
# Final - AI
# Assumed Time: hr
# Actual Time: hr
# Reasoning: 

# imports
import wikipedia
import re
from textblob import TextBlob
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)

parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

def paraphrase(phrase):
    fullRephrase = ""
    sentances = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', phrase)
    unUsable =0
    for sentance in sentances:
        #print("DEBUG :: sentace :: ", sentance)
        try:
            para_phrases = parrot.augment(input_phrase=sentance)
            fullRephrase+=(para_phrases[0][0]) + ". "
            print("-", end="")
        except:
            #print("Unable to parse the following sentance :: \n " + sentance)
            fullRephrase+="**["+ sentance+"]"
            unUsable +=1
            print("x", end="")
    print("--] DONE!", end='')
    print(" --> Unusable sentances ::{0}/{1}".format(str(unUsable), str(len(sentances))))
    return fullRephrase

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
print("---] DONE!")

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
headings=re.findall('===?.*===?',content)
print("--] DONE!")

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
print("\nGathering data [", end="")
body = []
for selection in splitInput:
    bodyContent = re.findall(rf"{headings[int(selection)]}\n?\n?(.*?)\n", content)[0]
    #blob = TextBlob(bodyContent)
    #body.append({"title": headings[int(selection)], "body": str(blob.correct())})
    body.append({"title": headings[int(selection)], "body": bodyContent})
    #body.append(bodyContent)
    print("--", end="")

print("--] - DONE!")

print("Writting Paper")
print("WARNING :: this could take awhile")
print("-"*50)

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


paper = ""

def append(text, rePhrase):
    global paper
    if rePhrase == True: 
        paper += paraphrase(text)
    else:
        paper += text
    paper += "\n"

def appendDash(num = 50):
    global paper 
    for x in range(num):
        paper += "-"
    paper+="\n"

#title
print("Title [", end='')
appendDash()
append(wiki_page.title, False)
appendDash()
append("", False)


#summary
print("Summary [", end='')
append("Summary", False)
appendDash()
append(wiki_page.summary, True)
append("", False)

#body
print("Body")
for element in body:
    print("\t{0} [".format(element["title"]), end='')
    append(element["title"], False)
    appendDash()
    append(element["body"], True)
    append("", False)
append("", False)

#references
print("References [", end='')
append("References", False)
appendDash()
append(element["body"], True)
for ref in range(numReferences):
    append(str(references[ref]), False) 
    print("--", end="")    
print("--] DONE!")

log(paper)