import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from collections import Counter
import matplotlib.pyplot as plt

file_name = "austen_persuasion.txt"

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

tokens = word_tokenize(text)
print(f"Загальна кількість токенів у тексті: {len(tokens)}")

tokens_lower = [w.lower() for w in tokens]

freq_all = Counter(tokens_lower)
top10_all = freq_all.most_common(10)
print("\nТоп-10 найчастотніших слів (усі слова, без очищення):")
for word, count in top10_all:
    print(f"{word!r}: {count}")

words_all = [w for w, c in top10_all]
counts_all = [c for w, c in top10_all]

plt.figure(figsize=(10, 5))
plt.bar(words_all, counts_all)
plt.title("Top-10 words in 'Persuasion' (raw text)")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

stop_words = set(stopwords.words("english"))
punct = set(string.punctuation)

clean_tokens = [
    w for w in tokens_lower
    if w not in stop_words
    and w not in punct
    and w.isalpha()
]

print(f"\nКількість слів після очищення: {len(clean_tokens)}")

freq_clean = Counter(clean_tokens)
top10_clean = freq_clean.most_common(10)

print("\nТоп-10 найчастотніших слів після видалення стоп-слів і пунктуації:")
for word, count in top10_clean:
    print(f"{word!r}: {count}")

words_clean = [w for w, c in top10_clean]
counts_clean = [c for w, c in top10_clean]

plt.figure(figsize=(10, 5))
plt.bar(words_clean, counts_clean)
plt.title("Top-10 words in 'Persuasion' (without stopwords & punctuation)")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()