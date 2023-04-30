x = 'banana'
y = max(x)
z = y * 2

def stuff():
    print('Hello')
    return
    print('World')

stuff()

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print(p)
