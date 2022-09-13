def add_numbers(first, second):
    total = first + second
    return total


def add_numbers_2(first, second):
    total = first + second
    print('In the function:', total)
    return total


a = 20
c = 120
d = 200
y = 50
b = 30
x = 40

n = add_numbers(a, b)
print('result:', n)

result = add_numbers_2(c, d)
print('result:', result)