import pandas as pd
import testing_utils

import sys
# Creating the DataFrame

import unittest

sys.path.append("../") 
import prepare
# Assuming Table class is defined in a module named table_module
# from table_module import Table

class TestTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        table = testing_utils.settings()
        settings = testing_utils.patient_table()
        cls.prepare_class = prepare.Prepare(settings, table)

    @classmethod
    def test_prepare_for_conversion(self):
        self.prepare_class.prepare_for_conversion()
        # add assert that the files are the same 
        pass

    @classmethod
    def test_prepare_for_reconall(self):
        self.prepare_class.prepare_for_reconall()
        pass

    @classmethod
    def test_prepare_for_samseg(self):
        self.prepare_class.prepare_for_samseg()
        pass

    @classmethod
    def test_prepare_for_registration(self):
        self.prepare_class.prepare_for_registration()
        pass

    @classmethod
    def test_prepare_for_tables(self):
        self.prepare_class.prepare_for_tables()
        pass

if __name__ == '__main__':
    unittest.main()
    

