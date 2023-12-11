import random

#question keywords
keywords = ["White House", 
            "first president", 
            "the moon",
            "diamond play button",
            "H2"]

#Questions
questions = ["Where is the White House?",
            "Who is the first president of USA?",
            "Who first came to the moon?",
            "Who was the first person to achieve the diamond play button of Youtube in VietNam?",
            "H2 + O2 = ?"]

#Choice
choices = [
        ["Washington D.C", "New York", "Ohio ", "Texas"],
        ["Abraham Lincoln", "James Madison", "George Washington", "Theodore Roosevelt"],
        ["Kalpana Chawla", "Neil Armstrong", "Sunita Williams", "Valentina Tereshkova"],
        ["CrisDevilGamer", "NTN", "Misthy", "MTP"],
        ["HOHO", "HO2", "O2", "H2O"]
        ]

def play_game(keywords, questions, choice_map):
    correct_count = 0
    money = 0

    #Map number from 1-4 to A-D
    choice_map = {idx: letter for idx, letter in enumerate("ABCD", start = 1)}

    #combines list
    combined = list(zip(keywords, questions, choices))

    #shuffle the list
    random.shuffle(combined)
    shuffled_questions, shuffled_keywords, shuffled_choices = zip(*combined)


    #loop through keyword
    for keyword, question, choice in zip(shuffled_questions, shuffled_keywords, shuffled_choices):
        print(question)
        for idx, option in enumerate(choice, start = 1):
            print(f"{choice_map[idx]}.{option}")  

            #Ask user input
        while True:
            user_answer = input("Your answer: ").upper() #Conver user input to capital

            if user_answer in ["A", "B", "C", "D"]:

                #Check answer
                correct_answers = {
                    "White House": ["A"],
                    "first president": ["C"],
                    "the moon": ["B"],
                    "diamond play button": ["B"],
                    "H2": ["D"]
                }

                if user_answer.strip() in correct_answers.get(keyword, []):
                    print("Correct") 
                    correct_count += 1
                    money += 600
                    print("-" * 30)
                    break
                else:
                    print("Incorrect. See you next time. GG")
                    print("You receive: $" + str(money)) 
                    return
            else:
                print("Incorrect answer. Please choose again")
        if correct_count == 5:
            print("ALL FIVE QUESTIONS? GGEZ") 
            print("Congrates for receive a total of $" + str(money)) 

#instruction
print("Mesdames et messieurs, welcome to \"WHO WANTS TO BE A MILLIONAIRE? \" game")
user_name = input("Can I have your name, please: ")
print("Greetings, " + user_name)
print("In this game you will answer five question, and you will receive $600 for each correct answer. ")

yesNo = input("Are you ready? (Please type y/n): ")
if yesNo == "y":
    print("Well then, let's the show BEGIN.")
    print("-" * 30)
    play_game(keywords, questions, choices)
else:
    print("Okay, thanks for participating, Bye")