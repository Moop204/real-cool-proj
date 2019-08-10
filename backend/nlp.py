from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

analyzer = SentimentIntensityAnalyzer()

USER_PRIORITY = {
    "school": 3,
    "reviews": 4,
    "food": 2,
    "ent": 1
}

PARRAMATTA = {
    "filePath": "./ReviewText/Parramatta.txt",
    "food": 4/5,
    "ent": 3/5,
    "school": 2/5 
}

SURRY_HILLS = {
    "filePath": "./ReviewText/SurryHills.txt",
    "food": 4/5,
    "ent": 2/5,
    "school": 3/5
}

BLACKTOWN = {
    "filePath": "./ReviewText/Blacktown.txt",
    "food": 3/5,
    "ent": 2/5,
    "school": 4/5
}

FAIRFIELD = {
    "filePath": "./ReviewText/Fairfield.txt",
    "food": 3/4,
    "ent": 3/4,
    "school": 5/5
}

def getSentiment(area):
    score = 0
    total = 0
    with open(area["filePath"], "r") as f:
        for line in f.read().split('\n'):
            vs = analyzer.polarity_scores(line)


            if (vs['compound'] != 0):
                score = score + vs['compound']
                total = total + 1
    
    total = USER_PRIORITY["reviews"]*(score/total) + USER_PRIORITY["food"]*area["food"] + USER_PRIORITY["ent"]*area["ent"] + USER_PRIORITY["school"]*area["school"]
    
    return total
