X = set(map(int, raw_input().split()))
Y = int(raw_input())
isstrictsuperset = True
for z in range(Y):
    a = set(map(int, raw_input().split()))
    if not a.issubset(X):
        isstrictsuperset = False
    if len(a) >= len(X):
        isstrictsuperset = False
print isstrictsuperset 