from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {
        "status": "ok",
        "engine": "riskdna",
        "version": "1.0.0"
    }
