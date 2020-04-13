count = list(map(int, raw_input().strip().split()))
x = count[0]
y = count[1]
Arr = list(map(int, raw_input().strip().split()))
a = set(map(int, raw_input().strip().split()))
b = set(map(int, raw_input().strip().split()))
result = 0
for i in Arr:
    if i in a:
        result += 1
    elif i in b:
        result += -1
print(result)