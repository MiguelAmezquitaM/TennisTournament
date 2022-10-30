from tennis_player import tennis_player, female_tennis_player, male_tennis_player


# Algorithm for decide witch player win
# eval the difference between luck and ability
# sum it, and compare
class clash_of_players:
    def clash(self, p1: tennis_player, p2: tennis_player):
        # asserts
        assert (0 <= p1.ability <= 100 and 0 <= p2.ability <= 100)
        assert (0 <= p1.luck <= 100 and 0 <= p2.luck <= 100)

        # difference
        da = (p1.ability - p2.ability + 100.0) / 200
        dl = (p1.luck - p2.luck + 100.0) / 200

        # luck has a weight of 35 percent and ability 65
        p_p1 = da * 65 + dl * 35
        p_p2 = 100 - p_p1

        return {'p1': p_p1, 'p2': p_p2}


class clash_of_male_players(clash_of_players):
    def clash(self, p1: male_tennis_player, p2: male_tennis_player):
        # asserts
        assert (0 <= p1.strength <= 100 and 0 <= p1.velocity <= 100)
        assert (0 <= p2.strength <= 100 and 0 <= p2.velocity <= 100)

        # parent class evaluate luck and ability
        prev = super().clash(p1, p2)

        # here strength and speed are evaluated
        ds = (p1.strength - p2.strength + 100.0) / 200.0
        dv = (p1.velocity - p2.velocity + 100.0) / 200.0

        # velocity has a weigth of 40% and strength the rest
        p_p1 = ds * 60 + dv * 30
        p_p2 = 100 - p_p1

        # is averaged with previous results
        prev['p1'] = (prev['p1'] + p_p1) / 2
        prev['p2'] = (prev['p2'] + p_p2) / 2

        return prev


class clash_of_female_players(clash_of_players):
    def clash(self, p1: female_tennis_player, p2: female_tennis_player):
        # asserts
        assert (0 <= p1.reaction_time <= 100)
        assert (0 <= p2.reaction_time <= 100)

        # parent class evaluate luck and ability
        prev = super().clash(p1, p2)

        # evaluate reaction time
        drt = (p1.reaction_time - p2.reaction_time + 100.0) / 2

        # reaction time contributes 30% of the points to win
        prev['p1'] = prev['p1'] * 0.7 + drt * 0.3

        return prev
