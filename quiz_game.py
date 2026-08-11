class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print(f"\n문제: {self.question}")
        for i in range(len(self.options)):
            print(f"{i+1}. {self.options[i]}")

    def check_answer(self, user_answer):
        if user_answer == self.answer:
            return True
        else:
            return False

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        self.score = 0
        print("\n🍿 천만 영화 퀴즈 게임을 시작합니다! 🍿")

        for quiz in self.questions:
            quiz.display()

            # 💡 올바른 정답을 입력할 때까지 계속 물어보는 반복문
            while True:
                try:
                    raw = input("정답 번호를 입력하세요 (1~4): ").strip()

                    if raw == "":  # 빈 입력 처리
                        print("⚠️ 번호를 입력해주세요.")
                        continue

                    user_input = int(raw)  # 문자 -> 숫자 변환

                    if user_input < 1 or user_input > 4:  # 범위 벗어남 처리
                        print("⚠️ 1~4 사이의 번호만 입력할 수 있어요.")
                        continue

                    break  # 정상 입력 -> while 탈출하고 채점으로 넘어감

                except ValueError:  # abc처럼 숫자 변환 실패 시
                    print("⚠️ 숫자만 입력해주세요! (예: 1)")

            # 채점
            if quiz.check_answer(user_input):
                print("✅ 정답입니다! 🎉")
                self.score += 1
            else:
                print(f"❌ 땡! 오답입니다. 😢 (정답은 {quiz.answer}번)")

        # 결과 출력
        print(f"\n게임 종료! 최종 점수 {self.score} / {len(self.questions)}점 입니다.")

        if self.score == len(self.questions):
            print("🏆 완벽합니다! 당신은 진정한 천만 영화 마스터!")
        elif self.score >= 3:
            print("👍 훌륭합니다! 영화를 꽤 좋아하시는군요!")
        else:
            print("🎬 아쉽네요. 이번 주말엔 영화 감상 어떠신가요?")


# --- 🎬 1. 퀴즈 데이터 준비 ---
movie_questions = [
    Quiz("영화 '명량'에서 이순신 장군 역을 맡은 배우는?", ["송강호", "최민식", "류승룡", "황정민"], 2),
    Quiz("영화 '극한직업'에서 형사들이 위장 창업한 가게의 메뉴는?", ["짜장면", "피자", "수원왕갈비통닭", "마라탕"], 3),
    Quiz("영화 '신과함께-죄와 벌'에서 주인공 자홍의 직업은?", ["경찰", "소방관", "의사", "변호사"], 2),
    Quiz("영화 '국제시장'의 배경이 되는 부산의 시장 이름은?", ["자갈치시장", "국제시장", "부전시장", "해운대시장"], 2),
    Quiz("영화 '괴물'에서 괴물이 나타난 장소는?", ["한강", "해운대", "남산", "제주도"], 1)
]

# --- 🎮 2. 게임 객체 생성 ---
game = QuizGame(movie_questions)


# --- 🖥️ 3. 메인 메뉴 시스템 (무한 반복) ---
while True:
    print("\n=== 🎬 천만 영화 퀴즈 게임 ===")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가하기 (준비 중)")
    print("3. 퀴즈 목록 보기 (준비 중)")
    print("4. 최근 점수 확인 (준비 중)")
    print("5. 게임 종료")
    
    try:
        choice = input("원하는 메뉴 번호를 입력하세요 (1~5): ").strip()
        
        if choice == "":
            print("⚠️ 아무것도 입력되지 않았어요. 번호를 입력해주세요.")
            continue
            
        if choice == '1':
            game.play()  # 퀴즈 게임 실행!
        elif choice == '2':
            print("🛠️ 퀴즈 추가 기능은 아직 준비 중입니다.")
        elif choice == '3':
            print("🛠️ 퀴즈 목록 보기 기능은 아직 준비 중입니다.")
        elif choice == '4':
            print("🛠️ 최근 점수 확인 기능은 아직 준비 중입니다.")
        elif choice == '5':
            print("👋 게임을 종료합니다. 플레이해주셔서 감사합니다!")
            break  # while 반복문 탈출 -> 프로그램 종료
        else:
            print("❌ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
            
    except KeyboardInterrupt:
        print("\n\n🚨 강제 종료되었습니다. 안녕히 가세요!")
        break
    except EOFError:
        print("\n\n🚨 입력이 끊겼습니다. 게임을 종료합니다.")
        break