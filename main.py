from fastapi import FastAPI

# 1. FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 2. 첫 번째 API 엔드포인트 (루트 경로)
@app.get("/")
async def read_root():
  return {"message": "Hello World!!!, FastAPI 세상에 오신 것을 환영합니다. PyCharm에서 만들었어요."}

# 3. 이름으로 인사하는 API 엔드포인트
@app.get("/hello/{name}")
async def say_hello(name: str):
  # name 매개변수는 URL 경로에서 받아오고, 타입은 문자열(str)로 지정합니다.
  # FastAPI가 자동으로 데이터 유효성 검사도 해줍니다.
  return {"message": f"안녕하세요, {name}님! 반갑습니다."}

# PyCharm에서 실행 설정을 사용하거나, 터이멀에서 uvicorn을 직접 실행할 수 있습니다.
# 터미널에서 실행하려면: uvicorn main:app --reload