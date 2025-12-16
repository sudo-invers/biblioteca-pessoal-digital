import unittest


def add(a, b):
    return a + b


class RepositoryTest(unittest.TestCase):
    def testCreateBook(self):
        self.assertEqual(add(1, 2), 3)

    def testUpdateBook(self):
        self.assertEqual(add(-1, -2), -3)

    def testDeleteBook(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)
    
    
    def testCreateMagazine(self):
        self.assertEqual(add(1, 2), 3)

    def testUpdateMagazine(self):
        self.assertEqual(add(-1, -2), -3)

    def testDeleteMagazine(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)
    
    
    def testCreateAnnotation(self):
        self.assertEqual(add(1, 2), 3)

    def testUpdateAnnotation(self):
        self.assertEqual(add(-1, -2), -3)

    def testDeleteAnnotation(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

if __name__ == "__main__":
    unittest.main()
