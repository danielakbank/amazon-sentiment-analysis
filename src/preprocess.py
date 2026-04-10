import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)       # remove HTML tags
    text = re.sub(r'[^a-z\s]', '', text)   # remove punctuation and numbers
    return text.strip()