#  File: Graph.py

#  Description: Looking at cities using Graphs

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/26/21

#  Date Last Modified: 05/01/21

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

    def head(self):
        return self.queue[0]


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

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

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        vert1 = self.get_index(fromVertexLabel)
        vert2 = self.get_index(toVertexLabel)

        if vert1 == -1 or vert2 == -1:
            return -1
        elif self.adjMat[vert1][vert2] == 0:
            return -1
        else:
            return self.adjMat[vert1][vert2]

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        vert = self.get_index(vertexLabel)
        lst = []
        next_v = self.get_adj_unvisited_vertex(vert)
        while next_v is not -1:
            lst.append(next_v)
            next_v = self.get_adj_unvisited_vertex(vert)
        return lst

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        lst = []
        for i in self.Vertices:
            lst.append(i)
        return lst

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

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        # you have to insert two 0's in the adjacency matrix
        # both verts have weight of 0
        vert1 = self.get_index(fromVertexLabel)
        vert2 = self.get_index(toVertexLabel)
        # check if undirected or directed
        # if undirected
        self.adjMat[vert1][vert2] = 0
        self.adjMat[vert2][vert1] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    # go to adj matrix delete the row, and the column where the very is
    # then delete the individual vert from the lst
    def delete_vertex(self, vertexLabel):
        the_vert = self.get_index(vertexLabel)

        # to delete column, we use a for loop
        for row in range(len(self.adjMat)):
            self.adjMat[row].pop(the_vert)

        # to delete a row
        self.adjMat.pop(the_vert)
        # delete the vertex
        self.Vertices.pop(the_vert)


def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # test depth first search
    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()

    # test breadth first search
    # do the breadth first search
    print("Breadth First Search")
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    print("Deletion of an edge")
    line = sys.stdin.readline().strip().split()
    c1 = line[0]
    c2 = line[1]
    cities.delete_edge(c1, c2)
    print()

    # use two for loops to make matrix
    print('Adjacency Matrix')
    for row in range(num_vertices):
        for col in range(num_vertices):
            if col != num_vertices - 1:
                print(cities.adjMat[row][col], end=' ')
            else:
                print(cities.adjMat[row][col])

    print()

    # test deletion of a vertex
    print("Deletion of a vertex")
    line = sys.stdin.readline().strip()
    print()

    print("List of Vertices")
    cities.delete_vertex(line)
    new_cities = cities.Vertices
    num_vertices = len(new_cities)
    for cit in new_cities:
        print(cit)
    print()

    # matrix again
    print('Adjacency Matrix')
    for row in range(num_vertices):
        for col in range(num_vertices):
            if col != num_vertices - 1:
                print(cities.adjMat[row][col], end=' ')
            else:
                print(cities.adjMat[row][col])


if __name__ == "__main__":
    main()
