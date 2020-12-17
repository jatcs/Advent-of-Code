SPLIT_GROUP = '\n\n'
SPLIT_PEOPLE = '\n'

def total_chars(the_list):
    """
    Sums up the number of characters in a list of strings with non repeating characters
    :param the_list: the list of group answers (already made to account for repeated characters)
    :return: the total number of characters
    """
    total = 0
    for a_string in the_list:
        total += len(a_string)
    return total


def part_1():
    with open('group_answers_puzzle_input.txt', 'r') as the_file:
        # separate each group into their own string and then split each group -> list
        old_group_answers = ''.join(the_file.readlines()).split(SPLIT_GROUP)
        # remove inner \n's
        clean_group_answers = []
        for term in old_group_answers:
            clean_term = ''
            for character_index in range(0, len(term)):
                # ensure there are no character repeats at the same time of checking / removing newlines
                if term[character_index] not in clean_term and term[character_index: character_index + 1] != '\n':
                    clean_term += term[character_index]
            clean_group_answers.append(clean_term)
        sum = total_chars(clean_group_answers)
        print('Sum of counts = {}'.format(sum))


def part_2():
    # find the number of questions everyone answered yes to
    with open('group_answers_puzzle_input.txt', 'r') as the_file:
        old_group_answers = ''.join(the_file.readlines()).split(SPLIT_GROUP)
        # store all of the groups answers in one list of strings without newlines
        # will still use old_group_answers to see where the groups/people were split
        clean_group_answers = []
        for term in old_group_answers:
            clean_term = ''
            for character_index in range(0, len(term)):
                # checking / removing newlines
                if term[character_index: character_index + 1] != '\n':
                    clean_term += term[character_index]
            clean_group_answers.append(clean_term)
        # find the total number of questions everyone in a group answered yes to
        counts_sum = 0
        for term_index in range(len(clean_group_answers)):
            counts_dict = {}
            # see how many people are by seeing how many new line sequences there are
            # (not including the end)
            num_people = len(old_group_answers[term_index].strip().split(SPLIT_PEOPLE))

            for character in clean_group_answers[term_index]:
                if character not in counts_dict:
                    counts_dict[character] = 1
                else:
                    counts_dict[character] += 1
            # see how many questions everyone answered yes to in this group
            for character_key in counts_dict:
                if counts_dict[character_key] == num_people:
                    counts_sum += 1
        print('Count:', counts_sum)

part_2()






