# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
b = sorted(a)
result = b[n-1]*b[n-2]
print(result)
