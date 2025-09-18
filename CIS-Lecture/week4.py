


'''
#print numbers from 1..10
number=1

while number<=10:
    print(number)
    number+=1
'''
#print even numbers from 1..10
'''
number=2
while number<=10:
    print(number)
    number+=2
'''
'''
number=1
while number<=10:
    if number%2==0:
        print(number)
    number+=1
'''
'''
#print all odd numbers between 5 and some
#number entered by user

number = int(input("Enter a number:"))
while number >= 5:
    if number % 2 == 1:
        print(number)
    number -= 1
while number <= 5:
    if number % 2 == 1:
        print(number)
    number += 1

'''
'''
#write a program that adds numbers until the user says stop

total = 0

user_number= int(input("Enter a number or type s to end:"))

while user_number != 's':
    total += int(user_number)
    user_number = input("Enter a number or type s to end:")

print("The total is:", total)
'''

