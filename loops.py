"i will show you how to use loops"

#a loop is a function which allows you to repeat that samething again and again
#there are two types of loops.

#- a "for" loop is used if you want to repeat a certain amount of TimeoutError
#- a "while" loop is repeating stuff aslong as the statement is true

#example "for" loop

for i in range(10):
    print(i) 


#this would print all number 0 to 10
#in any programming language you start counting with zero

#example for a while loop

while True:
    print("This is an example")


#this would print "This is an example" forever

#to break out of a loop we can use the keyword "break"

#example for "break"


IsRunning = True
Runs = 0

while IsRunning:
    Runs += 1 # this adds one to the current number
    if Runs > 10:
        break

#if the number is larger than 10 the loop will stop

# we can also use loops to go through lists or dicts
# we use for loops to do that

ExampleList = ["bananas", "mangos", "apples"]

# there are two ways to loop though list
# you can loop directly through it or you can used an "index"

for fruit in ExampleList:
    print(fruit)
# this will print the fruits

for i in range(len(ExampleList)): # len is a function from python which returns the amount of items in that list
    print(i + ". " + ExampleList[i])
# this will print the fruits and in which postition in the list it is