""" FIT2004 - Assignment 2
PROBLEM 1
- Create a RoadGraph with road and cafe lists
- Road list determines roads (edges) and locations (vertices)
- Cafe list determines which location is a cafe (has waiting time)
- Perform dijkstra from start to all cafes
    - Create a MinHeap of the vertices
    - Source will have dist = 0, prev = None, disc = True
    - Rest will have dist = inf, prev = None, disc and vis = False
    - Traverse MinHeap
        - Take edges of current V
        - For each vert v of the edge, check if the new dist is shorter, if yes, take it

PROBLEM 2
"""

from asyncio.windows_events import INFINITE
from math import inf
from collections import deque
INFINITY = inf


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ========================================== PROBLEM #1 ==========================================
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class RoadGraph:
    """ RoadGraph Class - Assignment 2: Problem 1 
    - The Graph object essentially acts as an adjacency list where:
        - self.vertices is a list of vertices
        - Each vertex has a list of edges (and reverse edges)
    """

    def __init__(self, roads: list[tuple[int, int, int]], cafes: list[tuple[int, int]]):
        """ Basic Constructor for RoadGraph class
        :Input:
            roads: A list of road tuples in the form (u, v, w)
                        representing the edges in the graph.
            cafes: A list of tuples in the form (loc, wait)
                        representing cafes and waiting time.

        :Time Complexity:       :Space Complexity:
            Best:  O(E)             Input:  O(E) 
            Worst: O(E)             Aux:    O(E)
            *where E = len(roads)
        """
        # Find the highest vertex id
        max_vert = -1
        for road in roads:
            u, v, _ = road
            max_vert = max(max_vert, max(u, v))

        self.vertices = [None] * (max_vert + 1)

        # Loop through the edges to add vertices (to graph) and edges (to vertices)
        for road in roads:
            u, v, w = road
            u_vert = self.vertices[u] or Vertex(u)
            v_vert = self.vertices[v] or Vertex(v)

            # Adding the vertices to self.vertices if not already done
            if not self.vertices[u]:
                self.vertices[u] = u_vert
            if not self.vertices[v]:
                self.vertices[v] = v_vert

            # Adding edges to Vertex u and reverse edges to Vertex v
            u_vert.add_edge(v_vert, w)
            v_vert.add_rev_edge(u_vert, w)

        # Adding waiting times to locations that are cafes
        for c in cafes:
            cafe, wait = c
            vert = self.vertices[cafe]
            vert.set_waiting_time(wait)

    def dijkstra(self, source_id: int, fromEnd: bool = False) -> None:
        """ Dijkstra Function to find the shortest distance from source to the other Locations
        :Input:
            source_id:      The id of the source Vertex
            fromEnd:        A boolean value stating whether source is the start or end from routing()

        :Post Condition:    All Vertices will have their respective distances from source as their attribute values

        :Time Complexity:           :Space Complexity:
        Best:   O(E)                Input:  O(1)
        Worst:  O(E log V)          Aux:    O(V)

        *where E = len(roads), V = len(self.vertices)
        """
        def update(u, v):
            """ Updates distance, previous/next vertex and the MinHeap """
            v.distance[fromEnd] = new_dist
            v.prev_next_pair[fromEnd] = u
            dijk_minheap.rise(v)

        # Getting start vertex and assign initial values
        source = self.vertices[source_id]
        source.distance[fromEnd], source.discovered, source.prev_next_pair[fromEnd] = 0, True, None

        # Creating MinHeap of vertices
        dijk_minheap = MinHeap(len(self.vertices), fromEnd)

        # Resetting all vertices
        for vert in self.vertices:
            dijk_minheap.append(vert)
            if vert.id != source_id:
                vert.distance[fromEnd], vert.discovered, vert.visited, vert.prev_next_pair[fromEnd] = INFINITY, False, False, None

        # Traversing the entire graph
        while len(dijk_minheap) > 0:
            u = dijk_minheap.serve()

            # No routes from source to u exists
            if not u.discovered:
                continue

            # If fromEnd, then we need to consider the reverse edges
            u.visited, edges = True, u.rev_edges if fromEnd else u.edges

            # Going through all edges of u
            for edge in edges:
                v, new_dist = edge.v, edge.w + u.distance[fromEnd]

                # Add neighbouring vertices to discovered if not in already
                if not v.discovered:
                    v.discovered = True
                    update(u, v)

                # Not visited = not finalised
                elif not v.visited and v.distance[fromEnd] > new_dist:
                    update(u, v)

    def routing_hi(self, start: int, end: int) -> list[int] | None:
        """ Routing function that finds the shortest route from start to end
                which passes a cafe to get coffee too

        :Input:
            start:  The starting vertex id
            end:    The ending vertex id

        :Returns:   The route from start to end that passes a cafe
                    None if no route exists

        :Time Complexity:           :Space Complexity:
        Best:   O(E log V)          Input:  O(1)
        Worst:  O(E log V)          Aux:    O(E)

        *where E = len(roads), V = len(self.vertices)
        """
        # If either of start or end does not exist in graph
        length = len(self.vertices)
        if length <= start or length <= end:
            return

        # Perform dijkstra from start to all locations
        # and from end to all locations (using reversed edges)
        self.dijkstra(start), self.dijkstra(end, True)

        # Find the cafe with the shortest travel + wait time
        min_time, cafe = INFINITY, None
        for vert in self.vertices:
            if vert.isCafe and (new_min := sum(vert.distance) + vert.wait) < min_time:
                min_time, cafe = new_min, vert

        # Retrieve the (returning) route from start to cafe to end
        def pathfinder(vert):
            if not vert:
                return []
            res = pathfinder(vert.prev_next_pair[0])
            res.append(vert.id)
            return res

        # Backtracking to find route from start to end, passing a cafe
        route = pathfinder(cafe)
        while cafe and cafe.prev_next_pair[1]:
            route.append(cafe.prev_next_pair[1].id)
            cafe = cafe.prev_next_pair[1]

        # If route is nothing, return None
        return route or None

    def routing(self, start, end):
        length = len(self.vertices)
        if length <= start or length <= end:
            return

        def update(u, v):
            v.path_data = [u, has_cafe, wait]
            v.distance = new_dist
            route_minheap.rise(v)

        src = self.vertices[start]
        src.distance = 0
        src.discovered = True
        wait = src.wait if src.isCafe else INFINITY
        src.path_data = [None, src.isCafe, wait]

        route_minheap = MinHeap(len(self.vertices))
        for vert in self.vertices:
            route_minheap.append(vert)
            if vert.id != src.id:
                vert.distance, vert.discovered, vert.visited, vert.path_data[0] = INFINITY, False, False, None
        
        while len(route_minheap) > 0:
            u = route_minheap.serve()
            _, has_cafe, wait = u.path_data

            if not u.discovered:
                continue

            u.visited = True
            for edge in u.edges:
                v = edge.v
                
                has_cafe = has_cafe or v.isCafe
                wait = min(v.wait, wait) if v.isCafe else wait
                new_dist = edge.w + u.distance + (wait if has_cafe else 0)
                
                if not v.discovered:
                    v.discovered = True
                    update(u, v)
                elif not v.visited and new_dist < v.distance:
                    update(u, v)

        def pathfinder(vert):
            if not vert:
                return []
            res = pathfinder(vert.path_data[0])
            res.append(vert.id)
            return res
        final = self.vertices[end]
        return pathfinder(final) if final.path_data[1] else None


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ========================================== PROBLEM #2 ==========================================
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def optimalRoute_hi(downhillScores, start: int, finish: int) -> list[int] | None:
    """ optimalRoute Function - Assignment 2: Problem 2
    Function to find the most optimal route that acquires 
            the maximum amount of points from start to finish
    :Input:
        downhillScore:  A tuple that indicates the starting, ending and points acquired of a downhill segment
        start:          The starting point (id) of the route
        finish:         The finishing point (id) of the route

    :Returns:           A list of integers, representing the route from start to finish with the greatest score
                        None if no route exists

    :Time Complexity:       :Space Complexity:
            Best:  O(D)             Input:  O(D) 
            Worst: O(D)             Aux:    O(D)
            *where D = len(downhillScores)
    """
    # Create RevGraph
    hillGraph = RevGraph(downhillScores)

    # Create source, i.e., the end/finish
    src = hillGraph.vertices[finish]

    # If the source does not exist
    if not src:
        return

    # Reset source's profit and create a queue for the vertices
    src.profit, vert_list = 0, deque([src])

    # For other endpoints (vertex with no incoming edges, but not src),
    # decrement their neighbour's incoming_count by 1
    for v in hillGraph.vertices:
        if not v.incoming_count and v.id != src.id:
            for e in v.edges:
                e.v.incoming_count -= 1

    # Traverse all vertices
    while vert_list:
        u = vert_list.popleft()

        # No need to check start
        if u.id == start:
            continue

        # Look at all (reversed) edges of u
        for edge in u.edges:
            v, new_prof = edge.v, u.profit + edge.w
            v.incoming_count -= 1 if v.incoming_count else 0

            # Check if the new profit is larger than what v already has
            # If yes, override the profit value
            if new_prof > v.profit:
                v.profit, v.prev_next_pair[1] = new_prof, u

            if not v.incoming_count:
                vert_list.append(v)

    # Have an empty returning list and start backtracking from start
    returning_list, path_vert = [], hillGraph.vertices[start]

    # The backtracking ends when path_vert reaches None
    while path_vert:
        returning_list.append(path_vert.id)
        path_vert = path_vert.prev_next_pair[1]

    # If the route does not have the finishing vertex, return None
    return returning_list if returning_list[-1] == finish else None


