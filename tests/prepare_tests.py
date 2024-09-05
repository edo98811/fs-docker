import pandas as pd
import tests.testing_utils as testing_utils
import fs_docker_manager.create_table as create_table

import sys
# Creating the DataFrame

import unittest

sys.path.append("../") 
import fs_docker_manager.prepare as prepare
# Assuming Table class is defined in a module named table_module
# from table_module import Table
# python -m unittest tests.prepare_tests

class TestPrepare(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        settings = testing_utils.settings()
        
        table = create_table.Table(settings, find_type="nifti", testing = True)
        table.create_table_df(settings["nifti"], testing_utils.testing_paths())
        table.create_subj_info()
        table.add_processing_info("test", "test", "test")
        cls.prepare_class = prepare.Prepare(settings, table)
        
    @classmethod
    def test_sanity_check(cls):
        # print("Before assertion")
        cls.assertTrue(False, "This should always fail")
    
    @classmethod
    def test_prepare_for_conversion(cls):
        origins, _ = cls.prepare_class.prepare_for_conversion(testing=True)
        message = "test_prepare_for_conversion for origin file not correct"

                                # Write the contents of origins to a text file
        with open('origins_test_prepare_for_conversion.txt', 'w') as f:
            for origin in origins:
                f.write(f"{origin}\n")
                
        with open('origins_test_prepare_for_conversion.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]

        print("ciao")
        cls.assertTrue(testing_utils.test_files(origins, expected_file), message)
        

    @classmethod
    def test_prepare_for_reconall(cls):
        cls.prepare_class.df['converted'] = testing_utils.update_converted()
        origins, _ = cls.prepare_class.prepare_for_reconall(testing=True)
        message = "test_prepare_for_reconall for origin file not correct"

        
                # Write the contents of origins to a text file
        with open('origins_test_prepare_for_reconall.txt', 'w') as f:
            for origin in origins:
                f.write(f"{origin}\n")

        with open('origins_test_prepare_for_reconall.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(origins, expected_file), message)
        

    @classmethod
    def test_prepare_for_samseg(cls):
        cls.prepare_class.df['converted'] = testing_utils.update_converted()
        origins, _ = cls.prepare_class.prepare_for_samseg(testing=True)
        message = "test_prepare_for_samseg for origin file not correct"

        cls.prepare_class.df.loc[0, "samseg"] = "Prepared"     

                # Write the contents of origins to a text file
        with open('origins_test_prepare_for_samseg.txt', 'w') as f:
            for origin in origins:
                f.write(f"{origin}\n")

        with open('origins_test_prepare_for_samseg.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(origins, expected_file), message)
        

    @classmethod
    def test_prepare_for_registration(cls):
        cls.prepare_class.df['converted'] = testing_utils.update_converted()
        origins, _ = cls.prepare_class.prepare_for_registration(testing=True)
        message = "test_prepare_for_registration for origin file not correct"
        
        
                # Write the contents of origins to a text file
        with open('origins_test_prepare_for_registration.txt', 'w') as f:
            for origin in origins:
                f.write(f"{origin}\n")

        with open('origins_test_prepare_for_registration.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(origins, expected_file), message)
        
    
    @classmethod
    def test_prepare_for_conversion_destination(cls):
        _, destinations = cls.prepare_class.prepare_for_conversion(testing=True)
        message = "test_prepare_for_conversion for destinations file not correct"

        # Write the contents of origins to a text file
        with open('destinations_test_prepare_for_conversion.txt', 'w') as f:
            for destination in destinations:
                f.write(f"{destination}\n")

        with open('destinations_test_prepare_for_conversion.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        

    @classmethod
    def test_prepare_for_reconall_destination(cls):
        cls.prepare_class.df['converted'] = testing_utils.update_converted()
        _, destinations = cls.prepare_class.prepare_for_reconall(testing=True)
        message = "test_prepare_for_reconall for destinations file not correct"
        
        
        # Write the contents of origins to a text file
        with open('destinations_test_prepare_for_reconall.txt', 'w') as f:
            for destination in destinations:
                f.write(f"{destination}\n")

        with open('destinations_test_prepare_for_reconall.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        

    @classmethod
    def test_prepare_for_samseg_destination(cls):
        cls.prepare_class.df['converted'] = testing_utils.update_converted()
        _, destinations = cls.prepare_class.prepare_for_samseg(testing=True)
        message = "test_prepare_for_samseg for destinations file not correct"
        
     
        # Write the contents of origins to a text file
        with open('destinations_test_prepare_for_samseg.txt', 'w') as f:
            for destination in destinations:
                f.write(f"{destination}\n")

        with open('destinations_test_prepare_for_samseg.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        

    @classmethod
    def test_prepare_for_registration_destination(cls):
        cls.prepare_class.df.loc[0, "samseg"] = "Prepared"   
        _, destinations = cls.prepare_class.prepare_for_registration(testing=True)
        message = "test_prepare_for_registration for destinations file not correct"
        
        
        
        # Write the contents of origins to a text file
        with open('destinations_test_prepare_for_registration.txt', 'w') as f:
            for destination in destinations:
                f.write(f"{destination}\n")

        with open('destinations_test_prepare_for_registration.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        

    @classmethod
    def test_prepare_for_tables(cls):
        cls.prepare_class.df.loc[0, "reconall"] = "Done" 
        destinations = cls.prepare_class.prepare_for_tables(testing=True)
        message = "test_prepare_for_tables for destinations file not correct"
        
        # Write the contents of origins to a text file
        with open('destinations_test_prepare_for_tables.txt', 'w') as f:
            for destination in destinations:
                f.write(f"{destination}\n")

        with open('destinations_test_prepare_for_tables.txt', 'r') as file:
            # Read all lines from the file and remove newline characters
            expected_file = [line.strip() for line in file.readlines()]
        
        cls.assertTrue(testing_utils.test_files(destinations, expected_file), message)
        

if __name__ == '__main__':
    unittest.main()
    

