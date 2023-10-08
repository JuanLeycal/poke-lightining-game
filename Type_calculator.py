type_names = [
    'normal',
    'fighting',
    'flying',
    'poison',
    'ground',
    'rock',
    'bug',
    'ghost',
    'steel',
    'fire',
    'water',
    'grass',
    'electric',
    'psychic',
    'ice',
    'dragon',
    'dark',
    'fairy'
]


type_base = [
    # normal:
    [1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1],
    # fighting:
    [2,1,0.5,0.5,1,2,0.5,0,2,1,1,1,1,0.5,2,1,2,0.5],
    # flying:
    [1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1],
    # poison:
    [1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2],
    # ground:
    [1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1],
    # rock:
    [1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1],
    # bug:
    [1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5],
    # ghost:
    [0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1],
    # steel:
    [1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2],
    # fire:
    [1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1],
    # water:
    [1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1],
    # grass:
    [1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1],
    # electric:
    [1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1],
    # psychic
    [1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1],
    # ice:
    [1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1],
    # dragon:
    [1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0],
    # dark:
    [1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5],
    # fairy:
    [1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]
]


def type_calculator(attack, types):
    total = 1

    for i in types:
        atk = type_names.index(attack)
        dfd = type_names.index(i)
        df_index = type_base[atk][dfd]
        if df_index == 0:
            return 0
        else:
            total = total * df_index
        
    return total

