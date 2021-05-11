import unittest

from neo4j.exceptions import CypherSyntaxError

from database.handler.component_handler import get_component_list, add_component, delete_component
from unittesting.database_handler.test_data_component_handler import ADD_COMPONENT_IN
from unittesting.database_handler.test_data_processs_handler import *
from database.handler.process_handler import *


class TestGetProcess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(GET_PROCESS_SETUP_AND_OUT)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        GET_PROCESS_IN["uid"] = cls.uid
        GET_PROCESS_SETUP_AND_OUT["process"]["uid"] = cls.uid

    def test_2001(self):
        is_dict = get_process(GET_PROCESS_IN)
        is_dict["process"].pop("creation_timestamp")
        is_dict["process"].pop("last_timestamp")
        self.assertEqual(is_dict, GET_PROCESS_SETUP_AND_OUT)

    def test_2002_2003(self):
        uids_to_be_tested = [1.5, 'abc']

        for uid in uids_to_be_tested:
            GET_PROCESS_IN['uid'] = uid
            with self.assertRaises(IndexError):
                get_process(GET_PROCESS_IN)

    def test_2004(self):

        GET_PROCESS_IN.pop("uid")
        GET_PROCESS_IN["test1"] = 12
        with self.assertRaises(KeyError):
            get_process(GET_PROCESS_IN)

    @classmethod
    def tearDownClass(cls):
        GET_PROCESS_IN["uid"] = cls.uid
        delete_process(GET_PROCESS_IN)


class TestAddProcess(unittest.TestCase):

    def test_2101(self):
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(GET_PROCESS_SETUP_AND_OUT)
        # get new process_list
        process_list_post = get_process_list()['processes']

        uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                uid = post_uid['uid']
        GET_PROCESS_SETUP_AND_OUT["process"]["uid"] = uid
        GET_PROCESS_IN["uid"] = uid
        is_dict = get_process(GET_PROCESS_IN)
        is_dict["process"].pop("creation_timestamp")
        is_dict["process"].pop("last_timestamp")
        self.assertEqual(is_dict, GET_PROCESS_SETUP_AND_OUT)
        delete_process(GET_PROCESS_IN)

    def test_2102(self):
        # add incorrect values to dict
        GET_PROCESS_SETUP_AND_OUT["target_metrics"]["downtime"]["average"] = "ABC"

        with self.assertRaises(ValueError):
            add_process(GET_PROCESS_SETUP_AND_OUT)
        delete_process(GET_PROCESS_IN)

    def test_2103(self):
        # add incorrect structure to dict
        GET_PROCESS_SETUP_AND_OUT.pop("target_metrics")

        with self.assertRaises(KeyError):
            add_process(GET_PROCESS_SETUP_AND_OUT)
        delete_process(GET_PROCESS_IN)


class TestUpdateProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(GET_PROCESS_SETUP_AND_OUT)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        GET_PROCESS_IN["uid"] = cls.uid
        GET_PROCESS_SETUP_AND_OUT["process"]["uid"] = cls.uid

    def test_2201(self):
        process_dict = get_process(GET_PROCESS_IN)
        process_dict["process"]["name"] = "New Name"

        update_process(process_dict)

        new_process_dict = get_process(GET_PROCESS_IN)
        process_dict["process"].pop("last_timestamp")
        new_process_dict["process"].pop("last_timestamp")

        self.assertEqual(new_process_dict, process_dict)

    def test_2202(self):
        process_dict = get_process(GET_PROCESS_IN)
        process_dict["target_metrics"]["downtime"]["average"] = "ABD"

        with self.assertRaises(CypherSyntaxError):
            update_process(process_dict)

    def test_2203(self):
        process_dict = get_process(GET_PROCESS_IN)
        process_dict["process"].pop("name")

        with self.assertRaises(KeyError):
            update_process(process_dict)

    def test_2204(self):
        process_dict = get_process(GET_PROCESS_IN)
        process_dict["process"]["uid"] = "ABC"

        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            update_process(process_dict)


    @classmethod
    def tearDownClass(cls):
        delete_process(GET_PROCESS_IN)


