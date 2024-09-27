from collections import deque


def is_palindrome(input_string):
    # Обробляємо рядок
    normalized_string = ''.join(char.lower()
                                for char in input_string if char.isalnum())

    # Створюємо двосторонню чергу
    char_deque = deque(normalized_string)

    # Порівнюємо символи з обох кінців deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


user_input = input("Введіть рядок для перевірки: ")

# Перевіряємо, чи є введений рядок паліндромом
if is_palindrome(user_input):
    print(f"'{user_input}' є паліндромом.")
else:
    print(f"'{user_input}' не є паліндромом.")
