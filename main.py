import random
import sys

chrs = [chr(code) for code in range(ord('a'), ord('z') + 1)]
capitalize_chrs = [chr.capitalize() for chr in chrs]
nums = [str(digit) for digit in range(10)]
spec_chrs = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "/", ":", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "}", "~"]

chrs_half_len = len(chrs) // 2

def to_binary(num: int):
    s = ""
    while num != 0:
        s = str(num%2) + s
        num //= 2
    return s

def hard(length: int = 8, possible_words: str = None):
    characters = chrs[:chrs_half_len] + nums
    password = [random.choice(characters) for i in range(length)]
    for index, letter in enumerate(password):
        if letter.isalpha():
            password[index] = letter.upper()
            return "".join(password)

def strong(length: int = 12):
    characters = chrs[:chrs_half_len] + capitalize_chrs[chrs_half_len:] + nums
    password = [random.choice(characters) for i in range(length)]
    return "".join(password)

def strongest(length: int = 16):
    characters = chrs[:chrs_half_len] + capitalize_chrs[chrs_half_len:] + spec_chrs + nums
    password = []
    while len(password) < int(length):
        char = str(random.choice(characters))
        if char.isdigit():
            char = to_binary(int(char))
            password.append(char)
        else:
            password.append(char)
    return "".join(password)
