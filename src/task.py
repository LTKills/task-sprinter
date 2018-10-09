

class Task:
    def __init__(self, title, time):
        self.title = title
        self.time = time # time in minutes

    def __str__(self):
        return str(self.title + ' (' + str(self.time) + 'min)')

