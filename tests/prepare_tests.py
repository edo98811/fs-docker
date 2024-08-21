import pandas as pd
import testing_utils

import sys
# Creating the DataFrame

import unittest

sys.path.append("../") 
import fs_docker_manager.prepare as prepare
# Assuming Table class is defined in a module named table_module
# from table_module import Table

class TestPrepare(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        settings = testing_utils.settings()
        table = testing_utils.patient_table()
        cls.prepare_class = prepare.Prepare(table, settings)

    @classmethod
    def test_prepare_for_conversion(self):
        origins, _ = self.prepare_class.prepare_for_conversion(testing=True)
        message = "test_prepare_for_conversion for origin file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(origins, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_reconall(self):
        origins, _ = self.prepare_class.prepare_for_reconall(testing=True)
        message = "test_prepare_for_reconall for origin file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(origins, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_samseg(self):
        origins, _ = self.prepare_class.prepare_for_samseg(testing=True)
        message = "test_prepare_for_samseg for origin file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(origins, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_registration(self):
        origins, _ = self.prepare_class.prepare_for_registration(testing=True)
        message = "test_prepare_for_registration for origin file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(origins, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_tables(self):
        origins, _ = self.prepare_class.prepare_for_tables(testing=True)
        message = "test_prepare_for_tables for origin file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(origins, expected_file), message)
        pass
    
    @classmethod
    def test_prepare_for_conversion(self):
        _, destinations = self.prepare_class.prepare_for_conversion(testing=True)
        message = "test_prepare_for_conversion for destinations file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_reconall(self):
        _, destinations = self.prepare_class.prepare_for_reconall(testing=True)
        message = "test_prepare_for_reconall for destinations file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_samseg(self):
        _, destinations = self.prepare_class.prepare_for_samseg(testing=True)
        message = "test_prepare_for_samseg for destinations file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_registration(self):
        _, destinations = self.prepare_class.prepare_for_registration(testing=True)
        message = "test_prepare_for_registration for destinations file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        pass

    @classmethod
    def test_prepare_for_tables(self):
        _, destinations = self.prepare_class.prepare_for_tables(testing=True)
        message = "test_prepare_for_tables for destinations file not correct"

        expected_file = [""]
        self.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        pass

if __name__ == '__main__':
    unittest.main()
    

