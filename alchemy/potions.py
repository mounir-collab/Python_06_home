from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {create_air()} and {create_water()}"


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with all elements:\n "
        f"{create_water()}\n "
        f"{create_air()}\n "
        f"{create_fire()}\n "
        f"{create_earth()}"
    )
