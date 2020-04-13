from Node import Node
import utils
from tqdm import tqdm
import numpy as np
import random
import time


class Server:
    def __init__(self, args):
        self.n_nodes = args.n_nodes
        self.verbose = args.verbose
        self.arrival_distn = args.arrival_distn
        self.service_distn = args.service_distn
        self.load_balancing_alg = args.load_balancing_alg
        self.num_arrivals = args.num_arrivals
        self.queue_size = args.queue_size
        self.num_fast_nodes = args.num_fast_nodes
        self.dropped_requests = 0
        self.cur_time = 0
        self.nodes = []
        self.service_times = []
        self.arrival_times = []
        self.build()

    def build(self):
        num_fast_nodes = 0
        for i in range(self.n_nodes):
            if self.num_fast_nodes < num_fast_nodes:
                self.nodes.append(Node(self.queue_size, 2))
                num_fast_nodes +=1
            else:
                self.nodes.append(Node(self.queue_size, 1))
        if self.verbose:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
            print("Generating Arrival and Service Times...")
        for i in tqdm(range(self.num_arrivals)):
            self.arrival_times.append(utils.generate(self.arrival_distn))
            self.service_times.append(utils.generate(self.service_distn))
        self.arrival_times.sort()

    def simulate(self):
        print("Starting Simulation...")
        self.start_time = time.time()
        for arrival, service in tqdm(zip(self.arrival_times, self.service_times)):
            fin_loop = False
            while(not fin_loop):
                cur_time = time.time()

                #If process has arrived
                if cur_time - self.start_time >= arrival:
                    success_assign = self.assign_task(arrival, service)
                    if not success_assign:
                        self.dropped_requests += 1
                    fin_loop = True

                # If something to be served
                if len([i.arrival_queue[0] for i in self.nodes if len(i.arrival_queue) > 0]) > 0:
                    for i in self.nodes:
                        i.update(cur_time)
        print("Simulation Terminated...")

    def assign_task(self, arrival, service):
        available_nodes = [i for i in self.nodes if not i.at_capacity()]
        # At capacity so this is a failure
        if len(available_nodes) == 0:
            return False
        if self.load_balancing_alg == "random":
            node_to_assign = random.randint(0, len(available_nodes)-1)
            available_nodes[node_to_assign].add_process(arrival, service)
        elif self.load_balancing_alg == "priority_fastest":
            node_to_assign = np.argmax(i.speed_multiplier for i in available_nodes)
            available_nodes[node_to_assign].add_process(arrival, service)
        return True

    def get_stats(self):
        stats = {}
        stats['utilization'] = 0
        stats['proportion_dropped'] = self.dropped_requests / self.num_arrivals
        return stats