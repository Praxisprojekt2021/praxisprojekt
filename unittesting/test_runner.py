import unittest
import HtmlTestRunner

# import your test modules
import unittesting.test_database_handler.test_metric_handler
import unittesting.test_database_handler.test_component_handler
import unittesting.test_database_handler.test_process_handler

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(unittesting.test_database_handler.test_metric_handler))
suite.addTests(loader.loadTestsFromModule(unittesting.test_database_handler.test_component_handler))
suite.addTests(loader.loadTestsFromModule(unittesting.test_database_handler.test_process_handler))

# initialize a runner, pass it your suite and run it
outfile = "reports"
runner = HtmlTestRunner.HTMLTestRunner(
    output=outfile
)

result = runner.run(suite)

if __name__ == '__main__':
    unittest.main()
