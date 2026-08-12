import json
import os
from datetime import datetime

STATE_FILE = "state.json"

default_quiz = [
    {
        "question": "1 + 1은?", 
        "options": ["1", "2", "3", "4"], 
        "answer": "2"
    },
    {
        "question": "파이썬의 창시자는?", 
        "options": ["귀도 반 로섬", "스티브 잡스", "빌 게이츠", "일론 머스크"], 
        "answer": "귀도 반 로섬"
    }
]

# 💡 복구(초기화) 기능이 완벽하게 들어간 함수
def load_quiz_data():
    try:
        # 1. 정상적으로 열기 시도
        with open("quiz.json", "r", encoding="utf-8") as file:
            return json.load(file)
            
    except FileNotFoundError:
        # 2. 파일이 없을 때 -> 안내 메시지 띄우고 파일 새로 만들기(초기화)
        print("\n🚨 경고: quiz.json 파일을 찾을 수 없습니다. 기본 퀴즈로 초기화합니다!")
        
        with open("quiz.json", "w", encoding="utf-8") as file:
            json.dump(default_quiz, file, ensure_ascii=False, indent=4) # 파일 생성!
            
        return default_quiz
        
    except json.JSONDecodeError:
        # 3. 파일이 손상되었을 때 -> 안내 메시지 띄우고 파일 덮어쓰기(복구)
        print("\n🚨 경고: quiz.json 파일이 손상되었습니다. 기본 퀴즈로 복구합니다!")
        
        with open("quiz.json", "w", encoding="utf-8") as file:
            json.dump(default_quiz, file, ensure_ascii=False, indent=4) # 파일 복구!
            
        return default_quiz
    
# 1. 퀴즈 클래스
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }
    def check_answer(self, user_input):
    # user_input은 사용자가 입력한 번호(예: "2")
        try:
            idx = int(user_input) - 1  # 1번을 입력하면 0번 인덱스
            # 선택한 번호가 범위 내에 있는지 확인
            if 0 <= idx < len(self.options):
                selected_answer = self.options[idx]
                return selected_answer == self.answer
            else:
                return False
        except ValueError:
            return False

# 2. 게임 엔진 클래스
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        self.score = 0
        print(f"\n총 {len(self.questions)}문제를 시작합니다!")
        for i, q in enumerate(self.questions, 1):
            print(f"\nQ{i}. {q.question}")
            for idx, opt in enumerate(q.options, 1):
                print(f"  {idx}) {opt}")
            
            try:
                user_ans = int(input("정답 번호를 입력하세요."))
                if q.check_answer(user_ans):
                    print("✅ 정답입니다!")
                    self.score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 '{q.answer}'입니다.")

            except (ValueError, IndexError):
                print("⚠️ 잘못된 입력입니다. 오답 처리됩니다.")
        
        print(f"\n게임 종료! 최종 점수: {self.score}/{len(self.questions)}")
        return self.score

# 3. 데이터 관리 함수들
def load_data():
    if not os.path.exists(STATE_FILE):
        initial_data = {
            "quizzes": [
                {"question": "영화 '기생충'의 감독은?", "options": ["봉준호", "박찬욱", "이창동", "연상호"], "answer": "봉준호"},
                {"question": "역대 한국 박스오피스 1위 영화는?", "options": ["명량", "극한직업", "신과함께", "국제시장"], "answer": "명량"}
            ],
            "scores": []
        }
        save_data(initial_data)
        return initial_data
    
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 1. 최고 점수 불러오기
def load_high_score():
    data = load_data()          # 학생님이 만든 함수로 데이터를 불러옵니다.
    scores = data["scores"]     # "scores" 리스트를 가져옵니다.
    
    if len(scores) > 0:         # 리스트에 점수가 하나라도 있다면?
        return max(scores)      # max() 함수로 가장 높은 점수를 찾아서 반환!
    else:
        return 0                # 아직 게임을 한 번도 안 했다면 0점 반환!

# 2. 내 점수 저장하기
def save_score(my_score):
    data = load_data()          # 1. 기존 데이터를 불러옵니다.
    data["scores"].append(my_score) # 2. "scores" 리스트에 내 점수를 추가합니다.
    save_data(data)             # 3. 변경된 데이터를 다시 파일에 저장합니다.
    
def save_score(score):
    data = load_data()
    new_score = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score
    }
    data["scores"].append(new_score)
    save_data(data)
    print("📝 점수가 저장되었습니다.")

def add_quiz():
    print("\n--- 새 퀴즈 추가 ---")
    question = input("질문을 입력하세요: ")
    options = []
    for i in range(4):
        options.append(input(f"보기 {i+1}번을 입력하세요: "))
    answer = input("정답 내용을 입력하세요 (보기 중 하나와 일치해야 함): ")
    
    data = load_data()
    new_quiz = Quiz(question, options, answer)
    data["quizzes"].append(new_quiz.to_dict())
    save_data(data)
    print("✅ 퀴즈가 추가되었습니다!")

def view_quizzes():
    data = load_data()
    print("\n--- 현재 등록된 퀴즈 목록 ---")
    for i, q in enumerate(data["quizzes"], 1):
        print(f"{i}. {q['question']}")

def show_scores():
    data = load_data()
    print("\n--- 최근 점수 기록 ---")
    if not data["scores"]:
        print("기록이 없습니다.")
    for s in data["scores"][-5:]:  # 최근 5개만 표시
        print(f"[{s['date']}] 점수: {s['score']}")

# 4. 메인 함수
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
                # 게임 시작 직전에 데이터를 새로 불러와서 객체로 변환합니다.
                data = load_data()
                movie_questions = []
                for item in data["quizzes"]:
                    movie_questions.append(Quiz(item["question"], item["options"], item["answer"]))
                
                if not movie_questions:
                    print("❌ 퀴즈가 없습니다. 먼저 추가해주세요.")
                    continue
                
                game = QuizGame(movie_questions)
                score = game.play() 
                high_score = load_high_score() # 기존 최고 점수 확인

                print(f"\n게임 종료! 이번 게임의 점수는 {score}점 입니다.")

                if score > high_score:
                    print(f"🎉 축하합니다! 최고 점수를 갱신했습니다! (기존: {high_score}점 -> 현재: {score}점) 🎉")
                else:
                    print(f"아쉽네요! 최고 점수({high_score}점)를 넘지 못했습니다.")
                    
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