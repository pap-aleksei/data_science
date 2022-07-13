"""Game: guess the number."""
import numpy as np

number = np.random.randint(1, 101) #Select number to guess

count = 0
while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))

    if predict_number > number:
        print('Number is smaller!')

    elif predict_number < number:
        print('Number is bigger!')

    else:
        print(f'You guessed the number within {count} tries! This is = {number}')
        break
