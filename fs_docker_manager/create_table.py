import os
import pandas as pd
import ast
import re
from pathlib import Path

# Funtion to modify each time, it returns the aquisition name
def acquisition_name(folder_path, image_name, base_directory = ""):
    # print(folder_path)
    return folder_path.split("/")[-1]
    # if it is not nifti or it is a CT scan
    if "CCT " in image_name or not image_name.endswith(".nii.gz"):
        return None
    
    # match this string (r string literal) with the last folder in the root
    # pattern = r'^(.*?)(?=_{2,})'
    rel_path = os.path.relpath(folder_path, base_directory)
    rel_path = rel_path.replace("/", "_")


    pattern = r'(.{5,})(?=.*\1)'
    result = re.sub(pattern, '', rel_path)



    return result
    # For each subdirectory in the directory (returns the acquistion name)
    if folder_path.split('/')[-2].startswith("01"):
        return None
    else:
        return f"{folder_path.split('/')[-2]}_{folder_path.split('/')[-1]}"

class Table():
    def __init__(self, SET: dict, find_type: str, new: bool = True): 
        self.find_type: str = find_type
        self.SET: dict = SET
        self.new: bool = new
        self._setup_table()
        
        
    def _setup_table(self):
        self._load_or_create_table()
        self._divide_image_type()
        self._add_pipelines()
        self._check_processing_status()
        
    def _load_or_create_table(self):
        if self._table_already_exists(): self._load_table()
        else: self._create_table_from_dataset()
        
    def _divide_image_type(self):
        self._find_mri_type_from_table("t1")
        self._find_mri_type_from_table("t2")
        self._find_mri_type_from_table("t2_flair")
        self._find_mri_type_from_table("t1_flair")

    def _add_pipelines(self):
        self._add_pipeline_samseg()
        self._add_pipeline_reconall()

    def _check_processing_status(self):
        self._check_samseg()
        self._check_reconall()
        self._check_converted()

    
    def _create_table_from_dataset(self):
        
        data = {
        "acquisition": [],
        "mris": [],
        "paths": []
        }
        
        base_directory = os.path.join(self.SET["rawdata"])
        
        for root, dirs, files in os.walk(base_directory):
            if self.find_type == "dicom": 
                for image in dirs: 
                    acquisition, rel_path, image = self.find_dicom(root, image, base_directory)
                    if acquisition is not None: self._add_image(data, acquisition, rel_path, image)
            if self.find_type == "nifti":
                for image in files: 
                    acquisition, rel_path, image = self.find_nifti(root, image, base_directory)
                    if acquisition is not None: self._add_image(data, acquisition, rel_path, image) 
                    
        self.table = pd.DataFrame(data)


    @staticmethod
    def _add_image(data: dict, acquisition: str, rel_path: str, image: str):
        
        if len(data["acquisition"])!= 0:

            # If it is not the same subject (acquisition ID al fondo della lista != acquisition ID attuale)
            if not (data["acquisition"][-1] == acquisition):
                data["acquisition"].append(acquisition)
                data["mris"].append([image]) # [] list because i need to be able to append to it other mris
                data["paths"].append([rel_path]) # to convert, it is not in the direct childern
            
            # If it only a new acquisition, but not new subject, the index is the last subject
            else:
                data["mris"][-1].append(image) 
                data["paths"][-1].append(rel_path)

            # If it is the first iteration, this is needed because of this data["acquisition"][-1]  if condition 
        else: 
            data["acquisition"].append(acquisition)
            data["mris"].append([image]) 
            data["paths"].append([rel_path])
    
    def _table_already_exists(self):
        return os.path.isfile(os.path.join(self.SET["table_path"], self.SET["table_name"])) and not self.new
    
    def _load_table(self):
        print("loading table from: ", os.path.join(self.SET["table_path"], self.SET["table_name"]))
        self.table = pd.read_excel(os.path.join(self.SET["table_path"], self.SET["table_name"]))
        columns_to_list = ['mris', 'paths', 'converted']
        self.table[columns_to_list] = self.table[columns_to_list].map(self.safe_eval)
        
    def _find_mri_type_from_table(self, img_type: str):
        self.table[f"{img_type}"] = [list() for _ in range(len(self.table.index))]
    
        # Add the images that have a image identifier, dont add images that have a img_identifyier no
        for rowname, row in self.table.iterrows():
            for mri in row["mris"]:
                if any(MRI_name_substring in mri for MRI_name_substring in self.SET["file_identifiers"][f"{img_type}"]) and \
                    not any(MRI_name_substring in mri for MRI_name_substring in self.SET["file_identifiers"][f"{img_type}_no"]):
                        
                    self.table.at[rowname, f"{img_type}"].append(mri)
            
            # pref not loop 
            to_delete = set()
            for mri in self.table.at[rowname, f"{img_type}"]:
                
                # If I I find a pref not, i add it to the to delete set
                if any(MRI_name_substring in mri for MRI_name_substring in self.SET["file_identifiers"][f"{img_type}_pref_not"]):
                    to_delete.add(mri)
                                # If there are no more images i leave the ones that are there, even if they are pref not
                if len(self.table.at[rowname, f"{img_type}"]) <= len(to_delete) + 1:
                    break
                
            for n in to_delete: 
                self.table.at[rowname, f"{img_type}"].remove(n)

    def _check_samseg(self):
        for index, row in self.table.iterrows(): 

            to_check = os.path.join(self.SET["nifti"], f"{row['acquisition']}", "flair_reg.nii")
            if os.path.exists(to_check):
                self.table.at[index, "samseg"] = "Prepared"

            to_check = os.path.join(self.SET["samseg"], f"{row['acquisition']}", "samseg.stats")
            if os.path.exists(to_check):
                self.table.at[index, "samseg"] = "Done"
    
    def _check_reconall(self):
        for index, row in self.table.iterrows(): 
            to_check = os.path.join(self.SET["reconall"], f"{row['acquisition']}")

            if os.path.exists(to_check):
                if os.listdir(f"{to_check}/stats"):
                    self.table.at[index, "reconall"] = "Done"
                else: 
                    self.table.at[index, "reconall"] = "Error (or in progress)"
    
    def _check_converted(self):
        self.table["converted"] = [list() for _ in range(len(self.table.index))]
        for index, row in self.table.iterrows(): 
            for _ , mri in enumerate(row["mris"]):
                if os.path.isfile(os.path.join(self.SET["nifti"], f"{row['acquisition']}", f"{mri}.nii.gz")) or \
                    os.path.isfile(os.path.join(self.SET["nifti"], f"{row['acquisition']}", f"{mri}.nii")): 
                    self.table.at[index, "converted"].append(True)
                else:
                    self.table.at[index, "converted"].append(False)

    def _add_pipeline_samseg(self):
        # reconall
        self.table["reconall"] = ["Not possible" for x in range(len(self.table.index))]
        
        for rowname, row in self.table.iterrows():
            if len(row["t1"]) >=1: 
                self.table.at[rowname, "reconall"] = "Possible"
            if len(row["t1"]) >=1: 
                self.table.at[rowname, "reconall"] = "Possible" 
    
    def _add_pipeline_reconall(self):
        self.table["samseg"] = ["Not possible" for x in range(len(self.table.index))]
        
        for rowname, row in self.table.iterrows():

            if len(row["t1"]) >=1 and len(row["t2"]) >=1: 
                self.table.at[rowname, "samseg"] = "Possible - only t2 not fl"
            elif len(row["t1"]) >=1 and len(row["t1_flair"]) >=1: 
                self.table.at[rowname, "samseg"] = "Possible - only t1fl not t2fl"
            elif len(row["t1"]) >=1 and len(row["t2_flair"]) >=1: 
                self.table.at[rowname, "samseg"] = "Possible"
                
    # To be sure that when reading the table the contenent is parsed correctly (ex: lists are loaded as lists and not string)           
    @staticmethod
    def safe_eval(s: str) -> str:
        try:
            return ast.literal_eval(s)
        except (SyntaxError, ValueError):
            return s
    
    @staticmethod
    def find_dicom(root, image, base_directory):
        # If a directory contains only files
        if all(os.path.isfile(os.path.join(root, image, item)) for item in os.listdir(os.path.join(root, image))): 
            acquisition = acquisition_name(root, image)
        else: return None, None, None
        
        rel_path = os.path.relpath(os.path.join(root, image), base_directory)
        image = image + ".nii"
            
        return (acquisition, rel_path, image)
        
    @staticmethod
    def find_nifti(root: str, image: str, base_directory: str):
        if image.endswith(".nii.gz") or image.endswith(".nii"):
            acquisition = acquisition_name(root, image, base_directory)
        else: return None, None, None
            
        rel_path = os.path.relpath(os.path.join(root, image), base_directory)
        # image = image[:-7] if image.endswith(".nii.gz") else image[:-4]
            
        return (acquisition, rel_path, image)
    
    def save_table(self, sheet_name="subjects") -> None:
        
        excel_filename = os.path.join(self.SET["table_path"], self.SET["table_name"])
        print("saving table in: ", excel_filename)
        
        # Create a Pandas Excel writer using the XlsxWriter engine
        writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')

        # Write the self.table to the Excel file
        self.table.to_excel(writer, sheet_name=sheet_name, index=False, startrow=1, header=False)

        # Get the xlsxwriter workbook and worksheet objects
        workbook  = writer.book
        worksheet = writer.sheets[sheet_name]

        # Add a header format with bold and a border
        header_format = workbook.add_format({'bold': True, 'border': 1, 'align': 'center', 'valign': 'vcenter'})

        # Write the column headers with the defined format
        for col_num, value in enumerate(self.table.columns.values):
            worksheet.write(0, col_num, value, header_format)
        
        num_rows, num_cols = self.table.shape
        worksheet.add_table(0, 0, num_rows + 1, num_cols - 1, {'columns': [{'header': column} for column in self.table.columns], 'style': None})
        # worksheet.add_table(0, 0, num_rows, num_cols - 1)

        # Close the Pandas Excel writer and save the Excel file
        writer._save()

