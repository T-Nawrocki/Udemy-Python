# contains material from lecture 36

# f strings are a new way to format values in a string
# however, there's no plans to back-port them to versions earlier than python 3.6, so they're not heavily used yet
# you might want to avoid if you're possibly gonna be working with an older version of python at all

age = 26
print(f"I am {age} years old")  # f before the string lets you use variables in {} like a replacement field

# all the other formatting things we looked at in stringreplacementfields.py still apply here
print(f"Pi is approximately {22/7:12.50f}")

# so f-strings are much neater than replacement fields, but aren't fully supported by older versions
