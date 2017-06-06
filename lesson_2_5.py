from subprocess import Popen

import os.path
import glob

files_path = (os.path.abspath('2.4-external-programs/result'))
files = glob.glob(os.path.join(files_path, "*.jpg"))
program_path = os.path.abspath('2.4-external-programs/convert.exe')

for file in files:
        args = [program_path, file, '-resize', '200', file]
        proc = Popen(args)





