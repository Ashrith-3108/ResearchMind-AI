from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router


app = FastAPI(
    title="ResearchMind AI API",
    description="Industry-grade Multi-Agent Research Paper Analysis System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

app.include_router(router)

# ---------------------------------------------------------
# Root
# ---------------------------------------------------------


@app.get("/")
def root():

    return {
        "application": "ResearchMind AI",
        "version": "1.0.0",
        "status": "Running",
        "documentation": "/docs",
    }


# ---------------------------------------------------------
# Health
# ---------------------------------------------------------


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "ResearchMind AI",
    }