import pandas as pd
import sys
import testing_utils

import unittest

# Assuming Table class is defined in a module named table_module
# from table_module import Table

sys.path.append("../") 
import fs_docker_manager.create_table as create_table

class TestTable(unittest.TestCase):

    def setUp(self):
        self.testing_paths = [
            "",  
        ]
        settings = testing_utils.patient_table()
        self.table = create_table.Table(settings, find_type="nifti", new=True, testing_paths=self.testing_paths)

    def test_init(self):

        self.assertEqual(self.table.table)

    def test_add_subject_info(self):

        self.table.create_subj_info()
        self.assertTrue(testing_utils.check_table(self.table.table))

if __name__ == '__main__':
    unittest.main()