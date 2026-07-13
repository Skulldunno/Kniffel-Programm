class ScoreSheet:
    def __init__(self, name: str):
        self.name = name

        # Oben
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None

        # Unten
        self.three_of_a_kind = None
        self.four_of_a_kind = None
        self.full_house = None
        self.small_straight = None
        self.large_straight = None
        self.kniffel = None
        self.chance = None

    # Hilfsfunktionen
    def _values(self, dice_list: list["Dice"]) -> list[int]:
        return [d.get_eyes() for d in dice_list]

    def _count(self, dice_list: list["Dice"], n: int) -> int:
        return sum(1 for d in dice_list if d.get_eyes() == n)

    # Punkteberechnung
    def score_upper(self, dice_list, number):
        return self._count(dice_list, number) * number

    def score_three_of_a_kind(self, dice_list):
        vals = self._values(dice_list)
        for n in range(1, 7):
            if vals.count(n) >= 3:
                return sum(vals)
        return 0

    def score_four_of_a_kind(self, dice_list):
        vals = self._values(dice_list)
        for n in range(1, 7):
            if vals.count(n) >= 4:
                return sum(vals)
        return 0

    def score_full_house(self, dice_list):
        vals = self._values(dice_list)
        counts = [vals.count(n) for n in range(1, 7)]
        return 25 if (3 in counts and 2 in counts) else 0

    def score_small_straight(self, dice_list):
        vals = set(self._values(dice_list))
        straights = [
            {1,2,3,4},
            {2,3,4,5},
            {3,4,5,6}
        ]
        return 30 if any(s.issubset(vals) for s in straights) else 0

    def score_large_straight(self, dice_list):
        vals = set(self._values(dice_list))
        return 40 if vals in ({1,2,3,4,5}, {2,3,4,5,6}) else 0

    def score_kniffel(self, dice_list):
        vals = self._values(dice_list)
        return 50 if len(set(vals)) == 1 else 0

    def score_chance(self, dice_list):
        return sum(self._values(dice_list))
