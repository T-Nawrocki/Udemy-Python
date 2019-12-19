# there's two main reasons why we might want to read/write binary files:
# 1. we want to handle binary data, like an image file
# 2. we want to store the variables in our program so they can be reloaded later

# basic principles of reading/writing text files still apply here
# although strings and integers cannot be directly written to a binary file
# they first need to be converted to bytes
with open("../text-samples/binary", "bw") as bin_file:  # note no file extension,
    # and that "bw" is used to specify binary not text
    for i in range(17):
        bin_file.write(bytes([i]))  # converts i to bytes.
        # need to pass a list. If you pass an integer, bytes() creates a byte sequence with that many bytes
        # when you pass a list, it properly creates a representation of the entries of the list as bytes

with open("../text-samples/binary", "ba") as bin_file:
    bin_file.write(bytes(range(17, 33)))  # can skip the for loop by just writing with
    # a range—bytes can take range as an argument because they're a sequence

with open("../text-samples/binary", "br") as bin_file:
    for b in bin_file:
        print(b)
        # output shows in hex, because that's how the binary data is stored (i think)
        # 9 is shown as \t and 10 as \n because those are (for some reason) the conventional way of showing
        # those numbers in hex (also d (13) is shown as \r)
        # basically, these characters have other purposes within the operating system, so they're represented
        # with those purposes (as if you try to read the contents of the file from your command line, you'll
        # get whatever the extra purpose is—tab, new line, or whatever else)

# bytes() returns a byte object, which is an immutable version of a byte array, whcih we'll get to later
# essentially, though, it's just a sequence of integers in the range 0-255 (a sequence of bytes)

a = 65534  # hex FF FE
b = 65535  # hex FF FF
c = 65536  # hex 00 01 00 00
x = 2998302  # hex 00 2D C0 1E

with open("../text-samples/binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))  # to_bytes() automatically converts to bytes
    bin_file.write(b.to_bytes(2, "big"))  # first argument is number of bytes to convert to
    bin_file.write(c.to_bytes(4, "big"))  # second argument is the "byte size", which determines if the result is
    bin_file.write(x.to_bytes(4, "big"))   # returned as "big endian" or "little endian"
    bin_file.write(x.to_bytes(4, "little"))
    # big indian stores most significant byte first, followed by the others in order (ie like you'd write it)
    # little indian stores the least significant byte first and then goes backwards in sequence
    # originally, this was a distinction from computer engineers and was largely arbitrary
    # (ibm chose big endian, intel chose little endian, etc)
    # however now the decision's made, it is maintained for backwards compatibility

with open("../text-samples/binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")  # converts bytes to int,
    f = int.from_bytes(bin_file.read(2), "big")  # using filename.read(number of bytes), "endianness"
    g = int.from_bytes(bin_file.read(4), "big")
    h = int.from_bytes(bin_file.read(4), "big")
    i = int.from_bytes(bin_file.read(4), "big")  # deliberately reading little-endian as big-endian
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)  # note different output to what we input; this is because we're reading in the opposite direction
    # to how we wrote in the first place—must be consistent or you'll break things.

