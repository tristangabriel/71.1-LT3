r, c= [int(_) for _ in input().split()]
st = [input() for _ in range(r)]
laser = [0]*c

for i in range(c):
    for s in st:
        if s[i]=='X':
            laser[i]=1
            break

for s in st:
    for i in range(c):
        print('*' if laser[i] else s[i], end='')
    print()