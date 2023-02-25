from Bio import SeqIO
import os

## run with done_searching folder
count = 0
curr_dir = os.getcwd()
for filename in os.listdir(curr_dir):
    #print(filename)
    if filename.endswith('.fasta'):
        for record in SeqIO.parse(filename, "fasta"):
            count = count + len(record.seq)
            #print(len(record.seq))

print('the total number of basepairs in 770 chromosomes is ' + str(count))

total_num_of_chromo = 770
avg_chromo_size = count/total_num_of_chromo

print('The average number of basepairs of chromosome is ' + str(avg_chromo_size))
print('done')


#10+8+5