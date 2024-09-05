import pandas as pd
import sys
import tests.testing_utils as testing_utils
import pandas.testing as pd_testing

import unittest

# Assuming Table class is defined in a module named table_module
# from table_module import Table
#  python -m unittest tests.create_table_tests

sys.path.append("../") 
import fs_docker_manager.create_table as create_table

class TestTable(unittest.TestCase):
    
    def assertDataframeEqual(self, a, b, msg):
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e
        
    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)
        self.testing_paths = testing_utils.testing_paths()
        self.settings = testing_utils.settings()
        self.table = create_table.Table(self.settings, find_type="nifti", testing = True)
        

    def test_init(self):
 
        self.table.create_table_df(self.settings["nifti"], self.testing_paths)
        table = testing_utils.patient_table()
        
        pd.testing.assert_frame_equal(self.table.table, table)

    def test_add_subject_info(self):
        
        self.table.create_table_df(self.settings["nifti"], self.testing_paths)
        self.table.create_subj_info()
        
        table = testing_utils.patient_table(parts = [True, False])
        # self.table.table.to_excel("test.xlsx")

        pd.testing.assert_frame_equal(self.table.table, table)

    def test_add_processing_info(self):
        self.table.create_table_df(self.settings["nifti"], self.testing_paths)
        self.table.create_subj_info()
        self.table.add_processing_info("test", "test", "test")
        
        table = testing_utils.patient_table(parts = [True, True])
        # self.table.table.to_excel("test_test.xlsx")
        
        pd.testing.assert_frame_equal(self.table.table, table)

if __name__ == '__main__':
    unittest.main()