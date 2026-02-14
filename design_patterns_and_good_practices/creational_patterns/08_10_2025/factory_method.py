''' Exemplu ce ilustreaza utilizarea patter-ului Factory Method'''

# Clasa abstracta care defineste interfata pt. jocuri
class Game:
    def get_name(self):
        pass

    def get_type(self):
        pass

    def get_min_number_of_players(self):
        pass

    def get_max_number_of_players(self):
        pass

    def can_be_played_remotely(self):
        pass


class BoardGame(Game):
    def __init__(self, name, type, max_player_num):
        self._name = name                                      # Stocheaza numele jocului
        self._type = type                                      # Stocheaza tipul jocului
        self._max_player_num = max_player_num                  # Stocheaza nr. maxim de jucatori

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return 2                                               # Presupunem ca "BoardGames" are minim doi jucatori

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return False                                           # "BoardGames" nu poate fi jucat remote

    def __str__(self):                                         # String reprezentativ pentru obiect
        return f"{__name__} [name='{self._name}', type='{self._type}', max_player_num={self._max_player_num}]"


class PCGame(Game):
    def __init__(self, name, type, min_player_num, max_player_num, is_online):
        self._name = name
        self._type = type
        self._min_player_num = min_player_num
        self._max_player_num = max_player_num
        self._is_online = is_online

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return self._min_player_num

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return self._is_online

    def __str__(self):
        return (f"{__name__} [name='{self._name}', type='{self._type}', min_player_num={self._min_player_num}"
                f", max_player_num={self._max_player_num}, is_online={self._is_online}]")


# Clasa abstracta "Factory"
class GameFactory:
    def create(self):
        pass                                                   # Metoda care va fi implementata de fabricile concrete


class MonopolyGameCreator(GameFactory):
    def create(self):
        return BoardGame("Monopoly", "Family Game", 4) # Creaza un "BoardGAme"


class ValorantGameCreator(GameFactory):
    def create(self):
        return PCGame("Valorant", "FPS", 4, 10, True) # Creaza un "PCGame"


def main():
    game_type = input("Enter the type of game [PC, Board]: ")          # Cere tipul de joc de la user
    game_factory = None                                                # Initial nu avem fabrica
    if game_type == "PC".lower():
        game_factory = ValorantGameCreator()                           # Alegem fabrica pt. PC
    elif game_type == "Board".lower():
        game_factory = MonopolyGameCreator()                           # Alegem fabrica pt. Board

    if game_factory:
        game = game_factory.create()                                   # Folosim fabrica pentru a crea jocul
        print(game)                                                    # Afisam detaliile jocului


if __name__ == "__main__":
    main()                                                             # Punctul de intrare al programului
