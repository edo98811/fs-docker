
Tool to simplify the automation of freesurfer using docker on a server
### Introduction


### Installation 
```
git clone https://github.com/edo98811/fs-docker.git
cd fs-docker-manager
pip install (-e) .

```
e for developement installation 

### Preparation 
This can work on any folder, what needs to be written ever time is a funtion to find the subject name in the directory tree every time an mri is found. it can be a directory level, a part of the directory name, anthing. The mri that have the same subject name are put togehter and are considered as from the same subject. 


### Commands 

 - **`fs_docker init_config`** Requires one argument, path to the new config file that needs to be created, it needs to be a .json file
Arguments: string, path to config file, including the name of the file, the name needs to be ajson file. example: "/mnt/S/edoardoStorage/config.json"

- **`fs_docker tool fstables`** create the tables using the freesurfer command 

- **`fs_docker tool register`**  Register the t2 to the t1 to run the samseg

- **`fs_docker tool preparenifti`**  move the nifti files to another folder if the nifti folder is different from dicom folder in settings

- **`fs_docker tool convertdicom`**  convert the dicom files to nifti

- **`fs_docker tool samseg`** run samseg, after performing the registration 

- **`fs_docker tool table`**  To run first you need to run create table, it can be either done starting from nifti or from dicom, default is starting from dicom, when you want to start from nifti you need to use -start_type nifti
This creates a table that contains all the info on the subjects ordered in these columns: 
ID, mris, paths. 


- **`fs_docker tool fstables`** 

#### Workflow example: 
install package 

```
fs_docker init_config
```
set in settings the parameters and the substrings to to check for matching

```
fs_docker tool convertdicom
create the table
fs_docker tool preparenifti
```
Then
```
fs_docker tool reconall 
```
or 
```
fs_docker tool registration 
fs_docker tool samseg
```




### Configuration File Description
This file is used for set up the program for the current dataset

#### Paths

- **nifti**: The path to the directory containing NIfTI files.
- **base_path**: The base directory path for various tools and outputs.
- **dicom**: The path to the directory containing DICOM files.
- **app_path**: The path to the application directory.
- **reconall**: The path to the directory for recon-all results.
- **samseg**: The path to the directory for SAMSEG results.
- **license_path**: The path to the license file.
- **table_path**: The path to the directory for table results.
- **table_name**: The name of the table file.

#### File Identifiers

- **file_identifiers**: A dictionary containing identifiers for different types of MRI files.
  - **T1**: Identifiers for T1 MRI files.
  - **T2**: Identifiers for T2 MRI files.
  - **FLAIR**: Identifiers for FLAIR MRI files.
  - **T1_no**: Identifiers for files that are not T1 MRI (selection by exclusion).
  - **T2_no**: Identifiers for files that are not T2 MRI.
  - **FLAIR_no**: Identifiers for files that are not FLAIR MRI.




