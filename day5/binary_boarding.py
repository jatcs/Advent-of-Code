NUM_ROWS = 128 # indexes 0 to 127
NUM_COLS = 8
FRONT = 'F'
BACK = 'B'
LEFT = 'L'
RIGHT = 'R'

def part_1():
    with open('passports_strings.txt', 'r') as the_file:
        your_seat_ids = [] # store results of boarding passes
        for row_string in the_file:
            current_row_range = range(NUM_ROWS)
            current_col_range = range(NUM_COLS)
            directions_string = row_string.strip()
            # string acts like binary search
            # tells you which direction to take
            for character in directions_string:
                # print('Current rows:', current_row_range)
                # print('Current cols:', current_col_range)
                # take lower half of columns
                if character == LEFT:
                    if len(current_col_range) > 1:
                        current_col_range = current_col_range[0: len(current_col_range) // 2]
                    else:
                        current_col_range = [current_col_range[0]]
                # take upper half of columns
                elif character == RIGHT:
                    if len(current_col_range) > 1:
                        current_col_range = current_col_range[(len(current_col_range) // 2): len(current_col_range)]
                    else:
                        current_col_range = [current_col_range[0]]
                # take lower half of rows
                elif character == FRONT:
                    if len(current_row_range) > 1:
                        current_row_range = current_row_range[0: len(current_row_range) // 2]
                    else:
                        current_row_range = [current_row_range[0]]
                # take upper half of rows
                elif character == BACK:
                    if len(current_row_range) > 1:
                        current_row_range = current_row_range[(len(current_row_range) // 2): len(current_row_range)]
                    else:
                        current_row_range = [current_row_range[0]]
            seat_id = (current_row_range[0] * 8) + current_col_range[0]
            your_seat_ids.append(seat_id)
            # print('{}: row {}, column {}, seat ID {}.'.format(\
            #    directions_string, current_row_range[0], current_col_range[0], seat_id))
        print('The max seat id is {}.'.format(max(your_seat_ids)))
# part_1()

# currently unsuccessful :/
def part_2():
    with open('passports_strings.txt', 'r') as the_file:
        your_seat_ids = [] # store results of boarding passes
        for row_string in the_file:
            current_row_range = range(NUM_ROWS)
            current_col_range = range(NUM_COLS)
            directions_string = row_string.strip()
            # string acts like binary search
            # tells you which direction to take
            for character in directions_string:
                # print('Current rows:', current_row_range)
                # print('Current cols:', current_col_range)
                # take lower half of columns
                if character == LEFT:
                    if len(current_col_range) > 1:
                        current_col_range = current_col_range[0: len(current_col_range) // 2]
                    else:
                        current_col_range = [current_col_range[0]]
                # take upper half of columns
                elif character == RIGHT:
                    if len(current_col_range) > 1:
                        current_col_range = current_col_range[(len(current_col_range) // 2): len(current_col_range)]
                    else:
                        current_col_range = [current_col_range[0]]
                # take lower half of rows
                elif character == FRONT:
                    if len(current_row_range) > 1:
                        current_row_range = current_row_range[0: len(current_row_range) // 2]
                    else:
                        current_row_range = [current_row_range[0]]
                # take upper half of rows
                elif character == BACK:
                    if len(current_row_range) > 1:
                        current_row_range = current_row_range[(len(current_row_range) // 2): len(current_row_range)]
                    else:
                        current_row_range = [current_row_range[0]]
            seat_id = (current_row_range[0] * 8) + current_col_range[0]
            your_seat_ids.append(seat_id)
            your_seat_ids.append(seat_id + 1)
            your_seat_ids.append(seat_id - 1)
            print('{}: row {}, column {}, seat ID {}.'.format(\
                directions_string, current_row_range[0], current_col_range[0], seat_id))
        print('The max seat id is {}.'.format(max(your_seat_ids)))

part_2()



