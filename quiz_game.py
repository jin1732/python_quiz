class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    # 메서드 1: 퀴즈 출력 (문제와 4개의 보기를 화면에 보여줌)
    def display(self):
        print(f"\n 문제: {self.question}")
        for i in range(4):
            print(f"{i+1}.{self.options[i]}")

    # 메서드 2: 정답 확인 (사용자가 입력한 답과 정답이 맞는지 확인)
    def check_answer(self, user_answer):
        if user_answer == self.answer:
            return True
        else:
            return False

class QuizGame:
    def __init__(self):
        self.quizzes = [] 
        self.score = 0    

    def start_game(self):
        print("게임을 시작합니다!") 

if __name__ == "__main__":
    game = QuizGame()
    game.start_game() 

    # 보기(options)가 들어간 퀴즈 객체를 하나 만들어봅니다.
    test_quiz = Quiz("파이썬의 창시자는?", ["1. 스티브 잡스", "2. 귀도 반 로섬", "3. 일론 머스크"], 2)

    print("\n--- 임시 데이터 테스트 ---")
    print("질문:", test_quiz.question)
    print("보기:", test_quiz.options)
    print("정답 번호:", test_quiz.answer)
    print("테스트 성공! 클래스가 완벽하게 작동합니다. 🎉")