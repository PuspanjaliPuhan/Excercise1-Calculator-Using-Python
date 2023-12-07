#Simple calculator
# This uses Pre-Defined value to Calculate.
#First code are just simply used operator's 
x=33
y=77
a=x+y
b=x-y
c=x*y
d=x/y
e=x//y
f=x%y
g=x^y
print('The value of',x,'+',y,'is',a)
print('The value of',x,'-',y,'is',b)
print('The value of',x,'*',y,'is',c)
print('The value of',x,'/',y,'is',d)
print('The value is',x,'//',y,'is',e)
print('The value of',x,'%',y,'is',f)
print('The value of',x,'^',y,'is',g)

#This one is Using function 
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if x!=0:
      return x/y
    else:
        print('It cannot be divived')

print('Addition', add(x,y))
print('Substraction',substract(x,y))
print('Multiplication', multiplication(x,y))
print('Division',division(x,y))

    
