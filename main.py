from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
app=FastAPI()
@app.get("/")
def root():
    return RedirectResponse(url="/docs")
app.middleware("http")(timing_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(issues_router)





    