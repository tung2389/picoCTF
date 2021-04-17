"""
Purpose:  This script is used to add new problems to README.md automatically. For more detail on how to use it, run "python updateREADME.md -h"
Author: Tung Luu
"""

from optparse import OptionParser

categoriesList = [
    "General Skills",
    "Cryptography",
    "Forensics",
    "Reverse Engineering",
    "Web exploitation",
    "Binary Exploitation"
]

def parseStrToList(option, opt, value, parser):
  setattr(parser.values, option.dest, value.split(','))

def main():
    parser = OptionParser()
    parser.add_option(
        "-c", 
        '--category',
        help = 'A comma-seperated list of categories. Category mapping: 0 - General Skills.   1 - Cryptograph.   2 - Forensics.  3 - Reverse Engineering  4. Web exploitation  5. Binary Exploitation',
        action = 'callback',
        type = 'string',
        dest = 'category',
        callback = parseStrToList,
    )
    parser.add_option(
        "-n", 
        '--name',
        help = 'A comma-seperated list of problem names',
        action = 'callback',
        type = 'string',
        dest = 'name',
        callback = parseStrToList,
    )

    (options, args) = parser.parse_args()

    if len(options.category) != len(options.name):
        parser.error('The category list must have the same length as the name list')

    if len(options.category) == 0:
        parser.error('At least one category must be correctly specified')
    
    if len(options.name) == 0:
        parser.error('At least one problem name must be specified')

    newContent = open('README.md', 'r').read()

    for i in range(len(options.category)):\
        # Category in string type
        category = categoriesList[int(options.category[i])]
        probName = options.name[i]

        if category not in categoriesList:
            parser.error('Invalid category')

        if not probName:
            parser.error('Problem name cannot be empty')

        idx = newContent.find(category)
        newContent = newContent[0 : idx] + newContent[idx : idx + len(category)] \
            + '\n\n' + '[' + probName + ']' + '(./picoGym/' + probName.replace(' ', '%20') + '/solution.md' + ')' \
            + newContent[idx + len(category) : ]

    readme = open('README.md','w')
    readme.write(newContent)
    readme.close()

main()