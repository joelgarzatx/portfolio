from random import randint
from datetime import datetime

NUMBER_OF_QUESTIONS = 5

def quiz_sum(num_1, num_2):
    return num_1 + num_2

class Question(object):
    
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_sum = quiz_sum(self.num_1,self.num_2)


if __name__ == '__main__':
    quest_list = []
    question_string_fmt = "What is the sum of {0} and {1}?  "
    response_string_fmt = "{0} is {1}!"
    summary_string_fmt = "Question #{0} took about {1} seconds to complete and was {2}."
    
    quest_list = [Question(randint(1,10),randint(1,10)) for count in range(NUMBER_OF_QUESTIONS)]

    for quest in quest_list:
        timer_start = datetime.now()
        
        try:
            answer = int(input(question_string_fmt.format(quest.num_1, quest.num_2)))
            if answer != quest.num_sum:
                quest.response = 'wrong'
            else:
                quest.response = 'right'
            print(response_string_fmt.format(answer, quest.response))         
        except ValueError:
            print("Invalid Input!")
            quest.response = 'invalid'
    
        timer_end = datetime.now()
        
        elapsed_time = timer_end - timer_start
        quest.time = elapsed_time.seconds

    total_time = 0
    for i, quest in enumerate(quest_list):
        print(summary_string_fmt.format(i+1 ,quest.time, quest.response))
        total_time += quest.time
        
    print("You took {0} seconds to finish the quiz".format(total_time))
    print("Your average time was {0} seconds per question".format(total_time/NUMBER_OF_QUESTIONS))
            
        
        