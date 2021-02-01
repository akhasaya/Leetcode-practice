# returns true if one digit in the number is the sum of rest of the digits
def sol(number):
    number = abs(number)
    if number == 0:
        return True

    digits = []
    while number > 0:
        digits.append(number % 10)
        number = number / 10

    sum_d = sum(digits)
    if sum_d % 2 == 0 and sum_d / 2 < 10 and sum_d / 2 in digits:
        return True

    return False

a = 32922
print(str(a)+" "+str(sol(a)))