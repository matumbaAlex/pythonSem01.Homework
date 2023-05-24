# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('enter  n: '))
m = int(input('enter  m: '))
k = int(input('enter  k: '))

if n == m == 1: print("no")
elif k < n and k < m: print('no')
elif (k % m == 0 or k % n == 0) and (k < (m*n)): print('Yes')
elif (k == m or k == n) and (k < (m*n)): print('Yes')
else: print('no')
