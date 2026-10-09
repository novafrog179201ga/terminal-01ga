"""
Simple terminal task manager.
"""

import argparse, json, os, sys

TASK_FILE = 'tasks.json'

class TaskManager:
    def __init__(self, file=TASK_FILE):
        self.file = file
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(self.file):
            return []
        with open(self.file) as f:
            return json.load(f)

    def _save(self):
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, text):
        self.tasks.append(text)
        self._save()

    def list(self):
        for i, t in enumerate(self.tasks, 1):
            print(f'{i}. {t}')

    def remove(self, idx):
        try:
            del self.tasks[idx-1]
            self._save()
        except IndexError:
            print('Invalid index', file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='Task manager')
    sub = parser.add_subparsers(dest='cmd', required=True)
    sub.add_parser('list')
    add = sub.add_parser('add')
    add.add_argument('text')
    rem = sub.add