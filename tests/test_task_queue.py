import pytest

from task_queue.task_queue import TaskQueue
from task_models.task import Task
from task_models.resources import Resources

def test_task_queue():
    queue = TaskQueue()
    tasks = [
        Task(id=1, priority=5, resources=Resources(ram=2, cpu_cores=1, gpu_count=0), content="Task 1"),
        Task(id=2, priority=10, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task 2"),
        Task(id=3, priority=1, resources=Resources(ram=8, cpu_cores=4, gpu_count=1), content="Task 3")
    ]
    for task in tasks:
        queue.add_task(task)

    resources = Resources(ram=16, cpu_cores=4, gpu_count=1)

    retrieved_task = queue.get_task(resources)
    assert retrieved_task.id == 2, "Expected task 2 to be retrieved first based on priority"

    retrieved_task = queue.get_task(Resources(ram=16, cpu_cores=4, gpu_count=0))
    assert retrieved_task.id == 1, "Expected task 1 to be retrieved next based on available resources"

    retrieved_task = queue.get_task(resources)
    assert retrieved_task.id == 3, "Expected task 3 to be retrieved"


def test_insufficient_resources():
    queue = TaskQueue()
    tasks = [
        Task(id=1, priority=5, resources=Resources(ram=16, cpu_cores=8, gpu_count=2), content="High Resource Task 1"),
        Task(id=2, priority=10, resources=Resources(ram=32, cpu_cores=16, gpu_count=4), content="Higher Resource Task 2")
    ]
    for task in tasks:
        queue.add_task(task)
    
    insufficient_resources = Resources(ram=8, cpu_cores=4, gpu_count=1)
    
    task = queue.get_task(insufficient_resources)
    assert task is None, "Expected no task to be executable due to insufficient resources"

