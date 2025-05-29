from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register_cow(data: dict):
    return {"tx_hash": "0xabc123..."}