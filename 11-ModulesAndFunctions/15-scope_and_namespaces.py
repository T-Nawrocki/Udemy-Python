# python has no concept of "private variables/functions"—you have to rely on the underscore-before-name convention
# to mark things which are not supposed to be externally accessed

# you can nest functions within functions with python, which has some impact on scope
# this could be useful for initialisation before a "recursive function call"
# a recursive function is a function which calls itself
# they can be useful for handling structures which can contain themselves (eg directories within a computer file system
# or handling recursive mathematical functions—like factorials)


def iterative_factorial(n):
    """calculates n! iteratively"""
    # this is a docstring—a comment which documents the purpose of functions, classes, etc

    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def recursive_factorial(n):
    """calculates n! recursively"""
    # the iterative version of this might be the most efficient way of calculating factorials,
    # but factorials are also a good way to demonstrate recursion
    # this is because n! = n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


for i in range(26):
    print(f"{i}! = {iterative_factorial(i)}")

print("=" * 40)

for i in range(26):
    print(f"{i}! = {recursive_factorial(i)}")

# ========================================
print("=" * 40)
# ========================================


# The fibonacci sequence is another recursive mathematical function
def fibonacci(n):
    """calculates and returns the fibonacci sequence from t0 up to tn"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# you'll notice this is INCREDIBLY inefficient—it slows right down very quickly
# this is because we're calling the whole function twice for each term,
# which means we're doing the calculations exponentially many times for each term of the sequence
for i in range(33):
    print(f"t{i} = {fibonacci(i)}")

print("=" * 40)


def efficient_fibonacci(n):
    """a more efficient fibonacci sequence, without using recursion"""
    if n < 2:
        result = n
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for f in range(1, n):
            result = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = result
    return result


for i in range(33):
    print(f"t{i} = {efficient_fibonacci(i)}")
