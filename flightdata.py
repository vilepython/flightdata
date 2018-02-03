# -*- coding: utf-8 -*-
"""
flightdata.py

Process Flight Circle export data and prepare for import to a billing tool

Copyright (c) 2018.  See LICENSE for rights, restrictions, permissions.

"""
from pathlib import Path

import argparse

INVALID_DATE = "1/1/1979"

"""
Object for Flight Circle data processing
"""   
class fc_data( object ):
    
    def __init__( self ):
        self.pilot = ""
        self.date = INVALID_DATE
        self.hobbs = 0.0
        self.tach = 0.0

"""
Object for Flight Circle data processing
"""   
class fc_data_parser( object ):

    """
    Initialize the fc_data_parser object
    
    Args:
        self:   Required self-reference
    """     
    def __init__( self ):
        
        #Define members as empty strings
        self.input_file = ""
        self.output_file = ""
        self.flights = []

    """
    Parse file
    
    Args:
        self:   Required self-reference
    """  
    def parse( self ):
        #Validate input file exists
        #Validaate output file can exist
        #Open input file
        #For each row
            #Create object with fields
            #Perform sanity check on data
            #Add object to data array
        #Close input file
        
        #Open output file
        #For each array object
            #Build output CSV string
            #Write string to file
        #Close output file
        
        pass


"""
Validates a file exists

Args:
    full_path:   A path and file name
    
Returns:
    A boolean value - file exists
"""    
def file_exists( path ):

    #Generate a Path object based on desired path
    my_file = Path( path )
    
    #Determine if the Path item is a file
    if my_file.is_file():
        retval = True
    else:
        retval = False
    
    return retval

"""
Validates a path exists

Args:
    full_path:   A path name
    
Returns:
    A boolean value - path exists
"""    
def path_exists( path ):
    
    #Generate a Path object based on desired path
    my_file = Path( path )
    
    #Determine if the Path item is a file
    if my_file.exists():
        retval = True
    else:
        retval = False
    
    return retval

if __name__ == "__main__":
    
    # Set up an argument parser.  Gather input and output file names.
    parser = argparse.ArgumentParser(description='Process Flight Cirle data')
    parser.add_argument('-i', '--input', dest='input_file', default='input.csv',
                        help='Input file name.  Include path if needed.')
    parser.add_argument('-o', '--output', dest='output_file', default='output.csv',
                        help='Output file name.  Include path if needed.')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Enable debugging mode')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    
    args = parser.parse_args()
    
    fcd = fc_data_parser()
    fcd.input_file = args.input_file
    fcd.output_file = args.output_file
    fcd.parse()
