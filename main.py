import argparse
from Server import Server
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--n_nodes', dest='n_nodes', default=4)
parser.add_argument('--verbose',    dest='verbose', default=True)
parser.add_argument('--arrival_distn', dest='arrival_distn', default='gaussian')
parser.add_argument('--service_distn', dest='service_distn', default='gaussian')
parser.add_argument('--load_balancing_alg', dest='load_balancing_alg', default='random')
parser.add_argument('--num_arrivals', dest='num_arrivals', default=10000)
parser.add_argument('--queue_size', dest='queue_size', default=3)
parser.add_argument('--num_fast_nodes', dest='num_fast_nodes', default=1)
args = parser.parse_args()



dropped = []


for i in range(10):
    model = Server(args)
    model.simulate()
    stats = model.get_stats()
    dropped.append(stats['proportion_dropped'])
print(dropped)
print(np.average(dropped))
