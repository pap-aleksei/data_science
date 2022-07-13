"""Game: guess the number v2
Computer is trying itself.
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Guessing random number.

    Args:
        number (int, optional): Pick the number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)

def score_game(random_predict) -> int:
    """Average score number out of 1000 tries

    Args:
        random_predict (_type_): Score function

    Returns:
        int: Average number of tries
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))

    print(f'Your method can guess the number in {score} tries average')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
