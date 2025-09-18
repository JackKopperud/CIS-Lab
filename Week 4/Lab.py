'''
# Question 1

larger_num = int(input("Enter the larger number: "))
smaller_num = int(input("Enter the smaller number: "))

num = 0
while larger_num > smaller_num:
    larger_num = larger_num / 2
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num}")
'''
'''
#Question 2

word = input("Enter a word: ")
result = ""
for i in range (1, len(word) - 1,2) :
    result += word[i]
    print(f"output = {result}")

'''
'''
#Question 3
for number in range(37,1050 + 1):
    if number % 2 == 0:
        print(number)

'''
'''
#Question 4

word = ""

while True:
    user_in = input("Enter a letter: ")
    if user_in == "done":
        break
    else:
        word += user_in

print(f"The final word is {word}")
'''

#Question 5

start = 50
end = 517
for i in range (start + 1, end + 1, 2):
    print(i)