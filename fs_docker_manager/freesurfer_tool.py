
from fs_docker_manager import create_table as t
from fs_docker_manager import prepare as p
from fs_docker_manager import docker as d
from fs_docker_manager import helper_functions as h


class FreesurferTool():
    def __init__(self, settings, test_mode=False, origin_folder="rawdata", destination_folder="nifti", start_type="dicom", new = False):
        self.SET = settings
        self.Docker = d.DockerInstance(self.SET, origin_folder, destination_folder)
        self.Table = t.Table(self.SET, find_type=start_type, new=new)
        self.Prepare = p.Prepare(self.SET, self.Table)