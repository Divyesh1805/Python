


tasks = []
#to add task
def add_task(task):
    task_data = {'task': task,'completed':False}
    tasks.append(task_data)
    print('Task added:', task)
#view task
def view_tasks():
    print('Tasks:')
    for i, task in enumerate(tasks):
        print(i+1, task['task'],"(completed)" if task['completed'] else "")
#delete a task
def delete_task(index):
    task = tasks.pop(index-1)
    print('Task deleted:', task['task'])
#mark task completed
def mark_task_completed(index):
    tasks[index-1]['completed'] = True
    print('Mark Task Completed:', tasks[index-1]['task'])
#main function
def main():
    while True:
        action= input('What would you like to do?  (add/view/delete/complete/quit):  ')
        if action =='add':
            task = input('Enter the new task:  ')
            add_task(task)
        elif action=='view':
            view_tasks()
        elif action=='delete':
            delete_task(index)
        elif action=='complete':
            index= int(input('Enter task no.  '))
            mark_task_completed(index)
        elif action=='quit':
            break
        else:
            print('Wrong input')
#start
if __name__=='__main__':
    main()
    

    