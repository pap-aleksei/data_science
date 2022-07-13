import random
my_list = []
S = 0
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
while S < 10:
    for x in my_list:
        S += x
print(S)
for i, dynamic in enumerate(user_dynamics):
