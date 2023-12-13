N = int(input())
S = input()

letters = 'atcoder'
dic = {}
for letter in letters:
    dic[letter] = {}
    for i, s in enumerate(S):
        if s == letter:
            dic[letter].add(i)

i = 0
j = 0
while True:
    if i in dic[letter[j]]
    i += 1