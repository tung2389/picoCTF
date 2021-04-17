from optparse import OptionParser

categoriesList = [
    "General Skills",
    "Cryptography",
    "Forensics",
    "Reverse Engineering",
    "Web exploitation",
    "Binary Exploitation"
]



parser = OptionParser()
parser.add_option(
    "-c", 
    '--category',
    help = 'Choose a category: 0 - General Skills.   1 - Cryptograph.   2 - Forensics.  3 - Reverse Engineering  4. Web exploitation  5. Binary Exploitation',
    action = 'store',
    type = 'int',
    dest = 'category'
)
parser.add_option(
    "-n", 
    '--name',
    help = 'Problem name',
    action = 'store',
    dest = 'name'
)

(options, args) = parser.parse_args()

if (options.category == None) or options.category < 0 or options.category > 5:
    parser.error('A category must be correctly specified')

if not options.name:
    parser.error('Name cannot be empty')

origContent = open('README.md', 'r').read()
# Category in string type
category = categoriesList[options.category]
probName = options.name

idx = origContent.find(category)
newContent = origContent[0 : idx] + origContent[idx : idx + len(category)] \
    + '\n\n' + '[' + probName + ']' + '(./picoGym/' + probName.replace(' ', '%20') + '/solution.md' + ')' \
    + origContent[idx + len(category) : ]

readme = open('README.md','w')
readme.write(newContent)
readme.close()