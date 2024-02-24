import heapq
from task_models.task import Task
from task_models.resources import Resources

class TaskQueue:
    def __init__(self, resource_key='gpu_count'):
        self.tasks_heap = []

    def add_task(self, task: Task):
        heapq.heappush(self.tasks_heap, (-task.priority, task))

    def get_task(self, available_resources):
        temp_tasks = []
        suitable_task = None

        while self.tasks_heap and suitable_task is None:
            _, task = heapq.heappop(self.tasks_heap)
            if self.is_resource_sufficient(task.resources, available_resources):
                suitable_task = task
            else:
                temp_tasks.append((task.priority, task))

        for priority, task in temp_tasks:
            heapq.heappush(self.tasks_heap, (-priority, task))

        return suitable_task

    @staticmethod
    def is_resource_sufficient(task_res, available_res):
        return task_res.ram <= available_res.ram and \
               task_res.cpu_cores <= available_res.cpu_cores and \
               task_res.gpu_count <= available_res.gpu_count
