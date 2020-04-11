import argparse
import Server

parser = argparse.ArgumentParser()
parser.add_argument('--n_nodes', dest='n_nodes', default=1)
parser.add_argument('--verbose',    dest='verbose', default=True)
parser.add_argument('--arrival_distn', dest='arrival_distn', default='exponential')
parser.add_argument('--service_distn', dest='service_distn', default='exponential')
parser.add_argument('--load_balancing_alg', dest='load_balancing_alg', default='Random')
parser.add_argument('--num_arrivals', dest='num_arrivals', default=10000)
parser.add_argument('--queue_size', dest='queue_size', default=10)
args = parser.parse_args()
model = Server(args)
model.build()

model.simulate()

