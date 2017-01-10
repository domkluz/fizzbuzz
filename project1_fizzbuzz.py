
# Requirements:
# if divisible by 3 then Fizz
# if by 5 then buzz
#if divisible by 3 and 5 then Fizz and Buzz
# set an upper limit for n so lets say 200
#"Fizz buzz counting up to 200"
# Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.


import sys

print("The name of this script is {}".format(sys.argv))
print("User supplied {} arguments at run time".format(len(sys.argv)))

upperlimit=""

for upperlimit in sys.argv[1:]:
    print(upperlimit)

if upperlimit =="":
    upperlimit = input("Enter the number you would like to count to...")

print("fizz buzz counting to {}".format(upperlimit))

count=1
upperlimit=int(upperlimit)

while count != (upperlimit+1):
    if count%3==0 and count%5==0:
        print("FizzBuzz")
    elif count%3==0:
        print("Fizz")
    elif count%5==0:
        print("Buzz")
    else:
        print(count)
    count += 1
