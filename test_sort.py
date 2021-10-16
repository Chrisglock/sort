import unittest
import sort

class TestSortingAlgorithms(unittest.TestCase):

    def test_quick_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])
        
    def test_quick_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.quick_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])
        
    def test_quick_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.quick_sort(a)
        self.assertEqual(a, [1])

    def test_quick_sort_4(self):
        """
        Prueba caso general #4
        """
        a = [1, 5, 5, 0, 3, 4, 11]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 1, 3, 4, 5, 5, 11])

    def test_bubble_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [110, 20, 3, 50, 23, 40, 53]
        sort.bubbleSort(a)
        self.assertEqual(a, [3, 20, 23, 40, 50, 53, 110])

    def test_bubble_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [0, 3, 2, 0, 2, 1, 0]
        sort.bubbleSort(a)
        self.assertEqual(a, [0, 0, 0, 1, 2, 2, 3])  

    def test_bubble_sort_3(self):
        """
        Prueba caso general #3
        """
        a = [7, 6, 5, 4, 3, 2, 1]
        sort.bubbleSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])  

    def test_bubble_sort_4(self):
        """
        Prueba caso lista tamaño 1 #4
        """
        a = [9]
        sort.bubbleSort(a)
        self.assertEqual(a, [9])

    def test_insertion_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [20, 7, 5, 4, 10, 1, 5]
        sort.insertionSort(a)
        self.assertEqual(a, [1, 4, 5, 5, 7, 10, 20])

    def test_insertion_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [7, 9, 4, 3, 2, 1, 1130]
        sort.insertionSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 7, 9, 1130])  

    def test_insertion_sort_3(self):
        """
        Prueba caso general #3
        """
        a = [110, 78, 345, 23, 324, 547, 158]
        sort.insertionSort(a)
        self.assertEqual(a, [23, 78, 110, 158, 324, 345, 547])  

    def test_insertion_sort_4(self):
        """
        Prueba caso lista tamaño 1 #4
        """
        a = [200]
        sort.insertionSort(a)
        self.assertEqual(a, [200])

    def test_selection_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [5, 1, 6, 3, 2, 7, 4]
        sort.selectionSort(a)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])  

    def test_selection_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [50, 10, 60, 30, 20, 70, 40]
        sort.selectionSort(a)
        self.assertEqual(a, [10, 20, 30, 40, 50, 60, 70])  

    def test_selection_sort_3(self):
        """
        Prueba caso general #3
        """
        a = [500, 100, 600, 300, 200, 700, 400]
        sort.selectionSort(a)
        self.assertEqual(a, [100, 200, 300, 400, 500, 600, 700])  

    def test_selection_sort_4(self):
        """
        Prueba caso lista tamaño 1 #4
        """
        a = [500]
        sort.selectionSort(a)
        self.assertEqual(a, [500])

          

if __name__ == '__main__':
    unittest.main()