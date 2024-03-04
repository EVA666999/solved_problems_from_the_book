class Question:
    
    def __init__(self, question, A, B, C, D, real_answer) -> None:
        self.__question = question
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
        self.__real_answer = real_answer

    def set_question(self, question):
        self.__question = question

    def get_question(self):
        return self.__question
    

    def set_ansere(self, A, B, C, D):
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
    
    def get_answer(self):
        return self.__A, self.__B, self.__C, self.__D
    
    def set_real_answer(self, real_answer):
        self.__real_answer = real_answer

    def get_real_answer(self):
        return self.__real_answer 