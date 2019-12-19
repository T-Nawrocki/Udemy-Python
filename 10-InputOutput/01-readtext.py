file_path = "../text-samples/jabberwocky.txt"

# if file can't be found in path, will give an error
# unless we trap the error and close the file before doing anything more (more on this later)
jabberwocky = open(file_path, "r")  # opens the text file for reading ("r" declares read only)

# can iterate through lines of a file as though it were a list
for line in jabberwocky:
    # can also select which lines to manipulate as you'd expect
    if "jabberwock" in line.lower():
        print(line, end="")  # use end="" because the lines already end with a linebreak character, so don't need double

jabberwocky.close()  # closes the file. DO NOT FORGET THIS, or you can corrupt the file or get performance errors etc

# =============================================
print("=" * 50)

# with keyword can be used to keep everything tidy automatically
# ie no need to explicitly close the file
# note that with x as y binds x to the variable y
# additional benefit of this is that there's no error raised if the file can't be found
# or rather the error will be trapped and the file will be closed before the program is terminated.
with open(file_path, "r") as jabberwocky:
    for line in jabberwocky:
        if "jab" in line.lower():
            print(line, end="")

# ============================================
print("=" * 50)

with open(file_path, "r") as jabberwocky:
    line = jabberwocky.readline()  # explicitly reads the next (ie first) line of the text file
    # if there's no lines in the file, with keyword will trap the error and close the file,
    # so we don't get to the while loop at all.
    while line:
        print(line, end="")
        line = jabberwocky.readline()

# ============================================
print("=" * 50)

with open(file_path, "r") as jabberwocky:
    lines = jabberwocky.readlines()  # reads all lines of the file as a list
    # may not be the best option for large files, but has some other applications, eg indexing/slicing lines
print(lines)
for line in lines:
    print(line, end="")

# ============================================
print("=" * 50)

with open(file_path, "r") as jabberwocky:
    whole_text = jabberwocky.read()  # reads entire file as string
print(whole_text)