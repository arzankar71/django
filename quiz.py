name = input("what is your name: ")
point = 0
question_1 = input("what is apple? ")
question_2 = input("what is BMW? ")
question_3 = input("what is pizza? ")
question_4 = input("what is football? ")
question_5 = input("what is dog? ")

QUESTIONS = (question_1, question_2, question_3, question_4, question_5)

for q in QUESTIONS:
    if question_1 == "fruit":
        point += 4
        continue
    if question_2 == "car":
        point += 4
        continue
    if question_3 == "food":
        point += 4
        continue
    if question_4 == "sport":
        point += 4
        continue
    if question_5 == "animal":
        point += 4
print(name)
print(point)
