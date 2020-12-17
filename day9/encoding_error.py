from random import randint  # used in creating cases to test

NUM_PREAMBLE_TERMS = 5  # constant so I can change it when testing cases, usually = 25
SEPARATE_NUMS = '\n'


def find_sums(a_preamble):
    """
    Helper function for part 1
    Finds all possible sums from terms in the preamble.
    :param a_preamble: the first 25 numbers in the data set whose
    combinations (sums) determine the validity of its following terms
    :return: a dictionary of the sums (key = sum, value = string of which terms made that sum)
    """
    sum_possibilities = {}
    for term_one in a_preamble:
        for term_two in a_preamble:
            sum_num = term_one + term_two
            sum_string = str(term_one) + ' + ' + str(term_two)
            sum_possibilities[sum_num] = sum_string
    return sum_possibilities

def determine_validity(preamble_and_term):
    """
    Figures out if the terms following
    :param preamble_and_term: a list with the first 25 terms as the preamble
    :return: True/False
    """
    print('\nChecking the validity of this list:\n{}'.format(preamble_and_term))
    if len(preamble_and_term) >= NUM_PREAMBLE_TERMS:
        the_preamble = preamble_and_term[0: NUM_PREAMBLE_TERMS]
        other_term = preamble_and_term[len(preamble_and_term) - 1]
    print('Separated the preamble from the term we are checking:'
          '\nPreamble = {}\nTerm to check = {}'.format(the_preamble, other_term))
    preamble_sums = find_sums(the_preamble)

    if other_term not in preamble_sums:
        print('Term {} is invalid (not a sum of preamble terms)'.format(other_term))
        return False
    # if it got through that without returning False, must be True
    print('Term is a valid sum of preamble terms ({}).'.format(preamble_sums[other_term]))
    return True


def part1_test():
    # test out helper functions on cases where we know the outcome
    example_preamble = [x + 1 for x in range(NUM_PREAMBLE_TERMS)]
    example_list = example_preamble + [randint(2, 50) for x in range(10)]
    determine_validity(example_list)

def part_one():
    # this time the "preamble" is just the 25 terms before it
    with open('xmax_number_transmissions.txt', 'r') as numbers_file:
        numbers_list = [int(num_string) for num_string in numbers_file.read().split(SEPARATE_NUMS)]
        print('Running part 1 on this list:', numbers_list)
        # check indexes after its preamble (the NUM_PREAMBLE_TERMS before the current index)
        for term_index in range(NUM_PREAMBLE_TERMS, len(numbers_list) - 1):
            current_preamble_and_term = numbers_list[term_index - NUM_PREAMBLE_TERMS: term_index + 1]  # + 1 to include the current term
            current_term_validity = determine_validity(current_preamble_and_term)
            if not current_term_validity:
                print('Not going to continue traversing through numbers since this term is invalid')
                return
        print('Congrats! The whole set is valid!')

def find_invalid_numbers(numbers_list):
    invalid_nums_list = []
    # modified version of part 1 to find all invalid numbers
    print('Finding invalid numbers from this list:', numbers_list)
    # check indexes after its preamble (the NUM_PREAMBLE_TERMS before the current index)
    for term_index in range(NUM_PREAMBLE_TERMS, len(numbers_list) - 1):
        current_preamble_and_term = numbers_list[term_index - NUM_PREAMBLE_TERMS: term_index + 1]  # + 1 to include the current term
        current_term_validity = determine_validity(current_preamble_and_term)
        if not current_term_validity:
            # found an invalid term -> store it
            # "it" being the last term of checked list (the term being checked)
            invalid_nums_list.append(current_preamble_and_term[len(current_preamble_and_term) - 1])
    return invalid_nums_list

def find_contigiguous_set(list_of_numbers, sum_value):
    """
    Helper Function for part 2
    :param list_of_numbers: the puzzle input
    :param sum_value: the invalid number from part 1
    :return: a list of at least two numbers which add up to the sum_value
    """
    MIN_NUMBER_OF_TERMS = 2
    # go through slices of the numbers list to find
    # sums of contigious terms in the list that equal the sum value
    for index_offset in range(len(list_of_numbers) - MIN_NUMBER_OF_TERMS):
        for slice_length in range(MIN_NUMBER_OF_TERMS, MIN_NUMBER_OF_TERMS + index_offset + 1):
            print('Slicing numbers list from index {} to {}'.format(index_offset, index_offset + slice_length))
            current_slice = list_of_numbers[index_offset: index_offset + slice_length]
            current_sum = sum(current_slice)
            print('Checking if slice {} adds up to {} (actual current sum = {})'.
                  format(current_slice, sum_value, current_sum))
            if current_sum == sum_value:
                print('Found the slice ({}) that adds up to the invalid number {}'.format(current_slice, sum_value))
                return current_slice # the contiguous set of numbers that sum up to the right value
    print('Looks like we were unable to find a contiguous set'
          ' that adds up to {} in the numbers list'.format(sum_value))
    return []

def find_encryption_weakness(contiguous_set):
    # get the sum of the smallest and largest number in the contigious range
    smallest = min(contiguous_set)
    largest = max(contiguous_set)
    print('Found smallest ({}) and largest ({}) in contiguous set'
          '\nReturning the sum of the two ({})'.format(smallest, largest, smallest + largest))
    return smallest + largest

def part2_test():
    # must find a contiguous set of at least two numbers in your
    with open('testing_nums.txt', 'r') as numbers_file:
        numbers_list = [int(number_string) for number_string in numbers_file.read().split(SEPARATE_NUMS)]
        invalid_numbers = find_invalid_numbers(numbers_list)
        print(invalid_numbers)
        for num in invalid_numbers:
            the_contiguous_set = find_contigiguous_set(numbers_list, num)
            print('Contiguous set for {} = {}'.format(num, the_contiguous_set))
            encryption_weakness = find_encryption_weakness(the_contiguous_set)
            print('Ta Da! Found the encryption weakness:', encryption_weakness)


def part_two():
    # basically the test function but with a different file input
    with open('xmax_number_transmissions.txt', 'r') as numbers_file:
        the_numbers_list = [int(number_string) for number_string in numbers_file.read().split(SEPARATE_NUMS)]
        the_contiguous_set = find_contigiguous_set(the_numbers_list, 23278925)
        find_encryption_weakness(the_contiguous_set)

part_two()