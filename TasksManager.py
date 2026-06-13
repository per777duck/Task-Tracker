import json
import os

class TasksManager:
    def __init__(self, file_name='data.json'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []

        with open(self.file_name, 'r') as f:
            return json.load(f)