class Quiz:
    """개별 퀴즈 정보를 담는 클래스"""
    def __init__(self, question, options, answer):
        self.question = question  # 질문
        self.options = options    # 보기 (리스트)
        self.answer = answer      # 정답

class QuizGame:
    """퀴즈 게임의 전체 흐름을 관리하는 클래스"""
    def __init__(self):
        self.quizzes = []  # 퀴즈 객체들을 담을 리스트
        self.score = 0     # 사용자의 점수

    def start_game(self):
        """게임을 시작하는 메서드"""
        print("🎮 파이썬 퀴즈 게임을 시작합니다!")
        # 여기에 나중에 퀴즈를 내는 로직을 추가할 거예요.

# 게임 실행 테스트
if __name__ == "__main__":
    game = QuizGame()
    game.start_game()