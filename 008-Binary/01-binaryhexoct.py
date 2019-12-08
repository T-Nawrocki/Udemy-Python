# lecture 64 & 65

# BINARY VALUES TABLE

# 256 128  64  32  16   8   4   2   1        Decimal
#   8   7   6   5   4   3   2   1   0        Power of 2
# ===================================        Decimal Value
#       0   0   0   0   0   0   0   0        0
#       0   0   0   0   0   0   0   1        1
#       0   0   1   0   1   1   1   1        47
#       1   1   1   1   1   1   1   1        255
#   1   0   0   0   0   0   0   0   0        256

for i in range(17):
    print(f"{i:>2} in binary is {i:>08b}")
# >2 spaces first field with 2 characters
# >08 spaces second field to 8 chars, and includes leading 0s
# b formats as binary

# 0b designates value as binary
n = 0b01101011
print(n)

# ===========================================

# each binary byte (8 bits) can be represented by only two hex digits
for i in range(256):
    print(f"{i:>2} in hex is {i:>02x}")  # note x to format in hex, not h

x = 0x20  # 0x prefix designates value as hex
y = 0x0a
print(hex(x * y))  # hex() changes decimal value to hex

# ============================================

# octal is very rare these days
# linux file permissions are one of the only cases where it's still used

