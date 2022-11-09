""" Documentation Format
# For classes
*Brief Description*
ATTRIBUTES:
    ...

# For methods
*Brief Description*
:Input:
    
:Returns / Post Condition / Outcome:

:Time Complexity:       :Space Complexity:
    Best :                  Input:
    Worst:                  Space:
"""


class FlowNetwork:
    """ Basic Flow Network class 
    ATTRIBUTES:
        vertices: A list of vertices in the Flow Network 
                    which essentially acts as an adjacency list
    """

    def __init__(self, e_list) -> None:
        """ Flow Network constructor method
        :Input:
            e_list:
        :Time Complexity:       :Space Complexity:
            Best :  O(V + E)        Input:  O(E)
            Worst:  O(V + E)        Space:  O(V + E)   

        How should e_list be like hmm?
        (u_id, v_id, flo, cap?)
        """
        # Finding the highest vertex id to create a vertices list of appropriate length
        max_v_id = -1
        for u, v, _, _ in e_list:
            max_v_id = max(max_v_id, max(u, v))
        self.vertices = [None] * (max_v_id + 1)

        # Looping through the edges list to add vertices and edges to the FlowNetwork and Vertices
        for u, v, f, c in e_list:
            u_vert = self.vertices[u] or Vertex(u)
            v_vert = self.vertices[v] or Vertex(v)

            # Adding vertices to the adj list if not already. 
            if not self.vertices[u]:
                self.vertices[u] = u_vert
            if not self.vertices[v]:
                self.vertices[v] = v_vert

            # Adding edges to the vertices
            # This may change into a matrix for assg3
            u_vert.add_edge(v_vert, f, c)
            v_vert.add_res_edge(u_vert, c - f, f)


class Vertex:
    """ Basic Vertex class for Flow Network
    ATTRIBUTES:
        id:         The id of the vertex
        edges:      A list of edges from the vertex
        res_edges:  A list of edges going to the vertex
        visited:    A boolean stating if the vertex has been visited during traversal
        discovered: A boolean stating if the vertex has been discovered during traversal
        is_s:       A boolean stating if the vertex can b reached by the Start vertex
    """

    def __init__(self, id) -> None:
        """ Vertex constructor method 
        :Input:
            id: The id of the vertex

        :Time Complexity:       :Space Complexity:
            Best :  O(1)            Input:  O(1)
            Worst:  O(1)            Space:  O(1)
        """
        self.id = id
        self.edges = []
        self.res_edges = []

        self.visited = False
        self.discovered = False
        self.is_s = False

    def add_edge(self, v, f, c) -> None:
        """ Method to add an edge to the Vertex's edge list """
        self.edges.append(Edge(self, v, f, c))

    def add_res_edge(self, u, f, c):
        """ Method to add a residual edge to the Vertex's res_edge list """
        self.res_edges.append(Edge(u, self, f, c))


class Edge:
    """ Basic Vertex class for Flow Network
    ATTRIBUTES:
        u:      The starting vertex of the edge
        v:      The ending vertex of the edge
        flow:   The current flow of the edge
        cap:    The capacity of the edge
    """

    def __init__(self, u, v, flow, cap) -> None:
        """ Edge Constructor method 
        :Input:
            u:      The starting vertex of the edge
            v:      The ending vertex of the edge
            flow:   The current flow of the edge
            cap:    The capacity of the edge

        :Time Complexity:       :Space Complexity:
            Best :  O(1)            Input:  O(1)
            Worst:  O(1)            Space:  O(1)
        """
        # The starting and ending vertex of the edge
        self.u, self.v = u, v

        # The flow and capacity of the edge
        # flow <= capacity
        self.flow, self.cap = flow, cap
