from math import inf

INFINITY = inf


class Graph:
    """
    Adjancency list of a graph
    """
    # Defining types
    Vertex = "Vertex"

    def __init__(self, maximum):
        """ Constructor for the Graph Class
        :Input:
            v_list: A list of integers, each representing a vertex of the graph
        """
        self.vertices = [None] * maximum
        self.length = 0

    def __len__(self):
        return self.length

    def bfs(self, source):
        bfs_list = []
        discovered = [source]

        # Traversing the entire graph
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.visited = True
            bfs_list.append(u)

            # Going through all edges of u
            for edge in u.edges:
                v = edge.v

                # Add neighbouring vertices to discovered if not in already
                if not v.discovered:
                    discovered.append(v)
                    v.discovered = True

        return bfs_list

    def dfs(self, source):
        dfs_list = []
        discovered = [source]

        # Traversing the entire graph
        while len(discovered) > 0:
            u = discovered.pop()
            u.visited = True
            dfs_list.append(u)

            # Going through all edges of u
            for edge in u.edges:
                v = edge.v

                # Add neighbouring vertices to discovered if not in already
                if not v.discovered:
                    discovered.append(v)
                    v.discovered = True

        return dfs_list

    def add_vert(self, v_id):
        self.vertices[len(self)] = Vertex(v_id)
        self.length += 1

    def add_edges(self, u_id, v_id, w=1):
        """ Method to add edges into vertex u inside the graph
        :Input:
            u: The vertex the edge is outgoing from
            v: The vertex the edge is incoming to
            w: The weight of the edge

        :Post condition: The vertex u in the graph will have a new edge from u to v with weight w
        """
        self.vertices[u_id].add_edge(self.vertices[v_id], w)

    def dijkstra(self, source_id):
        """ Finding distance from source to other vertices using Dijkstra algorithm
        :Input:
            source: The starting vertex

        :Post condition: All vertices in the graph will have their closest distance from source
        """
        # Starting vertex and initialising MinHeap and returning list
        source = self.vertices[source_id]
        source.distance = 0
        source.discovered = True

        dijk_minheap = MinHeap(len(self.vertices))

        # Resetting all vertices
        for vert in self.vertices:
            if vert.id != source_id:
                vert.distance = INFINITY
                vert.discovered = False
                vert.visited = False
            dijk_minheap.append(vert)

        # Traversing the entire graph
        while len(dijk_minheap) > 0:
            u = dijk_minheap.serve()
            u.visited = True

            # Going through all edges of u
            for edge in u.edges:
                v = edge.v
                new_dist = u.distance + edge.w

                # Add neighbouring vertices to discovered if not in already
                if not v.discovered:
                    v.discovered = True

                    # Updating distance and previous vertex
                    v.distance, v.previous = new_dist, u
                    dijk_minheap.update(v)

                # Not visited = not finalised
                elif not v.visited and v.distance > new_dist:
                    # Updating distance and previous vertex
                    v.distance, v.previous = new_dist, u
                    dijk_minheap.update(v)

    def __str__(self):
        """ toString method for the Graph Class"""
        return ','.join(self.vertices)


class Vertex:
    def __init__(self, id):
        """ Constructor for the Vertex class
        :Input:
            id: The id of the vertex
        """
        self.id = id
        self.edges = []
        self.visited = False
        self.discovered = False
        self.distance = INFINITY
        self.previous = None

    def add_edge(self, v, w=1):
        self.edges.append(Edge(self, v, w))

    def __str__(self) -> str:
        """ toString method for the Vertex Class """
        return str(self.id)


class Edge:
    def __init__(self, u, v, w=1):
        """ Constructor for the Edge Class
        :Input:
            u:  The origin of the edge
            v:  The destination of the edge
            w:  The weight of the edge
        """
        self.u = u
        self.v = v
        self.w = w


class MinHeap:
    def __init__(self, maximum):
        # Heap array to hold (vertex, dist) values
        self.heap_arr = [None] * (maximum + 1)

        # for vertex v, array[v] holds its index in heap_array
        self.ind_arr = [None] * maximum

        # This length only counts how many vertices is in the heap
        # len(self) + 1 == len(self.heap_arr)
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def rise(self, source):
        src_ind = self.ind_arr[source.id]
        while src_ind > 1:
            if source.distance < self.heap_arr[src_ind // 2].distance:
                self.swap(src_ind, src_ind // 2)
                src_ind //= 2
            else:
                break

    def sink(self, source):
        src_ind = self.ind_arr[source.id]
        while src_ind * 2 <= len(self):
            smallest_ind = self.smallest_child(source)
            if self.heap_arr[smallest_ind].distance < source.distance:
                self.swap(smallest_ind, smallest_ind // 2)
                src_ind = smallest_ind
            else:
                break

    def smallest_child(self, source):
        heap_ind = self.ind_arr[source.id]
        if heap_ind * 2 == len(self) or self.heap_arr[heap_ind * 2].distance < self.heap_arr[heap_ind * 2 + 1].distance:
            return heap_ind * 2
        return heap_ind * 2 + 1

    def swap(self, child_ind, parent_ind):
        child, parent = self.heap_arr[child_ind].id, self.heap_arr[parent_ind].id

        # Swapping child and parent vertices in both index_arr and heap_arr
        self.ind_arr[child], self.ind_arr[parent] = parent_ind, child_ind
        self.heap_arr[child_ind], self.heap_arr[parent_ind] = self.heap_arr[parent_ind], self.heap_arr[child_ind]

    def append(self, vert):
        self.length += 1
        self.heap_arr[self.length] = vert
        self.ind_arr[vert.id] = self.length
        self.rise(vert)

    def serve(self):
        """ Equivalent to get_min """
        self.swap(1, len(self.heap_arr) - 1)
        vert = self.heap_arr.pop()
        self.length -= 1
        if len(self) > 0:
            self.sink(self.heap_arr[1])
        return vert

    def update(self, vert):
        """ Since the vertices are objects, 
            the distance and previous attributes would already be updated
            So we only need to call rise.
        """
        self.rise(vert)

    def __str__(self):
        return str([str(v) for v in self.heap_arr])


if __name__ == '__main__':
    g = Graph(6)
    v_list = [0, 1, 2, 3, 4, 5]
    for v in v_list:
        g.add_vert(v)

    g.add_edges(0, 2, 5)
    g.add_edges(0, 4, 2)
    g.add_edges(0, 5, 4)
    g.add_edges(1, 4, 3)
    g.add_edges(1, 5, 3)
    g.add_edges(2, 0, 5)
    g.add_edges(2, 3, 1)
    g.add_edges(2, 4, 6)
    g.add_edges(3, 2, 1)
    g.add_edges(4, 0, 2)
    g.add_edges(4, 1, 3)
    g.add_edges(4, 2, 6)
    g.add_edges(4, 5, 10)
    g.add_edges(5, 0, 4)
    g.add_edges(5, 1, 3)
    g.add_edges(5, 4, 10)

    g.dijkstra(0)
    for v in g.vertices:
        print("Vertex", str(v.id), "with distance", str(
            v.distance), "and previous vertex", str(v.previous))

