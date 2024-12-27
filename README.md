
task_tracker
  |
  |-task_tracker.py (main file)
  |
  |-tasks.json (store your data- Add, delete, update, list, channge_update, status)

Test each feature using the CLI.
Examples:
  ```bash
  python task_tracker.py add "Buy groceries"
  python task_tracker.py list
  python task_tracker.py update 1 "Buy groceries and cook dinner"
  python task_tracker.py status 1 "in progress"
  python task_tracker.py delete 1
  ```