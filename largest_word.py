sentence="i want become AI expert"
words=sentence.split()
longest=""
for word in words:
    if len(word)>len(longest):
     longest=word
print("Longest word:",longest)