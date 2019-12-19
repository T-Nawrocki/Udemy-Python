# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.

minimum = 0  # can change these values to alter valid range for calculator
maximum = 65535  # default max is 65535 ((2 ** 16) - 1)

# populates powers_of_2 with values up to maximum
powers_of_2 = []
i = 0
while (2 ** i) <= maximum:
    powers_of_2.append(2 ** i)
    i += 1
powers_of_2.reverse()  # sorts list from largest to smallest


# validates number input to only allow digits
def number_input():
    while True:
        try:
            user_input = int(input(f"Please enter a whole number between {minimum} and {maximum}: "))
        except ValueError:
            print("That's not a valid whole number. Please try again.")
        else:
            return user_input


decimal = number_input()
# validates number input against min/max values
while True:
    if decimal < minimum:
        print("That value is too small. Please try again.")
        decimal = number_input()
    elif decimal > maximum:
        print("That value is too large. Please try again.")
        decimal = number_input()
    else:
        break

remainder = decimal  # remainder is a working value to track remainder of number which hasn't been converted yet
answer = ""  # initialise answer string so we can append to it

for power in powers_of_2:
    if remainder // power > 0:
        answer += "1"
        remainder = remainder % power
    else:
        answer += "0"

for char in answer:  # strips leading 0
    if char == "0" and len(answer) > 1:  # need len(answer) > 1 to account for where the answer is 0
        answer = answer[1::]
    else:  # when you hit the first non-zero character, stop strippinɡ characters
        break

print(f"{decimal} in binary is {answer}")


