import math

K1 = 0.3819660112501051
K2 = 0.6180339887498949

def FormBine(n) -> int:
    return (int((0.5 * (1 + math.sqrt(5))) ** n / math.sqrt(5)) if n >= 40 else
    int(((0.5 * (1 + math.sqrt(5))) ** n - (0.5 * (1 - math.sqrt(5))) ** n) / math.sqrt(5)))

f = lambda x: (x - 7) ** 2

def FindFib(value):
    counter = 0
    a = 1
    b = 1
    c = a + b
    while (c < value):
        v = c
        a = b
        b = v
        c = b + a
        counter += 1
    return counter

def GoldenRatioMethod(eps = 1e-7, a0 = -2.0, b0 = 20.0):

    x1, x2, fx1, fx2, a, b = [], [], [], [], [], []
    fCount = 0
    # step 0
    n = 0
    a.append(a0)
    b.append(b0)
    x1.append(a0 + K1 * (b0 - a0))
    x2.append(a0 + K2 * (b0 - a0))
    fx1.append(f(x1[0]))
    fx2.append(f(x2[0]))
    fCount += 2
    # step 1+
    while True:
        n += 1
        if fx1[-1] <= fx2[-1]:
            a.append(a[-1])
            b.append(x2[-1])
            x2.append(x1[-1])
            x1.append(a[-1] + K1 * (b[-1] - a[-1]))
            fx2.append(fx1[-1])
            fx1.append(f(x1[-1]))
        else:
            a.append(x1[-1])
            b.append(b[-1])
            x1.append(x2[-1])
            x2.append(a[-1] + K2 * (b[-1] - a[-1]))
            fx1.append(fx2[-1])
            fx2.append(f(x2[-1]))
        fCount += 1
        #print (n, '{:.8e}'.format(fx2[-1]), '{:.8e}'.format(fx1[-1]), '{:.8e}'.format(b[-1]), '{:.8e}'.format(a[-1]), '{:.8e}'.format(b[-1] - a[-1]), logi)
        if abs(b[-1] - a[-1]) <= eps:
            #print ("X_min = {:.7e}".format(0.5 * (x1[-1] + x2[-1])))
            #print ("Functions called:", fCount)
            return fCount

def DichotomyMethod(eps = 1e-7, a0 = -2.0, b0 = 20.0):
    a, b, x1, x2 = [], [], [], []
    fCount = 0
    a.append(a0)
    b.append(b0)
    x1.append((a0 + b0 - eps / 2) / 2)
    x2.append((a0 + b0 + eps / 2) / 2)
    n = 1
    while abs(b[-1] - a[-1]) > eps:
        if f(x1[-1]) <= f(x2[-1]):
            a.append(a[-1])
            b.append(x2[-1])
        else:
            a.append(x1[-1])
            b.append(b[-1])
        fCount += 2
        x1.append((a[-1] + b[-1] - eps / 2) / 2)
        x2.append((a[-1] + b[-1] + eps / 2) / 2)
        #print (n, '{:.7e}'.format((x1[-1] + x2[-1]) / 2.0))
        n += 1
    #print ("X_min = {:.7e}".format(0.5 * (x1[-1] + x2[-1])))
    #print ("Functions called:", fCount)
    arr = []
    arr.append()
    return fCount

def FibonachiMethod(isReturn, eps = 1e-7, a0 = -2.0, b0 = 20.0):
    fCount = 0
    a, b, x1, x2, fx1, fx2 = [], [], [], [], [], []
    delt = b0 - a0
    n2 = FindFib(delt / eps)
    Fn2 = FormBine(n2)
    
    # step 0
    i = 0
    a.append(a0)
    b.append(b0)
    x1.append(a[0] + (b[0] - a[0]) * FormBine(n2 - 2) / Fn2)
    x2.append(a[0] + b[0] - x1[0])
    fx1.append(f(x1[0]))
    fx2.append(f(x2[0]))
    fCount += 2
    # step i
    while True:
        i += 1
        if fx1[-1] <= fx2[-1]:
            a.append(a[-1])
            b.append(x2[-1])
            x2.append(x1[-1])
            x1.append(a[-1] + delt * FormBine(n2 - i - 1) / Fn2)
            fx2.append(fx1[-1])
            fx1.append(f(x1[-1]))
        else:
            a.append(x1[-1])
            b.append(b[-1])
            x1.append(x2[-1])
            x2.append(a[-1] + delt * FormBine(n2 - i) / Fn2)
            fx1.append(fx2[-1])
            fx2.append(f(x2[-1]))
        #print (i, '{:.8e}'.format(fx2[-1]), '{:.8e}'.format(fx1[-1]), '{:.8e}'.format(b[-1]), '{:.8e}'.format(a[-1]), '{:.8e}'.format(b[-1] - a[-1]))
        fCount += 1
        if abs(b[-1] - a[-1]) <= eps:
            return fCount

def FindMinimum(a0 = -2.0):
    x = []
    x.append(a0)
    h = 0
    delt = 1e-1
    if f(x[0]) > f(x[0] + delt):
        x.append(x[0] + delt)
        h = delt
    elif f(x[0]) < f(x[0] + delt):
        x.append(x[0] - delt)
        h = -delt
    else:
        print ("Govno kakoe-to")
        exit
    
    k = 1
    while (True):
        h *= 2
        x.append(x[-1] + h)
        if f(x[-2]) > f(x[-1]):
            k += 1
        else:
            print ("[{:.7f}; {:.7f}]".format(x[-3], x[-1]))
            break

def Graph():
    nDich, nGold, nFibn = [], [], []
    currEps = 1e-1
    while currEps >= 1e-7:
        nDich.append(DichotomyMethod(currEps))
        nGold.append(GoldenRatioMethod(currEps))
        nFibn.append(FibonachiMethod(currEps))
        currEps /= 10.
    print (nDich)
    print (nGold)
    print (nFibn)






#Graph()
#FindMinimum()
DichotomyMethod()
#GoldenRatioMethod()
#print (GoldenRatioMethod(10 ** (-5)))
#FibonachiMethod()
#arrEps = [10 ** (-i) for i in range(1, 8)]
#for epsi in arrEps:
#    print (math.log10(epsi), FibonachiMethod(epsi))