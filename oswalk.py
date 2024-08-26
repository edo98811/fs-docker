import os

def save_os_walk_to_txt(start_directory: str, output_file: str) -> None:
    """
    Walk through the directory tree starting from 'start_directory' 
    and save the results to 'output_file'.

    Args:
    - start_directory (str): The directory to start the os.walk from.
    - output_file (str): The path to the output text file.
    """

    with open(output_file, "w") as file:
        file.write("\n".join("%s %s %s" % x for x in os.walk(start_directory)))
        
    print(f"Results have been saved to {output_file}")


# Example usage
start_directory = 'test_data/NIFTI'  # Starting from the current directory
output_file = 'os_walk_results.txt'

save_os_walk_to_txt(start_directory, output_file)