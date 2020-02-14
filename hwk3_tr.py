
import re
import stopwords
from nltk_tokenize import TweetTokenizer

def clean_text(tweet) -> str:
    """Remove RT, url, number and punctuation"""
    tweet = re.sub(re.compile(r'([RT])|(@[\w]+:?)|(\w+:\/\/\S+)'), ' ', tweet)
    return ' '.join(tweet.split()).strip()

def tokenize_text(cleaned_text) -> list:
    """Also filter out stop words"""
    tknzr = TweetTokenizer()
    token = tknzr.tokenize(cleaned_text)
    return [i for i in token if i not in stopwords.words()]

def replace_token_with_index(tokenized_text, max_length_dictionary=500) -> list:
    index_of_tweet = []
    with open("index_dict.txt") as index_dict:
        for _ in tokenized_text:
            index_of_tweet.append(1)
    return index_of_tweet

def pad_sequence(index_list, max_length_tweet=20) -> list:
    if len(index_list) > max_length_tweet:
        padded_seq = index_list[:20]
    else:
        padded_seq = index_list + 2

    return padded_seq

def oneForAll(tweet) -> list:
    """Do all conversion at once"""
    return pad_sequence(replace_token_with_index(
        tokenize_text(clean_text(tweet))))

