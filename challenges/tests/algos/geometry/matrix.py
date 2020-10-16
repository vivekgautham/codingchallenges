import unittest
from challenges.src.algos.geometry import matrix


class Test_Matrix(unittest.TestCase):

    def test_islandPerimeter(self):
        mat = [
            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
        ]
        self.assertEqual(matrix.islandPerimeter(mat), 14)
        mat = [
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
        ]
        self.assertEqual(matrix.islandPerimeter(mat), 10)
        mat = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(matrix.islandPerimeter(mat), 4)
        mat = [
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
        ]
        self.assertEqual(matrix.islandPerimeter(mat), 12)


    def test_numberOfIslands(self):
        mat = [
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
        ]
        self.assertEqual(matrix.numberOfIslands(mat), 1)

        mat = [
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0],
        ]
        self.assertEqual(matrix.numberOfIslands(mat), 4)

        mat = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(matrix.numberOfIslands(mat), 1)

        mat = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(matrix.numberOfIslands(mat), 1)

        mat = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(matrix.numberOfIslands(mat), 0)

if __name__ == '__main__':
    unittest.main()


