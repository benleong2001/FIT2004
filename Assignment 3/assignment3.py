""" FIT2004 - Assignment 3
Name:           Benjamin Leong Tjen Ho
Student ID:     32809824
Student Email:  bleo0009@student.monash.edu

QUESTION 1
- Create a FlowNetwork based on the allocations input
- Use Ford Fulkerson method to find out if the Network is feasible
- If it is, find out what's the allocation between housemates/restaurant and the meals
- Otherwise, just return None

QUESTION 2
- Create a Suffix Trie with the submission1 string
- Add the suffixes of submission2 into the same Trie
- While doing so, keep track of the deepest level/node which has a branch where each link is from different strings
- Based on the deepest level, find the % of similarities and the common substring
"""

import math


def floor(n):
    """ Function to return the floor of the input numeric value """
    return int(n // 1)


def ceil(n):
    """ Function to return the ceiling of the input numeric value """
    return int(n // 1 + (n != n // 1))


def round(n):
    """ Function to return the rounded value of the input numeric value """
    return floor(n) if n % 1 < 0.5 else ceil(n)


class FlowNetwork:
    """ Flow Network class for Question 1
    ATTRIBUTES:
        init_meals:     The smallest index in the .vertices array where the vertices represents a meal
        n:              The number of days
        vertices:       An array of vertices partitioned according to their categories
            INDEX           CATEGORY
            0               House
            1   - 6         Housemates/Restaurant
            7   - 6+m       Days
            7+m - 7+m+2n    Meals
                where m is the total number of days which the housemates are available to prepare the meals
    """

    def __init__(self, availability) -> None:
        """ Constructor for the FlowNetwork Class 
        :Input:
            availability:       A table representing the availabilities of the housemates

        :Time Complexity:       :Space Complexity:
        Best:   O(n)            Input:  O(n)
        Worst:  O(n)            Aux:    O(n)

        *where n = len(availability)
        """

        # Finding the total number of days which the housemates are available to prepare the meals
        no_of_availables = 0
        for day in availability:
            for avlb in day:
                if avlb:
                    no_of_availables += 1

        # Storing some values that will be helpful in future sections
        no_of_days = self.n = len(availability)
        no_of_vertices = 10 + no_of_availables + 2 * no_of_days
        self.init_meals = 7 + no_of_availables

        # Declaring all vertices - O(n)
        self.vertices = [None] * no_of_vertices
        for ind in range(no_of_vertices):
            if not ind:
                # Provider for the housemates
                self.vertices[ind] = Vertex(ind, -2*no_of_days)
            elif ind == no_of_vertices - 3:
                # A single vertex that all meals point to
                self.vertices[ind] = Vertex(ind, 2*no_of_days)
            else:
                # Any other vertex
                self.vertices[ind] = Vertex(ind)

        # Lowerbounds and capacities for housemates and restaurant
        lb_h_mates = floor(0.36 * no_of_days)
        cap_h_mates = ceil(0.44 * no_of_days)
        cap_rest = floor(0.1 * no_of_days)

        # Connecting house (source) to housemates and restaurant
        house = self.vertices[0]
        for person in range(6):
            hm = self.vertices[person + 1]
            if person == 5:
                house.add_edge(hm, 0, cap_rest)                 # Restaurant
            else:
                house.add_edge(hm, lb_h_mates, cap_h_mates)     # 5 Housemates

        # Connecting housemates to days and meals - O(n)
        curr_day = 7
        restaurant = self.vertices[6]
        for day, meals in enumerate(availability):
            bfast = self.vertices[self.init_meals + 2*day]
            dinner = self.vertices[self.init_meals + 2*day + 1]

            # For each day loop through every housemate's availability
            for person, available in enumerate(meals):
                person += 1
                # If not unavailable
                if available:
                    self.vertices[person].add_edge(
                        self.vertices[curr_day], 0, 1)

                    # Can prep breakfast
                    if available == 1:
                        self.vertices[curr_day].add_edge(bfast, 0, 1)

                    # Can prep dinner
                    elif available == 2:
                        self.vertices[curr_day].add_edge(dinner, 0, 1)

                    # Can prep either
                    else:
                        self.vertices[curr_day].add_edge(bfast, 0, 1)
                        self.vertices[curr_day].add_edge(dinner, 0, 1)
                    curr_day += 1

            # At the end of each day, add edge for restaurant to both meals of that day
            # Add edge from meals to all_meals (sink)
            restaurant.add_edge(bfast, 0, 1)
            restaurant.add_edge(dinner, 0, 1)
            bfast.add_edge(self.vertices[-3], 1, 1)
            dinner.add_edge(self.vertices[-3], 1, 1)

        source, sink = self.vertices[-2], self.vertices[-1]
        for i, v in enumerate(self.vertices):
            if i < len(self.vertices) - 2:
                demand = v.demand
                if demand > 0:
                    v.add_edge(sink, cap=demand)
                elif demand < 0:
                    source.add_edge(v, cap=-demand)
                v.demand = 0

    def ford_fulkerson(self):
        """ Function to execute Ford Fulkerson's method on the Residual Network object
        :Time Complexity:       :Space Complexity:
        Best:   O(1)            Input:  O(1)
        Worst:  O(n^2)          Aux:    O(n)

        *where n = the number of days
        """
        residual = ResidualNetwork(self.vertices)
        source, sink = residual.vertices[-2], residual.vertices[-1]

        # While the residual network still has path
        while residual.dfs(source, sink):
            current = residual.vertices[-1]
            min_flow = current.min_flow

            # Augmenting flow
            while current.id != source.id:
                prev_edge = current.previous
                opp_edge = prev_edge.opposite

                prev_edge.flow -= min_flow
                opp_edge.flow += min_flow

                prev_edge.ori_edge.flow += min_flow * \
                    (-1 if prev_edge.is_rev else 1)

                current = current.previous.u

        source_flow = 0
        for edge in self.vertices[-2].edges:
            source_flow += edge.flow
        print(source_flow)

        return source_flow == 2 * self.n

    def __str__(self):
        res = ""
        for v in self.vertices:
            res += str(v) + "\n"
        return res


class ResidualNetwork:
    """ Residual Network class for Ford Fulkerson method. 
    ATTRIBUTES:
        vertices:   An array of vertices in the Residual Network
    """

    def __init__(self, vertices) -> None:
        """ Constructor for the Residual Network class
        :Input:
            vertices:   An adjacency list of an existing FlowNetwork

        :Time Complexity:       :Space Complexity:
        Best:   O(n)            Input:  O(n)
        Worst:  O(n)            Aux:    O(n)

        *where n = len(vertices)
        """
        # Creating all the vertices in the Residual Network
        self.vertices = [None] * len(vertices)
        for i in range(len(vertices)):
            self.vertices[i] = Vertex(i)

        for u_id, init_u in enumerate(vertices):
            for edge in init_u.edges:
                v_id = edge.v.id

                # Retrieving the Residual Network vertices
                u, v = self.vertices[u_id], self.vertices[v_id]

                # Creating edge for both directions with their respective flows
                forward_edge, backward_edge = Edge(u, v, 0, edge.cap - edge.flow),\
                    Edge(v, u, 0, edge.flow)

                # Each edge's opposite is each other and both vertice's original edge is the same
                forward_edge.opposite, backward_edge.opposite = backward_edge, forward_edge
                forward_edge.ori_edge, backward_edge.ori_edge = edge, edge

                backward_edge.is_rev = True

                u.append_edge(forward_edge)
                v.append_edge(backward_edge)

    def dfs(self, source, sink):
        """ DFS Function
        :Input:
            source: The starting vertex of the traversing path
            sink:   The ending vertex of the traversing path

        :Time Complexity:       :Space Complexity:
        Best:   O(1)            Input:  O(1)
        Worst:  O(n)            Aux:    O(1)

        *where n = the number of days   
        """
        # Resetting all vertices
        for v in self.vertices:
            v.discovered, v.previous, v.min_flow = False, None, math.inf

        discovered = [source]

        # Traversing the entire graph
        while len(discovered) > 0:
            u = discovered.pop()

            # Ending vertex was reached
            if u.id == sink.id:
                return True

            # Going through all edges of u
            for edge in u.edges:
                v = edge.v

                # Add neighbouring vertices to discovered if not in already
                if not v.discovered and edge.flow:
                    discovered.append(v)
                    v.discovered = True
                    v.previous = edge

                    # Finding the min_flow of the current path
                    v.min_flow = min(edge.flow, u.min_flow)
        return False


class Vertex:
    """ Basic Vertex class for FlowNetwork
    ATTRIBUTES:
        id          A unique identifier for the vertex
        demand      The demand for the vertex (default is 0)
        edges       A list of edges which are outgoing from the vertex
        discovered  A boolean stating if it's been discovered (for DFS)
        previous    The previous edge pointing into this vertex (for DFS)
        min_flow    The minimum flow of the current path which passes this vertex (for DFS)
    """

    def __init__(self, id, demand=0) -> None:
        """ Constructor for Vertex class """
        self.id = id
        self.demand = demand
        self.edges = []
        self.discovered = False
        self.previous = None
        self.min_flow = math.inf

    def add_edge(self, v, lb=0, cap=math.inf, flow=0):
        """ Creates an Edge and appends it to the vertex's list of edges """
        self.demand += lb
        v.demand -= lb
        self.edges.append(Edge(self, v, cap-lb, flow))

    def append_edge(self, edge):
        """ Appends the input edge to the vertex's list of edges """
        self.edges.append(edge)

    def __str__(self):
        res = "Vertex " + str(self.id)
        res += "\tDemand: " + str(self.demand)
        res += "\nEdges: \n" + "\n".join([str(e) for e in self.edges]) + "\n"
        return res


class Edge:
    """
    ATTRIBUTES:
        u:          The starting vertex of the edge
        v:          The ending vertex of the edge
        cap:        The capacity of the edge
        flow:       The current flow of the edge
        opposite:   The edge which is from v to u, i.e., goes in the opposite direction
        ori_edge:   The edge on the original network that aligns with this edge
        is_rev:     A boolean value stating if the edge is reverse from its original edge
    """

    def __init__(self, u, v, cap, flow) -> None:
        """ Constructor for Edge class """
        self.u, self.v = u, v
        self.cap = cap
        self.flow = flow
        self.opposite = None
        self.ori_edge = None
        self.is_rev = False

    def __str__(self):
        res = "From: " + str(self.u.id)
        res += "\tTo: " + str(self.v.id)
        res += "\tFlow: " + str(self.flow)
        res += "\tCap: " + str(self.cap)
        return res


def allocate(availability):
    """ Function to allocate housemates to meals in the next n days 
    :Input:
        availability:   A table representing the availabilities of the housemates

    :Time Complexity:       :Space Complexity:
    Best:   O(1)            Input:  O(n)
    Worst:  O(n^2)          Aux:    O(n)

    *where n = len(availability)

    Details:
    - After checking if the network is feasible using the Ford Fulkerson method,
        the original FlowNetwork will contain the flow from housemates/restaurant to their allocated meals.
    - allocate_meals() function is used to allocate the housemates/restaurant to meals
    """
    def allocate_meals(current, person, is_meals):
        """ Function to allocate all the meals to the input person
        :Input:
            current:    The current day/restaurant vertex
            person:     The person (housemate) id

        :Time Complexity:       :Space Complexity:
        Best:   O(n)            Input:  O(1) 
        Worst:  O(n)            Aux:    O(1)

        *where n is the number of days

        Note: Allocation is done by checking the edges of the current vertices with flows. 
                The vertices connected will then be the meals allocated to the respective housemates/restaurant.
        """
        # Checking all edges with flow
        for edge in current.edges:
            if edge.flow:

                # If the next vertex is a meal, allocate accordingly, else, go to next vertex
                if is_meals:
                    meal = edge.v.id - init_meals
                    allocation[meal % 2][meal // 2] = person
                else:
                    day = edge.v
                    allocate_meals(day, person, True)

    # Creating a FlowNetwork based on the availability input
    originalNetwork = FlowNetwork(availability)

    # If the FlowNetwork is feasible, proceed, else, return None
    if originalNetwork.ford_fulkerson():

        # Getting the smallest index of a meal and the number of days
        init_meals, n = originalNetwork.init_meals, originalNetwork.n

        # Allocating housemates/restaurant to each meals
        allocation = ([None] * n, [None] * n)
        for i in range(1, 7):

            # Getting housemate/restaurant vertex
            current = originalNetwork.vertices[i]
            allocate_meals(current, i - 1, i == 6)

        # Return the filled up allocation
        return allocation


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Question 2
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
class Trie:
    def __init__(self) -> None:
        """ Constructor for Trie Class """
        self.root = Node(level=0)

    def insert_string(self, string, is_1=True):
        """ Function to insert every suffix of the input string into the trie 
        :Input:
            string:     The string where it's suffixes are to be added the the Trie
            is_1:       A boolean value stating if the string is submission1

        :Time Complexity:       :Space Complexity:
        Best:   O(N^2)           Input:  O(N) 
        Worst:  O(N^2)           Aux:    O(N^2)

        *where N = len(string)

        Details:
        - Suffixes are found by changing the starting index pointer.
        - Suffixes are then added letter by letter
        - While adding, we keep track of the deepest level/node which has a branch where each link is from different strings
        """
        start_index, max_level = 0, 0
        for i in range(len(string)):
            current, node_level, new_max = self.root, 1, 0

            # Traversing Trie
            for j in range(i, len(string)):

                # Index of character in .link array
                ind = 1 if string[j] == " " else ord(string[j]) - 95

                # If character node does not exist in .link array
                if not current.link[ind]:
                    current.link[ind] = Node(level=node_level, is_1=is_1)

                elif current.link[ind].is_1:
                    new_max = node_level

                current = current.link[ind]
                node_level += 1

            # If the terminal does not exist, create one
            if not current.link[0]:
                current.link[0] = Node(level=node_level, is_1=is_1)

            if new_max > max_level:
                start_index, max_level = i, new_max

        return start_index, max_level


class Node:
    """
    ATTRIBUTES:
        level:  The level of the node in the Trie
        link:   A list of nodes which the current node links to
        is_1:   A boolean value stating if the letter the node represents is from submission1
    """

    def __init__(self, level=None, size=28, is_1=True) -> None:
        """ Constructor for Node class """
        self.level, self.link, self.is_1 = level, [None] * size, is_1


def compare_subs(submission1, submission2):
    """ Function to compare 2 strings
    :Input:
        submission1:    The first string to be compared
        submission2:    The second string to be compared

    :Time Complexity:       :Space Complexity:
    Best:  O((N+M)^2)       Input:  O(N+M) 
    Worst: O((N+M)^2)       Aux:    O((N+M)^2)

    *where N = len(submission1), M = len(submission2)

    Details:
    - insert_string() function is used to both insert the (suffixes of) strings 
        as well as compare similarities between the strings
    - We then return the sliced string (common substring) and their % of similarities.
        Common substring  = submission2 sliced based on the deepest level
        % of similarities = deepest level / length of string * 100
    """
    if not(submission1 and submission2):
        return ['', 0, 0]
    main_trie = Trie()

    # Inserting the 2 strings into the Trie created
    # Comparison is done whilst insertion
    (_, _), (start, deepest) = main_trie.insert_string(
        submission1), main_trie.insert_string(submission2, is_1=False)

    return [submission2[start: start + deepest], round(deepest/len(submission1)*100), round(deepest/len(submission2) * 100)]