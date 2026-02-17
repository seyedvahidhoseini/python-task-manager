task = []

def add_task(user_input):
    task.append(user_input)


def del_task(item):

    for i in task:
        if i == item:
            task.remove(i)

def show_tasks():
    for i in range(len(task)):
        print(f"{i+1}. *+* {task[i]}")


add_task("nan")
add_task("varzesh")
add_task("ketab")

del_task("nan")

show_tasks()

