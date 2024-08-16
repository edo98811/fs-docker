import pandas as pd

# Creating the DataFrame
data = {
    'acquisition': ['Kuhnke_Christel', 'Merkel_Erika', 'EngmannUte_mr_20200929_112615776_', 'Laupenmhlen_Ulrich'],
    'mris': [
        ['20180405_152956t1fl2dtra3mmKuhnkeChristel', '20180405_152956t1mprnssagp2isoKMKuhnkeChristel', 
         '20180405_152956t1mprnssagp2isoKMKuhnkeChristelA', '20180405_152956t1mprnssagp2isoKMKuhnkeChristelB', 
         '20180405_152956t1mprnssagp2isoKMKuhnkeChristelC', '20180405_152956t1mprnssagp2isoKMKuhnkeChristelD', 
         '20180405_152956t1mprnssagp2isoKMKuhnkeChristelE', '20180405_152956t1mprnssagp2isoKMKuhnkeChristelF', 
         '20180405_152956t1mprnssagp2isoKuhnkeChristel', '20180405_152956t2fl3dtrap2swihighresKuhnkeChristel', 
         '20180405_152956t2fl3dtrap2swihighresKuhnkeChristelA', '20180405_152956t2fl3dtrap2swihighresKuhnkeChristelB', 
         '20180405_152956t2fl3dtrap2swihighresKuhnkeChristelC', '20180405_152956t2hastecorKuhnkeChristel', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristel', '20180405_152956t2spcnssagp2isoKuhnkeChristelA', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristelB', '20180405_152956t2spcnssagp2isoKuhnkeChristelC', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristelD', '20180405_152956t2spcnssagp2isoKuhnkeChristelE', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristelF', '20180405_152956t2spcnssagp2isoKuhnkeChristelG', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristelH', '20180405_152956t2spcnssagp2isoKuhnkeChristelI', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristelJ', '20180405_152956t2spcnssagp2isoKuhnkeChristelK', 
         '20180405_152956t2spcnssagp2isoKuhnkeChristelL', '20180405_152956t2tsecor2mm512KMKuhnkeChristel', 
         '20180405_152956t2tsetra448p23mmKuhnkeChristel'],
        ['20170825_092731t1mpragetra2mmMerkelErika', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErika', 
         '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaA', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaB', 
         '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaC', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaD', 
         '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaE', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaF', 
         '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaG', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaH', 
         '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaI', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaJ', 
         '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaK', '20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaL', 
         '20170825_092731t1setraMerkelErika', '20170825_092731t2fl2dtrahemoMerkelErika', 
         '20170825_092731t2spcirprepnssagdarkflp2isoMerkelErika', '20170825_092731t2tserstcorVerzkorrMerkelErika', 
         '20170825_092731t2tsetrap2320MerkelErika'],
        ['20150710_113414t1mprnssagp2isoEngmannUte', '20150710_113414t1mprnssagp2isoEngmannUteA', 
         '20150710_113414t1mprnssagp2isoEngmannUteB', '20150710_113414t1mprnssagp2isoEngmannUteC', 
         '20150710_113414t1mprnssagp2isoEngmannUteD', '20150710_113414t1mprnssagp2isoEngmannUteE', 
         '20150710_113414t1mprnssagp2isoEngmannUteF', '20150710_113414t2fl3dtrap2swihighresEngmannUte', 
         '20150710_113414t2fl3dtrap2swihighresEngmannUteA', '20150710_113414t2fl3dtrap2swihighresEngmannUteB', 
         '20150710_113414t2fl3dtrap2swihighresEngmannUteC', '20150710_113414t2hastecorEngmannUte', 
         '20150710_113414t2hastesagEngmannUte', '20150710_113414t2tsetra448p23mmEngmannUte'],
        ['20170214_192218t1fl2dtra3mmLaupenmhlenUlrich', '20170214_192218t1mprnssagp2isoKMLaupenmhlenUlrich', 
         '20170214_192218t1mprnssagp2isoKMLaupenmhlenUlrichA', '20170214_192218t1mprnssagp2isoKMLaupenmhlenUlrichB']
    ],
    'paths': [
        ['Kuhnke_Christel/20180405_152956t1fl2dtra3mmKuhnkeChristel.nii', 'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristel.nii', 
         'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristelA.nii', 'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristelB.nii', 
         'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristelC.nii', 'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristelD.nii', 
         'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristelE.nii', 'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKMKuhnkeChristelF.nii', 
         'Kuhnke_Christel/20180405_152956t1mprnssagp2isoKuhnkeChristel.nii', 'Kuhnke_Christel/20180405_152956t2fl3dtrap2swihighresKuhnkeChristel.nii', 
         'Kuhnke_Christel/20180405_152956t2fl3dtrap2swihighresKuhnkeChristelA.nii', 'Kuhnke_Christel/20180405_152956t2fl3dtrap2swihighresKuhnkeChristelB.nii', 
         'Kuhnke_Christel/20180405_152956t2fl3dtrap2swihighresKuhnkeChristelC.nii', 'Kuhnke_Christel/20180405_152956t2hastecorKuhnkeChristel.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristel.nii', 'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelA.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelB.nii', 'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelC.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelD.nii', 'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelE.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelF.nii', 'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelG.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelH.nii', 'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelI.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelJ.nii', 'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelK.nii', 
         'Kuhnke_Christel/20180405_152956t2spcnssagp2isoKuhnkeChristelL.nii', 'Kuhnke_Christel/20180405_152956t2tsecor2mm512KMKuhnkeChristel.nii', 
         'Kuhnke_Christel/20180405_152956t2tsetra448p23mmKuhnkeChristel.nii'],
        ['Merkel_Erika/20170825_092731t1mpragetra2mmMerkelErika.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErika.nii', 
         'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaA.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaB.nii', 
         'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaC.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaD.nii', 
         'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaE.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaF.nii', 
         'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaG.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaH.nii', 
         'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaI.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaJ.nii', 
         'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaK.nii', 'Merkel_Erika/20170825_092731t1mprnssagp2isoVerzKorrKMMerkelErikaL.nii', 
         'Merkel_Erika/20170825_092731t1setraMerkelErika.nii', 'Merkel_Erika/20170825_092731t2fl2dtrahemoMerkelErika.nii', 
         'Merkel_Erika/20170825_092731t2spcirprepnssagdarkflp2isoMerkelErika.nii', 'Merkel_Erika/20170825_092731t2tserstcorVerzkorrMerkelErika.nii', 
         'Merkel_Erika/20170825_092731t2tsetrap2320MerkelErika.nii'],
        ['EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUte.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUteA.nii', 
         'EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUteB.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUteC.nii', 
         'EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUteD.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUteE.nii', 
         'EngmannUte_mr_20200929_112615776_/20150710_113414t1mprnssagp2isoEngmannUteF.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t2fl3dtrap2swihighresEngmannUte.nii', 
         'EngmannUte_mr_20200929_112615776_/20150710_113414t2fl3dtrap2swihighresEngmannUteA.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t2fl3dtrap2swihighresEngmannUteB.nii', 
         'EngmannUte_mr_20200929_112615776_/20150710_113414t2fl3dtrap2swihighresEngmannUteC.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t2hastecorEngmannUte.nii', 
         'EngmannUte_mr_20200929_112615776_/20150710_113414t2hastesagEngmannUte.nii', 'EngmannUte_mr_20200929_112615776_/20150710_113414t2tsetra448p23mmEngmannUte.nii'],
        ['Laupenmhlen_Ulrich/20170214_192218t1fl2dtra3mmLaupenmhlenUlrich.nii', 'Laupenmhlen_Ulrich/20170214_192218t1mprnssagp2isoKMLaupenmhlenUlrich.nii', 
         'Laupenmhlen_Ulrich/20170214_192218t1mprnssagp2isoKMLaupenmhlenUlrichA.nii', 'Laupenmhlen_Ulrich/20170214_192218t1mprnssagp2isoKMLaupenmhlenUlrichB.nii']
    ],
    'converted': [
        [True, True, False, False, False, False, False, False, True, True, False, False, False, True, True, 
         False, False, False, False, False, False, False, False, False, False, False, True, True],
        [True, True, False, False, False, False, False, False, False, False, False, False, False, True, True, 
         True, True, True],
        [True, False, False, False, False, False, False, True, False, False, False, True, True, True],
        [True, True, False, False]
    ]
}

