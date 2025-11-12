def is_armstrong(num):
    n=len(str(num))
    sum_of_powers=0
    for digit in str(num):
        sum_of_powers+=int(digit)**n
    return num==sum_of_powers
