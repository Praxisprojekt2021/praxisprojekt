import unittest

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
        print(GET_PROCESS_IN)
        delete_process(GET_PROCESS_IN)


class TestAddProcess(unittest.TestCase):
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


    @classmethod
    def tearDownClass(cls):
        GET_PROCESS_IN["uid"] = cls.uid
        print(GET_PROCESS_IN)
        delete_process(GET_PROCESS_IN)
