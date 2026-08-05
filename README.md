# 파이썬 퀴즈 게임 프로젝트

파이썬을 이용한 간단한 퀴즈 게임 프로그램입니다.
---

<dr>

##  파이썬 퀴즈 프로젝트 진행 기록 (Roadmap)

### ① 프로젝트 기초 공사 (작업실 세팅)
- mkdir python_quiz: 프로젝트 폴더 생성 (내 작업실 이름 정하기)
- cd python_quiz: 폴더로 이동 (작업실 안으로 들어가기)
- git init: Git 저장소 시작 (이 폴더의 모든 변화를 기록할 준비 완료)
- git config --global user.name "손희진": 내 이름 등록 (기록자 이름 남기기)
- git config --global user.email "이메일주소": 내 이메일 등록 (기록자 연락처 남기기)

### ② 첫 기록 남기기 (로컬 저장소 저장)
- touch README.md: 프로젝트 설명서 파일 생성
- quiz_game.py 작성: 파이썬 클래스 구조와 기본 실행 코드 작성
- git add .: 변경된 모든 파일(README, py파일)을 장바구니에 담기
- git commit -m "Initial commit: 프로젝트 시작 및 README 작성": 현재 상태를 사진 찍듯 내 컴퓨터에 영구 기록 (커밋 번호: d28ac80)

### ③ 세상에 공개하기 (GitHub 연결)
- GitHub 저장소 이름 변경: my-docker3 → python_quiz로 변경 (VS 코드 폴더명과 일치시킴)
- git remote add origin https://github.com/jin1732/python_quiz.git: 내 컴퓨터와 GitHub 저장소를 연결 (원격 주소 등록)
- git branch -M main: 기본 브랜치 이름을 master에서 main으로 변경 (최신 표준)
- git push -u origin main: 내 컴퓨터의 기록을 GitHub 서버로 전송 (최종 업로드)