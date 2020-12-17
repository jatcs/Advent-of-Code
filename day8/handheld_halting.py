PLUS = '+'
MINUS = '-'
OPERATOR_INDEX = 0
NUMBER_INDEX = 1
COMMAND_INDEX = 0

VALUE_INDEX = 1
ACC_COMMAND = 'acc'
JUMP_COMMAND = 'jmp'
NO_OP_COMMAND = 'nop'


class HandheldGameConsole:
    accumulator = 0
    instructions = ['acc', 'jmp', 'nop']

    def acc(self, value_op_string, current_index):
        """
        (just adding or subtracting from accumulator)
        :param value_op_string: a string with an operation and an integer
        :return: The next instruction index to execute
        """
        print('Adding {} to accumulator (currently {})'.format(value_op_string, self.accumulator))
        if PLUS == value_op_string[OPERATOR_INDEX]:
            self.accumulator += int(value_op_string[NUMBER_INDEX: len(value_op_string)])
        elif MINUS == value_op_string[OPERATOR_INDEX]:
            self.accumulator -= int(value_op_string[NUMBER_INDEX: len(value_op_string)])

        return current_index + 1

    def jmp(self, offset, current_index):
        """
        Jumps to a new instruction relative to itself
        :param current_index: the index of the current jmp call
        :param offset: how many indexes up or down to jump to
        :return: THe new index of the jumped to instruction
        """
        print('Attempting to jump from {} to position with offset {}'.format(current_index, offset))
        if PLUS == offset[OPERATOR_INDEX]:
            return current_index + int(offset[NUMBER_INDEX: len(offset)])
        elif MINUS == offset[OPERATOR_INDEX]:
            return current_index - int(offset[NUMBER_INDEX: len(offset)])

    def nop(self, place_holder, current_index):
        """
        Do nothing. Just move on to the next instruction
        :return: next instruction index
        """
        print('Called no operation. Moving on to next instruction {} from {}'.format(current_index + 1, current_index))
        return current_index + 1

    def run_command(self, command_name, value1_param, index_param):
        if command_name == ACC_COMMAND:
            return self.acc(value_op_string=value1_param, current_index=index_param)
        elif command_name == JUMP_COMMAND:
            return self.jmp(offset=value1_param, current_index=index_param)
        elif command_name == NO_OP_COMMAND:
            return self.nop(place_holder=value1_param, current_index=index_param)

    def basic_read_instructions(self, instructions_list= []):
        self.accumulator = 0
        instructions_list.append('')
        if not instructions_list:
            with open('hhh_instructions.txt') as the_instructions:
                instructions_list = the_instructions.readlines()
        checked_indexes = []
        index = 0
        while instructions_list[index] != '' and not checked_indexes == list(range(len(instructions_list))):
            # print('Attempting to execute instruction {} ({}) from instructions list'.format(index, instructions_list[index].strip()))
            split_command = instructions_list[index].split()
            command = split_command[COMMAND_INDEX]
            value = split_command[VALUE_INDEX]
            index = self.run_command(command, value, index)
            if index not in checked_indexes:
                checked_indexes.append(index)
                # print('\tCurrently these indexes are checked {}.'.format(checked_indexes))
        return self.accumulator

    def read_instructions(self):
        # part 1 of the coding problem
        with open('hhh_instructions.txt') as the_instructions:
            instructions_list = the_instructions.readlines()
            checked_indexes = []
            index = 0
            while not checked_indexes == list(range(len(instructions_list))) \
                    and index in range(len(instructions_list)):
                print('Attempting to execute instruction {} ({}) from instructions list'.format(index, instructions_list[index]))
                split_command = instructions_list[index].split()
                command = split_command[COMMAND_INDEX]
                value = split_command[VALUE_INDEX]
                index = self.run_command(command, value, index)
                if index not in checked_indexes:
                    checked_indexes.append(index)
                    print('\tCurrently these indexes are checked {}.'.format(checked_indexes))
                else:
                    print('\tAvoiding doubling back on the same index. Returning accumulator...')
                    return self.accumulator


    def swap_to_other_cmd(self, a_list, index):
        the_instruction = a_list[index].split()
        if NO_OP_COMMAND in the_instruction:
            the_instruction[COMMAND_INDEX] = JUMP_COMMAND
        elif JUMP_COMMAND in the_instruction:
            the_instruction[COMMAND_INDEX] = NO_OP_COMMAND
        a_list[index] = the_instruction



    def find_and_fix_mistake(self, current_instructions=[]):
        self.accumulator = 0
        # change some jmp to nop so that the program terminates
        instructions_list = []
        if not current_instructions:
            the_instructions = open('hhh_instructions.txt')
            instructions_list = the_instructions.readlines()
        else:
            instructions_list = current_instructions
        checked_indexes = []
        index = 0
        while index in range(len(instructions_list)):
            print('Attempting to execute instruction {} ({}) from instructions list.'.format(index, instructions_list[index].strip()))
            split_command = instructions_list[index].split()
            command = split_command[COMMAND_INDEX]
            value = split_command[VALUE_INDEX]

            index = self.run_command(command, value, index)
            if index not in checked_indexes:
                checked_indexes.append(index)
                print('\tCurrently these indexes are checked {}.'.format(checked_indexes))
            else:
                print('\tIndex attempting to double back to one previoulsy checked...')
                print('\tAttempting to determine if this is the cause of infinite recursion')
                if command in [JUMP_COMMAND, NO_OP_COMMAND]:
                    print('\t\tIt was. Calling this function again with the new swapped list')
                    # attempt again with these commands switched
                    new_instructions = self.swap_to_other_cmd(instructions_list, index)
                    self.find_and_fix_mistake(new_instructions)
                else:
                    print('\t\tIt is not one of those instructions :/')
        print('Managed to exit the while loop. Returning accumulator...')
        return self.accumulator

    def find_jmps_nops(self, a_list):
        jmps_indeces_list = []
        nops_indeces_list = []
        for index in range(len(a_list)):
            if JUMP_COMMAND in a_list[index]:
                jmps_indeces_list.append(index)
            elif NO_OP_COMMAND in a_list[index]:
                nops_indeces_list.append(index)
        return jmps_indeces_list, nops_indeces_list


    def fix_mistake2(self):
        the_instructions = open('hhh_instructions.txt')
        current_instructions_list = the_instructions.readlines()
        jump_command_indecs, no_ops_indeces = self.find_jmps_nops(current_instructions_list)
        for jump_index in jump_command_indecs:
            try:
                return self.basic_read_instructions(current_instructions_list)
            except:
                print('Attempting again with switched jmp and nop')
                return self.basic_read_instructions(self.swap_to_other_cmd(current_instructions_list, jump_index))
        current_instructions_list = the_instructions.readlines()
        for nop_index in no_ops_indeces:
            try:
                return self.basic_read_instructions(current_instructions_list)
            except:
                return self.basic_read_instructions(self.swap_to_other_cmd(current_instructions_list, nop_index))



def part_1():
    my_h = HandheldGameConsole()
    a = my_h.read_instructions()
    print('Value of accumulator = {}.'.format(a))

def part_2():
    my_h = HandheldGameConsole()
    a = my_h.fix_mistake2()
    print('Value of accumulator = {}.'.format(a))

part_2()
