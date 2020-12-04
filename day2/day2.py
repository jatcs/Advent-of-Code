def part_one():
    with open('passwords.txt','r') as the_file:
        valid_passwords_count = 0
        for row in the_file:
            # min and max (inclusive) number separated by -
            # character to check is the second thing in the list
            # (separated by space -> new term - exclude :)
            # actual password is last term
            row_list = row.split()
            print('Checking', row_list)
            min = int(row_list[0].split('-')[0])
            max = int(row_list[0].split('-')[1])
            character = row_list[1][0]
            password = row_list[2]
            character_count = 0
            for lil_char in password:
                if lil_char == character:
                    character_count += 1
            if min <= character_count <= max:
                valid_passwords_count += 1
                print('{} is valid since it has {} {}\'s which is within {} and {}'.\
                      format(password, character_count, character, min, max))

        print('There are {} valid passwords'.format(valid_passwords_count))

def part_two():
    with open('passwords.txt', 'r') as the_file:
        valid_passwords_count = 0
        for row in the_file:
            # positions separated by -
            # character to check is the second thing in the list
            # (separated by space -> new term - exclude :)
            # actual password is last term
            row_list = row.split()
            print('Checking', row_list)
            position_one = int(row_list[0].split('-')[0]) - 1
            position_two = int(row_list[0].split('-')[1]) - 1
            character = row_list[1][0]
            password = row_list[2]
            if position_one in range(len(password)) and position_two in range(len(password)):
                if (password[position_one] == character and password[position_two] != character):
                    valid_passwords_count += 1
                    print(row_list)
                    print('Password {} is valid because it has character {} at index {} and not {}'. \
                          format(password, character, position_one, position_two))

                elif (password[position_one] != character and password[position_two] == character):
                    valid_passwords_count += 1
                    print(row_list)
                    print('Password {} is valid because it has character {} at index {} and not{}'.\
                          format(password, character, position_two, position_one))

        print('There are {} valid passwords'.format(valid_passwords_count))


part_two()