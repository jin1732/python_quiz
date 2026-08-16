from quiz import Quiz
from quizgame import QuizGame
from quizgame import load_data
from quizgame import load_high_score
from quizgame import save_score
from quizgame import add_quiz
from quizgame import view_quizzes
from quizgame import show_scores

def main():
    while True:
        print("\n=== 🎬 천만 영화 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가하기")
        print("3. 퀴즈 목록 보기")
        print("4. 최근 점수 확인")
        print("5. 게임 종료")
    
        try:
            choice = input("원하는 메뉴 번호를 입력하세요 (1~5): ").strip()
            
            if choice == "":
                print("⚠️ 아무것도 입력되지 않았어요. 번호를 입력해주세요.")
                continue
                
            if choice == "1":
                data = load_data()

                movie_questions = []

                for item in data["quizzes"]:
                    movie_questions.append(
                        Quiz(
                            item["question"], 
                            item["options"], 
                            item["answer"]
                        )
                    )
                
                if not movie_questions:
                    print("❌ 퀴즈가 없습니다. 먼저 추가해주세요.")
                    continue
                
                game = QuizGame(movie_questions)
                score = game.play() 

                high_score = load_high_score() # 기존 최고 점수 확인

                print(f"\n게임 종료! 이번 게임의 점수는 {score}점 입니다.")

                if score > high_score:
                    print(
                        f"🎉 축하합니다! 최고 점수를 갱신했습니다! "
                        f"(기존: {high_score}점 -> 현재: {score}점) 🎉"
                    )
                else:
                    print(
                        f"아쉽네요! 최고 점수({high_score}점)를 넘지 못했습니다."
                    )
                    
                save_score(score) 

            elif choice == '2':
                add_quiz()

            elif choice == '3':
                view_quizzes()

            elif choice == '4':
                show_scores()

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