import unittest
from database.handler.component_handler import get_component_list, get_component, delete_component, update_component, \
    add_component
from unittesting.test_database_handler.test_data_component_handler import *
from neomodel.exceptions import DoesNotExist, DeflateError
from neo4j.exceptions import CypherSyntaxError
import copy


class TestGetComponentList(unittest.TestCase):
    uid = []
    amount = 3

    @classmethod
    def setUpClass(cls):

        component_list_pre = get_component_list()['components']
        # add new component
        for i in range(0, cls.amount):
            add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.uid.append(post_uid['uid'])

    def setUp(self):
        i = 0
        for component in GET_COMPONENT_LIST_OUT['components']:
            component['uid'] = self.uid[i]
            i += 1

    def test_1401(self):

        self.assertEqual(len(self.uid), self.amount)

    def test_1402(self):
        result = get_component_list()

        components_to_be_deleted = []

        for component in result['components']:
            if component['uid'] not in self.uid:
                components_to_be_deleted.append(component)
            else:
                dict = component
                del dict['creation_timestamp']
                del dict['last_timestamp']

        for component in components_to_be_deleted:
            result['components'].remove(component)

        self.assertEqual(result, GET_COMPONENT_LIST_OUT)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):

        for uid in cls.uid:
            DELETE_COMPONENT_IN['uid'] = uid
            delete_component(DELETE_COMPONENT_IN)


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
        GET_COMPONENT_IN['uid'] = self.uid
        GET_COMPONENT_OUT['component']['uid'] = self.uid

    def test_1001(self):
        result = get_component(GET_COMPONENT_IN)

        del result['component']['creation_timestamp']
        del result['component']['last_timestamp']

        self.assertEqual(result, GET_COMPONENT_OUT)

    def test_1002_1003(self):
        uids_to_be_tested = [1.5, 'abc']

        for uid in uids_to_be_tested:
            GET_COMPONENT_IN['uid'] = uid

            with self.assertRaises(IndexError):
                get_component(GET_COMPONENT_IN)

    def test_1004(self):
        with self.assertRaises(KeyError):
            get_component({"test": 1, "test2": 2})

        with self.assertRaises(TypeError):
            get_component('abc')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):

        DELETE_COMPONENT_IN['uid'] = cls.uid
        delete_component(DELETE_COMPONENT_IN)


class TestAddComponent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.component_list_pre = get_component_list()['components']

    def setUp(self):
        pass

    def test_1301(self):
        result = add_component(ADD_COMPONENT_IN)
        self.assertEqual(result, ADD_COMPONENT_OUT)

        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid in self.component_list_pre:
                continue
            GET_COMPONENT_IN['uid'] = post_uid['uid']
            self.assertTrue(get_component(GET_COMPONENT_IN)['success'])

    def test_1302(self):
        with self.assertRaises(KeyError):
            add_component({"test": 1, "test2": 2})

    def test_1304(self):

        with self.assertRaises(DoesNotExist):
            wrong_input_dict = copy.deepcopy(ADD_COMPONENT_IN)
            wrong_input_dict['metrics']['test_metric'] = 2
            add_component(wrong_input_dict)

        with self.assertRaises((ValueError, DeflateError)):
            wrong_input_dict = copy.deepcopy(ADD_COMPONENT_IN)
            wrong_input_dict['metrics']['number_of_administrators'] = 'zwei'
            add_component(wrong_input_dict)

    def tearDown(self):
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid in self.component_list_pre:
                continue
            DELETE_COMPONENT_IN['uid'] = post_uid['uid']
            delete_component(DELETE_COMPONENT_IN)

    @classmethod
    def tearDownClass(cls):
        pass


class TestUpdateComponent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.component_list_pre = get_component_list()['components']

    def setUp(self):
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid in self.component_list_pre:
                continue
            self.uid = post_uid['uid']

        UPDATE_COMPONENT_IN['uid'] = self.uid
        GET_COMPONENT_IN['uid'] = self.uid

    def test_1201(self):
        result = update_component(UPDATE_COMPONENT_IN)
        self.assertEqual(result, UPDATE_COMPONENT_OUT)

        self.assertTrue(get_component(GET_COMPONENT_IN)['success'])

    def test_1202(self):
        with self.assertRaises(KeyError):
            update_component({"test": 1, "test2": 2})

    def test_1203(self):
        with self.assertRaises(CypherSyntaxError):
            wrong_input_dict = copy.deepcopy(UPDATE_COMPONENT_IN)
            wrong_input_dict['metrics']['number_of_administrators'] = 'zwei'
            update_component(wrong_input_dict)

    def test_1204(self):
        with self.assertRaises(CypherSyntaxError):
            UPDATE_COMPONENT_IN['uid'] = '123456789'
            update_component(UPDATE_COMPONENT_IN)

    def test_1205(self):
        UPDATE_COMPONENT_IN['uid'] = self.uid
        wrong_input_dict = copy.deepcopy(UPDATE_COMPONENT_IN)
        wrong_input_dict['metrics']['planned_maintenance_percentage'] = 2
        self.assertEqual(update_component(wrong_input_dict), UPDATE_COMPONENT_OUT)

        GET_COMPONENT_IN['uid'] = self.uid
        result = get_component(GET_COMPONENT_IN)

        self.assertTrue('test_metric' not in result['component']['metrics'])

    def tearDown(self):
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid in self.component_list_pre:
                continue
            GET_COMPONENT_IN['uid'] = post_uid['uid']
            delete_component(GET_COMPONENT_IN)

    @classmethod
    def tearDownClass(cls):
        pass


class TestDeleteComponent(unittest.TestCase):
    component_list_pre = []

    @classmethod
    def setUpClass(cls):
        cls.component_list_pre = get_component_list()['components']

    def setUp(self):
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid in self.component_list_pre:
                continue
            self.uid = post_uid['uid']

        DELETE_COMPONENT_IN['uid'] = self.uid
        GET_COMPONENT_IN['uid'] = self.uid

    def test_1101(self):

        self.assertTrue(get_component(GET_COMPONENT_IN)['success'])

        result = delete_component(DELETE_COMPONENT_IN)
        self.assertEqual(result, DELETE_COMPONENT_OUT)

        with self.assertRaises(IndexError):
            get_component(GET_COMPONENT_IN)

    def test_1102_1103_1105(self):

        uids_to_be_tested = [1.5, 'abc', '123456789']

        for uid in uids_to_be_tested:
            DELETE_COMPONENT_IN['uid'] = uid

            with self.assertRaises(CypherSyntaxError):
                delete_component(DELETE_COMPONENT_IN)

    def test_1104(self):
        with self.assertRaises(KeyError):
            delete_component({"test": 1, "test2": 2})

        with self.assertRaises(TypeError):
            delete_component('abc')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in cls.component_list_pre:
                GET_COMPONENT_IN['uid'] = post_uid['uid']
                delete_component(GET_COMPONENT_IN)


if __name__ == '__main__':
    unittest.main()
