# task-sprinter



Easily create and complete your tasks with routine sprinting. `task-sprinter` is an GTD (Getting Things Done) list helper. 
You can create, edit and delete routines with your tasks, set maximum time to finish each task and then start up a clock 
to keep you motivated.



## Dependencies



## Usage

Import the task and the routine modules

```
>>> import routine
>>> import task
```

Create your tasks

```
>>> dress = task.Task('Put on swimsuit', 5)
>>> swim = task.Task('Swim', 30)
>>> shower = task.Task('Shower', 10)
```

Create your routine

```
>>> go_for_a_swim = routine.Routine('Go for a swim', [dress, swim, shower])
```

Run the routine

```
>>> go_for_a_swim.run()

Starting routine go for a swim
Starting Put on swimsuit
Time's up!
Starting Swim
Time's up!
Starting Shower
Time's up!
Time's up for routine Go for a swim

```


## Contributing

