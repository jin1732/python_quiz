import json #맨 윗줄에 json 모듈 불러오기
# 1. 클래스들 (Quiz, QuizGame)
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

            while True:
                try:
                    raw = input("정답 번호를 입력하세요 (1~4): ").strip()

                    if raw == "":  
                        print("⚠️ 번호를 입력해주세요.")
                        continue

                    user_input = int(raw)  

                    if user_input < 1 or user_input > 4: 
                        print("⚠️ 1~4 사이의 번호만 입력할 수 있어요.")
                        continue

                    break  

                except ValueError:  
                    print("⚠️ 숫자만 입력해주세요! (예: 1)")

            if quiz.check_answer(user_input):
                print("✅ 정답입니다! 🎉")
                self.score += 1
            else:
                print(f"❌ 땡! 오답입니다. 😢 (정답은 {quiz.answer}번)")

        print(f"\n게임 종료! 최종 점수 {self.score} / {len(self.questions)}점 입니다.")

        if self.score == len(self.questions):
            print("🏆 완벽합니다! 당신은 진정한 천만 영화 마스터!")
        elif self.score >= 3:
            print("👍 훌륭합니다! 영화를 꽤 좋아하시는군요!")
        else:
            print("🎬 아쉽네요. 이번 주말엔 영화 감상 어떠신가요?")
# 2. 도구 함수 (데이터 불러오기)
def load_quizzes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    quiz_list = []
    for item in data:
        quiz = Quiz(item["question"], item["options"], item["answer"])
        quiz_list.append(quiz)
    return quiz_list

# 3. 메인 실행 함수 (프로그램의 전체 흐름)
def main():
    # 여기서 load_quizzes를 호출합니다!
    movie_questions = load_quizzes("quizzes.json")
    if not movie_questions:
        return # 데이터 없으면 종료

    game = QuizGame(movie_questions)

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
                game.play()  
            elif choice == '2':
                print("🛠️ 퀴즈 추가 기능은 아직 준비 중입니다.")
            elif choice == '3':
                print("🛠️ 퀴즈 목록 보기 기능은 아직 준비 중입니다.")
            elif choice == '4':
                print("🛠️ 최근 점수 확인 기능은 아직 준비 중입니다.")
            elif choice == '5':
                print("👋 게임을 종료합니다. 플레이해주셔서 감사합니다!")
                break  
            else:
                print("❌ 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
                
        except KeyboardInterrupt:
            print("\n\n🚨 강제 종료되었습니다. 안녕히 가세요!")
            break
        except EOFError:
            print("\n\n🚨 입력이 끊겼습니다. 게임을 종료합니다.")
            break

if __name__ == "__main__":
    main()