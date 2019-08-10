from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time


analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0
total = 0
score = 0

'''
#Surry Hills
'''

with open("positive.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)			#return value between -1 and 1

        if (vs['compound'] != 0):

        	score = score+vs['compound']
        	total = total + 1

print("------------------------------")

rev_data1 = score/total
print("Generally good review: {}".format(score/(total)))
print("Total: {}".format(total))
print("Score: {}".format((score)))


#Secne 1: priority - 
#normalise data out from 0 - 1
food1 = 1           #average rating out of 5
school1 = 2         #if greater than 5 schools -> 100 percetage
ent1 = 3                #if greater than 5 placed -> 100 percentage
review1 = 4         #review data -> make review data percentage 0->2 out of 2

food_data = (4/5)
school = 3/5
ent = 1/5

#max total is 50 - lowest 0 
total1 = review1* rev_data1 + ent1* ent_data + school1* school_data + food1*food_data



'''
#scene2: blacktown
'''

score = 0
total = 0
with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)			#return value between -1 and 1

        if (vs['compound'] != 0):
        	score = score+vs['compound']
        	total = total + 1
rev_data2 = score/total
print("Generally bad review: {}".format(score/(total)))
print("Total: {}".format(total))
print("Score: {}".format((score)))


food2 = 3
school2 = 1 
ent2 = 2
review2 = 4 

food_data = 1/5
school = 2/5
ent = 4/5

total2 = review2* rev_data2 + ent2* ent_data + school2* school_data + food2*food_data


'''
#Fairfield
'''


food3 = 2
school3 = 1 
ent3 = 2
review3 = 4 

food_data = 1/5
school = 2/5
ent = 4/5


score = 0
total = 0
with open("../ReviewText/Fairfield.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)         #return value between -1 and 1

        if (vs['compound'] != 0):
            score = score+vs['compound']
            total = total + 1
rev_data2 = score/total


#parramatta

food3 = 2
school3 = 1 
ent3 = 2
review3 = 4 

food_data = 1/5
school = 2/5
ent = 4/5


score = 0
total = 0
with open("../ReviewText/BlackTown.txt","r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)         #return value between -1 and 1

        if (vs['compound'] != 0):
            score = score+vs['compound']
            total = total + 1
rev_data2 = score/total



print("Surry Hills: {}".format(total1))
print("BlackTown: {}".format(total2))
print("Fairfield: {}".format(total3))
print("Parramatta: {}".format(total4))
