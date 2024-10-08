import testing_utils

import sys
# Creating the DataFrame

import unittest

sys.path.append("../") 
import fs_docker_manager.freesurfer_tool as freesurfer_tool

class TestTool(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        table = testing_utils.settings()
        settings = testing_utils.patient_table()
        cls.freesurfer_class = freesurfer_tool.FreesurferTool()
        