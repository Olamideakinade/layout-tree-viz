import unittest
from engine import TreeBuilder

class TestTreeBuilder(unittest.TestCase):
    def test_basic_tree(self):
        data = [('root', 'a'), ('a', 'b')]
        builder = TreeBuilder(data)
        self.assertEqual(len(builder.roots), 1)
        self.assertIn('root', builder.roots)

if __name__ == '__main__':
    unittest.main()