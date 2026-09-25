from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

# EmailStr needs to be installed separately using
# pip3 install "pytantic[email]"
from pydantic import BaseModel, EmailStr, Field

# from schemas import ApiResponse would fail when run
# from the project root.
from app.schemas import ApiResponse


class AddressDetails(BaseModel):
  city: str = Field(min_length=2)
  country: str = Field(min_length=2)
  pincode: str = Field(min_length=5, max_length=10)


class UserCreate(BaseModel):
  name: str = Field(min_length=2, max_length=50)
  email: EmailStr
  age: int = Field(ge=18)
  password: str = Field(min_length=8)
  address: AddressDetails


router = APIRouter()


# Return annotation doubles as response_model, and returning the model
# (not a dict) lets the type checker flag unknown or mistyped fields.
@router.post("/users/create", response_model=ApiResponse[UserCreate])
def create_user(user_details: UserCreate):
  return ApiResponse(
    status_code=status.HTTP_201_CREATED,
    message="User created",
    data=user_details,
  )


@router.get("/error")
def return_error():
  return JSONResponse(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    # This object is returned when I hit this endpoint in the browser
    # I also returned a string value in the content and it worked.
    content={
      "success": False,
      "message": "An error occured on the server",
      "data": None,
    },
  )
