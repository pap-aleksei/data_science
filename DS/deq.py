from collections import deque

def brackets(line):
    stash = deque()
    for i in line:
        if i == '(':
            stash.append(i)
        if i == ')':
            try:
                stash.pop()
            except IndexError:
                return False
    if len(stash) == 0:
        return True
    if len(stash) > 0:
        return False



print(brackets("(()())"))
print(brackets(""))
print(brackets("(()()))"))