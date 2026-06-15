import argparse

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Добавляет новую задачу')
    add_parser.add_argument('description', help='Задача, которую нужно добавить. В \"\" или \'\' указывается описание задачи')
    add_parser.set_defaults(function=lambda manager, args: manager.add_task(args.description))

    return parser