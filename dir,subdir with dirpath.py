import fnmatch
import os

barlist = []
for root, dirnames, filenames in os.walk('C:/Users/JiN/Downloads'):
    for filename in fnmatch.filter(filenames, '*docx'):
        print(os.path.join(root, filename))
#fn match is for file name pattern matching
#os.path.join is used for manipulate dir and file name
