

class Routine:
    '''
    Each Routine is a list of tasks, but with more information.
    Currently, the extra information is Description and Total Time.

    A routine ends when the last task in the routine is completed.
    '''

    '''
    Set the title for the routine.
    '''
    def __init__(self, title):
        self.title = title

    '''
    Return the title of the routine.
    '''
    def __str__(self):
        return self.title

    '''
    Start the execution of the list of tasks within the routine.
    '''
    def start(self):
        pass

    '''
    Add a new task to the list of tasks within the routine.
    '''
    def add(self):
        pass

    '''
    Remove a task from the list of tasks within the routine.
    '''
    def remove(self):
        pass

    '''
    Edit the description for the routine.
    '''
    def edit(self):
        pass
