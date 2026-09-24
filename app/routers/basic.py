from fastapi import APIRouter

router = APIRouter(prefix="/basic")


# param_id is url param, whereas catgeory & llmit are query params
@router.get("/{param_id}")
async def basic_params(param_id: int, category: str | None = None, limit: int = 10):
  return {
    "param_id": param_id,
    "category": category,
    "limit": limit,
  }

# route with multiple params
@router.get("/{category}/details/{category_id}")
async def multiple_params(category: str, category_id: int):
  return {
    "category": category,
    "category_id": category_id,
  }
