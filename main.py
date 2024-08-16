

questions = ["Q1. What is the capital of Norway?",
             "Q2. What is the currency of Norway?",
             "Q3. What is the largest city in Norway?",
             "Q4. When is constitution day (the national day) of Norway?",
             "Q5. What color is the background of the Norwegian flag?",
             "Q6. How many countries does Norway border?", "Q7. What is the name of the university in Trondheim?",
             "Q8. How long is the border between Norway and Russia?", "Q9. Where in Norway is Stavanger?",
             "Q10. From which Norwegian city did the world’s famous composer Edvard Grieg come?"]

alternatives = ["a. Bergen b. Oslo c. Stavanger d. Trondheim",
                "a. Euro b. Pound c. Krone d. Deutsche Mark",
                "a. Oslo b. Stavanger c. Bergend. Trondheim",
                "a. 27th May b. 17th May c. 17th April d. 27th April",
                "a. Red b. White c. Blue d. Yellow",
                "a. 1 b. 2 c. 3 d. 4",
                "a. UiS b. UiO c. NMBU d. NTNU",
                "a. 96km b. 196 km c. 296 km d. 396 km",
                "a. North b. South c. South-west d. South-east",
                "a. Oslo b. Bergen c. Stavanger d. Tromsø"]

correct = ["b", "c", "a", "b", "a", "c", "d", "b", "c", "b"]

answers = {}

def main():
    login_dic = {
        "username": "PGR107",
        "password": "Python"
    }

    name = input("enter username: ")
    passw = input("enter password: ")

    result = login_info(login_dic, name, passw)

    if result:
        print("you logged in")
        quiz()
    else:
        print("Invalid username and/or password")
        main()

def login_info(login_dic, name, passw):
    if login_dic["username"] == name and login_dic["password"] == passw:
        return True
    else:
        return False

def quiz():
    for i in range(len(questions)):
        print(questions[i])
        print(alternatives[i])
        answer = input("answer: ").lower()
        while answer not in ["a", "b", "c", "d"]:
            print("not valid answer, please pick a, b, c or d")
            answer = input("answer: ").lower()
        answers[questions[i]] = answer
    report(answers)

def report(answers):
    c_answer = 10
    w_answer = 0
    for i in range(len(answers)):
        if answers[questions[i]] != correct[i]:
            print("--------------------")
            print(f"{questions[i]}")
            print(f"you answered: {answers[questions[i]]}. The correct answer was {correct[i]}")

            w_answer +=1
    print("********************")
    print(f"You got {c_answer - w_answer} correct answers and {w_answer} wrong answers.")
    print("********************")

main()