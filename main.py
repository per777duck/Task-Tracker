from parser import create_parser
from tasks_manager import TasksManager
import shlex

manager = TasksManager("data/tasks.json")
parser = create_parser()

while True:
    console_input = input("Task tracker >>> ")

    if not console_input.strip():
        print("Введите --help для просмотра списка команд")
        continue

    args = parser.parse_args(shlex.split(console_input))

    args.function(manager, args)