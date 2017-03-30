import unittest
import exec_3


class TestDrawDiamondGraph(unittest.TestCase):
    def test_draw_diamond_graph_case_1(self):
        result = exec_3.draw_diamond_graph(3)
        self.assertEqual(result, """ *
* *
 *""")

    def test_draw_diamond_graph_case_2(self):
        result = exec_3.draw_diamond_graph(2)
        self.assertFalse(result)

    def test_draw_graph_case_3(self):
        result = exec_3.draw_diamond_graph(5)
        self.assertEqual(result, """  *
 * *
* * *
 * *
  *""")