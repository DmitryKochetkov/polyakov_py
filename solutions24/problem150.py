from string import ascii_uppercase

# counts = dict()
# for letter in ascii_uppercase:
#     counts[letter] = 0

counts = {k: 0 for k in ascii_uppercase}

with open('./data/24data/24-s2.txt') as f:
    s = f.readline()
    for i in range(len(s)-2):
        if s[i] == 'A' and s[i+2] == 'C':
            counts[s[i+1]] += 1

m = 0
answer = ''
for k, v in counts.items():
    if v > m:
        m = v
        answer = k

print(answer, m)