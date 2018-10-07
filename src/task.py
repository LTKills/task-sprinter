

class Task:
    '''
    Set the title for the task.
    '''
    def __init__(self, title, time):
        self.title = title
        self.time = time # time in minutes

    '''
    Return the title of the task.
    '''
    def __str__(self):
        return str(self.title + ' (' + str(self.time) + 'min)')

