def square_digits(num):
    result = ''
    for x in str(num):
        result += str(int(x)*int(x))
    return int(result)


print(square_digits(9119))