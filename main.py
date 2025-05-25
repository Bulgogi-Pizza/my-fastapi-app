from fastapi import FastAPI
from routers import items_api

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(
    title="나의 첫 FastAPI 프로젝트",
    description="FastAPI의 기본 기능들을 학습하며 만들어보고 있습니다. API 라우터와 문서 강화 기능을 적용했습니다.",
    version="0.2.0"
)

app.include_router(
    items_api.router, # items_api.py 파일 안에 있는 router 객체를 지정합니다.
    prefix="/api/v1", # 이 라우터의 모든 API 경로 앞에 /api/v1 접두사를 붙입니다.
    tags=["Items API - v1"] # 이 라우터의 모든 API에 Items API - v1 태그를 적용합니다.
)

@app.get(
    "/",
    tags=["General"],
    summary="Root Path",
    description="Returns a simple welcome message to the API"
)
async def read_root():
  return {"message": "Hello World!!!, FastAPI 세상에 오신 것을 환영합니다. PyCharm에서 만들었어요."}

@app.get(
    "/hello/{name}",
    tags=["General"],
    summary="Personalized Greeting",
    description="Returns a Personalized greeting to the given name"
)
async def say_hello(name: str):
  return {"message": f"안녕하세요, {name}님! 반갑습니다."}

# PyCharm에서 실행 설정을 사용하거나, 터이멀에서 uvicorn을 직접 실행할 수 있습니다.
# 터미널에서 실행하려면: uvicorn main:app --reload
# http://localhost:8000/docs - swagger UI 자동 제공
# http://localhost:8000/redoc - ReDoc 자동 제공
