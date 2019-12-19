# Write a program to append the times tables to challenge.txt
# We want the tables from 2 to 12, similar to the output
# from the for loops part 2 lecture in section 6

# first column of numbers should be right justified

with open("../text-samples/challenge.txt", "a") as file:
    for i in range(2, 13):
        print("=" * 25, file=file)
        for j in range(1, 13):
            print(f"{j:>2} times {i:<2} is {i * j:<3}", file=file)
