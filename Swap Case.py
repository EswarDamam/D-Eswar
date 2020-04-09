def change(y):
    if str.islower(y):
        return str.upper(y)
    else:
        return str.lower(y)


def swap_case(s):
    return ('').join(map(change,s))

if __name__ == '__main__':