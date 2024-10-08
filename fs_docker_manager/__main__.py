from fs_docker_manager import load_settings
import click
from pathlib import Path
from fs_docker_manager.freesurfer_tool import FreesurferTool


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
@click.option('--start_type', type=str, default = "dicom")
@click.pass_context
def table(ctx: click.Context , start_type: str):
    """Create a table."""
    
    fs = FreesurferTool(ctx.obj["config"], start_type=start_type, new = True)
    fs.Table.save_table()


@tool.command()
@click.option('--nsub', nargs=2, type=int, default = (120, 20))
@click.pass_context
def convertdicom(ctx: click.Context , nsub: tuple):
    """Convert DICOM files."""
    N1, N2 = nsub
    

    fs = FreesurferTool(ctx.obj["config"], origin_folder="rawdata", destination_folder="nifti")
    fs.Prepare.prepare_for_conversion()
    fs.Docker.run("convertdicom", N1, N2)


@tool.command()
@click.pass_context
def preparenifti(ctx: click.Context):
    """ Prepare nifti files. if the rawdata are already nifti. If the rawdata directory coincides with the nifti data, the image names and paths are saved. Otherwise they are moved to the nifti directory.
    """
    move = False if ctx.obj["config"]["rawdata"] == ctx.obj["config"]["nifti"] else True
    
    fs = FreesurferTool(ctx.obj["config"], origin_folder="rawdata", destination_folder="nifti")
    fs.Prepare.prepare_for_conversion(move=move)


@tool.command()
@click.option('--nsub', nargs=2, type=int, default=(120, 20))
@click.pass_context
def run_recon_all(ctx: click.Context , nsub: tuple):
    """Run recon-all."""
    N1, N2 = nsub

    
    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="reconall")
    fs.Prepare.prepare_for_reconall()
    fs.Docker.run("reconall", N1, N2)


@tool.command()
@click.option('--nsub', nargs=2, type=int, default=(120, 20))
@click.pass_context
def run_samseg(ctx: click.Context , nsub: tuple):
    """Run samseg after registration."""
    N1, N2 = nsub

    
    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="samseg")
    fs.Prepare.prepare_for_samseg()
    fs.Docker.run("samseg", N1, N2)
    
@tool.command()
@click.option('--nsub', nargs=2, type=int, default=(120, 20))
@click.pass_context
def run_samseg_onlyt1(ctx: click.Context , nsub: tuple):
    """Run samseg without a second image."""
    
    N1, N2 = nsub

    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="samseg")
    # fs.Prepare.prepare_for_samseg_only_t1()
    fs.Docker.run("samseg_t1", N1, N2)


@tool.command()
@click.option('--nsub', nargs=2, type=int, default=(120, 20))
@click.pass_context
def registration(ctx: click.Context , nsub):
    """Run registration for samseg."""
    N1, N2 = nsub

    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="nifti")
    fs.Prepare.prepare_for_registration()
    fs.Docker.run("register", N1, N2)
    
@tool.command()
@click.pass_context
def fstables(ctx: click.Context):
    """Using aparc2table and aseg2table on reconall results."""

    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="reconall")
    fs.Prepare.prepare_for_tables()
    fs.Docker.run("register", 1, 1)
    
@base.command()
@click.argument('destination', type=click.Path())
def init_config(destination):    
    """Initialize a new configuration file in the provided path."""
    load_settings.create_config(destination)
    
    
if __name__ == "__main__":
    base()