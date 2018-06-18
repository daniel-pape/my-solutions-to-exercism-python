# Score categories
# Change the values as you see fit
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'

from collections import Counter

def score(dice, category):
    def take_sum(dice, use_only_face = None):
        if use_only_face:
            return sum([_ for _ in dice if _ == use_only_face])
        else:
            return sum(dice)

    if category == ONES:
        return take_sum(dice, use_only_face=1)
    elif category == TWOS:
        return take_sum(dice, use_only_face=2)
    elif category == THREES:
        return take_sum(dice, use_only_face=3)
    elif category == FOURS:
        return take_sum(dice, use_only_face=4)
    elif category == FIVES:
        return take_sum(dice, use_only_face=5)
    elif category == SIXES:
        return take_sum(dice, use_only_face=6)
    elif category == FULL_HOUSE:
        cnts = Counter(dice).values()
        is_valid = (sorted(cnts) == [2, 3])
        return take_sum(dice) if is_valid else 0
    elif category == FOUR_OF_A_KIND:
        most_common = Counter(dice).most_common(1).pop()
        most_common_face = most_common[0]
        most_common_count = most_common[1]
        is_valid = (most_common_count >= 4)
        too_much = (most_common_count - 4)
        correction = (too_much * most_common_face)
        dice_sum = take_sum(dice, use_only_face=most_common_face)
        score = dice_sum - correction
        return score if is_valid else 0
    elif category == LITTLE_STRAIGHT:
        is_valid = (sorted(dice) == [1, 2, 3, 4, 5])
        return 30 if is_valid else 0
    elif category == BIG_STRAIGHT:
        is_valid = (sorted(dice) == [2, 3, 4, 5, 6])
        return 30 if is_valid else 0
    elif category == CHOICE:
        return take_sum(dice)
    elif category == YACHT:
        is_valid = (all([(face == dice[0]) for face in dice]))
        return 50 if is_valid else 0
    else:
        raise ValueError("Unknown category `category={}`".format(category))