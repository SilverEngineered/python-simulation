import time

class Node:
    def __init__(self, queue_size, speed_mulitplier):
        self.queue_size = queue_size
        self.service_queue = []
        self.arrival_queue = []
        self.static_service_queue = []
        self.static_arrival_queue = []
        self.idle = True
        self.time_serving = 0
        self.speed_multiplier = speed_mulitplier

    def get_utilization(self):
        return not self.idle

    def add_process(self, arrival, service):
        self.service_queue.append(service)
        self.arrival_queue.append(arrival)
        self.static_service_queue.append(service)
        self.static_arrival_queue.append(arrival)

    def at_capacity(self):
        return len(self.arrival_queue) == self.queue_size

    def finish_serving(self):
        self.arrival_queue = self.arrival_queue[1:]
        self.service_queue = self.service_queue[1:]
        self.time_serving = 0

    def update(self, cur_time):
        num_tasks = len(self.arrival_queue)
        if num_tasks is 0:
            return
        if self.idle and cur_time > self.arrival_queue[0]:
            self.idle = False
            self.time_serving = time.time()
            return
        if not self.idle and cur_time > self.time_serving + (self.service_queue[0]/self.speed_multiplier):
            self.finish_serving()
