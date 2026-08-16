import json
import os
from datetime import datetime

from quiz import Quiz


STATE_FILE = "state.json"


class QuizGame:

    def __init__(self):
        self.questions = []
        self.score = 0
        self.scores = []

        self.load_data()

    # ---------------------------------
    # 기본 퀴즈 데이터
    # ---------------------------------
    def create_default_quizzes(self):
        return [
            Quiz(
                "영화 '명량'에서 이순신 장군 역을 맡은 배우는 누구인가요?",
                [
                    "송강호",
                    "최민식",
                    "류승룡",
                    "황정민"
                ],
                "2"
            ),

            Quiz(
                "영화 '극한직업'에서 형사들이 잠복 수사를 위해 운영한 가게의 메뉴는 무엇인가요?",
                [
                    "짜장면",
                    "피자",
                    "수원왕갈비통닭",
                    "마라탕"
                ],
                "3"
            ),

            Quiz(
                "영화 '신과함께-죄와 벌'의 주인공 김자홍의 직업은 무엇인가요?",
                [
                    "경찰관",
                    "소방관",
                    "의사",
                    "변호사"
                ],
                "2"
            ),

            Quiz(
                "영화 '국제시장'의 주요 배경이 되는 시장의 이름은 무엇인가요?",
                [
                    "자갈치시장",
                    "국제시장",
                    "부전시장",
                    "해운대시장"
                ],
                "2"
            ),

            Quiz(
                "영화 '괴물'에서 괴물이 처음 등장한 장소는 어디인가요?",
                [
                    "한강",
                    "해운대",
                    "남산",
                    "제주도"
                ],
                "1"
            ),

            Quiz(
                "영화 '광해, 왕이 된 남자'에서 주인공 하선은 어떤 일을 하던 사람인가요?",
                [
                    "광대",
                    "상인",
                    "군인",
                    "관리"
                ],
                "1"
            )
        ]

    # ---------------------------------
    # 데이터 불러오기
    # ---------------------------------
    def load_data(self):

        # state.json이 없는 경우
        if not os.path.exists(STATE_FILE):
            print("⚠️ state.json이 없습니다.")
            print("기본 퀴즈 데이터로 시작합니다.")

            self.questions = self.create_default_quizzes()
            self.scores = []

            self.save_data()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.questions = [
                Quiz(
                    item["question"],
                    item["options"],
                    item["answer"]
                )
                for item in data.get("quizzes", [])
            ]

            self.scores = data.get("scores", [])

        except json.JSONDecodeError:
            print("⚠️ state.json 파일이 손상되었습니다.")
            print("⚠️ 기본 데이터로 초기화합니다.")

            self.questions = self.create_default_quizzes()
            self.scores = []

            self.save_data()

        except OSError:
            print("⚠️ state.json 파일을 읽을 수 없습니다.")
            print("⚠️ 기본 퀴즈 데이터로 시작합니다.")

            self.questions = self.create_default_quizzes()
            self.scores = []

    # ---------------------------------
    # 데이터 저장
    # ---------------------------------
    def save_data(self):

        data = {
            "quizzes": [
                quiz.to_dict()
                for quiz in self.questions
            ],
            "scores": self.scores
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(
                    data,
                    f,
                    ensure_ascii=False,
                    indent=4
                )

        except OSError:
            print("⚠️ 데이터를 저장하는 중 오류가 발생했습니다.")

    # ---------------------------------
    # 메뉴 출력
    # ---------------------------------
    def show_menu(self):
        print("\n=== 🎬 천만 영화 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가하기")
        print("3. 퀴즈 목록 보기")
        print("4. 최근 점수 확인")
        print("5. 게임 종료")

    # ---------------------------------
    # 메뉴 입력
    # ---------------------------------
    def get_menu_choice(self):

        while True:
            try:
                raw = input(
                    "원하는 메뉴 번호를 입력하세요 (1~5): "
                ).strip()

                if raw == "":
                    print(
                        "⚠️ 아무것도 입력되지 않았어요. "
                        "번호를 입력해주세요."
                    )
                    continue

                choice = int(raw)

                if choice < 1 or choice > 5:
                    print(
                        "❌ 1~5 사이의 숫자를 입력해주세요."
                    )
                    continue

                return choice

            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")

    # ---------------------------------
    # 퀴즈 풀기
    # ---------------------------------
    def play_quiz(self):

        if not self.questions:
            print("❌ 등록된 퀴즈가 없습니다.")
            print("먼저 퀴즈를 추가해주세요.")
            return

        self.score = 0

        print(
            f"\n총 {len(self.questions)}문제를 시작합니다!"
        )

        for i, quiz in enumerate(self.questions, 1):

            print(f"\nQ{i}. {quiz.question}")

            for idx, option in enumerate(
                quiz.options,
                1
            ):
                print(f"  {idx}) {option}")

            while True:
                try:
                    raw = input(
                        "정답 번호를 입력하세요 (1~4): "
                    ).strip()

                    if raw == "":
                        print("⚠️ 번호를 입력해주세요.")
                        continue

                    user_answer = int(raw)

                    if user_answer < 1 or user_answer > 4:
                        print(
                            "⚠️ 1~4 사이의 번호를 입력해주세요."
                        )
                        continue

                    break

                except ValueError:
                    print("⚠️ 숫자만 입력해주세요.")

            if quiz.check_answer(str(user_answer)):
                print("✅ 정답입니다!")
                self.score += 1

            else:
                print(
                    f"❌ 틀렸습니다. "
                    f"정답은 {quiz.answer}번입니다."
                )

        print(
            f"\n게임 종료! "
            f"최종 점수: "
            f"{self.score}/{len(self.questions)}"
        )

        self.save_score()

    # ---------------------------------
    # 점수 저장
    # ---------------------------------
    def save_score(self):

        new_score = {
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "score": self.score
        }

        self.scores.append(new_score)

        self.save_data()

        print("📝 점수가 저장되었습니다.")

    # ---------------------------------
    # 최고 점수 확인
    # ---------------------------------
    def get_high_score(self):

        if not self.scores:
            return 0

        return max(
            score["score"]
            for score in self.scores
        )

    # ---------------------------------
    # 퀴즈 추가
    # ---------------------------------
    def add_quiz(self):

        print("\n--- 새 퀴즈 추가 ---")

        # 문제 입력
        while True:
            question = input(
                "질문을 입력하세요: "
            ).strip()

            if question == "":
                print("⚠️ 질문을 입력해주세요.")
                continue

            break

        # 보기 4개 입력
        options = []

        for i in range(4):

            while True:
                option = input(
                    f"보기 {i + 1}번을 입력하세요: "
                ).strip()

                if option == "":
                    print("⚠️ 보기를 입력해주세요.")
                    continue

                options.append(option)
                break

        # 정답 번호 입력
        while True:
            try:
                raw_answer = input(
                    "정답 번호를 입력하세요 (1~4): "
                ).strip()

                if raw_answer == "":
                    print(
                        "⚠️ 정답 번호를 입력해주세요."
                    )
                    continue

                answer = int(raw_answer)

                if answer < 1 or answer > 4:
                    print(
                        "⚠️ 1~4 사이의 번호를 입력해주세요."
                    )
                    continue

                break

            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")

        # Quiz 객체 생성
        new_quiz = Quiz(
            question,
            options,
            str(answer)
        )

        # 퀴즈 추가
        self.questions.append(new_quiz)

        # 파일 저장
        self.save_data()

        print("✅ 퀴즈가 추가되었습니다!")

    # ---------------------------------
    # 퀴즈 목록
    # ---------------------------------
    def view_quizzes(self):

        print("\n--- 현재 등록된 퀴즈 목록 ---")

        if not self.questions:
            print("❌ 등록된 퀴즈가 없습니다.")
            print(
                "먼저 '2. 퀴즈 추가하기'를 선택해주세요."
            )
            return

        for i, quiz in enumerate(
            self.questions,
            1
        ):
            print(
                f"{i}. {quiz.question}"
            )

    # ---------------------------------
    # 점수 확인
    # ---------------------------------
    def show_scores(self):

        print("\n--- 최근 점수 기록 ---")

        if not self.scores:
            print("아직 퀴즈를 푼 기록이 없습니다.")
            return

        for score in self.scores[-5:]:
            print(
                f"[{score['date']}] "
                f"점수: {score['score']}"
            )

        print(
            f"\n🏆 최고 점수: "
            f"{self.get_high_score()}점"
        )

    # ---------------------------------
    # 게임 실행
    # ---------------------------------
    def run(self):

        while True:

            self.show_menu()

            try:
                choice = self.get_menu_choice()

                if choice == 1:
                    self.play_quiz()

                elif choice == 2:
                    self.add_quiz()

                elif choice == 3:
                    self.view_quizzes()

                elif choice == 4:
                    self.show_scores()

                elif choice == 5:
                    self.save_data()

                    print(
                        "👋 게임을 종료합니다. "
                        "플레이해주셔서 감사합니다!"
                    )

                    break

            except KeyboardInterrupt:
                print(
                    "\n\n🚨 프로그램이 중단되었습니다."
                )
                print("💾 현재 데이터를 저장합니다.")

                self.save_data()

                print("👋 안전하게 종료합니다.")
                break

            except EOFError:
                print(
                    "\n\n🚨 입력이 종료되었습니다."
                )
                print("💾 현재 데이터를 저장합니다.")

                self.save_data()

                print("👋 안전하게 종료합니다.")
                break