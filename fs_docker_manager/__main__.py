
import load_settings
import click
from pathlib import Path
from freesurfer_tool import FreesurferTool

@click.group()
def base():
    pass

@base.group()
@click.pass_context
def tool(ctx: click.Context):
    config = load_settings.load_config()

    ctx.ensure_object(dict)
    ctx.obj["config"] = config
    
@tool.command()
def create_table(start_type="dicom"):
    """Create a table."""
    fs = FreesurferTool(start_type=start_type)
    fs.Table.save_table()

@tool.command()
@click.option('--nsub', nargs=2, type=float, default = (120, 20))
def convert_dicom(nsub):
    """Convert DICOM files."""
    N1, N2 = nsub
    fs = FreesurferTool(origin_folder="rawdata", destination_folder="nifti")
    fs.Prepare.prepare_for_conversion()
    fs.Docker.run("convertdicom", N1, N2)

@tool.command()
def prepare_nifti():
    """Prepare NIfTI files. if the rawdata are already nifti"""
    fs = FreesurferTool(origin_folder="rawdata", destination_folder="nifti")
    fs.Prepare.prepare_for_conversion(move=True)

@tool.command()
def run_recon_all():
    """Run recon-all."""
    fs = FreesurferTool(origin_folder="nifti", destination_folder="reconall")
    fs.Prepare.prepare_for_reconall()
    fs.Docker.run("reconall", N1, N2)

@tool.command()
def run_samseg():
    """Run SAMSEG."""
    fs = FreesurferTool(origin_folder="nifti", destination_folder="samseg")
    fs.Prepare.prepare_for_samseg()
    fs.Docker.run("samseg", N1, N2)

@tool.command()
def registration():
    """Run registration."""
    fs = FreesurferTool(origin_folder="nifti", destination_folder="nifti")
    fs.Prepare.prepare_for_registration()
    
@base.command()
@click.argument('destination', type=click.Path())
def init_config(destination):
    """Initialize a new configuration file in the provided path."""
    load_settings.create_config(destination)
    
if __name__ == "__main__":
    base()