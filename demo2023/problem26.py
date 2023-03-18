with open('./26.txt') as f:
    n = int(f.readline())
    a = list(map(int, f.readlines()))

    a.sort(reverse=True)
    c = 1
    m = a[0]
    last = a[0]

    for i in range(n):
        if last - a[i] >= 3:
            last = a[i]
            c += 1
            m = a[i]
    
    print(c, m)
