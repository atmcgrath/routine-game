######
# Class Routine 3

# 2023.08.23
######

'''
What it does:
- Main menu
'''

import csv, time
from termcolor import colored, cprint
from random import random
#import threading

#######

task_list = []

score = 0

def calculate_score(task):
    global score
    possible = int(task['Time']) - 1
    x = round(possible * random()) + 1
    cprint(f"You earned {x} points!", 'magenta')
    score += x

def select_menu(menu_list):
    for count, m in enumerate(menu_list):
        cprint(f'{count}: {m[0]}', 'white')
    num = input()
    try:
        n = int(num)
        return menu_list[n]
    except:
        cprint("Input invalid", 'white')
        return select_menu(menu_list)

routines = [
    ('Ready to work', 'rtw.csv'),
    ('Test', 'abc.csv'),
    ('Today', 'today.csv'),
]

def load_routine(tasks=task_list):
    cprint("Which routine would you like to do? Options:", 'white')
    rtname, rtfilename = select_menu(routines) # rtname, rtfilename
    rtfilename = 'routines/' + rtfilename
    with open(rtfilename, newline='') as csvfile:
        tasklist = csv.DictReader(csvfile)
        for item in tasklist:
            item['Done'] = False
            item['Project'] = rtname
            tasks.append(item)
    return tasks

def task_timer(task):
    cprint(f"Your task: {task['Task']}!", 'white', 'on_blue')
    time.sleep(1)
    cprint(f"\n  You have {task['Time']} minutes.", 'white')
    cprint("  Press 'Ctrl+C' when done", 'white')
    try: 
        sleep_seconds = int(task['Time']) * 60
        time.sleep(sleep_seconds - 60)
        cprint(f"  You have 1 minute to finish up {task['Task']}", 'yellow')
        time.sleep(10)
        cprint(f"  Time's up!", 'red',)
        print('')
    except KeyboardInterrupt:
        print("\n")
    return check_status(task)

def remove_task(task):
    global task_list 
    task_list.remove(task)

def check_status(task):
    cprint(f"Did you finish {task['Task']}?", 'red')
    cprint('Y: Yes, N: No, D: Defer, C: Cancel task, M: Main menu', 'white')
    response = input().lower()
    if response == 'n':
        cprint("That's ok! Let's get back to it.\n", 'white')
        task_timer(task)
    elif response == 'y':
        cprint("Great job!", 'cyan', attrs=["bold", "blink"])
        calculate_score(task)
        cprint("Let's move to the next task.\n", 'white')
        task['Done'] = True
        return task
    elif response == 'd':
        cprint("Ok. We'll come back to this later", 'white')
    elif response == 'm':
        main_menu()
        task_timer(task)
    elif response == 'c':
        cprint("Removing task from list.", 'white')
        remove_task(task)

def incomplete(tasks=task_list):
    incomplete = [t for t in tasks if not t['Done']]
    return incomplete

def session(tasks=task_list):
    cprint("Let's begin!", 'red')
    for task in tasks:
        if not task['Done']:
            task_timer(task)
    if len(incomplete(tasks)) > 0:
        session()
    else:
        cprint("You have completed your tasks! Would you like to add more?", 'white')
        if input().lower() == 'y':
            main_menu()
            session()
        else:
            goodbye()

def report(tasks=task_list):
    remaining = incomplete(tasks)
    min = sum([int(i['Time']) for i in remaining])
    cprint(f"You're doing great! You've completed {len(tasks) - len(remaining)} tasks so far", "yellow")
    cprint(f"Current score: {score} points", "magenta")
    cprint(f"You have {len(remaining)} tasks remaining", "yellow")
    cprint(f"And approximately {min} minutes to go.", "yellow")
    cprint(f"Remaining tasks:", "white")
    for r in remaining:
        cprint(r["Task"], 'white')
    response = input("M: Main menu; C: Continue session")
    if response.lower() == "m":
        return main_menu()
    else:
        pass

def passfunct():
    pass

def add_task():
    task = input('What task would you like to add? ')
    time = input('How long will it take? ')
    try:
        int(time)
    except:
        time = '5'
    new_task = {'Task': task, 'Time': time, 'Done': False, 'Routine': 'New'}
    task_list.append(new_task)
    response = input('Would you like to add another? Y/N ')
    if response.lower() == 'y':
        add_task()
    else:
        pass
        #session()

def goodbye():
    cprint(f"Final score: {score} points!", "magenta")
    cprint("Goodbye!", 'white', "on_red")
    quit()

menu_options = [
    ("Add a task", add_task),
    ("Add a routine", load_routine),
    ("Session summary", report),
    ("Continue session", passfunct),
    ("Quit sesssion", goodbye)
]

def main_menu():
    print('')
    cprint("MAIN MENU", 'white')
    cprint("Options:", 'white')
    action = select_menu(menu_options)[1]
    return action()


cprint("Welcome! Let's get started!", 'magenta')
#task_list += load_routine()
cprint("Would you like to start with a routine? Y/N", 'white')
if input().lower() == 'y':
    load_routine()
else:
    cprint("Let's add some tasks!", 'white')
    add_task()
for t in task_list:
    if not t['Done']:
        print(t['Task'])
session()

cprint(f"Congratulations, you've finished all your tasks!", 'cyan', attrs=['bold'])
goodbye()