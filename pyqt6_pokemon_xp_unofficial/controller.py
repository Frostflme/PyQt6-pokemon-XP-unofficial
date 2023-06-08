# imports

# functions
def calculateXP(base_XP, victorious_level, defeated_level, ally_number, enemy_number, xp_multiplier, in_battle, not_evolved_fully, has_lucky_egg):
    # TODO docstring and types
    final_xp = base_XP * defeated_level
    final_xp /= 5

    if in_battle:
        temp1 = 1
    else:
        temp1 = 2
    final_xp *= (1/temp1)

    temp1 = 2 * defeated_level
    temp1 += 10
    temp1 = temp1 ** 2.5
    temp2 = defeated_level + victorious_level + 10
    temp2 = temp2 ** 2.5
    temp1 /= temp2
    final_xp *= temp1
    
    final_xp += 1

    if has_lucky_egg:
        temp1 = 1.5
    else:
        temp1 = 1
    if not_evolved_fully:
        temp2 = 4915/4096
    else:
        temp2 = 1
    final_xp *= temp1 * temp2
    # TODO work get ally/enemy numbers worked out
    final_xp *= xp_multiplier

# global scope
if __name__ == "__main__":
    pass