import random
import json

def main():
    dictionary = {}

    try:
        file = open("dictionary.json","r+")
        dictionary = json.load(file)
    except IOError:
        file = open("dictionary.json", "w+")

    while True:

        print("1. add word")
        print("2. ask for translation")
        print("3. take a quiz")
        print("4. quit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            word1 = input("Enter a word in your native language: ")
            word2 = input("Enter translation: ")
            dictionary[word1] = word2
            print(dictionary)

        if choice == 2:
            language = input("Do you want to translate from your native language? (yes/no) ")
            word = input("What word do you want to translate? ")
            translation = ""
            if language == "yes":
                translation = dictionary[word]
            else:
                for key,value in dictionary.items():
                    if word == value:
                        translation = key
                        break

            print(translation)


        if choice == 3:
            number = int(input("How many words do you want to be quizzed on? "))
            words = random.choices(list(dictionary.items()), k = number)

            for native,translation in words:
                question = native
                correct = translation
                number = random.randint(0,1)
                if number == 1:
                    question = translation
                    correct = native

                answer = input(question + ": ")

                if answer == correct:
                  print("Nice job!")
                else:
                  print("The correct translation is", correct)

        if choice == 4:
            quit = input("Are you sure you want to quit? (yes/no) ")

            if quit == "yes":
                file.seek(0)
                file.truncate()
                json.dump(dictionary,file)
                break
            else:
                continue


main()
