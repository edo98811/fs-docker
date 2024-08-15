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
def table(ctx: click.Context, start_type: str):
    """Create a table."""
    
    fs = FreesurferTool(ctx.obj["config"], start_type=start_type)
    fs.Table.save_table()


@tool.command()
@click.option('--nsub', nargs=2, type=float, default = (120, 20))
def convertdicom(ctx: click.Context, nsub: tuple):
    N1, N2 = nsub
    """Convert DICOM files."""

    fs = FreesurferTool(ctx.obj["config"], origin_folder="rawdata", destination_folder="nifti")
    fs.Prepare.prepare_for_conversion()
    fs.Docker.run("convertdicom", N1, N2)


@tool.command()
def preparenifti(ctx: click.Context):
    """
    Prepare nifti files. if the rawdata are already nifti
    If the rawdata directory coincides with the nifti data, the image names and paths are saved. Otherwise they are moved to the nifti directory
    """
    move = False if ctx.obj["config"]["rawdata"] == ctx.obj["config"]["nifti"] else True
    
    fs = FreesurferTool(ctx.obj["config"], origin_folder="rawdata", destination_folder="nifti")
    fs.Prepare.prepare_for_conversion(move=move)


@tool.command()
@click.option('--nsub', nargs=2, type=float, default=(120, 20))
def run_recon_all(ctx: click.Context, nsub: tuple):
    N1, N2 = nsub
    """Run recon-all."""
    
    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="reconall")
    fs.Prepare.prepare_for_reconall()
    fs.Docker.run("reconall", N1, N2)


@tool.command()
@click.option('--nsub', nargs=2, type=float, default=(120, 20))
def run_samseg(ctx: click.Context, nsub: tuple):
    N1, N2 = nsub
    """Run SAMSEG."""
    
    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="samseg")
    fs.Prepare.prepare_for_samseg()
    fs.Docker.run("samseg", N1, N2)


@tool.command()
def registration(ctx: click.Context):
    """Run registration."""
    fs = FreesurferTool(ctx.obj["config"], origin_folder="nifti", destination_folder="nifti")
    fs.Prepare.prepare_for_registration()
    
    
@base.command()
@click.argument('destination', type=click.Path())
def init_config(destination):
    """Initialize a new configuration file in the provided path."""
    load_settings.create_config(destination)
    
    
if __name__ == "__main__":
    base()