class BasicWord:
    def __init__(self, word: str, sub_words: list[str]) -> None:
        self.word = word
        self.sub_words = sub_words

    def check_word_in_sub_words(self, word: str) -> bool:
        return word in self.sub_words

    def get_count_sub_words(self) -> int:
        return len(self.sub_words)

    def __repr__(self) -> str:
        return f'BasicWord : word = {self.word}, sub_words = {self.sub_words}'
