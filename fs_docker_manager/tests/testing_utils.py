from pathlib import Path
import pandas as pd

def test_files(file1, file2): 
    if len(file1) != len(file2): return False
    
    for i in range(len(file1)): # use smaller length
        if (file2[i] != file1[i]): return False
    
    return True

def settings():
    return {
        "nifti": Path(__file__).parent /"NIFTI",
        "rawdata": Path(__file__).parent /"rawdata",
        "base_path": Path(__file__).parent,
        "reconall": Path(__file__).parent /"reconall",
        "samseg": Path(__file__).parent /"samseg",
        "license_path": "",
        "container_id": "1b0f81a8cb9f",
        "table_path": Path(__file__).parent /"",
        "table_name": "MRI_table.xlsx",
        "file_identifiers": {
            "T1": [
                "t1"
            ],
            "T1_pref_not": [
                "KM"
            ],
            "T2": [
                "t2"
            ],
            "t1FLAIR": [
                "t2fl",
                "fl"
            ],
            "t2FLAIR": [
                "t1fl",
                "fl"
            ],
            "T1_no": [
                "T2",
                "t2",
                "FLAIR"
            ],
            "T2_no": [
                "fl"
            ],
            "t1FLAIR_no": [
                "t2"
            ],
            "t2FLAIR_no": [
                "t1"
            ]
        }
    }
    
