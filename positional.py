#basic positional argument
def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,5)
print("sum=",result)

#student information
def student_info(name,roll,mark):
    print("name",name)
    print("roll no:",roll)
    print("mark:",mark)
student_info("ravi",101,85)

#simple interest
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest:",si)
simple_interest(10000,2,3)
simple_interest(5000,1.2,3)

#area of circle
def ar_circle(r):
   ar_circle=3.14*r*r
   print("area of circle:",ar_circle)
ar_circle(1.5)
ar_circle(4)

#check number positive negative or zero
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
check_value(0)
check_value(90)
check_value(-45)

#odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
odd_even(50)
odd_even(23)

#arithmatic operation substraction
#multiplication and division
def addition(a,b):
    add=a+b
    print("addition of two values:",add)
addition(69,11.5)
addition(100,600)