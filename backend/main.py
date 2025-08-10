
import os
from openai import AsyncOpenAI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- OpenAI API Key 설정 ---
# 환경 변수에서 API 키를 로드합니다.
# 이 코드를 실행하기 전에 터미널에서 `set OPENAI_API_KEY=your_api_key`를 실행해야 합니다.
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY 환경 변수를 설정해주세요.")

client = AsyncOpenAI(api_key=api_key)

# --- FastAPI 애플리케이션 설정 ---
app = FastAPI()

# CORS 설정: React 개발 서버(보통 localhost:3000)에서의 요청을 허용합니다.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 허용할 출처
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

# --- 데이터 모델 정의 ---
# 프론트엔드에서 받을 요청 본문의 형식을 정의합니다.
class ChatRequest(BaseModel):
    message: str
    history: list[dict] # 이전 대화 기록을 받기 위한 필드

# --- API 엔드포인트 정의 ---
@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    사용자의 메시지를 받아 OpenAI 챗봇의 응답을 반환하는 API
    """
    try:
        # 시스템 메시지와 이전 대화 기록, 그리고 새 사용자 메시지를 결합
        messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ] + request.history + [
            {"role": "user", "content": request.message}
        ]

        chat_completion = await client.chat.completions.create(
            messages=messages,
            model="gpt-4o-mini",
        )
        response_message = chat_completion.choices[0].message.content
        return {"reply": response_message}
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "API 호출 중 오류가 발생했습니다."}, 500

