initial_text = '''tHis iz your homeWork, copy these Text to variable.'

You NEED TO normalize it fROM letter CASEs point oF View.also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph."

it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.'

'last iz TO calculate nuMber OF Whitespace characteRS in this Tex.caREFULL, not only Spaces, but ALL whitespaces.I got 87.'''


def get_split_list(string, delimiter):
    return initial_text.split('\n\n')  # create a list with initial_text paragraphs


def remove_empty_element(split_list):
    split_list = [i for i in split_list if len(i) > 0] # remove an empty string
    return split_list


def remove_character(split_list, character):
    split_list = [i.strip(character) for i in split_list] # remove "'"
    return split_list


def get_main_text_and_last_sentence(split_list):
    pre_final_text = [] # create a variable for transform text without last sentence
    last_sentence = [] # create a list for join last words from the sentences
    for j in split_list: # j - each element of the list
        sentences = j.split('.') # split for separate sentences
        sentences = [i for i in sentences if len(i) > 0] # remove an empty string
        paragraph = [] # create a list with separate sentences
        for i in sentences: # i - each element of the sentences
            words = i.split() # split each sentence into words
            words = [w.lower() for w in words] # lowercase each word
            words[0] = words[0].capitalize() # capitalize first word
            last_sentence.append(words[-1]) # add last words of the sentences
            join_words = ' '.join(words) + '.' # join words to sentences
            paragraph.append(join_words) # add sentences to paragraphs
        join_sentences = ' '.join(paragraph) # join sentences to paragraphs
        pre_final_text.append(join_sentences) # add paragraphs

    return pre_final_text, last_sentence


def get_capitalize_first_word(last_sentence):
    last_sentence[0] = last_sentence[0].capitalize() # capitalize first word

    return last_sentence


def get_text_join(lst, ch):
    text_join = ch.join(lst) # + '.' # join last words to sentence
    return text_join


def get_text_replaced(string, chars_for_replace, chars_replace_with):
    text = string.replace(chars_for_replace, chars_replace_with) # replace  ' iz ', ' is '
    return text


def get_whitespaces_amount(string):
    whitespaces = 0 # start amount of whitespaces
    for i in string: # i - element in text
        if i.isspace():
            whitespaces = whitespaces + 1 # if whitespace is found - add +1
    return whitespaces


split_list = get_split_list(initial_text, '\n\n')
split_list = remove_empty_element(split_list)
split_list = remove_character(split_list, "'")
split_list = remove_character(split_list, '"')
pre_final_text, last_sentence = get_main_text_and_last_sentence(split_list)
last_sentence = get_capitalize_first_word(last_sentence)
last_sentence_join = get_text_join(last_sentence, ' ') + '.'
pre_final_text_join = get_text_join(pre_final_text, '\n\n')
final_text = pre_final_text_join + ' ' + last_sentence_join
final_text_replaced = get_text_replaced(final_text, ' iz ', ' is ')
whitespaces = get_whitespaces_amount(final_text_replaced)

print(final_text_replaced)
print('I got ' + str(whitespaces) + ' whitespaces' + '.') # an amount of whitespaces










