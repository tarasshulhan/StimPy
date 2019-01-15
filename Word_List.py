import random


class WordList:

    def __init__(self, file_name, extra_file_name):
        self.word_file = self.open_file(file_name)
        self.extra_file = self.open_file(extra_file_name)
        self.word_matrix = list(self.chunks(self.word_file, 5))
        self.spare_words = list(self.chunks(self.extra_file, 1))
        self.counter_len = ((len(self.word_matrix[0]))-1)*2
        self.possibilities_dictionary = {}
        self.all_possible_outcomes(self.word_matrix, self.possibilities_dictionary)
        self.experiment_list = self.create_experiment_list()
        self.all_word_lists = self.create_all_word_lists()
        self.fill_blanks()

    # open text file
    def open_file(self, file_name):
        with open(file_name, 'r') as infile:
            file = [line.strip() for line in infile][:120]
            return file

    # divide list into smaller lists of lenght n
    def chunks(self, l, n):
        # For item i in a range that is a length of list,
        for i in range(0, len(l), n):
            # Create an index range for list of n items:
            yield l[i:i+n]

    # create all possible outcomes for given target
    def create_possibilities(self, start_list, main_dict):
        for i in start_list[1:]:
            temp_list = ["", ""]
            temp_list[0] = i
            temp_list[1] = start_list[0]
            main_dict.setdefault(start_list.index(i), []).append(temp_list)
            temp_list = ["", "", "", "", "", ""]
            temp_list[0] = i
            temp_list[5] = start_list[0]
            main_dict.setdefault(start_list.index(i)+4, []).append(temp_list)

    # create all outcomes for all targets
    def all_possible_outcomes(self, start_list, main_dict):
        for i in start_list:
            self.create_possibilities(i, main_dict)

    # create experiment for one person
    def randomize_person(self, main_dict, personal_counter):
        personal_list = []
        loop_count = 0
        while True:
            choice = random.randint(1, 8)
            if personal_counter[choice - 1] != 0:
                random.shuffle(main_dict[choice])
                personal_list.append(main_dict[choice].pop())
                personal_counter[choice - 1] -= 1
                loop_count += 1
            else:
                continue
            if loop_count >= 24:
                break
        # print("personal count:", personal_counter)
        return personal_list

    def create_word_list(self, experiment_list):
        no_space_lists = []
        space_lists = []
        while experiment_list:
            if len(experiment_list[-1]) == 2:
                no_space_lists.append(experiment_list.pop())
            else:
                space_lists.append(experiment_list.pop())

        random.shuffle(no_space_lists)
        random.shuffle(space_lists)

        parallel_counter = 0
        while True:

            position_choice = random.randint(1,3)
            if position_choice == 1:
                space_lists[parallel_counter][1] = no_space_lists[parallel_counter][0]
                space_lists[parallel_counter][2] = no_space_lists[parallel_counter][1]
                parallel_counter += 1
            elif position_choice == 2:
                space_lists[parallel_counter][2] = no_space_lists[parallel_counter][0]
                space_lists[parallel_counter][3] = no_space_lists[parallel_counter][1]
                parallel_counter +=1
            elif position_choice == 3:
                space_lists[parallel_counter][3] = no_space_lists[parallel_counter][0]
                space_lists[parallel_counter][4] = no_space_lists[parallel_counter][1]
                parallel_counter += 1

            if parallel_counter >= 12:
                break

        return [item for sublist in space_lists for item in sublist]

    # creates a list of lists for experiments of all users
    def create_experiment_list(self):
        experiment_list = []
        for i in range(8):
            experiment_list.append(self.randomize_person(self.possibilities_dictionary, [3 for _ in range(self.counter_len)]))
        return experiment_list

    #creates a list of lists
    def create_all_word_lists(self):
        word_lists = []
        for i in self.experiment_list:
            word_lists.append(self.create_word_list(i))
        return word_lists

    #fill balnks and add extra words at the beginning
    def fill_blanks(self):
        for i in self.all_word_lists:
            for j in i:
                if j == '':
                    i[i.index(j)] = "".join(random.choice(self.spare_words))

        for x in self.all_word_lists:
            for _ in range(10):
                x.insert(0, "".join(random.choice(self.spare_words)))
















