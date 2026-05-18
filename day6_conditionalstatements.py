#check whether the number is postive or negative
'''n=int(input())
if n>0:
    print("Positive")
else:
    print("Negative")'''
#check whether the person is eligible for vote or not
'''age =int(input())
if age >= 18:
    print(" the person is eligible")
else:
    print(" the person is not eligible")'''
#find weather the number is even or odd:
'''num=int(input())
if num%2==0:
    print("number is even")
else:
    print("number is odd")'''
'''if num&1==0:
    print("even")
esle:
    print("odd")'''
'''if num%2:
    print("odd")
else:
    print("even")'''
#check if  number is divisible by 3 or not
'''num=int(input())
if num%3==0:
    print("number is divisible by 3")
else:
    print("number is not divisible by 3")'''
'''if num%3:
    print("number is not divisible by 3")
else:
    print("number is divisible by 3")'''
#check the number is divisible by both 3 and 5
num=int(input())
'''if num%3 or num%5:
    print("Buzz")
else:
    print("Fizz Buzz")'''
'''if num%3==0 and num%5==0:
    print("Fizz Buzz")
else:
    print("Buzz")'''
#check wether the num is positive , negative or zero
'''if num==0:
    print("number is zero")
elif num>0:
    print("number is postive")
else:
    print("number is negative")'''
#check number is divisible by 3 , 5 , 3and 5
'''if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("invalid")'''
#check the number is +ve even , +ve odd, -ve even, -ve odd
'''if num>=0 and num%2:
    print("positive odd")
elif num>=0 and num%2==0:
    print("positive even")
elif num<0 and num%2:
    print("negative odd")
else:
    print("negavtive even")'''
if num>=0:
    if num%2:
        print("positive odd")
    else:
        print("positive even")
else:
    if num%2:
        print("negative odd")
    else:
        print("negative even")
