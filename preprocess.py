import json
import re
import sys

# Define regex pattern for tokenization
pattern = re.compile(r"[\s\t\d\(\)\[\]\{\}\.\!\?;:,\+=\-_\"'`~#@&\*%€\$§\\/\^\>]+")


def load_stopwords(stopwords_file):
    with open(stopwords_file, "r") as f:
        stopwords = set(f.read().splitlines())
    return stopwords

def preprocess_review(review_data, stopwords):
    review_text = review_data.get("reviewText", "").lower()
    category = review_data.get("category", "")

    # Tokenization using regex pattern
    tokens = pattern.split(review_text)
    # Filter out stopwords and tokens consisting of only one character
    tokens = [token for token in tokens if token not in stopwords and len(token) > 1]
    return category, tokens

if __name__ == "__main__":
    # Load stopwords from file
    stopwords_file = "stopwords.txt"  # Adjust the path if needed
    stopwords = load_stopwords(stopwords_file)
    
    # Read input from stdin
    for line in sys.stdin:
        try:
            review_data = json.loads(line)
            category, tokens = preprocess_review(review_data, stopwords)
            if tokens:
                for token in tokens:
                    # Emit key-value pairs for Hadoop Streaming
                    print(f"{category}\t{token}")
        except Exception as e:
            # Log or handle any errors
            pass

