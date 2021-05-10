import unittest
from database.handler.component_handler import get_component_list, get_component, delete_component, update_component, add_component
from unittesting.database_handler.test_data_component_handler import *


class TestGetComponent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        component_list_pre = get_component_list()['components']
        # add new component
        add_component(GET_COMPONENT_SETUP)
        component_list_post = get_component_list()['components']

        cls.uid = None

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.uid = post_uid['uid']

    def setUp(self):
        pass

    def test_1001(self):

        self.assertEqual(1, 1)

    def test_1002(self):

        self.assertEqual(1, 1)

    def tearDown(self):
        print('Hi2')

    @classmethod
    def tearDownClass(cls):
        cls.test = 1
        print('Hi')

