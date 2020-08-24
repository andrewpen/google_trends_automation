import random
num = random.randint(1,10)
print(num)


# This program says hello and asks for my name

print ('Hello World')
print ('What is your name?')
myName = input()
print ('It is good to meet you, ' + myName)

if myName == 'Andrew' :
    print('Success!')


print ('The length of your name is: ')
print (len(myName))
print ('What is your age?') 
myAge = input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')

var = 0
while var < 5:
    print('Hello World')
    var = var + 1
