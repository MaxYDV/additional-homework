# Задание 1
# Пользователь вводит число. Определить, является ли оно четным.
##############################################################################################
# try:
#     number = int(input("Enter integer: "))
#     if number % 2 == 0:
#         print("The number is even.")
#     else:
#         print("Odd number.")
# except ValueError as error:
#     print("Enter only integer!")
##############################################################################################
# Задание 2
# Пользователь вводит два числа. Вывести на экран меньшее из этих чисел.
##############################################################################################
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if num1 <= num2:
#         print(f"The smallest number is {num1}.")
#     else:
#         print(f"The smallest number is {num2}.")
# except ValueError as error:
#     print("Enter only integer!")
##############################################################################################
# Задание 3
# Пользователь вводит число. Определить, положительное это число, отрицательное или равно нулю.
##############################################################################################
# try:
#     num1 = int(input("Enter first integer: "))
#     if num1 == 0:
#         print("The number 0 is neither a positive nor a negative number.")
#     elif num1 > 0:
#         print(f"The number {num1} is positive.")
#     else:
#         print(f"The number {num1} is negative")
# except ValueError as error:
#     print("Enter only integer!")
##############################################################################################
# Задание 4
# Пользователь с клавиатуры вводит 5 оценок студента.
# Определить, допущен ли студент к экзамену.
# Студент получает допуск, если его средний балл 4 балла и выше.
##############################################################################################
# try:
#     eval1 = int(input("Enter the first grade from 1 to 5 : "))
#     eval2 = int(input("Enter the second grade from 1 to 5: "))
#     eval3 = int(input("Enter the third grade from 1 to 5: "))
#     eval4 = int(input("Enter the fourth grade from 1 to 5: "))
#     eval5 = int(input("Enter the fifth grade from 1 to 5: "))
#     average = (eval1 + eval2 + eval3 + eval4 + eval5) / 5
#
#     if eval1 > 5 or eval1 <= 0 or eval2 > 5 or eval2 <= 0 or eval3 > 5 or eval3 <= 0 or eval4 > 5 or eval4 <= 0 or eval5 > 5 or eval5 <= 0:
#         print("Incorrect evaluation!")
#     else:
#         if 4 <= average <= 5:
#             print(f"Student accepted!Average score: {average}")
#         else:
#             print(f"Student not accepted!Average score: {average}")
#
# except ValueError as error:
#     print("Enter only integer!")
############################################################################################1##
# Задание 5
# Пользователь вводит с клавиатуры число.
# Если оно четное, умножить его на три, иначе – поделить на два.
# Результат вывести на экран.
##############################################################################################
# try:
#     num1 = int(input("Enter first integer: "))
#     if num1 % 2 == 0:
#         print(num1 * 3)
#     else:
#         print(num1 / 2)
# except ValueError as error:
#     print("Enter only integer!")
# except ZeroDivisionError as error:
#     print("You cannot divide by zero!")
##############################################################################################
# Задание 6
# Написать программу-калькулятор.
# Пользователь вводит два числа и выбирает арифметическое действие.
# Вывести на экран результат.