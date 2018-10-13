import task
import time

class Routine:
    '''
    Each Routine is a list of tasks, but with more information.
    Currently, the extra information is Description and Total Time.

    A routine ends when the last task in the routine is completed.
    '''

    '''
    Set the title for the routine.
    '''
    def __init__(self, title, tasks):
        self.title = title
        self.tasks = tasks
        #self.total_length = _get_total_time(tasks)

    '''
    Return the title of the routine.
    '''
    def __str__(self):
        return self.title

    '''
    Start the execution of the list of tasks within the routine.
    '''
    def run(self):
       print('Starting routine ' + self.title)
       for task in self.tasks:
           task.run()
       print("Time's up for routine " + self.title)

    '''
    Add a new task to the list of tasks within the routine.
    '''
    def add(self, task):
        self.tasks.append(task)

    '''
    Remove a task from the list of tasks within the routine.
    '''
    def remove(self, task):
        self.tasks.remove(task)

