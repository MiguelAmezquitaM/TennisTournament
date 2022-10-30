from unittest import TestCase, main
from src.clash_of_player import clash_of_female_players, clash_of_male_players, clash_of_players
from src.tennis_player import Sex, male_tennis_player, tennis_player


class test_class_of_player(TestCase):

    def test_clash_of_players(self):
        p1 = tennis_player(name='Matilda', sex=Sex.Female, ability=70, luck=50)
        p2 = tennis_player(name='Julia', sex=Sex.Female, ability=80, luck=40)

        clash = clash_of_players()

        result = clash.clash(p1, p2)

        self.assertGreater(result['p2'], result['p1'])
        self.assertEqual(result['p1'], 48.5)
        self.assertEqual(result['p2'], 51.5)

    def test_clash_of_males(self):
        p1 = male_tennis_player(
            'Harold', Sex.Male, ability=80, luck=70, strength=70, velocity=50)
        p2 = male_tennis_player(
            'Jake', Sex.Male, ability=70, luck=90, strength=60, velocity=90)

        clash = clash_of_male_players()

        result = clash.clash(p1, p2)

        self.assertGreater(result['p2'], result['p1'])
        self.assertEqual(result['p1'], 45.875)
        self.assertEqual(result['p2'], 54.125)


if __name__ == '__main__':
    main()
