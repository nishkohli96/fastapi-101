from enum import Enum

from fastapi import APIRouter, Path, Query


class OrderStatus(Enum):
  PENDING = "pending"
  COMPLETED = "completed"
  CANCELLED = "cancelled"


router = APIRouter(prefix="/basic")


# param_id is url param, whereas catgeory & limit are query params
@router.get("/{param_id}")
def basic_params(
  param_id: int,
  category: str | None = None,
  limit: int = 10,
):
  """Route description in swagger"""
  return {
    "param_id": param_id,
    "category": category,
    "limit": limit,
  }


# route with multiple params
@router.get("/{category}/details/{category_id}")
def multiple_params(
  category: str,
  category_id: int,
):
  return {
    "category": category,
    "category_id": category_id,
  }


# Validation of params and queryParams.
# If it fails, FastAPI rejects it before calling the handlder
@router.get("/user-details/{user_id}")
def return_username(
  user_id: int = Path(ge=1),
  role: str = Query(min_length=3, max_length=10),
  slug: str = Query(pattern="^[a-zA-Z0-9_]+$"),
  logs: int = Query(default=10, ge=1, le=100),
  order_status: OrderStatus = OrderStatus.PENDING
):
  return {
    "username": user_id,
    "role": role,
    "slug": slug,
    "logs": logs,
    "order_status": order_status
  }
