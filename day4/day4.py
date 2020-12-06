### Day 4: Passport Processing ###

BIRTH_YEAR = 'byr'
ISSUE_YEAR = 'iyr'
EXPIRATION_DATE = 'eyr'
HEIGHT = 'hgt'
HAIR_COLOR = 'hcl'
EYE_COLOR = 'ecl'
PASSPORT_ID = 'pid'
COUNTRY_ID = 'cid'
NUM_FIELDS = 8
SEPARATE_PASSPORTS = '\n\n\n'
SEPARATE_TERMS = '\n\n'

with open('passport_data.txt', 'r') as data_file:
    data_list = []
    '''
    for row in data_file:
        data_list.append(row.strip().split())
    '''
    # find each passport (separated by blank line)
    '''
    finished = False
    index = 0
    while not finished:
        complete_passport = False
        print('Data list is currently:', data_list)
        data_list.append([])
        while not complete_passport:
            if data_file.readline() != '\n':
                data_list[index] += data_file.readline().strip().split()
            else:
                complete_passport = True
        index += 1
        if not data_file.readline():
            finished = True
    '''
    first_list = '\n'.join(data_file.readlines()).split(SEPARATE_PASSPORTS)

    print(first_list)
    data_list = first_list


    # data_list = data_file.split('\n') # each passport's data

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

