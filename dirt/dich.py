#import numpy as np
#import pandas as pd
import math

K1 = (3 - math.sqrt(5)) / 2
K2 = (math.sqrt(5) - 1) / 2
K3 = (1 + math.sqrt(5)) / 2

f = lambda x: (x - 8) ** 2

def FindFib(value):
    a = 1
    b = 1
    c = a + b
    while (c < value):
        v = c
        a = b
        b = v
        c = b + a
    return c, a

def GoldenRatioMethod(eps = 10 ** (-7), a0 = -2.0, b0 = 20.0):
    x1, x2, xm, a, b = [], [], [], [], []
    a.append(a0)
    b.append(b0)
    x1.append(a0 + K1 * (b0 - a0))
    x2.append(a0 + K2 * (b0 - a0))
    xm.append(0)
    n = 1
    while (abs(b[n - 1] - a[n - 1]) > eps):
        if (f(x1[n - 1]) <= f(x2[n - 1])):
            a.append(a[n - 1])
            b.append(x2[n - 1])
            x2.append(x1[n - 1])
            x1.append(a[n] + b[n] - x1[n - 1])
            xm.append(x1[n - 1])
        else:
            a.append(x1[n - 1])
            b.append(b[n - 1])
            x1.append(x2[n - 1])
            x2.append(a[n] + b[n] - x2[n - 1])
            xm.append(x2[n - 1])
        n += 1
    return ('{:.7e}'.format(8 - xm[n - 1]))
    #print (len(a), len(b), len(x1), len(x2))

def DichotomyMethod(eps = 10**(-7), a0 = -2.0, b0 = 20.0):
    a, b, x1, x2 = [], [], [], []
    a.append(a0)
    b.append(b0)
    x1.append((a0 + b0 - eps / 2) / 2)
    x2.append((a0 + b0 + eps / 2) / 2)
    n = 1
    while (abs(b[n - 1] - a[n - 1]) > eps):
        if (f(x1[n - 1]) <= f(x2[n - 1])):
            a.append(a[n - 1])
            b.append(x2[n - 1])
        else:
            a.append(x1[n - 1])
            b.append(b[n - 1])
        x1.append((a[n] + b[n] - eps / 2) / 2)
        x2.append((a[n] + b[n] + eps / 2) / 2)
        n += 1
    return ('{:.7e}'.format(8 - (x1[n - 1] + x2[n - 1]) / 2))

def FibonachiMethod(eps = 10 ** (-7), a0 = -2.0, b0 = 20.0):
    fn2, fn0 = FindFib((b0 - a0) / eps)
    a, b, x1, x2, xm = [], [], [], [], []
    a.append(a0)
    b.append(b0)
    x1.append(a[0] + (b[0] - a[0]) * fn0 / fn2)
    x2.append(a[0] + b[0] - x1[0])
    xm.append(0)
    n = 0
    while (abs(b[n] - a[n]) > eps):
        if (f(x1[n]) <= f(x2[n])):
            a.append(a[n])
            b.append(x2[n])
            x2.append(x1[n])
            x1.append(a[n + 1] + b[n + 1] - x1[n])
            xm.append(x1[n])
        else:
            a.append(x1[n])
            b.append(b[n])
            x1.append(x2[n])
            x2.append(a[n + 1] + b[n + 1] - x2[n])
            xm.append(x2[n])
        n += 1
    #print (len(a), len(b), len(x1), len(x2))
    print (n)
    return ('{:.7e}'.format(8 - (xm[n])))

def FindMinimum(a0 = -2.0, b0 = 20.0):
    k = 0
    x = []
    x.append(a0)
    h = 0
    delt = 10 ** (-8)
    if (f(x[0]) > f(x[0] + delt)):
        k += 1
        x.append(x[0] + delt)
        h = delt
    elif (f(x[0]) < f(x[0] + delt)):
        k += 1
        x.append(x[0] - delt)
        h = -delt
    else:
        print ("Govno kakoe-to")
        exit
    
    flag = True
    while (flag):
        h *= 2
        x.append(x[k] + h)
        if (f(x[k]) > f(x[k + 1])):
            k += 1
        else:
            flag = False
            print ('[', x[k - 2], ';', x[k], ']')




FindMinimum()
#DichotomyMethod()
#GoldenRatioMethod()
#print (GoldenRatioMethod(10 ** (-5)))
#FibonachiMethod()
#arrEps = [10 ** (-i) for i in range(1, 8)]
#for epsi in arrEps:
#    print (math.log10(epsi), FibonachiMethod(epsi))