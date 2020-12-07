### Day 3: Tobaggan Trajectory ###

TREE = '#'
MARK_TREE = 'X'
NORMAL = '.'
MARK_NORMAL = 'O'
def part_1():
    with open('forest.txt', 'r') as the_forest:
        # create a two-d list of trees and normal positions from the file
        forest_list = [row.split() for row in the_forest]
        i = 0 # initialize so Pycharm is happy
        new_list = [list(forest_list[i][j]) for j in range(len(forest_list[i])) for i in range(len(forest_list))]

        # find and mark path through the forest with
        move_right = 3
        move_down = 1
        num_trees = 0
        outer_dimension = 0
        inner_dimension = 0
        # display the forest pre-marks
        for row in new_list:
            print(row)

        # continue marking positions until you reach the bottom of the forest
        while outer_dimension < len(new_list):
            if new_list[outer_dimension][inner_dimension] == TREE:
                num_trees += 1
                new_list[outer_dimension][inner_dimension] = MARK_TREE
            elif new_list[outer_dimension][inner_dimension] == NORMAL:
                new_list[outer_dimension][inner_dimension] = MARK_NORMAL
            outer_dimension = (move_down + outer_dimension)
            inner_dimension = (move_right + inner_dimension) % len(new_list[0])
        # display the forest post-marks
        for row in new_list:
            print(''.join(row))
        print('Number of trees ecountered:', num_trees)

def part_2():
    # same thing except doing it with several slopes to navigate the forest
    with open('forest.txt', 'r') as the_forest:
        # index 0 of tuple = move right, index 1 of tuple = move down
        slopes_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        tree_counts = []
        # had to move this outside for loop because the second iteration would
        # only create an empty list (along with the_forest.readlines())
        # probably since the cursor was at the bottom of the file
        forest_list = [row.split() for row in the_forest]
        for slope in slopes_list:
            # create a two-d list of trees and normal positions from the file
            i = 0  # initialize so Pycharm is happy
            new_list = [list(forest_list[i][j]) for j in range(len(forest_list[i])) for i in range(len(forest_list))]

            # find and mark path through the forest with
            move_right = slope[0]
            move_down = slope[1]
            num_trees = 0
            outer_dimension = 0
            inner_dimension = 0

            # continue marking positions until you reach the bottom of the forest
            while outer_dimension < len(new_list):
                if new_list[outer_dimension][inner_dimension] == TREE:
                    num_trees += 1
                    new_list[outer_dimension][inner_dimension] = MARK_TREE
                elif new_list[outer_dimension][inner_dimension] == NORMAL:
                    new_list[outer_dimension][inner_dimension] = MARK_NORMAL
                outer_dimension = (move_down + outer_dimension)
                inner_dimension = (move_right + inner_dimension) % len(new_list[0])

            print('Number of trees ecountered:', num_trees)
            tree_counts.append(num_trees)

        # calculate product of all trees encountered from using different slopes
        product_counts = 1
        for number in tree_counts:
            product_counts *= number
        print('Product of trees encountered:', product_counts)

part_2()

