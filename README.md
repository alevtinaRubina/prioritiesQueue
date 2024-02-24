# prioritiesQueue
Task queue with priorities and resource limits

## Overview
This project implements a priority-based task queue system with resource constraints. Tasks within the queue are processed according to their priority and the resources available.

## Project Structure

- `task_models/`: Directory containing data class definitions.
  - `__init__.py`
  - `resources.py`: Defines the `Resources` class representing resources.
  - `task.py`: Defines the `Task` class representing a task.
- `task_queue/`: Directory for queue system components.
  - `__init__.py`
  - `task_queue.py`: Implementation of the `TaskQueue` class.
- `tests/`: Directory for tests.
  - `test_task_queue.py`: Tests for `TaskQueue` using `pytest`.

## Usage

To use the task queue system, import and instantiate the `TaskQueue` class, then add tasks using the `add_task` method. Retrieving a task from the queue is done by calling the `get_task` method, which returns the highest priority task that matches the available resources.

### Example Code

```python
from task_queue.task_queue import TaskQueue
from task_models.task import Task
from task_models.resources import Resources

# Create a task queue
queue = TaskQueue()

# Add tasks to the queue
queue.add_task(Task(id=1, priority=5, resources=Resources(ram=2, cpu_cores=1, gpu_count=0), content="Task 1"))
queue.add_task(Task(id=2, priority=10, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task 2"))

# Retrieve a task from the queue
task = queue.get_task(Resources(ram=16, cpu_cores=4, gpu_count=1))
print(f"Retrieved Task: {task.content}")

# To execute the tests, open a terminal at the project root and run
```pytest
