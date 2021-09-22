import random

random_number = random.randint(2, 10) # choose the amount of dicts
print(random_number)

random_dicts = [] # create list
for i in range(random_number): # i - an amount of dicts we've  got
    d = {} # create a dict
    random_dict_number = random.randint(1,26) # determine range for lowercase letters
    print(random_dict_number)
    random_keys = random.sample(range(ord('a'), ord('z')), random_dict_number)  # list of ordered bumbers, 'ord' - ordered number for each letter in Unicode
    random_keys = [chr(i) for i in random_keys] # using 'chr' - get letter by it's order number
    for j in range(random_dict_number): # j - an amount of iterations (depends on amount of letters)
        random_value = random.randint(0,100) # add random values
        d[random_keys[j]] = random_value # make pairs key-value
    random_dicts.append(d) # add dicts to the list
print(random_dicts)

dict_with_positions_and_values = {} # create dict, where for each letter will create list with number of dictionary and value
for i in range(len(random_dicts)): # i - an amount of iterations (depends on the amount of dicts)
    for k, v in random_dicts[i].items():  # returns key-value for each dict
        print(k, v, random_dicts[i])
        if k not in dict_with_positions_and_values:
            dict_with_positions_and_values[k] = [[i + 1, v]] # we add key and value to the dict in case its absence
        else:
            dict_with_positions_and_values[k].append([i + 1, v]) # we add additional list to the list which already exists to choose max value further
print(dict_with_positions_and_values)

final_dict ={} # create a dict
for k,v in dict_with_positions_and_values.items(): # make pairs key-value
    if len(dict_with_positions_and_values[k]) == 1: # if the letter has only one value - it should be added to the final_dict
        final_dict[k] = v[0][1] # we take the key and its value. as we have only one list we need to use position [0] to get it and we choose position [1] because at this position we have our values
    else:
        max_value = v[0] # variable for max value. at the beginning we choose [0] position
        for i in v: # i - list in value
            if i[1] > max_value[1]:
                max_value = i # in case i > max value, we change max value for i value
        final_dict[k + '_' + str(max_value[0])] = max_value[1] # add to the key '_' and number of position and also max value to the final dict
print(final_dict)

