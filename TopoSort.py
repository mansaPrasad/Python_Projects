#  File: TopoSort.py

#  Description: using topological sort for a directed acyclic graph

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/30/21

#  Date Last Modified: 04/05/21

import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)

    # returns the first item in the queue
    def head(self):
        return self.queue[0]


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.in_path = False
        self.in_degree = 0

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        vertex_size = len(self.Vertices)
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        # increases the in degree of finish
        self.Vertices[finish].in_degree += 1

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while not theStack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if u == -1:
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        # create the Queue
        theQueue = Queue()

        # mark the vertex v as visited and enqueue onto queue
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit all the other vertices according to depth
        while not theQueue.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theQueue.head())
            if u == -1:
                u = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        # the queue is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    def delete_vertex(self, vertexLabel):
        the_vert = self.get_index(vertexLabel)

        # to delete column, we use a for loop
        for row in range(len(self.adjMat)):
            self.adjMat[row].pop(the_vert)

        # to delete a row
        self.adjMat.pop(the_vert)
        # delete the vertex
        self.Vertices.pop(the_vert)

    def get_neighbors(self, v):
        vert = self.get_index(v)
        lst = []
        for i in range(len(self.Vertices)):
            if self.adjMat[vert][i] != 0:
                lst.append(i)
        return lst

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def hasCycle(self):
        # Modified dfs for each vertex
        for i in range(len(self.Vertices)):
            # create a stack
            theStack = Stack()

            # mark the vertex as visited and push on the stack
            (self.Vertices[i]).visited = True
            theStack.push(i)

            # Once empty, all vertices have been visited
            while not theStack.is_empty():
                # Actual modification: detects if there is a back edge to the
                # starting vertex
                if self.linksTo(theStack.peek(), i):
                    return True
                # get an adjacent unvisited vertex
                u = self.get_adj_unvisited_vertex(theStack.peek())
                if (u == -1):
                    u = theStack.pop()
                else:
                    (self.Vertices[u]).visited = True
                    theStack.push(u)

            # stack is empty reset the flags
            self.resetVisited()

        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        queue1 = Queue()
        lst = []
        # while lst of vertices aren't empty
        while len(self.Vertices) != 0:
            temp_lst = []
            for v in self.Vertices:
                if v.in_degree == 0:
                    temp_lst.append(v)
                    self.delete_vertex(v)
            temp_lst.sort()
            for i in temp_lst:
                queue1.enqueue(i)

        # dequeue the items and add that to lst
        while queue1.is_empty() == False:
            item = queue1.dequeue()
            lst.append(item.label)

        return lst


def main():
    # convert graph to work with letters to numbers and then we have to convert this back
    # create a Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read in all the characters
    for i in range(num_vertices):
        line = sys.stdin.readline()
        char = line.strip()
        theGraph.add_vertex(char)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        # use get index to get index of str
        start = theGraph.get_index(edge[0])
        finish = theGraph.get_index(edge[1])
        weight = 1

        theGraph.add_directed_edge(start, finish, weight)

    # test if a directed graph has a cycle
    if theGraph.has_cycle():
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if not theGraph.has_cycle():
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)


if __name__ == "__main__":
    main()