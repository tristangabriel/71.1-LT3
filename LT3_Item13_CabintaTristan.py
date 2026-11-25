n, k= [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

b = [sum(a[:k])]
for i in range(n-k):
    b.append(b[-1]-a[i]+a[i+k])
print(*b)