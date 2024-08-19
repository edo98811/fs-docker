import testing_utils

import sys
# Creating the DataFrame

import unittest

sys.path.append("../") 
import freesurfer_tool

class TestTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        table = testing_utils.settings()
        settings = testing_utils.patient_table()
        cls.docker_class = freesurfer_tool.FreesurferTool()