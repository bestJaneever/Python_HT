initial_text = '''tHis iz your homeWork, copy these Text to variable.'

You NEED TO normalize it fROM letter CASEs point oF View.also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph."

it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.'

'last iz TO calculate nuMber OF Whitespace characteRS in this Tex.caREFULL, not only Spaces, but ALL whitespaces.I got 87.'''

split_list = initial_text.split('\n\n')  # create a list with initial_text paragraphs
split_list = [i for i in split_list if len(i) > 0] # remove an empty string
split_list = [i.strip("'") for i in split_list] # remove "'"
split_list = [i.strip('"') for i in split_list] # remove '"'
print(split_list)

pre_final_text = [] # create a variable for transform text without last sentence
last_sentence = [] # create a list for join last words from the sentences
for j in split_list: # j - each element of the list
    sentences = j.split('.') # split for separate sentences
    sentences = [i for i in sentences if len(i) > 0] # remove an empty string
    paragraph = [] # create a list with separate sentences
    #print(sentences)
    for i in sentences: # i - each element of the sentences
        words = i.split() # split each sentence into words
        words = [w.lower() for w in words] # lowercase each word
        #print(words)
        words[0] = words[0].capitalize() # capitalize first word
        print(words)
        last_sentence.append(words[-1]) # add last words of the sentences
        join_words = ' '.join(words) + '.' # join words to sentences
        paragraph.append(join_words) # add sentences to paragraphs
    join_sentences = ' '.join(paragraph) # join sentences to paragraphs
    pre_final_text.append(join_sentences) # add paragraphs
print(pre_final_text)

last_sentence[0] = last_sentence[0].capitalize() # capitalize first word
last_sentence_join = ' '.join(last_sentence) + '.' # join last words to sentence
final_text = '\n\n'.join(pre_final_text) + ' ' + last_sentence_join # create final text, add whitespaces and sentence with last words
print(final_text)

text = final_text.replace(' iz ', ' is ') # replace
print(text)

whitespaces = 0 # start amount of whitespaces
for i in text: # i - element in text
    if i.isspace():
        whitespaces = whitespaces + 1 # if whitespace is found - add +1

print('I got ' + str(whitespaces) + ' whitespaces' + '.') # an amount of whitespaces










