import Node


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
        self.build()

    def build(self):
        for i in range(self.n_nodes):
            self.nodes.append(Node(self.queue_size))

    def simulate(self):
        pass
