

class Task:
    '''
    Set the title for the task.
    '''
    def __init__(self, title):
        self.title = title

    '''
    Return the title of the task.
    '''
    def __str__(self):
        return self.title
