from fastapi import APIRouter

from backend.service.categories import categoryService


category_router = APIRouter(prefix="/category", tags=["Categorias"])

@category_router.post("/newCategory")
async def newCategory(userId: int, category: str):
    return categoryService.createNewCategory(userId, category)