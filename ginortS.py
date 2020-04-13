from __future__ import print_function
A = raw_input().strip()
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
sorted_A = sorted(A, key=order.index)
print(*sorted_A, sep='')