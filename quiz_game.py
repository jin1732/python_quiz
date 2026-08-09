# 1. 개별 퀴즈 데이터를 담는 클래스 (퀴즈 붕어빵 틀)
class Quiz:
    # 퀴즈가 만들어질 때 질문, 보기, 정답을 초기화(세팅)하는 메서드
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

# 2. 퀴즈 게임 전체 흐름을 관리하는 클래스 (게임기)
class QuizGame:
     # 게임기가 켜질 때 초기 상태를 세팅하는 메서드
    def __init__(self):
        self.quizzes = [] # 여러 개의 퀴즈(Quiz 객체)를 담아둘 빈 주머니(리스트)
        self.score = 0    # 플레이어의 현재 점수 (0점으로 시작)

    # 게임을 시작하는 기능을 가진 메서드
    def start_game(self):
        print("게임을 시작합니다!") # 화면에 시작 메시지 출력

# 3. 프로그램 실행 부분(파이썬 파일이 직접 실행될 때만 아래 코드를 작동)
if __name__ == "__main__":
    game = QuizGame() # QuizGame 클래스(틀)를 이용해 'game'이라는 실제 게임기(객체) 생성
    game.start_game() # 만들어진 게임기의 start_game() 기능 실행

    # 보기(options)가 들어간 퀴즈 객체를 하나 만들어봅니다.
    test_quiz = Quiz("파이썬의 창시자는?", ["1. 스티브 잡스", "2. 귀도 반 로섬", "3. 일론 머스크"], 2)

    print("\n--- 임시 데이터 테스트 ---")
    print("질문:", test_quiz.question)
    print("보기:", test_quiz.options)
    print("정답 번호:", test_quiz.answer)
    print("테스트 성공! 클래스가 완벽하게 작동합니다. 🎉")