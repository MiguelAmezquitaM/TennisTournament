

from random import randint
from typing import List
from clash_of_player import clash_of_players

from tennis_player import tennis_player


class tournament:
    participants: List[tennis_player] = []
    clash: clash_of_players = None

    def __init__(self, clash: clash_of_players) -> None:
        self.clash = clash

    def add_participant(self, player: tennis_player):
        self.participants.append(player)

    def play(self) -> List[tennis_player]:
        # Ranking
        rank: List[tennis_player] = []
        # Players clasified, all at begin
        clasified: List[tennis_player] = self.participants.copy()
        # Eliminated players
        eliminated: List[tennis_player] = []

        while len(clasified) > 1:
            i = 0

            # single round
            while (i < len(clasified) - 1):
                p1, p2 = clasified[i], clasified[i+1]

                # play the round
                result = self.clash.clash(p1, p2)

                # determinate winner
                if result['p1'] > result['p2']:
                    eliminated.append(p2)
                elif result['p1'] < result['p2']:
                    eliminated.append(p1)
                else:
                    eliminated.append(clasified[randint(i, i + 1)])

                i += 2

            # remove all eliminateds
            for p in eliminated:
                try:
                    clasified.remove(p)
                except ValueError:
                    pass
        
        rank.append(clasified[0])

        eliminated.reverse()
        for p in eliminated:
            rank.append(p)
        
        return rank
