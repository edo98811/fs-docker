from typing import List
import os
import shutil
import pandas as pd
from fs_docker_manager import helper_functions as h
from pathlib import Path


# Helper functions 
def _save_files(source_docker_origin_path, source_docker_destination_path) -> None:
  h.create_tmp_folder()

  with open("tmp/origins.txt", "w") as fp:
    for item in source_docker_origin_path:
      fp.write(f"{item}\n")
  with open("tmp/destinations.txt", "w") as fp:
    for item in source_docker_destination_path:
      fp.write(f"{item}\n")

def _remove_spaces(data_path: str) -> None:

    original_directory = os.getcwd() 
    os.chdir(data_path)
    
    for old_directory, _, files in os.walk(data_path):
      new_directory = old_directory.replace(" ", "")  # Remove spaces from the folder name
      
      if old_directory != new_directory:
          os.rename(old_directory, new_directory)
          print(f"{old_directory} renamed to {new_directory}")
          
      os.chdir(original_directory)
      
"""
This class is used to prepare the data for processing 
"""
class Prepare():
  def __init__(self, SET, table):
    self.df = table.table
    self.SET = SET

  """
  This class is the most complex, it either prepares to convert some images or directly copies them if they are nicti
  it selects them iterating through the columns requested, then either taking the last image listed or selectign the biggest
  the takes the path from "paths" 
  it then adds it to the origin and destinations text files it if not yet converted (or copies) it to the nifti folder
  """
  
  def prepare_for_conversion(self, cols=["t1", "t2", "t2_flair", "t1_flair"], last=True, move=False, testing=False)-> None:
    
    source_docker_origin_path = []
    source_docker_destination_path = []

    os.makedirs(os.path.join(self.SET["nifti"]), exist_ok=True)
    f = open(Path(self.SET['nifti']) / "log.txt", "w")

    for _, row in self.df.iterrows():

      f.write(f"In subject {row['acquisition']}\n")

      # Iterate through the column of which the mris need to be converted
      for col in cols:
        try:
          column = row[col]
        except:
          raise Warning("invalid column {col}")

        rel_paths = row['paths']
        converted = row['converted']
        mris = row['mris']

        # If the column contains at least one mri
        if len(column) > 0:

            # in case only one per colum and move the biggest needs to be converted
            if last:
              if move:
                indexes = [i for i, elem in enumerate(mris) if elem in column]
                f.write(f"{indexes}\n")
                largest_size = 0

                for index in indexes:
                  file_size = os.path.getsize(os.path.join(self.SET["rawdata"], rel_paths[index]))

                  if file_size > largest_size:
                      largest_size = file_size
                      column = [mris[index]]

            # in case only one per colum (the last) needs to be converted
              else:
                column = [column[-1]] # to keep it as a list

            f.write(f"  from column {col} kept image {column}\n")

            # get the indexes of the wanted mris and find the correct rel path
            indexes = [i for i, elem in enumerate(mris) if elem in column]
            rel_paths_to_convert = []
            converted_to_convert = []
            for index in indexes: 

              rel_paths_to_convert.append(rel_paths[index])
              converted_to_convert.append(converted[index])
            
            # iterate though the list of mri to convert
            for last_element, last_path, c in zip(column, rel_paths_to_convert, converted_to_convert):
              # Create the key in the format "subj_id_acquisition"

              if (not c):
                if move:
                  if os.path.exists(os.path.join(self.SET["rawdata"], last_path)):
                    os.makedirs(os.path.join(self.SET["nifti"], row['acquisition']), exist_ok=True)
                    shutil.copy(os.path.join(self.SET["rawdata"], last_path), 
                                    os.path.join(self.SET["nifti"], row['acquisition'], f"{last_element}"))
                  else: 
                    raise Exception("trying to prepare nifti but dicom found, maybe you wanted to use 'convertdicom'")
                else:
                  if not os.path.isfile(os.path.join(self.SET["rawdata"], last_path)):
                    source_docker_origin_path.append(f"/ext/fs-subjects/{last_path[:-4]}")
                    source_docker_destination_path.append(f"/ext/processed-subjects/{row['acquisition']}/{last_element}")
                  else:
                    raise Exception("trying to convert dicom but file found, maybe you wanted to use 'preparnifti'")
      f.write("\n")
    f.close()
    
    if testing:
      return source_docker_origin_path, source_docker_destination_path
    else: 
      _save_files(source_docker_origin_path, source_docker_destination_path) 

    
  def prepare_for_reconall_from_source_deprecated(self, cols=["t1"], last=True, testing = False)-> None: 
    
    source_docker_origin_path = []
    source_docker_destination_path = []

    for _, row in self.df.iterrows():

        # Iterate through the column of which the mris need to be converted
        for col in cols:
          # select column if it exists, otherwise throw warning
          try:
            column = row[col]
          except:
            raise Warning("invalid column {col}")

          rel_paths = row['paths']
          converted = row['converted']
          mris = row['mris']
          
          # If the column contains at least one mri
          if len(column) > 0:

              # in case only one per colum (the last) needs to be converted
              if last:
                column = [column[-1]] # to keep it as a list
                print(f"kept column {column}")

              # get the indexes only of the wanted mris (they are in the searched column)
              indexes = [i for i, elem in enumerate(mris) if elem in column]
              rel_paths_to_convert = []
              converted_to_convert = []

              # Keep only the necessary paths
              for index in indexes: 

                rel_paths_to_convert.append(rel_paths[index])
                converted_to_convert.append(converted[index])
              
              # iterate though the list of mri to convert
              for last_element, last_path, c in zip(column, rel_paths_to_convert, converted_to_convert):
                # Create the key in the format "subj_id_acquisition"

                if (not c):
                  source_docker_origin_path.append(f"/ext/fs-subjects/{last_path}")
                  source_docker_destination_path.append(f"/ext/processed-subjects/{row['acquisition']}/{last_element}")

    if testing:
      return source_docker_origin_path, source_docker_destination_path
    else: 
      _save_files(source_docker_origin_path, source_docker_destination_path)

  def prepare_for_reconall(self, testing = False)-> None:
    
    source_docker_origin_path = []
    source_docker_destination_path = []

    for _, row in self.df.iterrows():

      if row["reconall"] == "Possible":

        # if the element in converted that has the same position as the mri I am checking in the mris vector is true
        t1 = None
        for mri in row["t1"]:
          if row["converted"][row["mris"].index(mri)]: t1 = mri
            
        if not t1: print(f"for subject {row['acquisition']} t1 not available"); continue
        
        if f"/ext/fs-subjects/{row['acquisition']}/{t1}" != f"/ext/fs-subjects/{row['acquisition']}/{t1}".replace(" ", ""):
          print (f"non valid name for freesurfer: /ext/fs-subjects/{row['acquisition']}/{t1}")
          continue
        

        source_docker_origin_path.append(f"/ext/fs-subjects/{row['acquisition']}/{t1}")
        source_docker_destination_path.append(f"{row['acquisition']}")
    
    if testing:
      return source_docker_origin_path, source_docker_destination_path
    else: 
      _save_files(source_docker_origin_path, source_docker_destination_path)
        
  def prepare_for_samseg(self, testing = False)-> None:
    
    source_docker_origin_path = []
    source_docker_destination_path = []

    for _, row in self.df.iterrows():

      if row["samseg"] == "Prepared":
        
        t1 = None
        # Select the t1 
        for mri in row["t1"]:
          if row["converted"][row["mris"].index(mri)]: t1 = mri
            
        if not t1: print(f"for subject {row['acquisition']} t1 not available"); continue

        # Add the paths to the origins and destination file
        source_docker_origin_path.append(f"/ext/fs-subjects/{row['acquisition']}/{t1}")
        source_docker_origin_path.append(f"/ext/fs-subjects/{row['acquisition']}/flair_reg.nii")
        source_docker_destination_path.append(f"{row['acquisition']}") # /ext/processed-subjects/
    
    if testing:
      return source_docker_origin_path, source_docker_destination_path
    else: 
      _save_files(source_docker_origin_path, source_docker_destination_path)

  def prepare_for_samseg_only_t1(self, testing = False)-> None:
    
    source_docker_origin_path = []
    source_docker_destination_path = []

    for _, row in self.df.iterrows():

      if row["reconall"] == "Possible" and row["samseg"] != "Done":
        
        t1 = None
        # Select the t1 
        for mri in row["t1"]:
          if row["converted"][row["mris"].index(mri)]: t1 = mri
            
        if not t1: print(f"for subject {row['acquisition']} t1 not available"); continue

        # Add the paths to the origins and destination file
        source_docker_origin_path.append(f"/ext/fs-subjects/{row['acquisition']}/{t1}")
        source_docker_destination_path.append(f"{row['acquisition']}") # /ext/processed-subjects/
    
    if testing:
      return source_docker_origin_path, source_docker_destination_path
    else: 
      _save_files(source_docker_origin_path, source_docker_destination_path)


  def prepare_for_registration(self, testing = False)-> None:
    
    source_docker_origin_path = []
    source_docker_destination_path = []

    for _, row in self.df.iterrows():
      
      # prepared is automatically excluded
      if row["samseg"] == "Possible" or row["samseg"] == "Possible - only t2 not fl" or row["samseg"] == "Possible - only t1fl not t2fl":
        
        t1 = None
        # Select the t1 as described below
        for mri in row["t1"]:
          if row["converted"][row["mris"].index(mri)]: t1 = mri

        if len(row["t2_flair"]) > 0:
          source = row["t2_flair"]
        elif len(row["t1_flair"]) > 0:
          source = row["t1_flair"]
        else:
          source = row["t2"]
          
        if not t1: print(f"for subject {row['acquisition']} t1 not available"); continue # In theory not necessary because i should be already checking it when i assign the value possible
        
        # Selects the mri that has already been converted in the source list. by checking which is marked as true in th converted vecteor
        for mri in source:
          if row["converted"][row["mris"].index(mri)]: # if the element in converted that has the same position as the mri I am checking in the mris vector is true
            flair = mri
            
        if not flair: print(f"for subject {row['acquisition']} flair not available"); continue
        # old: t2 = eval(row["t2_flair"])[-1] if len(eval(row["t2_flair"])) > 0 else eval(row["t2"])[-1]

        source_docker_origin_path.append(f"/ext/fs-subjects/{row['acquisition']}/{t1}")
        source_docker_origin_path.append(f"/ext/fs-subjects/{row['acquisition']}/{flair}.nii")
        source_docker_destination_path.append(f"{row['acquisition']}")
    
    if testing:
      return source_docker_origin_path, source_docker_destination_path
    else: 
      _save_files(source_docker_origin_path, source_docker_destination_path)

  def prepare_for_tables(self, testing = False)-> None:

    subjects = []

    for _, row in self.df.iterrows():
        
        if row["reconall"] == "Done": 

            subject = f"{row['acquisition']}"
            subjects.append(subject)
        
    if testing:
      return subjects
    else: 
      with open("tmp/subjects.txt", "w") as fp:
        for item in subjects:
          fp.write(f"{item}\n")