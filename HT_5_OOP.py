from datetime import datetime
import random  # function to generate random numbers
import os
import json
from HT_4 import normalize_elements

class News:
    def __init__(self, text, city):
        self.text = text
        self.city = city
        self.date = datetime.now()

    def publish(self):
        with open('Newsfeed.txt', 'a') as file:
            file.write('\n')
            file.write('\nNews: \n')
            file.write(self.text + '\n')
            file.write(self.city + ', ')
            file.write(str(self.date.strftime('%d/%m/%Y %H:%M')))


class Advertising:
    def __init__(self, text, expiration_date):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, '%d/%m/%Y')
        self.days_left = (self.expiration_date - datetime.now()).days

    def publish(self):
        with open('Newsfeed.txt', 'a') as file:
            file.write('\n')
            file.writelines('\nAdvertising: \n')
            file.write(self.text + '\n')
            file.write('Actual until: ' + str(self.expiration_date.date()))
            file.write(', ' + str(self.days_left) + ' days left')


# Phrase of the day creation
class Phrase:
    phrases = ['The best way to predict the future is to create it. - Abraham Lincoln',
               'Live as if you were to die tomorrow. Learn as if you were to live forever. - Gandhi',
               'Today a reader, tomorrow a leader. - Margaret Fuller',
               'The secret of getting ahead is getting started. - Mark Twain',
               'If you can dream it, you can do it. - Walt Disney',
               'It doesn’t matter how slowly you go as long as you do not stop. - Confucius',
               'Is it not enjoyable to learn and practise what you learn? – Confucius',
               'Reading is to the mind what exercise is to the body. - Joseph Addison',
               'To have another language is to possess a second soul. - Charlemagne']

    def __init__(self):
        self.phrase_of_the_day = random.choice(Phrase.phrases) # choose a phrase

    def publish(self):
        with open('Newsfeed.txt', 'a') as file:
            file.write('\n')
            file.write('\nPhrase of the Day: \n')
            file.write(self.phrase_of_the_day)


class File:

    def __init__(self, input_format, filepath='Files\myfile'):
        self.input_format = input_format
        self.filepath = filepath

    def process_file(self):
        if self.input_format == 'One':
            with open(self.filepath, 'r') as file, open('Newsfeed.txt', 'a') as update_file:
                s = file.readline()
                words = s.split()
                words = normalize_elements(words)
                s = ' '.join(words)
                update_file.write('\n')
                update_file.write(s + '\n')
        elif self.input_format == 'Many':
            with open(self.filepath, 'r') as file, open('Newsfeed.txt', 'a') as update_file:
                s = file.read()
                lines = s.split('\n')
                l = []
                for line in lines:
                    words = line.split()
                    words = normalize_elements(words)
                    s = ' '.join(words)
                    l.append(s)
                lines = '\n'.join(l)
                update_file.write('\n')
                update_file.write(lines + '\n')

    def remove_file(self):
        os.remove(self.filepath)

    def isfileexists(self):
        if os.path.exists(self.filepath):
            return True
        else:
            return False

class Json:

    def __init__(self, input_format, filepath='Files\\file.json'):
        self.input_format = input_format
        self.filepath = filepath

    def process_file(self):
        if self.input_format == 'One':
            with open(self.filepath, 'r') as file, open('Newsfeed.txt', 'a') as update_file:
                s = json.load(file)
                update_file.write('\n')
                update_file.write(s[0]["Category"])
                update_file.write('\n')
                update_file.write(s[0]["Text"])
                update_file.write('\n')
                update_file.write(s[0]["city"])
                update_file.write('\t')
                update_file.write(s[0]["date"])
        elif self.input_format == 'Many':
            with open(self.filepath, 'r') as file, open('Newsfeed.txt', 'a') as update_file:
                s = json.load(file)
                for i in s:
                    update_file.write('\n')
                    update_file.write(i["Category"])
                    update_file.write('\n')
                    update_file.write(i["Text"])
                    update_file.write('\n')
                    update_file.write(i["city"])
                    update_file.write('\t')
                    update_file.write(i["date"])

    def remove_file(self):
        os.remove(self.filepath)

    def isfileexists(self):
        if os.path.exists(self.filepath):
            return True
        else:
            return False

def main():
    name_class = input('What do you want to share: News? Advertising?'
                       ' Or we can share phrase of the day with you!'
                       ' If you want to add this from file - enter File'
                       ' Or press "Enter" for quit. Please, make your choice: ')
    if name_class == 'File':
        input_format = input('Enter format: One or Many records')
        filepath = input('Define file path here or enter "Default" for default')
        if filepath == 'Default':
            f = File(input_format)
        else:
            f = File(input_format,filepath)
        if f.isfileexists():
            f.process_file()
            f.remove_file()
        else:
            print("File doesn't exist")
    elif name_class == 'Json':
        input_format = input('Enter format: One or Many records')
        filepath = input('Define file path here or enter "Default" for default')
        if filepath == 'Default':
            f = Json(input_format)
        else:
            f = Json(input_format,filepath)
        if f.isfileexists():
            f.process_file()
            f.remove_file()
        else:
            print("File doesn't exist")
    elif name_class == 'News':
        message = input('Enter your text here: ')
        city = input('Enter your city here: ')
        news = News(message, city)
        news.publish()
        main()
    elif name_class == 'Advertising':
        message = input('Enter your text here: ')
        expiration_date = input('Actual till: (please, use the following format: dd/mm/yyyy ')
        adv = Advertising(message, expiration_date)
        adv.publish()
        main()
    elif name_class == 'Phrase':
        phr = Phrase()
        phr.publish()
        main()
    else:
        print('Goodbye!')


main()


