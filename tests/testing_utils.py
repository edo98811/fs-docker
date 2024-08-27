from pathlib import Path
import pandas as pd

def test_files(file1, file2): 
    if len(file1) != len(file2): return False
    
    for i in range(len(file1)): 
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
    
def patient_table(short: bool = False):
    data = {
        'acquisition': ['Angeli_Vassiliki', 'Baehr_Doris', 'Bauer_Horst', 'Beck_Renate'],
        'mris': [
            ['20210623_185600t1mpragesagp2isoAngeliVassilikis016a1001', '20210623_185600t2spacesagp2isoAngeliVassilikis020a1001', '20210623_185600t1fl2dtraAngeliVassilikis007a1001'],
            ['20200602_180510t1mpragesagp2isoBaehrDoris', '20200602_180510t2spacesagp2isoBaehrDoris', '20200602_180510t1fl2dtraBaehrDoris'],
            ['20200915_165803t1mpragesagp2isoBauerHorst', '20200915_165803t2spacesagp2isoBauerHorst', '20200915_165803t1fl2dtraBauerHorst'],
            ['20170831_152703t1setraBeckRenate', '20170831_152703t2tsetrap2320BeckRenate', '20170831_152703t2spcirprepnssagdarkflp2isoBeckRenate'],
            ],
        'paths': [
            ['../../test_data/NIFTI/Angeli_Vassiliki/20210623_185600t1mpragesagp2isoAngeliVassilikis016a1001.nii', '../../test_data/NIFTI/Angeli_Vassiliki/20210623_185600t2spacesagp2isoAngeliVassilikis020a1001.nii', '../../test_data/NIFTI/Angeli_Vassiliki/20210623_185600t1fl2dtraAngeliVassilikis007a1001.nii'],
            ['../../test_data/NIFTI/Baehr_Doris/20200602_180510t1mpragesagp2isoBaehrDoris.nii', '../../test_data/NIFTI/Baehr_Doris/20200602_180510t2spacesagp2isoBaehrDoris.nii', '../../test_data/NIFTI/Baehr_Doris/20200602_180510t1fl2dtraBaehrDoris.nii'],
            ['../../test_data/NIFTI/Bauer_Horst/20200915_165803t1mpragesagp2isoBauerHorst.nii', '../../test_data/NIFTI/Bauer_Horst/20200915_165803t2spacesagp2isoBauerHorst.nii', '../../test_data/NIFTI/Bauer_Horst/20200915_165803t1fl2dtraBauerHorst.nii'],
            ['../../test_data/NIFTI/Beck_Renate/20170831_152703t1setraBeckRenate.nii', '../../test_data/NIFTI/Beck_Renate/20170831_152703t2tsetrap2320BeckRenate.nii', '../../test_data/NIFTI/Beck_Renate/20170831_152703t2spcirprepnssagdarkflp2isoBeckRenate.nii'],
        ],
        'converted': [
            [False, False, False],
            [False, False, False],
            [False, False, False],
            [False, False, False],
        ]
    }
    
    if not short: data.update({
        't1': [
            ['20210623_185600t1mpragesagp2isoAngeliVassilikis016a1001', '20210623_185600t1fl2dtraAngeliVassilikis007a1001'],
            ['20200602_180510t1mpragesagp2isoBaehrDoris', '20200602_180510t1fl2dtraBaehrDoris'],
            ['20200915_165803t1mpragesagp2isoBauerHorst', '20200915_165803t1fl2dtraBauerHorst'],
            ['20170831_152703t1setraBeckRenate']
        ],
        't2': [
            ['20210623_185600t2spacesagp2isoAngeliVassilikis020a1001'],
            ['20200602_180510t2spacesagp2isoBaehrDoris'],
            ['20200915_165803t2spacesagp2isoBauerHorst'],
            ['20170831_152703t2tsetrap2320BeckRenate']
        ],
        't2_flair': [
            [],
            [],
            [],
            ['20170831_152703t2spcirprepnssagdarkflp2isoBeckRenate']
        ],
        't1_flair': [
            ['20210623_185600t1fl2dtraAngeliVassilikis007a1001'],
            ['20200602_180510t1fl2dtraBaehrDoris'],
            ['20200915_165803t1fl2dtraBauerHorst'],
            []
        ],
        'samseg': [
            ['Possible - only t2 not fl'],
            ['Possible - only t2 not fl'],
            ['Possible - only t2 not fl'],
            ['Possible - only t2 not fl']
        ],
        'reconall': [
            ['Possible'],
            ['Possible'],
            ['Possible'],
            ['Possible']
        ]
    })
        
    return pd.DataFrame(data)

def check_table(table, table_to_test):
    
    return True