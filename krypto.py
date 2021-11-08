# Das ist der Beginn einer wunderbaren Freundschaft <3
# test
#:D

def split10Bit(num: int) -> tuple:
    binary = bin(num)[2:].rjust(10, '0')
    return (int(binary[:5], 2), int(binary[5:], 2))

def concat5bit(first5bit: int, second5bit: int) -> int:
    return (first5bit<<5) | (second5bit)


def encrypt(s1: dict, s2: dict) -> list:
    key = int('0101010101', 2)
    text = int(input("Enter 10-bit clear text string: "), 2)
    text_per_round = []
    text_per_round.append(text)
    number_of_rounds: int = 5
    for _ in range(number_of_rounds):
        (first,second) = split10Bit(text)
        first_mapped = s1[first]
        second_mapped = s2[second]
        text = key ^ concat5bit(first_mapped,second_mapped)
        text_per_round.append(text)
    return text_per_round

def single_round_encrypt(s1: dict, s2: dict, text: int) -> int:
    key = int('0101010101', 2)
    (first,second) = split10Bit(text)
    first_mapped = s1[first]
    second_mapped = s2[second]
    new_text = key ^ concat5bit(first_mapped,second_mapped)
    return new_text


    


