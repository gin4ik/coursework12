from classes.basic_word import BasicWord
from classes.players import Player
from utils import load_random_word, validate_user_word


def main():
    username: str = input('Ввведите имя игрока\n')
    print(f'Привет, {username}!')
    player: Player = Player(username)

    random_word: BasicWord = load_random_word()
    print(f'Составьте {random_word.get_count_sub_words()} слов из слова {random_word.word.upper()}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"\n')
    print('Поехали, ваше первое слово?\n')

    while player.get_count_used_words() != random_word.get_count_sub_words():
        user_word = input().lower()
        answer = validate_user_word(user_word, random_word, player)
        if answer:
            print(answer)
        else:
            break

    print(f'Игра завершена, вы угадали {player.get_count_used_words()} слов!')


if __name__ == '__main__':
    main()
