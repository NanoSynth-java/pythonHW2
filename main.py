# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('сколько монеток? '))

head = int(input('Какое количество монет лежат орлом? '))
tail = int(input('Какое количество монет лежат решкой? '))

if tail > head:
    minimal = n - tail
    print(f'Что бы все монеты лежали одной стороной, необходимо перевернуть {minimal} монеты которые лежат орлом!')
elif tail == head:
    print('Одинаковое количество монет!')
else:
    minimal = n - head
    print(f'Что бы все монеты лежали одной стороной, необходимо перевернуть {minimal} монеты которые лежат решкой!')
