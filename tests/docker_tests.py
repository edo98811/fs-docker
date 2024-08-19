
import testing_utils

import sys
# Creating the DataFrame

import unittest

sys.path.append("../") 
import fs_docker_manager.docker as docker
# Assuming Table class is defined in a module named table_module
# from table_module import Table

class TestTable(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        table = testing_utils.settings()
        settings = testing_utils.patient_table()
        cls.docker_class = docker.DockerInstance()