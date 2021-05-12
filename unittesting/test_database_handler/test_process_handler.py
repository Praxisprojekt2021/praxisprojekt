import unittest

from neo4j.exceptions import CypherSyntaxError
import copy

from database.handler.component_handler import get_component_list, add_component, delete_component
from database.handler.process_handler import *
from unittesting.test_database_handler.test_data_component_handler import ADD_COMPONENT_IN
from unittesting.test_database_handler.test_data_processs_handler import *


class TestGetProcess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        UID_DICT["uid"] = cls.uid
        PROCESS_WITHOUT_TARGET_METRICS["process"]["uid"] = cls.uid

    def test_2001_correct_execution(self):
        is_dict = get_process(UID_DICT)
        is_dict["process"].pop("creation_timestamp")
        is_dict["process"].pop("last_timestamp")
        self.assertEqual(is_dict, PROCESS_WITHOUT_TARGET_METRICS)

    def test_2002_wrong_uid(self):
        uids_to_be_tested = [1.5, 'abc']

        for uid in uids_to_be_tested:
            UID_DICT['uid'] = uid
            with self.assertRaises(IndexError):
                get_process(UID_DICT)

    def test_2003_wrong_dict_structure(self):

        UID_DICT.pop("uid")
        UID_DICT["test1"] = 12
        with self.assertRaises(KeyError):
            get_process(UID_DICT)

    @classmethod
    def tearDownClass(cls):
        UID_DICT.pop("test1")
        UID_DICT["uid"] = cls.uid
        delete_process(UID_DICT)


class TestAddProcess(unittest.TestCase):

    def test_2101_correct_execution(self):
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                uid = post_uid['uid']
        PROCESS_WITHOUT_TARGET_METRICS["process"]["uid"] = uid
        UID_DICT["uid"] = uid
        is_dict = get_process(UID_DICT)
        is_dict["process"].pop("creation_timestamp")
        is_dict["process"].pop("last_timestamp")
        self.assertEqual(is_dict, PROCESS_WITHOUT_TARGET_METRICS)
        delete_process(UID_DICT)

    def test_2102_wrong_data(self):
        # add incorrect values to dict
        process_without_target_metrics = copy.deepcopy(PROCESS_WITHOUT_TARGET_METRICS)
        process_without_target_metrics["target_metrics"]["downtime"]["average"] = "ABC"

        with self.assertRaises(ValueError):
            add_process(process_without_target_metrics)
        delete_process(UID_DICT)

    def test_2103_wrong_dict_structure(self):
        # add incorrect structure to dict
        process_without_target_metrics = copy.deepcopy(PROCESS_WITHOUT_TARGET_METRICS)
        process_without_target_metrics.pop("target_metrics")

        with self.assertRaises(KeyError):
            add_process(process_without_target_metrics)
        delete_process(UID_DICT)


class TestUpdateProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        UID_DICT["uid"] = cls.uid
        PROCESS_WITHOUT_TARGET_METRICS["process"]["uid"] = cls.uid

    def test_2201_correct_execution(self):
        process_dict = get_process(UID_DICT)
        process_dict["process"]["name"] = "New Name"

        update_process(process_dict)

        new_process_dict = get_process(UID_DICT)
        process_dict["process"].pop("last_timestamp")
        new_process_dict["process"].pop("last_timestamp")

        self.assertEqual(new_process_dict, process_dict)

    def test_2202_wrong_metric_data(self):
        process_dict = get_process(UID_DICT)
        process_dict["target_metrics"]["downtime"]["average"] = "ABD"

        with self.assertRaises(CypherSyntaxError):
            update_process(process_dict)

    def test_2203_wrong_uid(self):
        process_dict = get_process(UID_DICT)
        process_dict["process"]["uid"] = "ABC"

        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            update_process(process_dict)

    def test_2204_wrong_dict_structure(self):
        process_dict = get_process(UID_DICT)
        process_dict["process"].pop("name")

        with self.assertRaises(KeyError):
            update_process(process_dict)

    @classmethod
    def tearDownClass(cls):
        delete_process(UID_DICT)


