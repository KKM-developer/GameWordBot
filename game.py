import random


class WordGame:
    def __init__(self):
        self.word = []
        with open('russian_nouns.txt', 'r', encoding='utf-8') as file:  # заполняем словарь русских слов из файла
            line = file.readline()
            while line:
                self.word.append(line[:-1])
                line = file.readline()
        random.shuffle(self.word)
        self.try_for_win = random.randint(5, 10)
        self.dropped_word = []

    def new_game(self):
        self.word = []
        with open('russian_nouns.txt', 'r', encoding='utf-8') as file:  # заполняем словарь русских слов из файла
            line = file.readline()
            while line:
                self.word.append(line[:-1])
                line = file.readline()
        random.shuffle(self.word)
        self.try_for_win = random.randint(5, 10)
        self.dropped_word = []

    def lastLetter(self, word):
        last_letter = word[-1]
        if last_letter in ['ъ', 'ы', 'ь']:
            last_letter = word[-2]
        return last_letter

    def progress(self, word):
        print(f'--->({word})')
        if self.try_for_win == 0:
            return 'Я сдаюсь, Вы выиграли!'
        if word in self.dropped_word:
            return 'Такое слово уже было'
        if word.lower() not in self.word:
            return 'Такого слова нет'
        if len(self.dropped_word) != 0:
            bot_last_letter = self.lastLetter(self.dropped_word[-1])
            if word[0].lower() != bot_last_letter:
                return f'Твое слово должно начинаться на {bot_last_letter}'
        self.dropped_word.append(word)
        last_latter = self.lastLetter(word)
        for botWord in self.word:
            if botWord[0] == last_latter:
                if botWord not in self.dropped_word:
                    self.dropped_word.append(botWord)
                    self.try_for_win -= 1
                    bot_last_letter = self.lastLetter(botWord)
                    print(self.try_for_win)
                    return f'Мне на {last_latter} Мое слово {botWord}\nТебе на {bot_last_letter}'
