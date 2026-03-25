def validate_ingredients(ingredients: str) -> str:

    valid_ingredients = ["fire", "water", "earth", "air"]
    for ingredient in valid_ingredients:
        if ingredient in ingredients:
            return f"{ingredient} - VALID"

    return f"{ingredients} - INVALID"
