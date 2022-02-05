'''Сколько 9-значных чисел, делящихся на 5, можно составить путем перестановки цифр числа 377 353 752?'''

from itertools import permutations

mas = []
for i in permutations('377353752', 9):
   if int(''.join(i)) % 5 == 0:
      mas.append(int(''.join(i)))
print(len(set(mas)))
