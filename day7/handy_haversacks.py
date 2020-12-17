# check rules about luggage bags (what they must contain)
COLORS_WITH_RULES = {'light red': 'light red bags contain 1 bright white bag, 2 muted yellow bags.',
                     'dark orange': 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
                     'bright white': 'bright white bags contain 1 shiny gold bag.',
                     'muted yellow': 'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
                     'shiny gold': 'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
                     'dark olive': 'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
                     'vibrant plum': 'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
                     'faded blue': 'faded blue bags contain no other bags.',
                     'dotted black': 'dotted black bags contain no other bags.'}
CAN_DIRECTLY_HOLD_SHINY_GOLD = ['bright white', 'muted yellow']
CAN_INDIRECTLY_HOLD_SHINY_GOLD = {'dark orange': 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
                                  'light red': 'light red bags contain 1 bright white bag, 2 muted yellow bags.'}
CANNOT_HOLD_OTHER_BAGS = ['faded blue', 'dotted black']

SPLIT_BAG_FROM_CONTENTS = ' bags contain '
NO_INNER_BAGS = 'no other bags.\n'
BAG_COLOR_INDEX = 0
INNER_BAGS_START_INDEX = 1
INNER_BAGS_END_INDEX = 3
END_LINE_CASE_SINGULAR = 'bag.'
END_LINE_CASE_PLURAL = 'bags.'
ONE_BAG_LENGTH = 4

class Bag:
    def __init__(self, color='', outer_bag=None):
        self.color = color
        self.outer_bag = outer_bag
        self.inner_bags_dict = {}  # dictionary with inner bag
        # key = color and amount = the value / amount of that color within this bag
        self.inner_bags_list = []
        self.can_hold_shiny_gold_count = 0

    def create_from_string(self, the_string, outer_bag_instance= None):
        # initialize lots of the stuff if it wasn't already inputted
        if not self.inner_bags_dict:
            split_contents = the_string.split(SPLIT_BAG_FROM_CONTENTS)
            print('\nInitializing inner bags from',split_contents)
            self.color = split_contents[BAG_COLOR_INDEX]
            # cases for inner bags
            # no inner bags
            if NO_INNER_BAGS not in split_contents:
                the_inner_bags = split_contents[INNER_BAGS_START_INDEX].split()
                # >= 1 bag -> separate by bags, ends in 'bags.' or 'bag'
                for inner_bag_index in range(0, len(the_inner_bags), ONE_BAG_LENGTH):
                    inner_bag_number = int(the_inner_bags[BAG_COLOR_INDEX + inner_bag_index])
                    # the color will be the next two terms as a list which needs to be joined back together into one color string
                    inner_bag_color = ' '.join(the_inner_bags[INNER_BAGS_START_INDEX + inner_bag_index: INNER_BAGS_END_INDEX + inner_bag_index])
                    self.inner_bags_dict[inner_bag_color] = inner_bag_number
                    self.inner_bags_list.append(inner_bag_color)
                print('Inner bags:', self.inner_bags_dict)
        if outer_bag_instance:
            self.outer_bag = outer_bag_instance



    def check_color_conditions(self, current_bag_index= 0, current_count= 0):
        # will it be able to hold the shiny gold bag based on its inner bags
        # can initialize each inner bag and check this condition on that
        # base case: can directly hold gold bags
        print('Checking a bag with color {}...'.format(self.color))
        if not self.inner_bags_dict and self.color in COLORS_WITH_RULES:
            self.create_from_string(COLORS_WITH_RULES[self.color])
        if self.color in CAN_DIRECTLY_HOLD_SHINY_GOLD:
            if self.outer_bag:
                self.outer_bag.can_hold_shiny_gold_count += self.outer_bag.inner_bags_dict[self.color]
            else:
                current_count += 1
                self.can_hold_shiny_gold_count = current_count
            # continue to check within that bag
            if current_bag_index + 1 in range(len(self.inner_bags_list)):
                current_inner_bag_color = self.inner_bags_list[current_bag_index]
                current_inner_bag = Bag(current_inner_bag_color, outer_bag=self)
                current_inner_bag.check_color_conditions(current_bag_index + 1, current_count)
            else:
                return current_count
        # other case: can hold through one of its inner bags:
        elif self.color not in CANNOT_HOLD_OTHER_BAGS and self.inner_bags_list:
            # check through inner bags list
            # if its true, get the number of that kind of bag from the dictionary
            current_inner_bag_color = self.inner_bags_list[current_bag_index]
            current_inner_bag = Bag(current_inner_bag_color, outer_bag= self)
            current_inner_bag.check_color_conditions(current_bag_index, current_count)
        # go back up to outer bag to switch to another inner bag within that outer one
        elif self.outer_bag:
            if current_bag_index + 1 in range(len(self.outer_bag.inner_bags_list)):
                current_bag_color = self.outer_bag.inner_bags_list[current_bag_index + 1]
                current_bag = Bag(current_bag_color)
                current_bag.check_color_conditions(current_bag_index + 1, current_count)
        else:
            self.can_hold_shiny_gold_count = current_count
            return current_count

    def find_can_hold_shiny_gold(self, iteration=0, count=0, bag_instance=None):
        print('On iteration {} of trying to find bags that can hold shiny gold. Current count= {}'.format(iteration, count))
        if iteration == 0 and not bag_instance:
            bag_instance = self
        if bag_instance.color in CAN_DIRECTLY_HOLD_SHINY_GOLD:
            print('Found {} that can hold shiny gold.'.format(bag_instance.color))
            '''if bag_instance.outer_bag:
                # add on however many of that color bag were in the original bag
                print('There are {} many of them being added to count.'.format(bag_instance.outer_bag.inner_bags_dict[bag_instance.color]))
                count += bag_instance.outer_bag.inner_bags_dict[bag_instance.color]
            else:
                print('There is 1 of them being added to count.')
                count += 1'''
            print('There is 1 of them being added to count.')
            count += 1
        elif bag_instance.color in CAN_INDIRECTLY_HOLD_SHINY_GOLD:
            for color in bag_instance.inner_bags_dict:
                count += bag_instance.inner_bags_dict[color]
        else:
            print('Bag with color {} cannot hold shiny gold directly or indirectly'.format(bag_instance.color))
        # iteration = index - 1
        for little_bag_color in bag_instance.inner_bags_dict:
            print(('\tChecking bag {} within bag with color {}'.format(little_bag_color, bag_instance.color)))
            '''if little_bag_color in CAN_DIRECTLY_HOLD_SHINY_GOLD:
                count += 1'''
            if little_bag_color not in CANNOT_HOLD_OTHER_BAGS:
                little_bag = Bag(little_bag_color)
                if little_bag_color in COLORS_WITH_RULES:
                    little_bag.create_from_string(COLORS_WITH_RULES[little_bag_color], outer_bag_instance= bag_instance)
                self.find_can_hold_shiny_gold(iteration= iteration + 1, count=count, bag_instance=little_bag)
        return count


