from math import inf
from graph import Vertex

INFINITY = inf


class MinHeap:
    def __init__(self) -> None:
        # Type hinting
        self.heap_arr: list[Vertex]

        # Heap array to hold (vertex, dist) values
        self.heap_arr = []

        # for vertex v, array[v] holds its index in heap_array
        self.ind_arr = []
        self.length = 1

    def __len__(self) -> int:
        return self.length

    def rise(self, source: Vertex) -> None:
        src_index = self.ind_arr[source.id]

        while src_index > 1:
            if source.distance < self.heap_arr[src_index // 2].distance:
                self.swap(src_index, src_index // 2)
                src_index //= 2
            else:
                break

    def sink(self, source: Vertex) -> None:
        src_ind = self.ind_arr[source]
        
        while src_ind * 2 <= len(self):
            smallest_ind = self.smallest_child(source)

            if self.heap_arr[smallest_ind].distance > source.distance:
                self.swap(smallest_ind, smallest_ind // 2)
                src_ind = smallest_ind
            
            else:
                break

    def smallest_child(self, source: Vertex) -> int:
        heap_ind = self.ind_arr[source.id]
        if heap_ind * 2 == self.length or self.heap_arr[heap_ind * 2].distance < self.heap_arr[heap_ind * 2 + 1].distance:
            return heap_ind * 2
        return heap_ind * 2 + 1

    def swap(self, child_ind: int, parent_ind: int) -> None:
        child, parent = self.heap_arr[child_ind].id, self.heap_arr[parent_ind].id

        # Swapping child and parent vertices in both index_arr and heap_arr
        self.ind_arr[child], self.ind_arr[parent] = parent_ind, child_ind
        self.heap_arr[child_ind], self.heap_arr[parent_ind] = self.heap_arr[parent_ind], self.heap_arr[child_ind]
        

    def push(self, vert: Vertex) -> None:
        self.heap_arr.append(vert)
        self.ind_arr[vert.id] = self.length
        self.length += 1
        self.rise(vert)

    def pop(self) -> Vertex:
        """ Equivalent to get_min """
        self.swap(1, len(self))
        self.length -= 1
        vert = self.heap_arr.pop()
        self.sink(self.heap_arr[1])
        return vert