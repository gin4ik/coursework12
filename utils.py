from random import choice

from requests import get

from classes.basic_word import BasicWord
from classes.players import Player
from settings import URL
import urllib3


def load_random_word() -> BasicWord:
    urllib3.disable_warnings()
    response: list[dict] = get(URL, verify=False).json()
    random_word: dict = choice(response)
    word = random_word['word']
    sub_words = random_word['subwords']
    return BasicWord(word, sub_words)


def validate_user_word(user_word: str, basic_word: BasicWord, player: Player) -> str:
    if user_word in 'stop':
        return ''
    if len(user_word) < 3:
        return 'слишком короткое слово'
    if basic_word.check_word_in_sub_words(user_word):
        return 'неверно'
    if player.check_used_word(user_word):
        return 'уже использовано'
    player.add_word_in_used_words(user_word)
    return 'верно'
