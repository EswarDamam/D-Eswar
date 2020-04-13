from string import split
def is_palindrome(a):
    if int(str(a)[::-1]) is a:
        return True
    return False
def is_positive(a):
    if a > 0:
        return True
    return False
b = int(raw_input())
nums = map(lambda a: int(a), split(raw_input()))
if all([is_positive(a) for a in nums]):
    if any([is_palindrome(a) for a in nums]):
        print True
    else:
        print False
else:
    print False    