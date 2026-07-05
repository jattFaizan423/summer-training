from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import init_db
from app.routers import auth, patients


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Patient Management API", lifespan=lifespan)

app.include_router(patients.router)
app.include_router(auth.router)


@app.get("/", tags=["meta"], summary="API root")
def root() -> dict[str, str]:
    return {"message": "Patient Management API - see /docs"}


@app.get("/health", tags=["meta"], summary="Health check")
def health() -> dict[str, str]:
    return {"status": "ok"}
