word=input()
word_upper= sum(1 for c in word if c.isupper())
word_lower=len(word)-word_upper
if word_upper>word_lower:
    corrected_word=word.upper()
else:
    corrected_word=word.lower()

print(corrected_word)