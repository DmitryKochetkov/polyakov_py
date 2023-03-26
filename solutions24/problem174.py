from string import ascii_uppercase

def closed_substrings(s):
    items = []
    for letter in ascii_uppercase:
        for item in s.split(letter)[1:-1]:
            if len(item) >= 1:
                items.append(letter + item + letter)
    return items

c = 0
l = 0
longest_item = ''
with open('./data/24data/24-174.txt') as f:
    for line in f.readlines():
        if line.count('R') < 30:
            items = closed_substrings(line)
            c += len(items)
            for item in items:
                if len(item) > l:
                    l = len(item)
                    longest_item = item
print(l, c)