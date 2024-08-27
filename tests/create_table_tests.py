import pandas as pd
import sys
import tests.testing_utils as testing_utils
import pandas.testing as pd_testing

import unittest

# Assuming Table class is defined in a module named table_module
# from table_module import Table

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
        self.testing_paths = [
            ("test_data/NIFTI", 
             ['Angeli_Vassiliki', 'Baehr_Doris', 'Bauer_Horst', 'Beck_Renate'], 
             []),
            ("test_data/NIFTI/Angeli_Vassiliki", 
             [], 
             ['20210623_185600t1mpragesagp2isoAngeliVassilikis016a1001.nii', '20210623_185600t2spacesagp2isoAngeliVassilikis020a1001.nii', '20210623_185600t1fl2dtraAngeliVassilikis007a1001.nii']),
            ("test_data/NIFTI/Baehr_Doris", 
             [], 
             ['20200602_180510t1mpragesagp2isoBaehrDoris.nii', '20200602_180510t2spacesagp2isoBaehrDoris.nii', '20200602_180510t1fl2dtraBaehrDoris.nii']),
            ("test_data/NIFTI/Bauer_Horst", 
             [], 
             ['20200915_165803t1mpragesagp2isoBauerHorst.nii', '20200915_165803t2spacesagp2isoBauerHorst.nii', '20200915_165803t1fl2dtraBauerHorst.nii']),
            ("test_data/NIFTI/Beck_Renate", 
             [], 
             ['20170831_152703t1setraBeckRenate.nii', '20170831_152703t2tsetrap2320BeckRenate.nii', '20170831_152703t2spcirprepnssagdarkflp2isoBeckRenate.nii']),
        ]
        self.settings = testing_utils.settings()
        self.table = create_table.Table(self.settings, find_type="nifti", new=True, testing_paths=self.testing_paths)
        

    def test_init(self):
        table_to_test = self.table.create_table_df(self.settings["nifti"], self.testing_paths)
        self.table.table.to_excel("test.xlsx")
        table = testing_utils.patient_table(short=True)
        table.to_excel("test_test.xlsx")
        self.assertEqual(table_to_test, table)

    def test_add_subject_info(self):

        self.table.create_subj_info()
        table = testing_utils.patient_table()
        self.assertEqual(self.table.table, table)

if __name__ == '__main__':
    unittest.main()