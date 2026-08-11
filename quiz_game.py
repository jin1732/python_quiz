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
    def __init__(self, questions):
        self.questions = questions # 여러 개의 퀴즈들을 넘겨받아 저장
        self.score = 0    

    def play(self):
            print("🍿 천만 영화 퀴즈 게임을 시작합니다! 🍿") 

         # questions 상자 안에 있는 퀴즈들을 하나씩 꺼내서 진행
        for quiz in self.question:
            quiz.display_question() # 문제 보여주기
            # 사용자에게 키보드로 정답 입력받기 (문자를 숫자로 변환하기 위해 int 사용)
            user_input = int(input("정답 번호를 입력하세요: "))
            # 정답 확인하기
            if quiz.check_answer(user_input):
                print("✅ 정답입니다!")
                self.score += 1 # 정답이면 점수 1점 증가
            else:
                print(f"❌ 땡! 정답은 {quiz.answer}번입니다.")

    # 게임이 모두 끝나면 최종 점수 출력
        print(f"\n🎉 게임 종료! 최종 점수: {self.score} / {len(self.questions)}점")


# 3. 실제로 게임 작동시키기 (실행 부분)
# 천만 영화 문제 3개를 만듭니다.
movie_quizzes = [
     Quiz("역대 한국 영화 박스오피스 1위는?", ["명량", "극한직업", "신과함께", "국제시장"], 1),
    Quiz("영화 '극한직업'에서 형사들이 위장 창업한 치킨집 이름은?", ["마약치킨", "수원왕갈비통닭", "대박치킨", "형사통닭"], 2),
    Quiz("영화 '베테랑'에서 조태오(유아인)의 명대사는?", ["묻고 더블로 가", "내가 빙다리 핫바지로 보이냐", "살려는 드릴게", "어이가 없네"], 4)
]

# 게임 매니저에게 문제 목록을 넘겨주고 게임 생성
game = QuizGame(movie_quizzes)

# 게임 시작! (버튼 누르기)
game.play()

