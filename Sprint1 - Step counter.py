# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:27:51 2023

@author: Нурбий
"""
import datetime as dt

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or (None in data):
        return False
    else:
        return True
'''    
    return not (len(data) != 2 or (None in data))
'''
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.

'''
def max_time(any_dict):
    keys = list(any_dict.keys())
    result = dt.time(0, 0)
    for key in keys:
        if result < dt.datetime.strptime(key, FORMAT).time():
            result = dt.datetime.strptime(key, FORMAT).time()
    return result  
'''

def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data == {} or time <= max(storage_data.keys()):
        return False
    else:
        return True
        
'''
    return time > max_time(storage_data) and storage_data
'''
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True 


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return (steps + sum(storage_data.values()))
    
    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.
    

def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return (steps * STEP_M / 1000)
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    minutes = (current_time.hour * 60.0 + current_time.minute)
    
    hours = (current_time.hour + current_time.minute / 60.0)
    
    mean_speed = dist / hours
    
    spent_calories = (K_1 * WEIGHT + (mean_speed**2 / HEIGHT) * K_2 * WEIGHT) * minutes
    
    return spent_calories
    # В уроке «Последовательности» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени; 
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return ('Отличный результат! Цель достигнута.')
    elif dist >= 3.9:
        return ('Неплохо! День был продуктивным.')
    elif dist >= 2:
        return ('Маловато, но завтра наверстаем!')
    else:
        return ('Лежать тоже полезно. Главное — участие, а не победа!')
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.


# Место для функции show_message.
def show_message(pack_time, day_steps, dist, spent_calories, achievement):
    print()
    print(f'Время: {pack_time.strftime(FORMAT)}.')
    print(f'Количество шагов за сегодня: {day_steps}.')
    print(f'Дистанция составила {dist:.2f} км.')
    print(f'Вы сожгли {spent_calories:.2f} ккал.')  
    print(achievement)                  
    print()
    

def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data) == False: # Если функция проверки пакета вернет False
        return 'Некорректный пакет'

    # Распакуйте полученные данные.
    pack_time = dt.datetime.strptime(data[0], FORMAT).time() # Преобразуйте строку с временем в объект типа time.

    if check_correct_time(pack_time): # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1]) # Запишите результат подсчёта пройденных шагов.
    
    dist = get_distance(day_steps) # Запишите результат расчёта пройденной дистанции.
    
    spent_calories = get_spent_calories(dist, pack_time) # Запишите результат расчёта сожжённых калорий.
    
    achievement = get_achievement(dist) # Запишите выбранное мотивирующее сообщение.
    
    # Вызовите функцию show_message().
    
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    
    # Добавьте новый элемент в словарь storage_data.
    
    storage_data[pack_time] = day_steps
    # Верните словарь storage_data.
    return storage_data


# Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)