class TestDeleteProcess(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        self.uid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                self.uid = post_uid['uid']

        UID_DICT["uid"] = self.uid

    def test_2301_correct_execution(self):
        self.assertEqual(delete_process(UID_DICT), success_handler())

    def test_2302_wrong_uid(self):
        UID_DICT["uid"] = "ABC"

        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            delete_process(UID_DICT)
            UID_DICT["uid"] = self.uid
            delete_process(UID_DICT)

    def test_2303_wrong_dict_structure(self):
        UID_DICT.pop("uid")
        UID_DICT["ABC"] = 12

        with self.assertRaises(KeyError):
            delete_process(UID_DICT)

        UID_DICT["uid"] = self.uid
        delete_process(UID_DICT)


class TestAddProcessReference(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None
        cls.componentUid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        UID_DICT["uid"] = cls.uid
        PROCESS_WITHOUT_TARGET_METRICS["process"]["uid"] = cls.uid

        component_list_pre = get_component_list()['components']
        # add new component
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.componentUid = post_uid['uid']

    def test_2401_correct_execution(self):
        ADD_PROCESS_REFERENCE["process_uid"] = self.uid
        ADD_PROCESS_REFERENCE["component_uid"] = self.componentUid

        self.assertEqual(add_process_reference(ADD_PROCESS_REFERENCE), success_handler())

        UID_DICT["uid"] = self.uid
        out_dict = get_process(UID_DICT)
        out_dict["process"].pop("last_timestamp")
        out_dict["process"].pop("creation_timestamp")
        out_dict["process"]["components"][0].pop("last_timestamp")
        out_dict["process"]["components"][0].pop("creation_timestamp")
        out_dict["process"]["components"][0]["uid"] = self.componentUid

        PROCESS_WITH_TARGET_METRICS["process"]["components"][0]["uid"] = self.componentUid
        PROCESS_WITH_TARGET_METRICS["process"]["uid"] = self.uid
        self.assertEqual(out_dict, PROCESS_WITH_TARGET_METRICS)

    def test_2402_wrong_uid(self):
        ADD_PROCESS_REFERENCE["process_uid"] = "ABC"
        ADD_PROCESS_REFERENCE["component_uid"] = "DCE"

        with self.assertRaises(CypherSyntaxError):
            add_process_reference(ADD_PROCESS_REFERENCE)

    def test_2403_wrong_dict_structure(self):
        add_process_reference_in = copy.deepcopy(ADD_PROCESS_REFERENCE)
        add_process_reference_in["twwe"] = "ABC"
        add_process_reference_in["wee"] = "DCE"
        add_process_reference_in.pop("process_uid")
        add_process_reference_in.pop("component_uid")

        with self.assertRaises(KeyError):
            add_process_reference(add_process_reference_in)

    @classmethod
    def tearDownClass(cls):
        UID_DICT["uid"] = cls.uid
        delete_process(UID_DICT)
        UID_DICT["uid"] = cls.componentUid
        delete_component(UID_DICT)


class TestDeleteProcessReference(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None
        cls.componentUid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        UID_DICT["uid"] = cls.uid
        PROCESS_WITHOUT_TARGET_METRICS["process"]["uid"] = cls.uid

        component_list_pre = get_component_list()['components']
        # add new component
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.componentUid = post_uid['uid']

    def setUp(self):
        ADD_PROCESS_REFERENCE["process_uid"] = self.uid
        add_process_reference(ADD_PROCESS_REFERENCE)

    def test_2501_correct_execution(self):
        ADD_PROCESS_REFERENCE["uid"] = self.uid
        self.assertEqual(delete_process_reference(ADD_PROCESS_REFERENCE), success_handler())

    def test_2502_wrong_uid(self):
        ADD_PROCESS_REFERENCE["uid"] = "ABC"

        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            delete_process_reference(ADD_PROCESS_REFERENCE)
            ADD_PROCESS_REFERENCE["uid"] = self.uid
            delete_process(ADD_PROCESS_REFERENCE)

    def test_2503_wrong_dict_structure(self):
        add_process_reference_in = copy.deepcopy(ADD_PROCESS_REFERENCE)
        add_process_reference_in.pop("uid")
        add_process_reference_in["ABC"] = 12

        with self.assertRaises(KeyError):
            delete_process(add_process_reference_in)
            add_process_reference_in["uid"] = self.uid
            delete_process(add_process_reference_in)

    @classmethod
    def tearDownClass(cls):
        UID_DICT["uid"] = cls.uid
        delete_process(UID_DICT)
        UID_DICT["uid"] = cls.componentUid
        delete_component(UID_DICT)


class TestUpdateProcessReference(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None
        cls.componentUid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        UID_DICT["uid"] = cls.uid
        PROCESS_WITHOUT_TARGET_METRICS["process"]["uid"] = cls.uid

        component_list_pre = get_component_list()['components']
        # add new component
        add_component(ADD_COMPONENT_IN)
        component_list_post = get_component_list()['components']

        for post_uid in component_list_post:
            if post_uid not in component_list_pre:
                cls.componentUid = post_uid['uid']

        ADD_PROCESS_REFERENCE["process_uid"] = cls.uid
        ADD_PROCESS_REFERENCE["component_uid"] = cls.componentUid

        add_process_reference(ADD_PROCESS_REFERENCE)

    def test_2601_correct_execution(self):
        UPDATE_PROCESS_REFERENCE["uid"] = self.uid

        self.assertEqual(update_process_reference(UPDATE_PROCESS_REFERENCE), success_handler())

        new_process_dict = get_process(UID_DICT)
        new_process_dict["process"].pop("creation_timestamp")
        new_process_dict["process"]["components"][0].pop("creation_timestamp")
        new_process_dict["process"].pop("last_timestamp")
        new_process_dict["process"]["components"][0].pop("last_timestamp")

        PROCESS_WITH_TARGET_METRICS["process"]["components"][0]["weight"] = 7
        PROCESS_WITH_TARGET_METRICS["process"]["components"][0]["uid"] = self.componentUid
        PROCESS_WITH_TARGET_METRICS["process"]["uid"] = self.uid

        self.assertEqual(new_process_dict, PROCESS_WITH_TARGET_METRICS)

    def test_2602_wrong_uid(self):
        update_process_reference_in = copy.deepcopy(UPDATE_PROCESS_REFERENCE)
        update_process_reference_in["uid"] = "ABC"
        # TODO: Is this the right Exception?
        with self.assertRaises(CypherSyntaxError):
            update_process_reference(update_process_reference_in)

    def test_2603_wrong_weight(self):
        update_process_reference_in = copy.deepcopy(UPDATE_PROCESS_REFERENCE)
        update_process_reference_in["old_weight"] = "ABC"
        with self.assertRaises(CypherSyntaxError):
            update_process_reference(update_process_reference_in)

    def test_2604_wrong_dict_structure(self):
        update_process_reference_in = copy.deepcopy(UPDATE_PROCESS_REFERENCE)
        update_process_reference_in.pop("old_weight")
        with self.assertRaises(KeyError):
            update_process_reference(update_process_reference_in)

    @classmethod
    def tearDownClass(cls):
        UID_DICT["uid"] = cls.uid
        delete_process(UID_DICT)
        UID_DICT["uid"] = cls.componentUid
        delete_component(UID_DICT)


class TestGetProcessList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        # get old process_list
        process_list_pre = get_process_list()['processes']
        # add new component
        add_process(PROCESS_WITHOUT_TARGET_METRICS)
        # get new process_list
        process_list_post = get_process_list()['processes']

        cls.uid = None
        cls.componentUid = None

        for post_uid in process_list_post:
            if post_uid not in process_list_pre:
                cls.uid = post_uid['uid']

        UID_DICT["uid"] = cls.uid

    def test_2701_correct_execution(self):
        process_without_target_metrics = copy.deepcopy(PROCESS_WITHOUT_TARGET_METRICS)
        process_without_target_metrics["process"]["uid"] = self.uid
        process_without_target_metrics["process"].pop("components")

        process_list = get_process_list()
        for process in process_list["processes"]:
            if process["uid"] == self.uid:
                process.pop("creation_timestamp")
                process.pop("last_timestamp")
                self.assertEqual(process, process_without_target_metrics["process"])

    @classmethod
    def tearDownClass(cls):
        UID_DICT["uid"] = cls.uid
        delete_process(UID_DICT)


if __name__ == '__main__':
    unittest.main()
