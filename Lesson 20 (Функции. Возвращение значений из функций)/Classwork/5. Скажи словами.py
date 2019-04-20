def number_to_words(num: int):
    nums = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"}

    excep = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"}

    dec = {
        2: "twenty ",
        3: "thirty ",
        4: "forty ",
        5: "fifty ",
        6: "sixty ",
        7: "seventy ",
        8: "eighty ",
        9: "ninety "}

    if num in excep:
        return excep[num]

    if len(str(num)) >= 2 and str(num)[-1] == '0':
        return dec[num // 10][:-1]

    ret = ""

    ret += dec[num // 10 % 10] if len(str(num)) >= 2 and num >= 20 else ""
    ret += nums.get(num % 10, "")

    return ret


def number_in_english(number):
    ret = ""
    if len(str(number)) >= 3:
        ret += number_to_words(number // 100 % 10) + " hundred"

        if str(number)[1:] and number % 100 != 0:
            ret += " and " + number_to_words(int(str(number)[1:]))

    else:
        ret = number_to_words(number)
    return ret

