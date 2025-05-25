from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Union # Union 타입을 사용하기 위해 가져온다. (Python 3.9 이하는 Optional을 사용하려면 from typing import Optional)

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# --- Pydantic 모델 정의 ---
class Item(BaseModel):
  name: str = Field(
      ...,
      title="Item Name",
      description="The name of the item. Must be between 3 and 50 characters",
      min_length=3,
      max_length=50
  )
  description: Union[str, None] = Field(
      default=None,
      title="Item Description",
      description="An optional description of the item. Max 200 Characters",
      min_length=200
  ) # 설명은 선택 사항 (문자열 또는 None)
  price: float = Field(
      ...,
      gt=0, # gt = greater than. 0보다 커야 합니다.
      title="Item Price",
      description="The price of the item. Must be greater than zero"
  )
  tax: Union[float, None] = Field(
      default=None,
      ge=0, # greater than or equal to. 0보다 크거나 같아야 합니다
      title="Item Tax",
      description="An optional tax for the item. Must be non-negative if provided"
  ) # 세금도 선택 사항 (실수 또는 None)

# --- 기존 엔드포인트들 ---
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
  # name 매개변수는 URL 경로에서 받아오고, 타입은 문자열(str)로 지정합니다.
  # FastAPI가 자동으로 데이터 유효성 검사도 해줍니다.
  return {"message": f"안녕하세요, {name}님! 반갑습니다."}

# PyCharm에서 실행 설정을 사용하거나, 터이멀에서 uvicorn을 직접 실행할 수 있습니다.
# 터미널에서 실행하려면: uvicorn main:app --reload
# http://localhost:8000/docs - swagger UI 자동 제공
# http://localhost:8000/redoc - ReDoc 자동 제공

# --- 새로운 POST 엔드포인트 추가 ---
# @app.post("/items")
# async def create_item(item: Item): # 요청 본문을 Item 모델로 받는다.
#   # 지금은 받은 아이템 그대로 반환한다.
#   # 실제 앱은 이 데이터를 데이터베이스에 저장할 것이다.
#   return item

# POST 엔드포인트 수정: response_model=Item 추가
@app.post(
    "/items/",
    response_model=Item,
    tags=["Items"],
    summary="Create an Item",
    description="""
Create an item with all the information:
- **name**: Each item must have a name (3 to 50 characters).
- **description**: Optional description (max 200 characters).
- **price**: Price must be greater than zero.
- **tax**: Optional tax, must be non-negative if provided.
    """,
    response_description="The item that was successfully created, conforming to the Item model."
)
async def create_item(item: Item): # 요청 본문은 Item 모델로 받습니다.
  # 'item'은 클라이언트로부터 받은 Item 모델의 인스턴스입니다.

  # 여기서 우리는 item 객체를 바로 반환합니다.
  # FastAPI는 reponse_model=Item 설정에 따라
  # 이 item 객체를 Item 스키마에 맞춰 JSON으로 직렬화하여 응답한디ㅏ.
  # 만약 item 객체에 Item 모델에 정의되지 않은 추가 속성이 있더라도,
  # response_model 덕분에 그 속성들은 최종 응답에서 필터링됩니다.

  # 데이터 필터링 기능을 더 명확히 보여주기 위한 예시:
  # 함수 내부에서 처리된 데이터가 Item 모델에 없는 추가 정보를 포함하고 있다고 가정해 봅시다.
  processed_data_with_extra_info = item.model_dump() # Pydantic 모델을 딕셔너리로 변환
  processed_data_with_extra_info["server_secret_code"] = "XYZ123_SECRET" # Item 모델에는 없는 필드
  processed_data_with_extra_info["item_statis"] = "processing" # Item 모델에는 없는 필드

  # 만약 위 processed_data_with_extra_info 딕셔너리를 반환하면,
  # FastAPI는 response_model=Item 에 정의된 필드들만 포함하여 응답을 구성합니다.
  # 즉, "server_secret_code"와 "item_status"는 최종 HTTP 응답에서 제외됩니다.

  print(f"서버 내부에서 처리된 데이터: {processed_data_with_extra_info}") # 로그 확인용

  # 하지만 지금은 위 딕셔너리 대신, 원래의 item 객체를 반환해서
  # response_model이 어떻게 동작하는기 기본적인 부분을 보겠습니다.
  # Pydantic 모델 객체를 반환하면, response_model에 정의된 필드만 직렬화됩니다.
  return item # 이 item 객체는 이미 Item 모델의 형태를 따릅니다.

# 쿼리 매개변수를 사용하는 새로운 GET 엔드포인트
@app.get(
    "/items_list/",
    tags=["Items"], # "Items" 태그로 그룹화합니다.
    summary="Read a List of Items",
    description="Retrieve a list of items. You can use `q` for searching by name, and `skip` & `limit` for pagination.",
    response_description="A dictionary containing the query parameters used and a list of items on the current page."
)
async def read_items_list(q: Union[str, None] = None, skip: int = 0, limit: int = 10):
  # q: 검색을 위한 선택적 문자열 쿼리 매개변수
  # skip: 건너뛸 아이템 수, 기본값 0
  # limit: 반환할 최대 아이템 수, 기본값 10

  # 실제 애플리케이션에서는 이 값들을 사용해서 데이터베이스에서 데이터를 조회하겠지만
  # 여기서는 간단히 받은 쿼리 매개변수들과 함께 가상의 아이템 목록을 반환해 봅시다.

  fake_items_db = [
    {"id": 1, "name": "노트북"},
    {"id": 2, "name": "마우스"},
    {"id": 3, "name": "키보드"},
    {"id": 4, "name": "모니터"},
    {"id": 5, "name": "USB 허브"},
    {"id": 6, "name": "웹캠"},
    {"id": 7, "name": "노이즈캔슬링 헤드폰"},
    {"id": 8, "name": "스마트폰"},
    {"id": 9, "name": "태블릿"},
    {"id": 10, "name": "블루투스 스피커"}
  ]

  current_items = fake_items_db

  if q:
    current_items = [item for item in current_items if q.lower() in item["name"].lower()]

  # skip과 limit 적용
  paginated_items = current_items[skip: skip + limit]

  return {"query_parameters": {"q": q, "skip": skip, "limit": limit}, "items_on_this_page": paginated_items}

