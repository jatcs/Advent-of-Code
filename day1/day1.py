def attempt1():
    # get numbers from text file
    number_file = open('numbers.txt', 'r')
    # check each number
    for number_string in number_file:
    # print('Current outer number:', number_string)
    # pair with each other number
        for number_string_2 in number_file:
            # print('Current inner number', number_string_2)
            # print('Current sum =', int(number_string.strip()) + int(number_string_2.strip()))
            if int(number_string.strip()) + int(number_string_2.strip()) == 2020:
                print('Found numbers:', number_string, number_string_2)
                product = int(number_string.strip()) * int(number_string_2.strip())
                print('Product = {}'.format(product))
    number_file.close()

number_file = open('numbers.txt', 'r')
numbers_list = number_file.read().split()
number_file.close()
# print(numbers_list)

for num1 in numbers_list:
    for num2 in numbers_list:
        if int(num1) + int(num2) == 2020:
            sum = int(num1) + int(num2)
            product = int(num1) * int(num2)
            print('Sum Check: {} + {} = {}'.format(num1, num2, sum))
            print('Product: {} * {} = {}'.format(num1, num2, product))


