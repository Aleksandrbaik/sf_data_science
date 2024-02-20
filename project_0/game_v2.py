"""Игра угадай число. Компьютер сам загадывает число"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число
    
    Args:
        number (int, optional): Загаданое число. Defaults to 1.

    Returns:
        int: Число попыток
    """
      
    count =0
    
    while True:
        count +=1
        predict_number = np.random.randint(1,100)  # предполагаемое число
        if number == predict_number:
            break # Выход из цикла, угадали число
    return (count)

print(f'Количество попыток:{random_predict()}')
        
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = [] # список для сохранения попыток
    np.random.seed(1) # фиксируем сид для воиспроводимости
    random_array = np.random.randint(1,100, size=(1000)) # Загадали список чисел 
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # Находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)
#RUN
if __name__  == '__main__':
    score_game(random_predict)