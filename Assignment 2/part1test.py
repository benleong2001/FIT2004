import unittest
import assignment2_chk

class TestMethods(unittest.TestCase):
    # Example 1
    # The roads represented as a list of tuple
    roads = [(0, 1, 4), (1, 2, 2), (2, 3, 3), (3, 4, 1), (1, 5, 2),
             (5, 6, 5), (6, 3, 2), (6, 4, 3), (1, 7, 4), (7, 8, 2),
             (8, 7, 2), (7, 3, 2), (8, 0, 11), (4, 3, 1), (4, 8, 10)]
    # The cafes represented as a list of tuple
    cafes = [(5, 10), (6, 1), (7, 5), (0, 3), (8, 4)]
    # Creating a RoadGraph object based on the given roads
    mygraph = assignment2_chk.RoadGraph(roads, cafes)

    def test_1(self):
        # Example 1.1
        start = 1
        end = 7

        self.assertEqual(self.mygraph.routing(start, end), [1, 7])

    def test_2(self):
        # Example 1.2
        start = 7
        end = 8

        self.assertEqual(self.mygraph.routing(start, end), [7, 8])

    def test_3(self):
        # Example 1.3
        start = 1
        end = 3

        self.assertEqual(self.mygraph.routing(start, end), [1, 5, 6, 3])

    def test_4(self):
        # Example 1.4
        start = 1
        end = 4

        self.assertEqual(self.mygraph.routing(start, end), [1, 5, 6, 4])

    def test_5(self):
        # Example 1.5
        start = 3
        end = 4

        self.assertEqual(self.mygraph.routing(start, end), [3, 4, 8, 7, 3, 4])

    def test_6(self):
        start = 5
        end = 5

        self.assertEqual(self.mygraph.routing(start, end), [5])

    def test_7(self):
        # The roads represented as a list of tuple
        roads = [(0, 1, 4), (1, 2, 2)]
        cafes = [(2, 10)]
        start = 0
        end = 0
        mygraph = assignment2_chk.RoadGraph(roads, cafes)

        self.assertEqual(mygraph.routing(start, end), None)

    def test_8(self):
        # The roads represented as a list of tuple
        roads = [(0, 1, 4), (1, 2, 2)]
        cafes = [(2, 10)]
        start = 2
        end = 0
        mygraph = assignment2_chk.RoadGraph(roads, cafes)

        self.assertEqual(mygraph.routing(start, end), None)

    def test_9(self):
        # The roads represented as a list of tuple
        roads = [(0, 1, 4), (1, 2, 2), (1, 3, 5), (3, 0, 4)]
        cafes = [(3, 10)]
        start = 2
        end = 0
        mygraph = assignment2_chk.RoadGraph(roads, cafes)

        self.assertEqual(mygraph.routing(start, end), None)


if __name__ == '__main__':
    unittest.main()
