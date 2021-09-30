import random


def get_random_number(min_val, max_val):
    # choose the amount of dicts
    return random.randint(min_val, max_val)


def get_random_dicts(rand_number):
    rand_dicts_list = []
    for i in range(rand_number):  # i - an amount of dicts we've  got
        d = {}  # create a dict
        random_dict_number = get_random_number(1, 26)  # determine range for lowercase letters
        random_keys = random.sample(range(ord('a'), ord('z')),
                                    random_dict_number)  # list of ordered bumbers, 'ord' - ordered number for each letter in Unicode
        random_keys = [chr(i) for i in random_keys]  # using 'chr' - get letter by it's order number
        for j in range(random_dict_number):  # j - an amount of iterations (depends on amount of letters)
            random_value = get_random_number(0, 100)  # add random values
            d[random_keys[j]] = random_value  # make pairs key-value
        rand_dicts_list.append(d)  # add dicts to the list
    return rand_dicts_list


def get_dict_with_positions_and_values(rand_dicts):
    dict_with_positions_and_values = {}  # create dict, where for each letter will create list with number of dictionary and value
    for i in range(len(rand_dicts)):  # i - an amount of iterations (depends on the amount of dicts)
        for k, v in rand_dicts[i].items():  # returns key-value for each dict
            if k not in dict_with_positions_and_values:
                dict_with_positions_and_values[k] = [[i + 1, v]]  # we add key and value to the dict in case its absence
            else:
                dict_with_positions_and_values[k].append(
                    [i + 1, v])  # we add additional list to the list which already exists to choose max value further
    return dict_with_positions_and_values


def get_final_dict(dictionary):
    final_dict = {}  # create a dict
    for k, v in dictionary.items():  # make pairs key-value
        if len(dictionary[
                   k]) == 1:  # if the letter has only one value - it should be added to the final_dict
            final_dict[k] = v[0][
                1]  # we take the key and its value. as we have only one list we need to use position [0] to get it and we choose position [1] because at this position we have our values
        else:
            max_value = v[0]  # variable for max value. at the beginning we choose [0] position
            for i in v:  # i - list in value
                if i[1] > max_value[1]:
                    max_value = i  # in case i > max value, we change max value for i value
            final_dict[k + '_' + str(max_value[0])] = max_value[
                1]  # add to the key '_' and number of position and also max value to the final dict
    return final_dict


random_number = get_random_number(2, 10)
random_dicts = get_random_dicts(random_number)
dict_with_positions_and_values = get_dict_with_positions_and_values(random_dicts)
final_dict = get_final_dict(dict_with_positions_and_values)
print(final_dict)