df = pd.DataFrame(data)


# Assuming Table class is defined in a module named table_module
# from table_module import Table

class TestTable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any class-wide resources, e.g., creating a DataFrame that will be reused in all tests
        data = {
            'acquisition': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
            'mris': ['T1', 'T2', 'T1', 'T2'],
            'paths': [
                ['path1', 'path2'],
                ['path3', 'path4'],
                ['path5', 'path6'],
                ['path7', 'path8']
            ],
            'converted': [
                [True, False],
                [True, True],
                [False, False],
                [True, False]
            ]
        }
        cls.df = pd.DataFrame(data)
        # cls.table = Table(cls.df)  # Instantiate the Table class with the test DataFrame

    def setUp(self):
        # Set up resources needed for each individual test
        pass

    def tearDown(self):
        # Clean up after each test if necessary
        pass

    def test_initialization(self):
        # Test initialization of the Table class
        # self.assertIsInstance(self.table, Table)
        pass

    def test_some_method(self):
        # Example test for a method in the Table class
        # result = self.table.some_method()
        # self.assertEqual(result, expected_value)
        pass

    def test_another_method(self):
        # Example test for another method in the Table class
        # result = self.table.another_method()
        # self.assertTrue(result)
        pass

    def test_edge_case(self):
        # Example test for an edge case
        # with self.assertRaises(SomeException):
        #     self.table.method_that_raises()
        pass

    @classmethod
    def tearDownClass(cls):
        # Clean up any class-wide resources if necessary
        pass

if __name__ == '__main__':
    unittest.main()