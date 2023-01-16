
"""This is the python module used to get data frame from given given map file.

This module takes below parameters.
file -- File that contains map data (Example: data.yaml)
"""

import pandas as pd
import yaml
import argparse


parser = argparse.ArgumentParser(
    description='Show dataframe from yaml file (map data)'
)
parser.add_argument(
    '-f',
    '--file',
    required=True,
    help='Provide yaml file with data(map) e.g. map_data.yaml')

args = parser.parse_args()
yaml_file = args.file

def get_map_data(file):
    """Gets the yaml file data as string
    
    Parameters:
        file (str) : data file with path (ex: data.yaml)
        
    Returns:
        str : data content
    """
    data = None
    with open(file, "r") as stream:
        try:
            data =yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return data

map_data = get_map_data(yaml_file)
data_frame = pd.DataFrame(data=map_data)
#print(data_frame.to_string(index=False))
print(pd.json_normalize(map_data))