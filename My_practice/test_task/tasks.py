import sys
import win32com.client


class taskSchedulerManager:
    def __init__(self):
        self.sheduler = win32com.client.Dispatch('Schedule.Service')
        self.sheduler.Connect()

    def get_tasks(self):
        tasks = []
        folders = [self.sheduler.GetFolder('\\')]
        while folders:
            folder = folders.pop(0)
            for task in folder.GetTasks(0):
                task_info = {"name": task.Name,
                             "path": task.Path,
                             "state": self.get_task_state(task.State)}
                tasks.append(task_info)
            folders.extend(folder.GetFolders(0))
        return tasks

    @staticmethod
    def get_task_state(state):
        states = {0: "Unknown",
                  1: "Disabled",
                  2: "Queued",
                  3: "Ready",
                  4: "Running"}
        return states.get(state, "Unknown")

if __name__ == 'main':
    manager = taskSchedulerManager()
    manager.get_tasks()
    data = taskSchedulerManager.get_tasks()
    print(manager.get_tasks())
