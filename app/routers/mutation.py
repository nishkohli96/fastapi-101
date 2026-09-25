from fastapi import APIRouter, Path, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/mutation", tags=["Mutation"])


class ProductCreate(BaseModel):
  name: str
  price: float
  # optional field
  category: str | None = None
  # field with default value
  stock: int = 1


class Supplier(BaseModel):
  name: str
  country: str


# Apply validation on individual fields
class UpdateProduct(BaseModel):
  name: str = Field(min_length=2, max_length=100)
  price: float = Field(gt=0)
  stock: int = Field(ge=0)
  # nested model
  supplier: Supplier


# For successful responses, "201" status code will be returned
@router.post("/create-product", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
  return product


@router.post("/update-product/{product_id}")
async def update_product(
  product: UpdateProduct,
  product_id: str = Path(min_length=2),
):
  return {
    "product_id": product_id,
    "product": product,
  }
