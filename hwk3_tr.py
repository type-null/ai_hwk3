"""Assignment 3"""

import re
import stopwords
from nltk_tokenize import TweetTokenizer

def clean_text(tweet) -> str:
    """Remove RT, handle and url"""
    tweet = re.sub(re.compile(r'([RT])|(@[\w]+:?)|(\w+:\/\/\S+)'), ' ', tweet)
    return ' '.join(tweet.split()).strip()

def tokenize_text(cleaned_text) -> list:
    """Also filter out stop words"""
    tknzr = TweetTokenizer()
    token = tknzr.tokenize(cleaned_text)
    return [i for i in token if i not in stopwords.words()]

def isnum(token: str) -> bool:
    """check if a string is number: for use of indexing"""
    try:
        int(token)
        return True
    except ValueError:
        return False

INDEX_DICT = {}
LINE_COUNT = 0
with open("index_dict.txt") as file:
    for line in file:
        INDEX_DICT[line] = LINE_COUNT

def replace_token_with_index(tokenized_text, max_length_dictionary: int = 500) -> list:
    """Index tokens"""
    index_of_tweet = []
    inconvertible_token = []
    for token in tokenized_text:
        if isnum(token):
            index_of_tweet.append(INDEX_DICT["<number>"])
        elif token.lower() in INDEX_DICT:
            index_of_tweet.append(INDEX_DICT[token.lower()])
        else:
            inconvertible_token.append(token) # for test
    return index_of_tweet

def pad_sequence(index_list, max_length_tweet=20) -> list:
    """padding a list of indices with 0 until a maximum length"""
    if len(index_list) > max_length_tweet:
        padded_seq = index_list[:max_length_tweet]
    else:
        zeros = [0] * (max_length_tweet-len(index_list))
        padded_seq = index_list + zeros
    return padded_seq

def one_for_all(tweet, max_length_dictionary=500, max_length_tweet=20) -> list:
    """Do all conversion at once"""
    return pad_sequence(replace_token_with_index(tokenize_text(
        clean_text(tweet)), max_length_dictionary), max_length_tweet)
