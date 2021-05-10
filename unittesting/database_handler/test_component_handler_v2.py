import unittest
from database.handler.component_handler import get_component_list, get_component, delete_component, update_component, add_component
from unittesting.database_handler.test_data_component_handler import *


class TestGetComponent(unittest.TestCase):

    uid = None

    @classmethod
    def setUpClass(cls):

        component_list_pre = get_component_list()['components']
        # add new component
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.uid = post_uid['uid']

    def setUp(self):
        pass

    def test_1001(self):
        GET_COMPONENT_IN['uid'] = self.uid
        GET_COMPONENT_OUT['component']['uid'] = self.uid

        result = get_component(GET_COMPONENT_IN)

        del result['component']['creation_timestamp']
        del result['component']['last_timestamp']

        self.assertEqual(result, GET_COMPONENT_OUT)

    def test_1002_1003(self):

        result = get_component(GET_COMPONENT_IN)

        del result['component']['creation_timestamp']
        del result['component']['last_timestamp']

        uids_to_be_tested = [1.5, 'abc']

        for uid in uids_to_be_tested:
            GET_COMPONENT_IN['uid'] = uid

            with self.assertRaises(IndexError):
                get_component(GET_COMPONENT_IN)



    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):

        GET_COMPONENT_IN['uid'] = cls.uid
        delete_component(GET_COMPONENT_IN)


