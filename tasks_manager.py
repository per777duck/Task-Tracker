from datetime import datetime
import json
import os

class TasksManager:
    def __init__(self, file_name='tasks.json'):
        self.file_name = file_name
        self._ensure_directory_exists()
        self.tasks = self.load_tasks()

    def _ensure_directory_exists(self) -> None:
        directory = os.path.dirname(self.file_name)

        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def load_tasks(self) -> list[dict]:
        if not os.path.exists(self.file_name):
            return []

        with open(self.file_name, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_tasks(self) -> None:
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, description: str) -> None:
        new_task = {
            "id":self._get_next_id(),
            "description": description,
            "status": "ToDo",
            "created_at": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Задача '{description}' успешно добавлена c ID: {new_task["id"]}")

    def _get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.get("id", 0) for task in self.tasks) + 1