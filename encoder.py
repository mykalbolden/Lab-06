def encode(phrase):
    phrase = str(phrase)
    new_phrase = ""
    for i in phrase:
        new_phrase += str(int(i) + 3)
    return new_phrase


def decode(phrase):
    phrase = str(phrase)
    new_phrase = ""
    for i in phrase:
        new_phrase += str(int(i) - 3)
    return new_phrase


def main():
    # looping menu
    option = '1'
    phrase = ''
    while option != '0':
        # print menu
        print('0. Exit')
        print('1. Enter a new phrase')
        print('2. Print encoded phrase')
        print('3. Print decoded phrase')
        option = input('Enter an option: ')

        if option == '1':
            phrase = input('Enter your phrase: ')
        elif option == '2':
            print('Encoded phrase is', encode(phrase))
        elif option == '3':
            print('Decoded phrase is', decode(phrase))
