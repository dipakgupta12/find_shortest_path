import csv
import os
from collections import defaultdict


class FindShortestPath:
    def __init__(self, start_node, goal_node, file_name):
        self.start_node = start_node
        self.goal_node = goal_node
        self.file_name = file_name

        self.data_rows = None
        self.edges = None
        self.graph = None
        self.short_path = None
        self.cost = None

    def load_csv(self):
        self.data_rows = []

        if not os.path.isfile(self.file_name):
            print("ERROR_MESSAGE: File doesn't exists.")
            return False

        with open(self.file_name) as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                self.data_rows.append(row)
        return True

    def get_edges(self):
        self.edges = []

        for edge in self.data_rows:
            self.edges.append(edge[:2])
        return True

    def build_graph(self):
        edges = self.edges
        self.graph = defaultdict(list)

        for edge in edges:
            a, b = edge[0], edge[1]

            self.graph[a].append(b)
            self.graph[b].append(a)
        return True

    def get_path(self):
        visited = []

        queue = [[self.start_node]]

        if self.start_node == self.goal_node:
            print("ERROR_MESSAGE: Given start and goal node values are same.")
            return False

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbours = self.graph[node]

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == self.goal_node:
                        self.short_path = new_path
                        return True

                visited.append(node)

        print("ERROR_MESSAGE: So sorry, but a connecting path doesn't exists.")
        return False

    def get_cost(self):
        self.cost = 0
        for count in range(len(self.short_path)):
            for row in self.data_rows:
                x = row[:2]
                y = self.short_path[count : count + 2]
                if x == y or x[::-1] == y:
                    self.cost += int(row[-1][0])
        return True

    def result(self):
        functions = [
            self.load_csv,
            self.get_edges,
            self.build_graph,
            self.get_path,
            self.get_cost,
        ]

        for func in functions:
            if not func():
                return False

        print(
            f"SUCCESS_MESSAGE: Path from {self.start_node} to {self.goal_node} is {'->'.join(self.short_path)}, and have cost {self.cost}."
        )
        return True


if __name__ == "__main__":
    file_name = str(input("What is graph file name: "))
    start_node = str(input("What is start node: "))
    goal_node = str(input("What is goal node: "))

    fsp = FindShortestPath(start_node, goal_node, file_name)
    fsp.result()