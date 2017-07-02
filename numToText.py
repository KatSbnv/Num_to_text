# coding=utf-8
# 321
# единицы 1
# десятки 2
# сотни 3

# 321 -> "триста двадцать один"

# 123 % 10 = 3 (3  единицы)
# (123 - 3) = 120 / 10 = 12 % 10 = 2 (2 десятки)


#######################

UNITS = [" ", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать",
         "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
         "восемьнадцать", "девятнадцать"]
TENS = [" ", "десять", "двадцать","тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
HUNDREDS = [" ", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

number = int(input("Ваше число: "))

def transform_group(number):
    units = number % 10                 #находим единицы
    tens = ((number - units) / 10) % 10  #находим десятки
    hundreds = number / 100              #находим сотни

    result = HUNDREDS[hundreds] + " "

    if tens == 1:
        result += UNITS[10 + units]
    else:
        result += TENS[tens] + " " + UNITS[units]
    return result


def transform(input):
    if input > 1000000:
        print "TOO LARGE"
        return

    # input = 321456
    # group_1 = 321456 % 1000 = 456

    group_1 = input % 1000  # 456
    group_2 = ((input - group_1) / 1000) % 1000  # 321

    result = transform_group(group_1)

    if group_2 > 0:
        result = transform_group(group_2) + " тысяч " + result

    print result


transform (number)