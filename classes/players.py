class Player:
    def __init__(self, username: str) -> None:
        self.username = username
        self.used_words = []

    def get_count_used_words(self) -> int:
        return len(self.used_words)

    def add_word_in_used_words(self, word: str) -> None:
        self.used_words.append(word)

    def check_used_word(self, word: str) -> bool:
        return word in self.used_words

    def __repr__(self) -> str:
        return f'Player : username = {self.username}, used_words = {self.used_words}'
