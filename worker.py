import time


def runTask(task_name):
    print(f' ')
    print(f' ')
    print(f' ')
    print(f' ')
    print(f'task {task_name} starting')  # in place of actual logging
    print(f' ')
    print(f' ')
    print(f' ')
    time.sleep(5)  # simulate long running task
    print(f' ')
    print(f' ')
    print(f' ')
    print(f'task {task_name} completed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(f' ')
    print(f' ')
    print(f' ')
    return {task_name: 'task complete'}
