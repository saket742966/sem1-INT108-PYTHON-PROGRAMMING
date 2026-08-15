# Take a sample of ten phishing e-mails (any text file) and find most common

from collections import Counter
import re

with open("phishing_emails.txt", "r") as file:
    text = file.read().lower()

words = re.findall(r'\b[a-z]+\b', text)

word_count = Counter(words)

most_common = word_count.most_common(10)

print("Most common words:")

for word, count in most_common:
    print(word, ":", count)
    
    