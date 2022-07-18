text = "Later in the course, you'll see how to use the collections Counter class."
word_count = {}
for char in text.casefold():
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1

for char, count in sorted(word_count.items()):
    print(char, count)
