# OpenAI 챗봇 애플리케이션 (React & FastAPI)

이 프로젝트는 React와 FastAPI를 사용하여 구축된 웹 기반 챗봇 애플리케이션입니다. OpenAI의 `gpt-4o-mini` 모델을 백엔드에서 호출하여 사용자와 실시간으로 대화하는 기능을 제공합니다.

## ✨ 주요 기능

-   **실시간 채팅 인터페이스**: 사용자와 챗봇 간의 메시지를 실시간으로 주고받는 깔끔한 UI
-   **대화 기록 유지**: 현재 세션 내에서 이전 대화의 맥락을 기억하고 이어가는 기능
-   **비동기 처리**: FastAPI를 통해 여러 사용자의 요청을 효율적으로 처리
-   **역할 분리 아키텍처**: 프론트엔드와 백엔드가 명확하게 분리되어 유지보수 및 확장 용이

## 🛠️ 기술 스택

-   **프론트엔드**:
    -   [React](https://reactjs.org/)
    -   JavaScript
    -   CSS
-   **백엔드**:
    -   [FastAPI](https://fastapi.tiangolo.com/)
    -   [Python](https://www.python.org/)
    -   [OpenAI API](https://platform.openai.com/docs/api-reference)
    -   [Uvicorn](https://www.uvicorn.org/)

## 📂 프로젝트 구조

```
chatbot-project/
├── backend/
│   ├── main.py         # FastAPI 애플리케이션 로직
│   └── requirements.txt  # Python 의존성 목록
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js      # React 메인 컴포넌트
│   │   ├── App.css     # App 컴포넌트 스타일
│   │   └── index.js    # React 앱 진입점
│   └── package.json    # Node.js 의존성 및 스크립트
└── README.md           # 프로젝트 안내 파일
```

## 🚀 설치 및 실행 방법

이 프로젝트를 로컬 환경에서 실행하기 위해 다음 단계를 따르세요.

### 사전 준비

-   [Node.js](https://nodejs.org/en/) 및 npm 설치
-   [Python](https://www.python.org/downloads/) 3.8 이상 설치
-   OpenAI API 키 발급

### 1. 백엔드 서버 설정

첫 번째 터미널을 열고 다음을 실행하세요.

```bash
# 1. 백엔드 폴더로 이동
cd C:\Users\rmsgh\chatbot-project\backend

# 2. 필요한 파이썬 라이브러리 설치
pip install -r requirements.txt

# 3. OpenAI API 키를 환경 변수로 설정
# Windows (CMD)
set OPENAI_API_KEY=sk-your_openai_api_key_here

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-your_openai_api_key_here"

# 4. 백엔드 서버 실행
uvicorn main:app --reload
```

서버가 `http://127.0.0.1:8000`에서 실행됩니다.

### 2. 프론트엔드 앱 설정

두 번째 새 터미널을 열고 다음을 실행하세요.

```bash
# 1. 프론트엔드 폴더로 이동
cd C:\Users\rmsgh\chatbot-project\frontend

# 2. 필요한 노드 모듈 설치
npm install

# 3. 리액트 개발 서버 실행
npm start
```

앱이 `http://localhost:3000`에서 자동으로 열립니다. 이제 브라우저에서 챗봇과 대화를 시작할 수 있습니다.
