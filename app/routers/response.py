from fastapi import APIRouter
from pydantic import BaseModel, Field

# from schemas import ApiResponse would fail when run
# from the project root.
from app.schemas import ApiResponse


class UserCreate(BaseModel):
  name: str = Field(min_length=2, max_length=50)
  email: str
  age: int = Field(ge=18)
  password: str = Field(min_length=18)


router = APIRouter()


# Return annotation doubles as response_model, and returning the model
# (not a dict) lets the type checker flag unknown or mistyped fields.
@router.post("/users/create", status_code=201)
def create_user(user_details: UserCreate) -> ApiResponse[UserCreate]:
  return ApiResponse(
    status_code=201,
    message="User created",
    data=user_details,
  )
