import csv
words_count = {}
with open ('Newsfeed.txt', 'r') as file:
    text = file.read()
    rows = text.split('\n')
    words = []
    for i in rows:
        w = i.split()
        w = [j.strip('.,:?!-') for j in w]
        w = [j.lower() for j in w]
        w = [j for j in w if j.isalpha()]
        words.extend(w)

    for i in words:
        if i in words_count:
            words_count[i] = words_count[i] + 1
        else:
            words_count[i] = 1
print(type(words_count))
csv.register_dialect('my_dialect', delimiter = '-')
with open ('words_count_csv.csv', 'w', newline = '') as wordsfile:
    writer = csv.writer(wordsfile, 'my_dialect')
    writer.writerows(words_count.items())


letters_count = {}
with open ('Newsfeed.txt', 'r') as file:
    text = file.read()
    rows = text.split('\n')
    letter = []
    for i in rows:
        w = i.split()
        w = [j.strip('.,:?!-') for j in w]
        w = [j for j in w if j.isalpha()]
        for h in w:
            l = list(h)
            letter.extend(l)

    for i in letter:
        if i in letters_count:
            letters_count[i] = letters_count[i] + 1
        else:
            letters_count[i] = 1
print(letters_count)
l_amount = 0
l_values = sum(letters_count.values())
print(l_values)

UPPER = {}

for k, v in letters_count.items():
    if k.isupper():
        UPPER[k] = letters_count[k]
letters_count = {k:v for (k,v) in letters_count.items() if k.islower()}
print(UPPER, letters_count)

letters_statistics = []

for k,v in letters_count.items():
    if k.upper() in UPPER:
        d = {'letter': k, 'count_all': v + UPPER[k.upper()], 'count_uppercase': UPPER[k.upper()], "percentage": round((v + UPPER[k.upper()]) / l_values * 100,2)}
        letters_statistics.append(d)
    else:
        d = {'letter': k, 'count_all': v, 'count_uppercase': 0,
             "percentage": round(v / l_values * 100,2)}
        letters_statistics.append(d)
print(letters_statistics)


with open ('words_count_2_csv.csv', 'w', newline = '') as wordsfile:
    headers = ['letter', 'count_all', 'count_uppercase', "percentage"]
    writer = csv.DictWriter(wordsfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(letters_statistics)







