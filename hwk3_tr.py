
import re
import stopwords

def clean_text(tweet) -> str:
    """Remove RT, url, number and punctuation"""
    tweet = re.sub(re.compile(r'([RT])|(@[\w]+:?)|(\w+:\/\/\S+)'), ' ', tweet)
    return ' '.join(re.sub(r'([^A-Za-z\'])', ' ', tweet).split()).strip()

def tweetTokenizer(text) -> list:
    """Load nltk.tokenize.TweetTokenizer"""

def tokenize_text(cleaned_text) -> list:
    """Also filter out stop words"""
    token = cleaned_text.split()
    return [i for i in token if i not in stopwords.words()]

def replace_token_with_index() -> list:
    
    return 

def pad_sequence() -> list:
    return 
