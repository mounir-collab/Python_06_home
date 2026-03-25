def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validtaion_result = validate_ingredients(ingredients)

    if "VALID" in validtaion_result:
        return f"Spell recorded: {spell_name} ({validtaion_result})"
    else:
        return f"Spell rejected: {spell_name} ({validtaion_result})"
