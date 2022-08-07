tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

from collections import defaultdict, deque
def task_manager(tasks):
    servers = defaultdict(deque)
    for n, server, vip in tasks:
        if vip is True:
            servers[server].appendleft(n)
        else:
            servers[server].append(n)
    return servers

print(task_manager(tasks))