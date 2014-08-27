from random import random
from timeit import Timer

lst_com = [random() for j in range(1000000)]
lst_gen = list(random() for j in range(1000000))

print(len(lst_com))
print(len(lst_gen))

print("List Comprehension")
timer1 = Timer("lst_com = [random() for j in range(1000000)]","from random import random")
print("time", timer1.timeit(number=10))
print("List function applied to generator")
timer2 = Timer("lst_gen = list(random() for j in range(1000000))","from random import random")
print("time", timer2.timeit(number=10))