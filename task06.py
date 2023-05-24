# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

number = int(input('enter ticket number: '))

leftSide = number // 1000
rightSide = number % 1000

leftSum = 0
while leftSide > 0:
    leftSum += leftSide % 10
    leftSide //= 10
rightSum = 0
while rightSide > 0:
    rightSum += rightSide % 10
    rightSide //= 10
if leftSum == rightSum: print('yes')
else: print('no')
