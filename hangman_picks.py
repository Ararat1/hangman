HANGMAN_PICKS = [
    """
    +---+
        |
        |
        |
        |
       ===
    """,
    """
    +---+
        |
    0   |
        |
        |
       ===
    """,
    """
    +---+
        |
    0   |
    |   |
        |
       ===
    """,
    """
    +---+
        |
    0   |
   /|   |
        |
       ===
    """,
    """
    +---+
        |
    0   |
   /|\  |
        |
       ===
    """,
    """
    +---+
        |
    0   |
   /|\  |
   /    |
       ===
    """,
    """
    +---+
        |
    0   |
   /|\  |
   / \  |
       ===
    """,
    """
    +---+
        |
   [0   |
   /|\  |
   / \  |
       ===
    """,
    """
    +---+
        |
   [0]  |
   /|\  |
   / \  |
       ===
    """,
    """
    +---+
    |   |
   [0]  |
   /|\  |
   / \  |
       ===
    """,
]

if __name__ == '__main__':
    for pick in HANGMAN_PICKS:
        print(pick)