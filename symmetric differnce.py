n1 = int(raw_input())
s1 = set(map(int, raw_input().split()))
n2 = int(raw_input())
s2 = set(map(int, raw_input().split()))
s3 = (s1.difference(s2)).union(s2.difference(s1))
for x in sorted(list(s3)):
    print x