def optimalRoute(downhillScores, start, finish):
    hill = RevGraph(downhillScores)
    src = hill.vertices[finish]
    src.profit = 0

    def traverse(current: Vertex):
        if current:
            for edge in current.edges:
                v, new_prof = edge.v, edge.w + current.profit
                if new_prof > v.profit:
                    v.profit = new_prof
                    v.prev_next_pair[1] = current
                traverse(v)

    traverse(src)

    vert = hill.vertices[start]
    route = []
    while vert:
        route.append(vert.id)
        vert = vert.prev_next_pair[1]

    return route if route[-1] == finish else None


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# ================================= OTHER CLASSES AND FUNCTIONS ==================================
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


class Vertex:
    """ A Vertex Class for Graphs
    ATTRIBUTES:
        id:             A unique id to distinguish vertices apart
        edges:          A list of Edges that are outgoing from the Vertex
        prev_next_pair: A list of two items, one for previous Vertex, one for next Vertex

        rev_edges:      A list of Edges that are incoming into the Vertex
        distance:       A list of 2 distances, one from start, one from end
        isCafe:         A boolean value stating if the Vertex is a cafe
        discovered:     A boolean value stating if the Vertex has been discovered (for dijkstra())
        visited:        A boolean value stating if the Vertex has been visited (for dijkstra())
        route_next:     The next Vertex when routing from start to cafe

        incoming_count: A counter keep track of how many unrelaxed incoming edges
        profit:         The max possible score acquired from this Vertex to finish
    """

    def __init__(self, id) -> None:
        """ Basic Constructor for Vertex class
        :Input:
            id: An integer representing the id of the Vertex

        :Time Complexity:       :Space Complexity:
            Best:  O(1)             Input:  O(1)
            Worst: O(1)             Aux:    O(1)
        """
        # General Attributes
        self.id = id
        self.edges = []
        self.prev_next_pair = [None, None]

        # Attributes for Problem 1
        self.rev_edges = []
        self.distance = [INFINITY, INFINITY]
        self.isCafe, self.discovered, self.visited = False, False, False
        self.route_next = None

        # Attributes for Problem 2
        self.incoming_count, self.profit = 0, -INFINITY

        # Attributes for Problem 1 - optimised
        self.distance = INFINITY
        # previous, has_cafe, waiting_time
        self.path_data = [None, False, INFINITY]

        #  Attributes for Problem 2 - optimised

    def add_edge(self, v, w): self.edges.append(Edge(self, v, w))
    """ Method to add an edge to the Vertex's list of edges
    :Input:
        v: The incoming vertex of the Edge
        w: The travelling time from self to Vertex v

    :Post condition: The vertex gains one more edge

    :Time Complexity:       :Space Complexity:
        Best:  O(1)             Input:  O(1)
        Worst: O(1)             Aux:    O(1)
    """

    def add_rev_edge(self, u, w): self.rev_edges.append(Edge(self, u, w))
    """ Method to add an edge to the Vertex's list of reversed edges
    :Input:
        u: The outgoing Vertex of the Edge
        w: The travelling time from Vertex u to self

    :Post condition: The vertex gains one more rev_edge

    :Time Complexity:       :Space Complexity:
        Best:  O(1)             Input:  O(1)
        Worst: O(1)             Aux:    O(1)
    """

    def set_waiting_time(self, wait): self.isCafe, self.wait = True, wait
    """ Mutator (setter) for the waiting time for the cafe.
        The method also sets isCafe to True since only cafes have waiting times.
    :Input:
        wait: The waiting time for the cafe

    :Time Complexity:       :Space Complexity:
        Best:  O(1)             Input:  O(1)
        Worst: O(1)             Aux:    O(1)
    """


