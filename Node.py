class Node:
    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.process_queue = []
        self.idle = True
        self.active_job = None

    def get_utilization(self):
        return not self.idle

    def add_process(self, process):
        if len(self.process_queue) >= self.queue_size:
            return False
        else:
            self.process_queue.append(process)

        # if the node is idle start this job which was just queued
        if self.idle:
            self.process_item()

    def process_item(self):
        # Check if there is anything in the queue or if we're already serving
        # if we are then we can't process the next job so return false
        if len(self.process_queue) is 0 or not self.idle:
            return False
        # In this case we can process the next job so put it as the active job
        elif self.idle:
            self.active_job = self.process_queue.pop()
            self.idle = False
        # Else case return False
        else:
            return False