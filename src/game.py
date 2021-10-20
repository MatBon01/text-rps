import random


def shuffle_symbols(symbols):
    """
    Symbols must be a tuple of three elements
    """

    list_of_symbols = list(symbols)
    random.shuffle(list_of_symbols)
    return tuple(list_of_symbols)


def print_symbols_as_moves(symbols):
    """
    Symbols msut be a tuple of three elements
    """
    index_in_symbols = {"rock": 0, "paper": 1, "scissors": 2}

    print(f"{symbols[index_in_symbols['rock']]} - Rock")
    print(f"{symbols[index_in_symbols['paper']]} - Paper")
    print(f"{symbols[index_in_symbols['scissors']]} - Scissors")


def main_game(symbols=("1", "2", "3")):
    shuffled_symbols = shuffle_symbols(symbols)
    print_symbols_as_moves(shuffled_symbols)
