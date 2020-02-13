
import re
import stopwords

def clean_text(tweet) -> str:
    """Remove RT, url, number and punctuation"""
    tweet = re.sub(re.compile(r'([RT])|(@[\w]+:?)|(\w+:\/\/\S+)'), ' ', tweet)
    return ' '.join(re.sub(r'([^A-Za-z\'])', ' ', tweet).split()).strip()

def tweetTokenizer(text) -> list:
    """Load nltk.tokenize.TweetTokenizer"""
    return

def tokenize_text(cleaned_text) -> list:
    """Also filter out stop words"""
    token = cleaned_text.split()
    return [i for i in token if i not in stopwords.words()]

def replace_token_with_index(tokenized_text) -> list:
    indexOfTweet = []
    with open("index_dict.txt") as indexDict:
        for token in tokenized_text:
            indexOfTweet.append(1)
    return indexOfTweet

def pad_sequence(index_list) -> list:
    return "Yes"

def oneForAll(tweet) -> list:
    """Do all conversion at once"""
    return pad_sequence(replace_token_with_index(
        tokenize_text(clean_text(tweet))))

