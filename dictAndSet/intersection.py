text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_arr = set(text.split(" "))
print(text_arr)

prep_used = text_arr.intersection(prepositions)
print(prep_used)
