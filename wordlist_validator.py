import re

def load_words(wordlist_filename):
    print("Loading word list from file...")
    wordlist = list()
    
    with open(wordlist_filename) as f:
        for line in f:
            wordlist.append(line.rstrip('\n'))
    
    print(f"{len(wordlist)} words loaded.")
    return wordlist

def is_valid_topic(topic):
    pattern = r'^[a-z0-9][a-z0-9-]{0,49}$'
    return bool(re.match(pattern, topic))

def validate_topics(wordlist):
    valid_topics = [word for word in wordlist if is_valid_topic(word)]
    return valid_topics

wordlist = load_words('wordlist.txt')
valid_topics = validate_topics(wordlist)

print(f"Valid topics: {', '.join(valid_topics)}")
