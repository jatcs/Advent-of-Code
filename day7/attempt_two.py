LR = 'light red'
DkOrange = 'dark orange'
BW = 'bright white'
MY = 'muted yellow'
SG = 'shiny gold'
DkOlive = 'dark olive'
VP = 'vibrant plum'
FB = 'faded blue'
DB = 'dotted black'
COLORS_WITH_RULES = [LR, DkOrange, BW, MY, SG, DkOlive, VP, FB, DB]
CAN_HOLD_DIRECTLY = [BW, MY]
CAN_HOLD_INDIRECTLY = [DkOrange, LR]
CANNOT_HOLD_OTHER_BAGS = [FB, DB]
CANNOT_HOLD_INDIRECTLY = [DkOlive, VP]
SEPARATE_BAGS = '\n'
COLOR_STRING_LENGTH = 2
MAIN_BAG_COLOR_INDEX = 0


def figure_inner_bags(current_color):
    """
    Determine inner bags for a certain color based on the problem rules
    :param current_color: the color of the bag
    :return:
    """
    # only the first four colors in the rules can eventually hold shiny gold
    if current_color == LR:
        return {BW: 1, MY: 2}
    elif current_color == DkOrange:
        return {BW: 3, MY: 4}
    elif current_color == BW:
        return {SG: 1}
    elif current_color == MY:
        return {DkOlive: 1, VP: 2}
    # so avoiding extra work by not trying to find a way with colors that can never hold shiny gold
    elif current_color in CANNOT_HOLD_OTHER_BAGS or current_color in CANNOT_HOLD_INDIRECTLY:
        return {}

def find_can_carry_shiny_gold(bag_color, inner_bags_dict={}):
    print('Checking a bag with color {}'.format(bag_color))
    # base case
    if bag_color in CAN_HOLD_DIRECTLY or bag_color in CAN_HOLD_INDIRECTLY:
        print('\tFound a bag that can hold shiny gold => OG bag can hold at least 1 -> True')
        return True
    # recursive case
    elif bag_color not in CANNOT_HOLD_OTHER_BAGS and bag_color not in CANNOT_HOLD_INDIRECTLY:
        if not inner_bags_dict:
            if bag_color in COLORS_WITH_RULES:
                print('Initializing possible inner bags for bag with color {}'.format(bag_color))
                inner_bags_dict = figure_inner_bags(bag_color)
                print('\tThe inner bags:', inner_bags_dict)
            else:
                inner_bags_dict = {}
        print('Determining how many of the inner bags within bag color {} can hold shiny gold.'.format(bag_color))
        found_can_hold_shiny_gold = False
        for inner_bag_color in inner_bags_dict:
            # number_inner_bag_color = inner_bags_dict[inner_bag_color]
            found_can_hold_shiny_gold = find_can_carry_shiny_gold(bag_color=inner_bag_color)
        print('\tWhether or not they were able to find one that can carry shiny gold = {}'.format(found_can_hold_shiny_gold))
        return found_can_hold_shiny_gold

    print('Finished calculating the number of bags that can carry shiny gold')
    return False


def turn_into_bag_color_dict(file_line):
    split_line = file_line.split()
    current_bag_dict = {}
    color_key = ' '.join(split_line[0: COLOR_STRING_LENGTH])
    inner_bag_dict = {}
    for index in range(4, len(split_line), 4):
        if split_line[index] == 'no':
            return {color_key: {}}  # no inner bags
        if split_line[index].isnumeric():
            color_num = int(split_line[index])
            inner_bag_color = ' '.join(split_line[index + 1: index + 1 + COLOR_STRING_LENGTH])
            inner_bag_dict[inner_bag_color] = color_num
            current_bag_dict[color_key] = inner_bag_dict
    return current_bag_dict


def test_finder_func(current_test_string):
    bag_dictionary = turn_into_bag_color_dict(current_test_string)
    print('\n{}'.format(bag_dictionary))
    for color in bag_dictionary:
        inner_bags = bag_dictionary[color]
        if find_can_carry_shiny_gold(color, inner_bags):
            return 1  # meaning this bag can hold a shiny gold
    return 0 # this bag cannot hold shiny gold

def part_one():
    with open('bags_file.txt') as the_file:
        split_file = the_file.read().split(SEPARATE_BAGS)
        total_count = 0
        for row in split_file:
            total_count += test_finder_func(row)
        print(total_count)


'''
def calculate_carry_capacity(bag_color, current_count=0):
    """

    :param bag_color:
    :param current_count:
    :return: The number of shiny gold bags this bag color can carry
    """
    # base case where it either is shiny gold or can hold it
    if bag_color == SG or bag_color in CAN_HOLD_DIRECTLY:
        return current_count + 1
    elif bag_color in CAN_HOLD_INDIRECTLY:
        if bag_color == LR:
            # contains 1 bright white bag + 2 muted yellow bags -> 3 possible to hold shiny gold
            return current_count + 3
        elif bag_color == MY:
            return current_count # can't really hold additional bags
            # contains 2 shiny gold (holds bags that cannot carry other bags), 9 faded blue (holds no other bags)
    elif bag_color not in CANNOT_HOLD_OTHER_BAGS:
        return calculate_carry_capacity()
'''

if __name__ == '__main__':
    part_one()