class Edge:
    """ An Edge class for Graphs """

    def __init__(self, u, v, w): self.u, self.v, self.w = u, v, w
    """ Basic Constructor for RoadGraph class """


class MinHeap:
    """ A priority heap class that prioritises the minimum element """

    def __init__(self, maximum):
        """ Basic Constructor for the MinHeap Class
        :Input:
            maximum: The greatest number of nodes in the heap
            fromEnd: A boolean value stating if dijkstra is executed from end
        """
        # Heap array and index array of the MinHeap
        self.heap_arr, self.ind_arr = [None] * (maximum + 1), [None] * maximum

        # This length only counts how many vertices is in the heap
        self.length = 0
    def __len__(self): return self.length  # Returns the length of the heap

    # Returns the appropriate dist length based on which dijk is executing
    def get_dist(self, v): return v.distance

    def append(self, vert):
        """ Adds a node to the heap """
        self.length += 1
        self.heap_arr[self.length], self.ind_arr[vert.id] = vert, self.length
        self.rise(vert)

    def serve(self):
        """ Equivalent to get_min """
        self.swap(1, len(self))
        vert = self.heap_arr.pop()
        self.length -= 1
        if len(self):
            self.sink(self.heap_arr[1])
        return vert

    def rise(self, source):
        """ Rises a node (source) to its correct position """
        src_ind = self.ind_arr[source.id]
        while src_ind > 1:
            if self.get_dist(source) < self.get_dist(self.heap_arr[src_ind // 2]):
                self.swap(src_ind, src_ind // 2)
                src_ind //= 2
            else:
                break

    def sink(self, source):
        """ Sinks a node (source) to its correct position """
        src_ind = self.ind_arr[source.id]
        while src_ind * 2 <= len(self):
            smallest_ind = self.smallest_child_ind(source)
            if self.get_dist(self.heap_arr[smallest_ind]) < self.get_dist(source):
                self.swap(smallest_ind, src_ind)
                src_ind = smallest_ind
            else:
                break

    def smallest_child_ind(self, source):
        """ Find the smallest child of source node 
        :returns: The index of the smallest child
        """
        heap_ind = self.ind_arr[source.id]
        if heap_ind * 2 == len(self) or self.get_dist(self.heap_arr[heap_ind * 2]) < self.get_dist(self.heap_arr[heap_ind * 2 + 1]):
            return heap_ind * 2
        return heap_ind * 2 + 1

    def swap(self, child_ind, parent_ind):
        """ Swaps two nodes """
        child, parent = self.heap_arr[child_ind].id, self.heap_arr[parent_ind].id

        # Swapping child and parent vertices in both index_arr and heap_arr
        self.ind_arr[child], self.ind_arr[parent] = parent_ind, child_ind
        self.heap_arr[child_ind], self.heap_arr[parent_ind] = self.heap_arr[parent_ind], self.heap_arr[child_ind]


# CLASS USED FOR PROBLEM 2
class RevGraph:
    """ RevGraph class creates a graph where all input edges are reversed """

    def __init__(self, e_list) -> None:
        """ Basic Constructor of the RevGraph class
        :Input:
            e_list:         A list of edges as a tuple (u, v, w)
                    u:      The starting vertex of the edge
                    v:      The ending vertex of the edge
                    w:      The weight of the edge

        :Time Complexity: 
            Best:           O(D) where D = len(e_list)
            Worst:          O(D) where D = len(e_list)

        :Space Complexity:
            Input:          O(D) where D = len(e_list)
            Aux:            O(D) where D = len(e_list)
        """
        e_list = [(v, u, w) for u, v, w in e_list]

        # Find the highest vertex id
        max_vert = -1
        for e in e_list:
            u, v, _ = e
            max_vert = max(max_vert, max(u, v))

        self.vertices = [None] * (max_vert + 1)

        # Loop through the edges to add vertices (to graph) and edges (to vertices)
        for e in e_list:
            u, v, w = e
            u_vert = self.vertices[u] or Vertex(u)
            v_vert = self.vertices[v] or Vertex(v)

            # Adding the vertices to self.vertices if not already done
            if not self.vertices[u]:
                self.vertices[u] = u_vert
            if not self.vertices[v]:
                self.vertices[v] = v_vert

            # Adding edges to Vertex u
            u_vert.add_edge(v_vert, w)

        for _, v, _ in e_list:
            self.vertices[v].incoming_count += 1
