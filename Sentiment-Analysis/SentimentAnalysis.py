from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()


# Using readlines()
file1 = open('TwitterPosts.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    line=line.strip()
    print("Tweet #{1}:: {0}".format(line, count))
    print("Analysis {0}\n".format(analyser.polarity_scores(line)))
