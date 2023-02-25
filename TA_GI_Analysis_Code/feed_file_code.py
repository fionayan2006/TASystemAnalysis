import os
from copy_of_main import *
import shutil
# assign directory
directory = 'split_chromo'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file   
    if os.path.isfile(f):
        if (filename.endswith('.fasta')):
            SSG_LUGIA(sequence_fasta_file_path=f,model_name='SSG-LUGIA-P')
            src = '/Users/siptest/SSG-LUGIA/codes/split_chromo/' + filename
            dest = '/Users/siptest/SSG-LUGIA/codes/done_searching/' + filename
            print('source is '+ src + ' Dest is ' + dest)
            shutil.move(src, dest)
            print('done moving')