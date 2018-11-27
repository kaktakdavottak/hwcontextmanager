import json
from datetime import datetime


class TimeDelta:
    def __enter__(self):
        print('Время начала {}'.format(datetime.now().time()))
        self.start = datetime.now()
        return self

    def __exit__(self, *args):
        print('Время окончания {}'.format(datetime.now().time()))
        self.end = datetime.now()
        self.result = self.end - self.start
        print('Потрачено времени {}'.format(self.result))


def open_json_file():
    with open('files\\newsafr.json', encoding='utf-8') as datafile:
        json_data = json.load(datafile)
    return json_data


def get_all_long_words():

    string_descriptions = ''

    for items in open_json_file()["rss"]["channel"]["items"]:
        string_descriptions += items["description"]

    list_descriptions = string_descriptions.split()
    long_words = []

    for word in list_descriptions:
        if len(word) > 6:
            long_words.append(word.lower())

    return long_words


def count_long_words():

    count_word_dict = {}

    for long_word in get_all_long_words():
        if long_word in count_word_dict:
            count_word_dict[long_word] += 1
        else:
            count_word_dict[long_word] = 1

    return count_word_dict



def get_top10_words():

    count_word_dict = count_long_words()

    def by_value(count_word_dict):
        return count_word_dict[1]

    top10_long_words = sorted(count_long_words().items(), key=by_value, reverse=True)
    print(top10_long_words[0:10])


if __name__ == "__main__":
    with TimeDelta():
        get_top10_words()


