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

To contribute to the project, please follow these recommendations:

1. View the [issues page](https://github.com/LTKills/task-sprinter/issues) for any ongoing fixes or suggestions for the project. Find what you would like to contribute to and inform the maintainer in the comments for the issue. This will let the maintainer as well as prospective contributors that you will be working on the issue.

2. When making a pull request, the pull request should reflect individual issues. If you are working on multiple issues make sure to have separate pull requests for separate issues. For any help on making pull requests, be sure to check [Digital Ocean's guide for pull requests.](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github) Separating the pull requests to each issue will also help with clarfying the description of the pull request.

3. When naming your pull requests, be sure the title is succinct and describes the change. (Example:"Added Contribution Guide" or "Fixed typos on FILE") The description should add details on what the contribution has in detail. Be sure to reference the issue number in your description as well as how the issue is resolved by the change.