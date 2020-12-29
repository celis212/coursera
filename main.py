txt = 'but soft what light in yonder window breaks'
words = txt.split()
# print(words)
t = list()
for word in words:
    t.append((len(word), word))
    print(t)
t.sort(reverse=True)#ordena the list in ascendent foprm
print(t)
res = list()
for length, word in t:
    res.append(word)
    print(res)


print(res)