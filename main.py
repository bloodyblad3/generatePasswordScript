import random
import sys

chrs = [chr(code) for code in range(ord('a'), ord('z') + 1)]
capitalize_chrs = [chr.capitalize() for chr in chrs]
nums = [str(digit) for digit in range(10)]
spec_chrs = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "/", ":", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "}", "~"]


def to_binary(num: int):
    s = ""
    while num != 0:
        s = str(num%2) + s
        num //= 2
    return s