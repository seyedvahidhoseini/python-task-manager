task = []

def add_task(user_input):
    task.append(user_input)

def show_tasks():
    for i in range(len(task)):
        print(f"{i+1}. {task[i]}")

add_task("خرید نان")
add_task("ورزش کردن")
add_task("مطالعه کتاب")

show_tasks()

