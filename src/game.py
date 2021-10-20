def shuffle_symbols(symbols):
    """
    Symbols must be a tuple of three elements
    """

    return symbols


def print_symbols_as_moves(symbols):
    """
    Symbols msut be a tuple of three elements
    """
    index_in_symbols = {"rock": 0, "paper": 1, "scissors": 2}

    print(f"{symbols[index_in_symbols['rock']]} - Rock")
    print(f"{symbols[index_in_symbols['paper']]} - Paper")
    print(f"{symbols[index_in_symbols['scissors']]} - Scissors")
