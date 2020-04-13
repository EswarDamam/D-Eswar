a,b = map(int, input().split())
rows = [input() for _ in range(a)]
c = int(input())
for row in sorted(rows, key=lambda row: int(row.split()[c])):
    print(row)