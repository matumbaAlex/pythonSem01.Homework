# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)   123123
# 100 -> 1 (1 + 0 + 0) |

number = int(input('enter number: '))
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(sum)


