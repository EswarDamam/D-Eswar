cmd_count = int(raw_input())
M = []
for i in range(cmd_count):
    cmd = raw_input().split()
    if cmd[0] == 'insert':
        M.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'print':
        print M
    elif cmd[0] == 'remove':
        M.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        M.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        M.sort()
    elif cmd[0] == 'pop':
        M.pop()
    elif cmd[0] == 'reverse':
        M.reverse()                
