from functools import reduce
import math


def break_even(pot, bet):
    #break even AKA required equity %
    total_pot = pot + 2*bet
    odds = bet / total_pot
    return round(odds,3) * 100

def pot_odds(pot_size, bet_size):
    result = [pot_size + bet_size, bet_size]
    denominator = reduce(math.gcd, result)
    result = [i / denominator for i in result]
    result[0] = round(result[0] / result[1], 1)
    result[1] = 1
    return result



pot, bet = 400,200
print("Pot size is ",pot, " and opponent bets ", bet, ".")
print("Pot odds: ", pot_odds(pot,bet), ", break even percentage: ",break_even(pot,bet), "%")