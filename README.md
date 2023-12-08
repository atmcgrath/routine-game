# Routine Game

A simple command line tool for task prompting and timing.


## Notes and issues
- Problem: when you select main menu or remove a task, it jumps the next thing in the order. Why?
  - Fixed it when you go to main menu
  - Not remove a task
  - Try iter() -> when you remove an item from a list, it skips the next one anyway (indexes?)
  - Otherwise iter() would be helpful
- Alternatives
  - Could pop() be helpful? Put it back if it isn't finished or deleted?


Flow:
1. Load a routine
2. List out the tasks
3. Session
   1. iterates through unfinished tasks
      1. for each task, calls task timer
         1. Task timer gives timer, returns check status
            1. Check status asks for response
               1. N: calls task timer
               2. Y: changes task to done, returns task
               3. D: does nothing (task remains on list)
               4. M: main menu, ~~returns task~~ calls TT
               5. C: remove task from global list
   2. when done, checks for skipped tasks and calls itself
   3. Otherwise, main menu, then calls itself