def test_finding_shiny_gold(colors_list=[]):
    sum = 0
    for color in colors_list:
        this_bag = Bag(color)
        if color in COLORS_WITH_RULES:
            this_bag.create_from_string(COLORS_WITH_RULES[color])
        x = this_bag.find_can_hold_shiny_gold()
        sum += x
        print('found %d bags that can hold shiny bags'%x)

    print(sum)

'''test_finding_shiny_gold(['light red', 
                         'dark orange', 
                         'bright white', 
                         'muted yellow', 
                         'shiny gold', 
                         'dark olive', 
                         'vibrant plum'])'''

def part_1():
    # color conditions
    # bright white or muted yellow bag
    #   -> can hold shiny gold bag directly
    # dark orange bag or light red bag
    #   -> can hold bright white and muted yellow bags
    #       -> either of these could shiny gold

    # want to carry your shiny gold bag in at least one other bag
    # sort through puzzle input and see how many bags are valid as the outer bag for the shiny gold

    with open('bags_file.txt', 'r') as the_file:
        valid_bags = 0
        the_bags = the_file.readlines()
        for bag_string in the_bags:
            this_bag = Bag()
            this_bag.create_from_string(bag_string)
            # this_bag.check_color_conditions()
            valid_bags += this_bag.find_can_hold_shiny_gold()  # this_bag.can_hold_shiny_gold_count
            print('Currently seeing {} bags able to hold shiny gold, {} total.'.format(this_bag.can_hold_shiny_gold_count, valid_bags))

part_1()