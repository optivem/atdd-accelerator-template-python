from fastapi import APIRouter


echo_api_router = APIRouter()


@echo_api_router.get("/echo")
async def echo() -> str:
    """Simple echo endpoint that returns 'Echo'."""
    return "Echo"