from enum import IntEnum

class Types(IntEnum):
    #List of different types.
    Normal = 0
    Water = 1
    Fire = 2
    Grass = 3
    Fighting = 4
    Flying = 5
    Ground = 6
    Poison = 7
    Rock = 8
    Bug = 9
    Ghost = 10
    Steel = 11
    Electric = 12
    Psychic = 13
    Ice = 14
    Dragon = 15
    Dark = 16
    Fairy = 17
    #End types list.

    def max():
        major = None
        for t in Types:
            if major == None:
                major = t
                continue

            if t.value > major.value:
                major = t

        return major 