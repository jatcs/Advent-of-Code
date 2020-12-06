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
SEPARATE_PASSPORTS = '\n\n\n' # 3 because it's usually 2 but I added 1 in the join statement
SEPARATE_TERMS = '\n\n' # usually 1, becomes 2 because of the 1 I added in the join

with open('passport_data.txt', 'r') as data_file:
    # store the passports from the file
    data_list = '\n'.join(data_file.readlines()).split(SEPARATE_PASSPORTS) # each passport's data
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