def patient_table():
    data = {
        'acquisition': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        'mris': [
                ['20210623_185600t1fl2dtraAngeliVassilikis007a1001', '20210623_185600t1mpragesagp2isoAngeliVassilikis016a1001', '20210623_185600t1mpragesagp2isoKMAngeliVassilikis028a1001', '20210623_185600t2Flaircor3mmAngeliVassilikis009a1001', '20210623_185600t2hastecorp2AngeliVassilikis005a1001', '20210623_185600t2spacesagp2isoAngeliVassilikis020a1001', '20210623_185600t2swi3dtrap212mmKMAngeliVassilikis023a1001', '20210623_185600t2swi3dtrap212mmKMAngeliVassilikis024a1001', '20210623_185600t2swi3dtrap212mmKMAngeliVassilikis025a1001', '20210623_185600t2swi3dtrap212mmKMAngeliVassilikis026a1001', '20210623_185600t2tsecor3842mmKMAngeliVassilikis027a1001', '20210623_185600t2tsetra512AngeliVassilikis006a1001', '20210623_185600t2tsetra512ErgnzungAngeliVassilikis008a1001'],
                ['20200602_180510t1fl2dtraBaehrDoris', '20200602_180510t1mpragesagp2isoBaehrDoris', '20200602_180510t1mpragesagp2isoKMBaehrDoris', '20200602_180510t2Flaircor3mmBaehrDoris', '20200602_180510t2hastecorp2BaehrDoris', '20200602_180510t2spacesagp2isoBaehrDoris', '20200602_180510t2swi3dtrap212mmKMBaehrDoris', '20200602_180510t2swi3dtrap212mmKMBaehrDorisA', '20200602_180510t2swi3dtrap212mmKMBaehrDorisB', '20200602_180510t2swi3dtrap212mmKMBaehrDorisC', '20200602_180510t2tsecor3842mmKMBaehrDoris', '20200602_180510t2tsetra512BaehrDoris'],
                ['20200915_165803t1fl2dtraBauerHorst', '20200915_165803t1mpragesagp2isoBauerHorst', '20200915_165803t1mpragesagp2isoKMBauerHorst', '20200915_165803t2Flaircor3mmBauerHorst', '20200915_165803t2hastecorp2BauerHorst', '20200915_165803t2spacesagp2isoBauerHorst', '20200915_165803t2swi3dtrap212mmKMBauerHorst', '20200915_165803t2swi3dtrap212mmKMBauerHorstA', '20200915_165803t2swi3dtrap212mmKMBauerHorstB', '20200915_165803t2swi3dtrap212mmKMBauerHorstC', '20200915_165803t2tsecor3842mmKMBauerHorst', '20200915_165803t2tsetra512BauerHorst'],
            ],
        'paths': [
            ['Angeli_Vassiliki/20210623_185600t1fl2dtraAngeliVassilikis007a1001.nii', 'Angeli_Vassiliki/20210623_185600t1mpragesagp2isoAngeliVassilikis016a1001.nii', 'Angeli_Vassiliki/20210623_185600t1mpragesagp2isoKMAngeliVassilikis028a1001.nii', 'Angeli_Vassiliki/20210623_185600t2Flaircor3mmAngeliVassilikis009a1001.nii', 'Angeli_Vassiliki/20210623_185600t2hastecorp2AngeliVassilikis005a1001.nii', 'Angeli_Vassiliki/20210623_185600t2spacesagp2isoAngeliVassilikis020a1001.nii', 'Angeli_Vassiliki/20210623_185600t2swi3dtrap212mmKMAngeliVassilikis023a1001.nii', 'Angeli_Vassiliki/20210623_185600t2swi3dtrap212mmKMAngeliVassilikis024a1001.nii', 'Angeli_Vassiliki/20210623_185600t2swi3dtrap212mmKMAngeliVassilikis025a1001.nii', 'Angeli_Vassiliki/20210623_185600t2swi3dtrap212mmKMAngeliVassilikis026a1001.nii', 'Angeli_Vassiliki/20210623_185600t2tsecor3842mmKMAngeliVassilikis027a1001.nii', 'Angeli_Vassiliki/20210623_185600t2tsetra512AngeliVassilikis006a1001.nii', 'Angeli_Vassiliki/20210623_185600t2tsetra512ErgnzungAngeliVassilikis008a1001.nii'],
            ['Baehr_Doris/20200602_180510t1fl2dtraBaehrDoris.nii', 'Baehr_Doris/20200602_180510t1mpragesagp2isoBaehrDoris.nii', 'Baehr_Doris/20200602_180510t1mpragesagp2isoKMBaehrDoris.nii', 'Baehr_Doris/20200602_180510t2Flaircor3mmBaehrDoris.nii', 'Baehr_Doris/20200602_180510t2hastecorp2BaehrDoris.nii', 'Baehr_Doris/20200602_180510t2spacesagp2isoBaehrDoris.nii', 'Baehr_Doris/20200602_180510t2swi3dtrap212mmKMBaehrDoris.nii', 'Baehr_Doris/20200602_180510t2swi3dtrap212mmKMBaehrDorisA.nii', 'Baehr_Doris/20200602_180510t2swi3dtrap212mmKMBaehrDorisB.nii', 'Baehr_Doris/20200602_180510t2swi3dtrap212mmKMBaehrDorisC.nii', 'Baehr_Doris/20200602_180510t2tsecor3842mmKMBaehrDoris.nii', 'Baehr_Doris/20200602_180510t2tsetra512BaehrDoris.nii'],
            ['Bauer_Horst/20200915_165803t1fl2dtraBauerHorst.nii', 'Bauer_Horst/20200915_165803t1mpragesagp2isoBauerHorst.nii', 'Bauer_Horst/20200915_165803t1mpragesagp2isoKMBauerHorst.nii', 'Bauer_Horst/20200915_165803t2Flaircor3mmBauerHorst.nii', 'Bauer_Horst/20200915_165803t2hastecorp2BauerHorst.nii', 'Bauer_Horst/20200915_165803t2spacesagp2isoBauerHorst.nii', 'Bauer_Horst/20200915_165803t2swi3dtrap212mmKMBauerHorst.nii', 'Bauer_Horst/20200915_165803t2swi3dtrap212mmKMBauerHorstA.nii', 'Bauer_Horst/20200915_165803t2swi3dtrap212mmKMBauerHorstB.nii', 'Bauer_Horst/20200915_165803t2swi3dtrap212mmKMBauerHorstC.nii', 'Bauer_Horst/20200915_165803t2tsecor3842mmKMBauerHorst.nii', 'Bauer_Horst/20200915_165803t2tsetra512BauerHorst.nii'],
        ],
        'converted': [
            [False, False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False, False, False],
        ],
        'samseg': [
            "Possible",
            "Possible",
            "Possible"
        ],
        'reconall': [
            "Possible",
            "Possible",
            "Possible"
        ]
    }
        
    return pd.DataFrame(data)