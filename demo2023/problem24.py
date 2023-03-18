vowels = 'AO'
consonants = 'CDF'

with open('./24.txt') as f:
    s = f.readline()
    b = 0
    m = 0
    s = s.replace('CA', '1')
    s = s.replace('CO', '1')
    s = s.replace('DA', '1')
    s = s.replace('DO', '1')
    s = s.replace('FA', '1')
    s = s.replace('FO', '1')

    for i in range(len(s)):
        if s[i] == '1':
            b += 1
            m = max(m, b)
        else:
            if i > 0 and s[i-1] == '1':
                b = 0

    m = max(m, b)

print(m)