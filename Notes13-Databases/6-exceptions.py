# Taking a break from databases to talk about exceptions.

# Exceptions are a type of runtime error—tht is to say, they are errors that occur while the
# program is running, which disrupt it and prevent it from running further. This is in contrast
# with compilation or syntax errors, which prevent the program being run at all.

# Examples of exceptions might include trying to create a database when there's no space on the
# disk, or trying to perform an operation on a component which no longer exists, or trying to
# perform an invalid operation on the wrong type of data.

# Exceptions can be HANDLED—ie, you can define what the program should do if it encounters that
# error. Unhandled exceptions will crash the program.

# There are a large number of built in exceptions, which can be found in the documentation.

# Exceptions are handled using try: x except: y syntax.
# Here's an example of handling a RecursionError, which throws when we have a recursive function
# that causes a stack overflow:


def factorial(n):
    if n <= 1:
        return 1
    elif n == 123:  # just adding this to throw another exception type
        return n / 0
    else:
        return n * factorial(n-1)


def try_factorial(n):
    try:
        print(factorial(n))
    except RecursionError:  # can just use except to handle any exception, or specify which exception to handle
        print("This program can't calculate factorials that high!")
    except ZeroDivisionError:  # can have multiple except clauses providing different responses to exceptions
        print("Why are you trying to divide by zero?")
    except (ReferenceError, NotImplementedError):
        print("These exceptions are just random ones that won't raise in this program, but are here to show "
              "that you can have one handler for multiple exceptions by using an except tuple clause.")



try_factorial(5)
try_factorial(500)
try_factorial(5000)
try_factorial(100)  # Note the exception throwing on the previous try_factorial call doesn't crash the program
try_factorial(123)