class TestDeleteProcess(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(GET_PROCESS_SETUP_AND_OUT)
        # get new process_list
        process_list_post = get_process_list()['processes']

        self.uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                self.uid = post_uid['uid']

        GET_PROCESS_IN["uid"] = self.uid

    def test_2301(self):
        self.assertEqual(delete_process(GET_PROCESS_IN), success_handler())

    def test_2302(self):
        GET_PROCESS_IN["uid"] = "ABC"

        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            delete_process(GET_PROCESS_IN)
            GET_PROCESS_IN["uid"] = self.uid
            delete_process(GET_PROCESS_IN)

    def test_2303(self):
        GET_PROCESS_IN.pop("uid")
        GET_PROCESS_IN["ABC"] = 12

        with self.assertRaises(KeyError):
            delete_process(GET_PROCESS_IN)

        GET_PROCESS_IN["uid"] = self.uid
        delete_process(GET_PROCESS_IN)


class TestAddProcessReference(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(GET_PROCESS_SETUP_AND_OUT)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None
        cls.componentUid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        GET_PROCESS_IN["uid"] = cls.uid
        GET_PROCESS_SETUP_AND_OUT["process"]["uid"] = cls.uid


        component_list_pre = get_component_list()['components']
        # add new component
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.componentUid = post_uid['uid']

    def test_2401(self):
        ADD_PROCESS_REFERENCE_IN["process_uid"] = self.uid
        ADD_PROCESS_REFERENCE_IN["component_uid"] = self.componentUid

        self.assertEqual(add_process_reference(ADD_PROCESS_REFERENCE_IN), success_handler())

        GET_PROCESS_IN["uid"] = self.uid
        out_dict = get_process(GET_PROCESS_IN)
        out_dict["process"].pop("last_timestamp")
        out_dict["process"].pop("creation_timestamp")
        out_dict["process"]["components"][0].pop("last_timestamp")
        out_dict["process"]["components"][0].pop("creation_timestamp")
        out_dict["process"]["components"][0]["uid"] = self.componentUid

        ADD_PROCESS_REFERENCE_OUT["process"]["components"][0]["uid"] = self.componentUid
        ADD_PROCESS_REFERENCE_OUT["process"]["uid"] = self.uid
        self.assertEqual(out_dict, ADD_PROCESS_REFERENCE_OUT)

    def test_2402(self):
        ADD_PROCESS_REFERENCE_IN["process_uid"] = "ABC"
        ADD_PROCESS_REFERENCE_IN["component_uid"] = "DCE"

        with self.assertRaises(CypherSyntaxError):
            add_process_reference(ADD_PROCESS_REFERENCE_IN)

    def test_2403(self):
        ADD_PROCESS_REFERENCE_IN["twwe"] = "ABC"
        ADD_PROCESS_REFERENCE_IN["wee"] = "DCE"
        ADD_PROCESS_REFERENCE_IN.pop("process_uid")
        ADD_PROCESS_REFERENCE_IN.pop("component_uid")

        with self.assertRaises(KeyError):
            add_process_reference(ADD_PROCESS_REFERENCE_IN)

    @classmethod
    def tearDownClass(cls):
        GET_PROCESS_IN["uid"] = cls.uid
        delete_process(GET_PROCESS_IN)
        GET_PROCESS_IN["uid"] = cls.componentUid
        delete_component(GET_PROCESS_IN)


class TestDeleteProcessReference(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(GET_PROCESS_SETUP_AND_OUT)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None
        cls.componentUid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        GET_PROCESS_IN["uid"] = cls.uid
        GET_PROCESS_SETUP_AND_OUT["process"]["uid"] = cls.uid


        component_list_pre = get_component_list()['components']
        # add new component
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.componentUid = post_uid['uid']

    def setUp(self):
        ADD_PROCESS_REFERENCE_IN["process_uid"] = self.uid
        add_process_reference(ADD_PROCESS_REFERENCE_IN)


    def test_2501(self):
        ADD_PROCESS_REFERENCE_IN["uid"] = self.uid
        self.assertEqual(delete_process_reference(ADD_PROCESS_REFERENCE_IN), success_handler())

    def test_2502(self):
        ADD_PROCESS_REFERENCE_IN["uid"] = "ABC"

        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            delete_process_reference(ADD_PROCESS_REFERENCE_IN)
            ADD_PROCESS_REFERENCE_IN["uid"] = self.uid
            delete_process(ADD_PROCESS_REFERENCE_IN)

    def test_2503(self):
        ADD_PROCESS_REFERENCE_IN.pop("uid")
        ADD_PROCESS_REFERENCE_IN["ABC"] = 12

        with self.assertRaises(KeyError):
            delete_process(ADD_PROCESS_REFERENCE_IN)
            ADD_PROCESS_REFERENCE_IN["uid"] = self.uid
            delete_process(ADD_PROCESS_REFERENCE_IN)

    @classmethod
    def tearDownClass(cls):
        GET_PROCESS_IN["uid"] = cls.uid
        delete_process(GET_PROCESS_IN)
        GET_PROCESS_IN["uid"] = cls.componentUid
        delete_component(GET_PROCESS_IN)