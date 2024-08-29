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
    
def patient_table(parts: list[bool] = [False, False]):
    data = {
        'acquisition': ['s1', 's2', 's3', 's4'],
        'mris': [
            ['20210623_185600t1mpragesagp2iso016a1001', '20210623_185600t2spacesagp2iso020a1001', '20210623_185600t1fl2dtra007a1001'],
            ['20200602_180510t1mpragesagp2iso', '20200602_180510t2spacesagp2iso', '20200602_180510t1fl2dtra'],
            ['20200915_165803t1mpragesagp2iso', '20200915_165803t2spacesagp2iso', '20200915_165803t1fl2dtra'],
            ['20170831_152703t1setra', '20170831_152703t2tsetrap2320', '20170831_152703t2spcirprepnssagdarkflp2iso'],
            ],
        'paths': [
            ['../../test_data/NIFTI/s1/20210623_185600t1mpragesagp2iso016a1001.nii', '../../test_data/NIFTI//20210623_185600t2spacesagp2iso020a1001.nii', '../../test_data/NIFTI//20210623_185600t1fl2dtra007a1001.nii'],
            ['../../test_data/NIFTI/s2/20200602_180510t1mpragesagp2iso.nii', '../../test_data/NIFTI/s2/20200602_180510t2spacesagp2iso.nii', '../../test_data/NIFTI/s2/20200602_180510t1fl2dtra.nii'],
            ['../../test_data/NIFTI/s3/20200915_165803t1mpragesagp2iso.nii', '../../test_data/NIFTI/s3/20200915_165803t2spacesagp2iso.nii', '../../test_data/NIFTI/s3/20200915_165803t1fl2dtra.nii'],
            ['../../test_data/NIFTI/s4/20170831_152703t1setra.nii', '../../test_data/NIFTI/s4/20170831_152703t2tsetrap2320.nii', '../../test_data/NIFTI/s4/20170831_152703t2spcirprepnssagdarkflp2iso.nii'],
        ]
    }
    
    if parts[0]: data.update({
        'converted': [
            [], # added in add processing info 
            [],
            [],
            [],
        ],
        't1': [
            ['20210623_185600t1mpragesagp2iso016a1001', '20210623_185600t1fl2dtra007a1001'],
            ['20200602_180510t1mpragesagp2iso', '20200602_180510t1fl2dtra'],
            ['20200915_165803t1mpragesagp2iso', '20200915_165803t1fl2dtra'],
            ['20170831_152703t1setra']
        ],
        't2': [
            ['20210623_185600t2spacesagp2iso020a1001'],
            ['20200602_180510t2spacesagp2iso'],
            ['20200915_165803t2spacesagp2iso'],
            ['20170831_152703t2tsetrap2320']
        ],
        't2_flair': [
            [],
            [],
            [],
            ['20170831_152703t2spcirprepnssagdarkflp2iso']
        ],
        't1_flair': [
            ['20210623_185600t1fl2dtra007a1001'],
            ['20200602_180510t1fl2dtra'],
            ['20200915_165803t1fl2dtra'],
            []
        ],
        'samseg': [ 
            'Possible - only t2 not fl',
            'Possible - only t2 not fl',
            'Possible - only t2 not fl',
            'Possible - only t2 not fl'
        ],
        'reconall': [
            'Possible',
            'Possible',
            'Possible',
            'Possible'
        ]
    })
    
    if parts[1]: data.update({                         
        'samseg': [ 
            'Possible - only t2 not fl',
            'Possible - only t2 not fl',
            'Possible - only t2 not fl',
            'Possible - only t2 not fl'
        ],
        'reconall': [
            'Possible',
            'Possible',
            'Possible',
            'Possible'
        ],
        'converted': [
            [False, False, False], 
            [False, False, False],
            [False, False, False],
            [False, False, False],
        ]
    })
        
    return pd.DataFrame(data)

def check_table(table, table_to_test):
    
    return True