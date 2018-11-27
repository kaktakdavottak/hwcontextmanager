from datetime import datetime
import time


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


with TimeDelta():
    time.sleep(10)
