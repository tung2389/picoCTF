"""
Example:
cd picoGym
python ../readmeGenerator.py -p './picoGym/' -s '/solution.md'
"""

from optparse import OptionParser
from pathlib import Path
from os import walk
import os

def main():
    parser = OptionParser()
    parser.add_option(
        "-p", 
        '--prefix',
        action = 'store',
        type = 'string',
        dest = 'prefix',
    )
    parser.add_option(
        "-s", 
        '--suffix',
        action = 'store',
        type = 'string',
        dest = 'suffix',
    )

    (options, args) = parser.parse_args()

    cwdName = os.getcwd().split('/')[-1]
    dirNames = [str(dirPath).split('/')[-1] for dirPath in sorted(Path(os.getcwd()).iterdir(), key=os.path.getmtime, reverse = True)]
    for dirName in dirNames:
        content = '[' + dirName + ']' + f'({options.prefix}' + dirName.replace(' ', '%20') + f'{options.suffix}' + ')' 
        print(content)
        print()

    # Get dirnames without order
    # cwdName = os.getcwd().split('/')[-1]
    # dirNames = [str(dirPath).split('/')[-1] for dirPath in sorted(Path(os.getcwd()).iterdir(), key=os.path.getmtime, reverse = True)]
    # for dirName in dirNames:
    #     content = '[' + dirName + ']' + f'({options.prefix}' + dirName.replace(' ', '%20') + f'{options.suffix}' + ')' 
    #     print(content)
    #     print()

main()