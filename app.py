from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# dothome 페이지에서 호출하려면, 해당 오리진을 CORS에 허용합니다.
ALLOWED_ORIGINS = [
    "https://park5300.dothome.co.kr",
    # 개발/테스트용으로 Render 기본 도메인도 허용(원하면 삭제)
    # "https://<서비스이름>.onrender.com",
]

app = FastAPI(
    title="park5300 intro API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS or ["*"],  # 빠른 테스트는 ["*"]도 가능(운영에선 도메인 지정 권장)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/me")
def me():
    return {
        "name": "박OO",
        "title": "백엔드 개발자",
        "intro": "Python/JS를 좋아합니다. 사이드프로젝트를 즐겨요.",
        "skills": ["Python", "FastAPI", "Django", "JavaScript"],
        "links": {
            "github": "https://github.com/park5300",
            "site":   "https://park5300.dothome.co.kr"
        }
    }
