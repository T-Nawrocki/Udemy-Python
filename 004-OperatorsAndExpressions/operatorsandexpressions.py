# containing material from lectures 23, 24 and 25

a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0 (float division)
print(a // b)  # 4 (integer division, rounded down)
print(a % b)  # 0 (modulo)

print()
for i in range(1, 4):  # range includes lower bound but not upper
    print(i)

print()
for i in range(1, a // b):  # must use // here because / would give float result, and can't mix int and float for range
    print(i)

# expressions are anything which can be evaluated to a single value
# so a + b is an expression
# similarly, any literal is an expression
# range(1, a // b) is an expression which contains two other expressions
# variables are also expressions, because they can be evaluated to their bound values
# however, the a and b on lines 3 and 4 are not expressions, because they are being bound to their values
# an expression cannot appear on the left of a binding
# similarly, i is an expression on line 15, but not line 14

print()
#################################

# OPERATOR PRECEDENCE

# BODMAS applies as you'd expect
print(a + b / 3 - 4 * 12)  # -35.0
print(((a + b) / 3 - 4) * 12)  # 12.0 (can use brackets freely as you'd expect)

c = a + b
d = c / 3
e = d - 4
print(e * 12)  # 12.0 (sometimes it'd make sense to break the expression up by binding variables to intermediate values

# remember that /* and +- have equal precedence, and so are evaluated from left to right
print(a / (b * a) / b)  # 0.111...


