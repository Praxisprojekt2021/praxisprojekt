import unittest
import database.handler.component_handler as component

class MyTestCase(unittest.TestCase):
    ##def test_something(self):
    ##    self.assertEqual(True, False)

    def test_delete_component(self):
        #1105
        uid_dict = {"uid": "999666111"}
        message = "Test value is not false."
        self.assertRaises(component.delete_component(uid_dict))
        #self.assertEqual(1+1,2)

        #1101

    def update_component(self):
        #1105
        uid_dict = {"uid": "999666111"}
        message = "Test value is not false."
        self.assertRaises(ValueError, component.update_component(uid_dict))
        #self.assertEqual(1+1,2)

        #1101


if __name__ == '__main__':
    unittest.main()

