def check_brackets(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    has_brackets = False

    for char in expression:
        if char in brackets.values():  # Відкриваючі дужки
            stack.append(char)
            has_brackets = True  # Знайдено дужку
        elif char in brackets.keys():  # Закриваючі дужки
            has_brackets = True  # Знайдено дужку
            if not stack or stack.pop() != brackets[char]:
                return "Несиметрично"

    if not has_brackets:
        return "Не знайдено дужок"

    return "Симетрично" if not stack else "Несиметрично"


user_input = input("Введіть рядок з дужками для перевірки: ")


print(user_input + ":", check_brackets(user_input))
