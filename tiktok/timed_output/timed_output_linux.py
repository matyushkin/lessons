#! /usr/bin/env python
# решение для Linux

import sys
import select

timeout = 10

print(f"У вас {timeout} секунд, чтобы ввести текст: ")
r, w, x = select.select([sys.stdin], [], [], timeout)


if __name__ == "__main__":
    if r:
        print(f"Вы ввели '{sys.stdin.readline().strip()}'.")
    else:
        print("Вы ничего не ввели.")
