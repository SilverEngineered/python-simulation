import Node
import utils
from tqdm import tqdm


class Server:
    def __init__(self, args):
        self.n_nodes = args.n_nodes
        self.verbose = args.verbose
        self.arrival_distn = args.arrival_distn
        self.service_distn = self.service_distn
        self.load_balancing_alg = args.load_balancing_alg
        self.num_arrivals = args.num_arrivals
        self.queue_size = args.queue_size
        self.nodes = []
        self.service_times = []
        self.arrival_times = []
        self.build()

    def build(self):
        for i in range(self.n_nodes):
            self.nodes.append(Node(self.queue_size))
        if self.verbose:
            print("Generating Arrival and Service Times...")
        for i in tqdm(range(self.num_arrivals)):
            self.arrival_times.append(utils.generate(self.arrival_distn))
            self.service_times.append(utils.generate(self.service_distn))


    def simulate(self):
        pass
