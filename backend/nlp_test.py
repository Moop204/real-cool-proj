from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time


analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0
total = 0
score = 0

with open("positive.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)			#return value between -1 and 1

        if (vs['compound'] != 0):

        	score = score+vs['compound']
        	total = total + 1

print("------------------------------")

print("Generally good review: {}".format(score/(total)))
print("Total: {}".format(total))
print("Score: {}".format((score)))


score = 0
total = 0
with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)			#return value between -1 and 1

        if (vs['compound'] != 0):
        	score = score+vs['compound']
        	total = total + 1

print("Generally bad review: {}".format(score/(total)))
print("Total: {}".format(total))
print("Score: {}".format((score)))


#normalise data out from 0 - 1
food = 1			#average rating out of 5
school = 2			#if greater than 5 schools -> 100 percetage
ent = 3				#if greater than 5 placed -> 100 percentage
review = 4			#review data -> make review data percentage 0->2 out of 2

#no. of max school
#no. of ent areas


#max total is 50 - lowest 0 
total = review* rev_data + ent* ent_data + school* school_data + food*food_data








'''neg_count = 0
neg_correct = 0

with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['pos'] > 0.1:
            if vs['pos']-vs['neg'] <= 0:
                neg_correct += 1
            neg_count +=1

print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
'''