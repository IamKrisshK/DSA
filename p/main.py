from parsearr import parser
from timer import Timer
from bubble import bubble_sort
from shaker import shaker_sort
a = parser()
t=Timer()
bs_res=shaker_sort(a)
t.timeit()
bs_res=bubble_sort(a)
t.timeit()
print(bs_res)
