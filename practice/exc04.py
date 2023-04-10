
x= 2
if x<2 :
    print('Below 2')
elif x >= 2 :
    print('Two or more')
else :
    print('Something else')


hrs = input("Enter Hours:")
hours = float(hrs)
rate = input("Enter the Rate:")
x = float(rate)
if hours <= 40:
    print( hours  * x)
elif hours > 40:
    print(40* x + (hours-40)*x*1.5)
