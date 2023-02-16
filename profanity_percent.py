import re
import pandas as pd

profanity_list = ["racial_slur1", "racial_slur2", "racial_slur3", ...] # 
list of racial slurs
tweet_file= pd.read_csv(r'tweet file.txt Path') # path to the tweet file
# Loop through each tweet in the file
    for tweet in tweet_file:
        # Remove any URLs from the tweet
        tweet = re.sub(r"http\S+", "", tweet)
        #removing the hash # sign from the word
        tweet = re.sub(r'#', '', tweet)
        # remove old style retweet text "RT"
        tweet = re.sub(r'^RT[\s]+', '', tweet)
        # Remove any special characters from the tweet
        tweet = re.sub(r'[^\w\s]','', tweet)
        # Convert the tweet to lowercase
        tweet = tweet.lower()
        
        # Split the tweet into individual words
        words = tweet.split()
        
        # Count the number of profanity indicators in the tweet
        profanity_count = 0
        for word in words:
            if word in profanity_list:
                profanity_count += 1
        
        # Calculate the degree of profanity as a percentage of the total 
words in the tweet
        degree_of_profanity = (profanity_count / len(words)) * 100
        
        # Print the degree of profanity for the tweet
        print("Tweet: " + tweet.strip())
        print("Degree of profanity: " + str(degree_of_profanity) + "%")
        print("\n")

