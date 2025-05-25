# My FastAPI App (my-fastapi-app)

이 프로젝트는 학습 목적으로 생성된 기본적인 FastAPI 애플리케이션입니다. FastAPI 서버의 기본 설정과 간단한 API 엔드포인트 구현을 보여줍니다.

## ✨ 주요 기능

* 환영 메시지를 반환하는 루트 엔드포인트 (`/`)
* 개인화된 인사말을 반환하는 `/hello/{name}` 엔드포인트
* Swagger UI (`/docs`) 및 ReDoc (`/redoc`)을 통한 자동 API 문서 제공

## ⚙️ 사전 준비 사항

* Python 3.7 이상 (이 프로젝트는 Python 3.9 환경에서 개발되었습니다.)
* `pip` (파이썬 패키지 설치 관리자)

## 🚀 설치 및 실행 방법

1.  **GitHub 저장소 복제 (Clone):**
    아직 GitHub에 올리지 않았다면, 올린 후에 실제 저장소 URL로 바꿔주세요.
    ```bash
    git clone [https://github.com/YOUR_USERNAME/my-fastapi-app.git](https://github.com/YOUR_USERNAME/my-fastapi-app.git) 
    cd my-fastapi-app
    ```
    *(주의: 위 `https://github.com/YOUR_USERNAME/my-fastapi-app.git` 부분을 실제 본인의 GitHub 저장소 주소로 변경해주세요!)*

2.  **가상 환경 생성 및 활성화:**
    프로젝트 폴더 내에서 다음 명령어를 실행합니다.
    ```bash
    # Python venv 모듈 사용 (권장)
    python -m venv venv
    ```
    가상 환경 활성화:
    * Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **의존성 패키지 설치:**
    프로젝트에 필요한 패키지들을 설치합니다. 먼저, `requirements.txt` 파일을 생성하는 것이 좋습니다. 가상 환경이 활성화된 상태에서 다음 명령을 실행하여 현재 설치된 패키지 목록으로 `requirements.txt` 파일을 생성할 수 있습니다:
    ```bash
    pip freeze > requirements.txt
    ```
    이제 `requirements.txt` 파일을 사용하여 의존성을 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```
    만약 `requirements.txt` 파일을 아직 만들지 않았다면, 직접 주요 패키지를 설치할 수도 있습니다:
    ```bash
    pip install fastapi "uvicorn[standard]"
    ```

4.  **애플리케이션 실행:**
    가상 환경이 활성화된 상태에서 Uvicorn을 사용하여 FastAPI 애플리케이션을 실행합니다:
    ```bash
    uvicorn main:app --reload
    ```
    애플리케이션은 `http://127.0.0.1:8000` 주소에서 실행됩니다. `--reload` 옵션은 코드 변경 시 서버를 자동으로 재시작해줍니다.

## 📖 API 엔드포인트

현재 다음과 같은 API 엔드포인트를 사용할 수 있습니다:

* **`GET /`**
    * 설명: 기본적인 환영 메시지를 반환합니다.
    * 요청 예시: `http://127.0.0.1:8000/`
    * 응답 예시:
        ```json
        {
          "message": "안녕하세요! FastAPI 세상에 오신 것을 환영합니다. PyCharm에서 만들었어요! 🎉"
        }
        ```

* **`GET /hello/{name}`**
    * 설명: URL 경로로 전달된 이름을 사용하여 개인화된 인사말을 반환합니다.
    * 경로 매개변수:
        * `name` (string): 인사말에 포함될 이름.
    * 요청 예시: `http://127.0.0.1:8000/hello/주니어개발자`
    * 응답 예시:
        ```json
        {
          "message": "안녕하세요, 주니어개발자님! 반갑습니다."
        }
        ```

### 📚 자동 생성 API 문서

FastAPI는 자동으로 대화형 API 문서를 제공합니다. 다음 URL을 통해 접근할 수 있습니다:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

---

이 README 파일은 `my-fastapi-app` 프로젝트를 시작하는 데 필요한 기본적인 안내를 제공합니다. 즐거운 코딩 되세요!