# imports
import wikipedia
import re
from textblob import TextBlob
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

print("Program libraries for: ")
print("Torch")
print("Wikipedia")
print("Parrot")
print("textblob\n\n")

print("\nCreating random seed with torch :: ",end='')
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)
random_state(1234)
print("Done")

print("\nDoing a wiki search for 'Mongolia' and showing result pages :: ")
num=0
wiki_page = wikipedia.search("Mongolia", results=10)
for res in wiki_page:
    print("{0}) {1}".format(num, res))
    num +=1
print("Done")

print("\nParot re-phrase")
print("-"*50)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
phrase = input("Enter Phrase :: ")
para_phrases = parrot.augment(input_phrase=phrase)
print("Paraphrase :: "+para_phrases[0][0])
print("End of parrot demo\n")

blob = TextBlob(para_phrases[0][0])
print("Text blob :: " + str(blob))

findExclementation = re.findall("!", para_phrases[0][0])
if(len(findExclementation) > 0):
    print("'!' Found with re")
else:
    print("'!' NOT found with re")
print("Program complete")