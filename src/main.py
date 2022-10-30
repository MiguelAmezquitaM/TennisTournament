from clash_of_player import clash_of_male_players
from tennis_player import Sex, male_tennis_player
from tournament import tournament


def main():
    _tournament_ = tournament(clash_of_male_players())

    _tournament_.add_participant(male_tennis_player(
        'Adrian', Sex.Male, ability=65, luck=78, strength=54, velocity=58))
    _tournament_.add_participant(male_tennis_player(
        'Fernan', Sex.Male, ability=78, luck=45, strength=26, velocity=65))
    _tournament_.add_participant(male_tennis_player(
        'German', Sex.Male, ability=62, luck=63, strength=98, velocity=45))
    _tournament_.add_participant(male_tennis_player(
        'Harold', Sex.Male, ability=89, luck=98, strength=44, velocity=69))
    _tournament_.add_participant(male_tennis_player(
        'Draken', Sex.Male, ability=99, luck=98, strength=100, velocity=100))

    _result_ = _tournament_.play()

    print('Result:')
    for _player_ in _result_:
        print(_player_)


if __name__ == '__main__':
    main()
