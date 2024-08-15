
import create_table as t
import prepare as p
import docker as d
import helper_functions as h


class FreesurferTool():
    def __init__(self, settings, origin_folder="rawdata", destination_folder="nifti", start_type="dicom"):
        self.SET = settings
        self.Docker = d.DockerInstance(self.SET, origin_folder, destination_folder)
        self.Table = t.Table(self.SET, find_type=start_type)
        self.Prepare = p.Prepare(self.SET, self.Table)