from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .services import capture_screenshot_logic

router = APIRouter(prefix="/screenshot", tags=["Screenshot Tool"])

class ScreenshotRequest(BaseModel):
    url: str

@router.post("/generate")
async def generate_ss(request: ScreenshotRequest):
    try:
        data = await capture_screenshot_logic(request.url)
        return {"success": True, "screenshots": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")