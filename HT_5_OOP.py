from datetime import datetime
import random  # function to generate random numbers


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


def main():
    name_class = input('What do you want to share: News? Advertising?'
                       ' Or we can share phrase of the day with you!'
                       ' Or press "Enter" for quit. Please, make your choice: ')
    if name_class == 'News':
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
