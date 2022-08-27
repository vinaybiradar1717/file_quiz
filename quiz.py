from random import choice
class Quizzy():

    def all_questions(self):

        f = open('questions.txt', 'r+')
        data = f.read()
        file_content = data.split('\n')
        f.close()

        return file_content

    def play_game(self, questions_list):
        question = choice(questions_list).split('.')

        print(question[1].strip())
        user_input = str(input('Enter your answer: '))
        if user_input.lower() == question[2].strip().lower():
            print("Correct!!!")
        else:
            print('Incorrect')



class_object = Quizzy()
class_object.play_game(class_object.all_questions())

# first = class_object.all_questions()[4]
# data = first.split('.')
# print(data[1])
# print(data[2])
