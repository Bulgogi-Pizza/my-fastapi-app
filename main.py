from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union # Union 타입을 사용하기 위해 가져온다. (Python 3.9 이하는 Optional을 사용하려면 from typing import Optional)

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# --- Pydantic 모델 정의 ---
class Item(BaseModel):
  name: str
  description: Union[str, None] = None # 설명은 선택 사항 (문자열 또는 None)
  price: float
  tax: Union[float, None] = None # 세금도 선택 사항 (실수 또는 None)

# --- 기존 엔드포인트들 ---
@app.get("/")
async def read_root():
  return {"message": "Hello World!!!, FastAPI 세상에 오신 것을 환영합니다. PyCharm에서 만들었어요."}

@app.get("/hello/{name}")
async def say_hello(name: str):
  # name 매개변수는 URL 경로에서 받아오고, 타입은 문자열(str)로 지정합니다.
  # FastAPI가 자동으로 데이터 유효성 검사도 해줍니다.
  return {"message": f"안녕하세요, {name}님! 반갑습니다."}

# PyCharm에서 실행 설정을 사용하거나, 터이멀에서 uvicorn을 직접 실행할 수 있습니다.
# 터미널에서 실행하려면: uvicorn main:app --reload
# http://localhost:8000/docs - swagger UI 자동 제공
# http://localhost:8000/redoc - ReDoc 자동 제공

# --- 새로운 POST 엔드포인트 추가 ---
@app.post("/items")
async def create_item(item: Item): # 요청 본문을 Item 모델로 받는다.
  # 지금은 받은 아이템 그대로 반환한다.
  # 실제 앱은 이 데이터를 데이터베이스에 저장할 것이다.
  return item