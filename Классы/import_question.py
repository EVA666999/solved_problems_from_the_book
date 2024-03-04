import questions_quiz

def main():
    result = []
    for i in range(10):
        i += 1
        question = input(f'Вопрос {i}: ')
        A = input(f'Возможный оответ для вопроса {i}: ')
        B = input(f'Возможный оответ для вопроса {i}: ')
        C = input(f'Возможный оответ для вопроса {i}: ')
        D = input(f'Возможный оответ для вопроса {i}: ')
        real_answer = input('Каков будет ответ?')
        obj = questions_quiz.Question(question, A, B, C, D, real_answer )
        result.append(obj)

    resukt_for_player_1 = result[:5]
    result_for_player_2 = result[5:]
    for i in resukt_for_player_1:
        print(f'Вопрос для первого игрока: {i.get_question()}\n' + \
              f'Ответы для первого игрока: {i.get_answer()}\n' + \
              f'Правильный ответ для первого игрока: {i.get_real_answer()}')
    for i in result_for_player_2:
        print(f'Вопрос для второго игрока: {i.get_question()}\n' + \
              f'Ответы для второго игрока: {i.get_answer()}\n' + \
              f'Правильный ответ для второго игрока: {i.get_real_answer()}')
        
    def player_1():
        count = 0
        for i in resukt_for_player_1:
            ask = input(f'Какой ответ для вопроса {i.get_question()}:\n' + \
                        f'Варианты ответа: {i.get_answer()}')
            if ask == i.get_real_answer():
                count += 1
        return count
    
    def player_2():
        count = 0
        for i in result_for_player_2:
            ask = input(f'Какой ответ для вопроса {i.get_question()}:\n' + \
                        f'Варианты ответа: {i.get_answer()}')
            if ask == i.get_real_answer():
                count += 1
        return count
    
    def winer():
        a = player_1()
        b = player_2()
        if a > b:
            return f'Выйграл первый игрок! у него {a} очков а у второго {b} очков'
        elif b > a:
            return f'Выйграл второй игрок! у него {b} очков а у первого {a} очков'
        else:
            return f'Ничья {a, b}'
    
    print(winer())

if __name__ == '__main__':

    main()
