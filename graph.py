class NeighborNotFound(Exception):
    pass

class Node(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = set()
        self.visited = False

    def __repr__(self):
        return "Node({0})".format(self.value)

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def is_neighbor(self, neighbor):
        return neighbor in self.neighbors

    def remove_neighbor(self, neighbor):
        if self.is_neighbor(neighbor):
            self.neighbors.remove(neighbor)
        else:
            raise NeighborNotFound("{0} is not a neighbor".format(neighbor))

class Graph(object):
    def __init__(self, values_list=[]):
        self.nodes = set()
        self.adjacencies_list = {}

        for value in values_list:
            new_node = Node(value)
            self.nodes.add(new_node)

    def __repr__(self):
        return "Graph({0})".format(self.nodes)

    @property
    def edges(self):
        edges_list = []
        for node in self.adjacencies_list:
            for neighbor in self.adjacencies_list[node]:
                edges_list.append((node, neighbor))
        return edges_list

    def add_node(self, value):
        new_node = Node(value)
        self.nodes.add(new_node)

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node

    def add_edge(self, value_tuple, bidirectional=True):
        if not isinstance(value_tuple, tuple):
            raise TypeError("Values should be given in a tuple")

        value_1, value_2 = value_tuple

        edge_1 = self.get_node(value_1)
        edge_2 = self.get_node(value_2)

        edge_1.add_neighbor(edge_2)
        
        try:
            self.adjacencies_list[edge_1].add(edge_2)
        except KeyError:
            self.adjacencies_list[edge_1] = set([edge_2])

        if bidirectional:
            self.add_edge((value_2, value_1), bidirectional=False)

if __name__ == "__main__":
    g = Graph()
    g.add_node(10)
    g.add_node(11)
    g.add_edge((10, 11))

    print(g, g.edges)