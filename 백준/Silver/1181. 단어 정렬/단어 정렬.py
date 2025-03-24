n = int(input())
words = {input().strip() for _ in range(n)}

def sort(word):
    return (len(word), word)

sorted_words = sorted(words, key=sort)

for word in sorted_words:
    print(word)
