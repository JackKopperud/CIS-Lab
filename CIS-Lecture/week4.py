


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

def get_season(month, day):
    # Dictionary of months with their number and days in each month
    months ='january': {'num': 1, 'days': 31}, 'february': {'num': 2, 'days': 29},  # Including leap year possibility'march': {'num': 3, 'days': 31},'april': {'num': 4, 'days': 30},'may': {'num': 5, 'days': 31},'june': {'num': 6, 'days': 30},'july': {'num': 7, 'days': 31},'august': {'num': 8, 'days': 31},'september': {'num': 9, 'days': 30},'october': {'num': 10, 'days': 31},'november': {'num': 11, 'days': 30},'december': {'num': 12, 'days': 31}
    
    
    # Check if month is valid
    if month_lower not in months:
        return "Invalid"
    
    # Check if day is valid for the given month
    if day < 1 or day > months[month_lower]['days']:
        return "Invalid"
    
    # Get month number
    month_num = months[month_lower]['num']
    
    # Determine season based on month and day
    if (month_num == 3 and day >= 20) or (month_num == 4) or (month_num == 5) or (month_num == 6 and day <= 20):
        return "Spring"
    elif (month_num == 6 and day >= 21) or (month_num == 7) or (month_num == 8) or (month_num == 9 and day <= 21):
        return "Summer"
    elif (month_num == 9 and day >= 22) or (month_num == 10) or (month_num == 11) or (month_num == 12 and day <= 20):
        return "Autumn"
    else:
        return "Winter"

# Get input from user
month_input = input().strip()
try:
    day_input = int(input().strip())
except ValueError:
    day_input = -1  # Invalid day if not an integer

# Get and print the season
result = get_season(month_input, day_input)
print(result)