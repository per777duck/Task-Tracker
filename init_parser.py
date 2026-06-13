import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('new_task', help='Добавляет новую задачу(в \"\" или \'\' указывается описание задачи)')
    # add_parser.set_defaults(func=)

    return parser