from backend.repositories import categoryRepository


def createNewCategory(userId: int, category: str):
    try:    
        newCategory = categoryRepository.setNewCategory(userId, category)
    except Exception:
        raise
