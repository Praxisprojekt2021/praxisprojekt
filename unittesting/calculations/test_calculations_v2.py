import unittest
import copy

from processing.calculations import start_calculate_risk, get_all_component_metrics, get_all_target_metrics, calculate_current_values, calculate_actual_values, compare_actual_target_metrics, calculate_risk_score
from unittesting.calculations.test_data_calculations import *


class TestStartCalculateRisk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_1201(self):
        self.assertTrue(True)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestGetAllComponentMetrics(unittest.TestCase):

    def test_4201(self):

        process1 = PROCESS_DICT_HEAD
        process1['process']['components'] = [COMPONENT_ALL_METRICS_1, COMPONENT_ALL_METRICS_2]
        self.assertEqual(get_all_component_metrics(process1), PROCESS_ACTUAL_METRICS_ALL_ALL)

        process2 = PROCESS_DICT_HEAD
        process2['process']['components'] = [COMPONENT_ALL_METRICS_1, COMPONENT_FEW_METRICS]
        self.assertEqual(get_all_component_metrics(process2), PROCESS_ACTUAL_METRICS_ALL_1_FEW)


class TestGetAllTargetMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_4301(self):
        self.assertTrue(True)

    def test_4302(self):
        self.assertTrue(True)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestCalculateCurrentValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_4301(self):
        self.assertTrue(True)

    def test_4302(self):
        self.assertTrue(True)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestCalculateActualValues(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_4301(self):
        self.assertTrue(True)

    def test_4302(self):
        self.assertTrue(True)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestCompareActualTargetMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_4301(self):
        self.assertTrue(True)

    def test_4302(self):
        self.assertTrue(True)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestCalculateRiskScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_4301(self):
        self.assertTrue(True)

    def test_4302(self):
        self.assertTrue(True)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass