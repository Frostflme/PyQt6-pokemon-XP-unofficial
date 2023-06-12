# imports

# functions
def calculateXP(base_XP: int, victorious_level: int, defeated_level: int, ally_number: int, enemy_number: int, xp_multiplier: float, in_battle: bool, not_evolved_fully: bool, has_lucky_egg: bool) -> int:
    """Calculates the final XP using all the neccessary variables."""
    # Calculation Part 1
    final_xp = base_XP * defeated_level
    final_xp /= 5

    # Adjusting for being outside of battle
    if in_battle:
        temp1 = 1
    else:
        temp1 = 2
    final_xp *= (1/temp1)

    # Calculation Part 2
    temp1 = 2 * defeated_level
    temp1 += 10
    temp1 = temp1 ** 2.5
    temp2 = defeated_level + victorious_level + 10
    temp2 = temp2 ** 2.5
    temp1 /= temp2
    final_xp *= temp1
    
    final_xp += 1

    # Extra multipliers
    if has_lucky_egg:
        temp1 = 1.5
    else:
        temp1 = 1
    if not_evolved_fully:
        temp2 = 4915/4096
    else:
        temp2 = 1
    final_xp *= temp1 * temp2
    # Adjusting for the number of teammates and enemies
    temp1 = enemy_number ** 1.5
    temp2 = ally_number ** 0.5
    temp1 *= temp2
    temp2 = ally_number ** 2.5
    temp1 /= temp2

    final_xp *= temp1

    # Adjusting for the XP multiplier
    final_xp *= xp_multiplier

    return int(final_xp)

# global scope
if __name__ == "__main__":
    pass