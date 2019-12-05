'''
let's implement consistent hashing in python!

considerations:
we want to store K keys across N machines
load should be relatively even, each machine shoudl get a similar amount of load
if we remove a machine, K/n keys should be redistributed (how do we handle the redistribution?)
'''


class Machine:
    keys = []

    def __init__(self, ip):
        self.ip = ip

    def add_key(self, key):
        self.keys.append(key)


keys = [45,1,235,599,11,35,8098]
machines = [Machine("1.1.1.1"), Machine("1.1.1.2"), Machine("1.1.1.3")]
conceptual_ring = [0 for _ in range(360)]


#where does the key go on the ring?

def compute_ring_location(key):
    landing = hash(key)%len(conceptual_ring)
    while not conceptual_ring[landing]:
        landing=(landing+1)%len(conceptual_ring)
    machine = conceptual_ring[landing]
    machine.add_key(key)


'''
distribute the machines across the conceptual ring, add a "scaling factor" to virtualize some machines
'''
def distribute_machines(machines, scale_factor):
    for machine in machines:
        for i in range(scale_factor):
            hash_factor = i*11
            bucket = (hash(machine)*hash_factor)%len(conceptual_ring)
            conceptual_ring[bucket] = machine


distribute_machines(machines, 10)

for key in keys:
    compute_ring_location(key)


for machine in machines:
    print(machine.ip + "->" + str(machine.keys))