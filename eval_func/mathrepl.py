import math

__version__ = "1.0"

ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

PS1 = "mr>>"

WELCOME = f"""
MathREPL {__version__} - обработчик математических выражений на Python!
Введите математическое выражение после приглашения "{PS1}".
Для дополнительной информации используйте команду help.
Чтобы выйти, наберите quit или exit.
"""

USAGE = f"""
Соберите математическое выражение из чисел и операторов.
Можно использовать любые из следующих функций и констант:

{', '.join(ALLOWED_NAMES.keys())}
"""


def evaluate(expression):
    """Вычисляет математическое выражение."""
    # Компиляция выражения в байт-код
    code = compile(expression, "<string>", "eval")

    # Валидация доступных имен
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"The use of '{name}' is not allowed")

    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)

def main():
    """Читает и рассчитывает введенное выражение"""
    print(WELCOME)
    while True:
        # Читаем пользовательский ввод
        try:
            expression = input(f"{PS1} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Поддержка специальных команд
        if expression.lower() == "help":
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Вычисление выражения и обработка ошибок
        try:
            result = evaluate(expression)
        except SyntaxError:
            # Некорректное выражение
            print("Вы ввели некорректное выражение.")
            continue
        except (NameError, ValueError) as err:
            # Если пользователь попытался использовать неразрешенное имя
            # или неверное значение в переданной функции
            print(err)
            continue

        # Выводим результат, если не было ошибок
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()