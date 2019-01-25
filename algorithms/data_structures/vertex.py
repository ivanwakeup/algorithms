class Vertex:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.child = None
        #finishing time, useful for computing topological sort
        self.finish = None
        self.begin = None
        self.cost = None

    def __str__(self):
        return "Vertex {} with Parent {} and Child {}".format(self.data, self.parent, self.child)

    def __repr__(self):
        return self.data

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return ord(self.data)

    def __lt__(self, other):
        return ord(self.data) < ord(other.data)