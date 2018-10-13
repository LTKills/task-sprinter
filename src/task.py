import time

class Task:
    def __init__(self, title, length):
        self.title = title
        self.length = length # time in minutes

    def __str__(self):
        return str(self.title + ' (' + str(self.time) + 'min)')

    def run(self):
        print('Starting ' + self.title)
        time.sleep(self.length*60)
        print("Time's up!")

