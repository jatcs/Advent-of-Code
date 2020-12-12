### Day 4: Passport Processing ###

BIRTH_YEAR = 'byr'
ISSUE_YEAR = 'iyr'
EXPIRATION_DATE = 'eyr'
HEIGHT = 'hgt'
HAIR_COLOR = 'hcl'
EYE_COLOR = 'ecl'
PASSPORT_ID = 'pid'
COUNTRY_ID = 'cid'
VALUE_START_INDEX = 4  # after the field and colon
NUM_FIELDS = 8
SEPARATE_PASSPORTS = '\n\n\n'  # 3 because it's usually 2 but I added 1 in the join statement
SEPARATE_TERMS = '\n\n'  # usually 1, becomes 2 because of the 1 I added in the join


def part_1():
    with open('passport_data.txt', 'r') as data_file:
        # store the passports from the file
        data_list = '\n'.join(data_file.readlines()).split(SEPARATE_PASSPORTS)
        valid_passports_count = 0
        for term in data_list:
            term = term.split()
            fields_met_count = 0
            found_cid = False
            for little_term in term:
                if BIRTH_YEAR in little_term or ISSUE_YEAR in little_term \
                or EXPIRATION_DATE in little_term or HEIGHT in little_term \
                or HAIR_COLOR in little_term or EYE_COLOR in little_term\
                or PASSPORT_ID in little_term or COUNTRY_ID in little_term:
                    fields_met_count += 1
                    if COUNTRY_ID in little_term:
                        found_cid = True
            missed_cid_case = (fields_met_count == NUM_FIELDS - 1) and not found_cid
            if fields_met_count == NUM_FIELDS or missed_cid_case:
                valid_passports_count += 1
                print('Passport {} is valid'.format(term))
        print('There are {} valid passports in this data'.format(valid_passports_count))

# currently unsuccessful :/
def part_2():
    # add data validation (requirements for each field)
    ALLOWED_ECL = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']  # valid eye colors
    with open('passport_data.txt', 'r') as data_file:
        # store the passports from the file
        data_list = '\n'.join(data_file.readlines()).split(SEPARATE_PASSPORTS) # each passport's data
        valid_passports_count = 0
        for term in data_list:
            term = term.split()
            print('\nChecking Passport', term)
            fields_met_count = 0
            found_cid = False
            for little_term in term:
                print('\tChecking little term', little_term, '\tCurrent number of valid terms=', fields_met_count, '(Needs to be at least 7)')
                field_value = little_term[VALUE_START_INDEX: len(little_term)]
                # this could likely all be one if statement (difficult because data type validation)
                # but its neater to break it up into multiple lines
                if BIRTH_YEAR in little_term:
                    print('\t\tChecking Birth Year term', field_value)
                    if field_value.isnumeric():
                        if len(field_value) == 4 and 1920 <= int(field_value) <= 2002:
                            print('\t\t\tValid birth year')
                            fields_met_count += 1
                        else:
                            print('\t\t\tInvalid birth year (birth year not in range)')
                    else:
                        print('\t\t\tInvalid birth year (birth year must be a number)')
                elif ISSUE_YEAR in little_term:
                    print('\t\tChecking the Issue Year term', field_value)
                    if field_value.isnumeric():
                        if len(field_value) == 4 and 2010 <= int(field_value) <= 2020:
                            print('\t\t\tValid Issue year (its a number with the correct length and its within range)')
                            fields_met_count += 1
                        else:
                            print('\t\t\tInvalid issue year {}(its a number'
                                  ' with the wrong length and/or not within range)')
                    else:
                        print('\t\t\tInvalid issue year {} (issue year must be a number)')
                elif EXPIRATION_DATE in little_term:
                    print('\t\tChecking the Expiration date term', field_value)
                    if field_value.isnumeric():
                        if len(field_value) == 4 and 2020 <= int(field_value) <= 2030:
                            print('\t\t\tValid Expiration date')
                            fields_met_count += 1
                        else:
                            print('\t\t\tInvalid Expiration date (wrong length or value range)')
                elif HEIGHT in little_term:
                    print('\t\tChecking the Height term', field_value)
                    if len(field_value) > 2:
                        field_number = int(field_value[0:-2])  # exclude the units cm or in
                        if (('cm' in field_value and 150 <= field_number <= 193)
                                or ('in' in field_value and 59 <= field_number <= 76)):
                            print('\t\t\tValid height')
                            fields_met_count += 1
                        else:
                            print('\t\t\tInvalid height (missed cm or in condition)')
                    else:
                        print('\t\t\tInvalid height (not long enough to hold number and units)')
                elif HAIR_COLOR in little_term:
                    print('\t\tChecking hair color term', field_value)
                    # must be '#' followed by 6 characters
                    if len(field_value) == 7:
                        if field_value[0] == '#':
                            chars_in_range_count = 0
                            for char in field_value[1:len(little_term)]:
                                # the ascii values for 0-9 and a-f
                                if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 102:
                                    chars_in_range_count += 1
                            if chars_in_range_count == 6:
                                print('\t\t\tValid hair color.')
                                fields_met_count += 1
                            else:
                                print('\t\t\tInvalid hair color (not enough valid characters)')
                        else:
                            print('\t\t\tInvalid hair color (no leading #)')
                    else:
                        print('\t\t\tInvalid hair color (wrong number of characters)')
                elif EYE_COLOR in little_term:
                    print('\t\tChecking eye color term', field_value)
                    if field_value in ALLOWED_ECL and len(field_value) == 3:
                        print('\t\t\tValid eye color.')
                        fields_met_count += 1
                    else:
                        print('\t\t\tInvalid eye color (either not in allowed ecl\'s or wrong length).')
                elif PASSPORT_ID in little_term:
                    print('\t\tChecking Passport id term', field_value)
                    # passport id must be a nine digit number, including leading zeroes
                    if len(field_value) == 9:
                        has_leading_zeroes = field_value[0] == '0'
                        if field_value.isnumeric():
                            print('\t\t\tValid passport id.')
                            fields_met_count += 1
                        else:
                            print('\t\t\tInvalid passport id (not entirely numeric).')
                    else:
                        print('\t\t\tInvalid passport id (length =/= 9)')

                if COUNTRY_ID in little_term:
                    print('\t\t\tIgnoring CID.')
                    found_cid = True
            missed_cid_case = (fields_met_count >= NUM_FIELDS - 1) and not found_cid
            if fields_met_count >= NUM_FIELDS - 1:
                valid_passports_count += 1
                print('Passport {} is valid'.format(term))
            elif missed_cid_case:
                valid_passports_count += 1
                print('Passport {} is valid (Missing CID case)'.format(term))
            else:
                print('Passport {} is invalid (only {} valid little terms)'.format(term, fields_met_count))
        print('There are {} valid passports in this data'.format(valid_passports_count))

part_2()

