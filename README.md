task_tracker/
├── task_tracker.py  # Main Python file that contains the application logic
├── tasks.json       # JSON file for storing task data (add, delete, update, change status)
├── README.md        # Documentation for the project, including installation and usage instructions

- Test each feature using the CLI.
- Examples:
  ```bash
  python task_tracker.py add "Buy groceries"
  python task_tracker.py list
  python task_tracker.py update 1 "Buy groceries and cook dinner"
  python task_tracker.py status 1 "in progress"
  python task_tracker.py delete 1
  ```