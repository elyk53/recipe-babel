#!/usr/bin/env python
# This part of  is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Top level module to handle initialization and provide the command line interface """
import argparse
import recipe_format
from recipe_format import RecipeFormat

def main():
    opts = parse_arguments()
    
def parse_arguments():
    """ Parse arguments of the form: <input file> <input format> <output file> <output format> """
    parser = argparse.ArgumentParser(
        description='Convert a recipe database between formats.',
        epilog='Supported file formats are: ' + recipe_format.list_valid_formats()
        )
    parser.add_argument('input_file', help='Input filename')
    parser.add_argument('input_format', help='Input format (see options below)', type=parse_fileformat)
    parser.add_argument('output_file', help='Output filename')
    parser.add_argument('output_format', help='Output format (see options below)', type=parse_fileformat)
    return parser.parse_args()
    
def parse_fileformat(optstr):
    """
    argparse doesn't directly support enum types. So we define a custom function to convert
    the raw argument string into the enum type. Idea from https://bugs.python.org/issue25061
    """
    try:
        return RecipeFormat[optstr.upper()]
    except KeyError:
        err = 'Unsupported file format "{0}". Valid formats are: {1}'.format(optstr, recipe_format.list_valid_formats())
        raise argparse.ArgumentTypeError(err)
    
if __name__ == "__main__":
    main()
