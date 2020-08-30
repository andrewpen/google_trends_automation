def hello(name):
    print('Hello ' + name)

hello('Andrew')
hello('Elijah')

def plusOne(number):
    return number + 1

newNumber = input()
newNumber = int(newNumber)
newNumber = plusOne(newNumber)
print(newNumber)