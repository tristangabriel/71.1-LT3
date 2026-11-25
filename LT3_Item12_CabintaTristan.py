bank = {}
n, t= [int(_) for _ in input().split()]
for i in range(n):
    name, b = input().split()
    bank[name] = float(b)

for _ in range(t):
    n1, op, n2, num = input().split()
    num = float(num)
    bank[n2] += num
    bank[n1] -= num

if any(bank[i]<0 for i in bank.keys()):
    print("Uh-oh :c")
else:
    print("Paid c:")