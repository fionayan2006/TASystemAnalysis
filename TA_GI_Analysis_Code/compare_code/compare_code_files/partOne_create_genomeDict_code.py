##By Fiona Yan, July 2022
# ##1.2 read GI as tuples. Test with N1_U00096.3.txt. Worked 10:00

# with open('result_files_final/N1_U00096.3.txt') as f:
#    mylist = [tuple(map(int, i.split('\t'))) for i in f]

# print(mylist)

# ##1.1 test get name of file minus .txt; worked 10:12
# full_name = 'N1_U00096.3.txt'
# clean_name = full_name[:-4]
# print (clean_name)

##ENTIRE PART 1
import os

genomeDict = {}
result_dir = 'result_files_final' ###change to result_files_final for actual run (get out of compare_code)
for curr_file_name in os.listdir(result_dir):
    ##print('current file is ' + curr_file_name)
    curr_file_path = os.path.join(result_dir, curr_file_name)

    if (curr_file_name.endswith('.txt')):
        with open(curr_file_path) as f:
         curr_file_islands = [tuple(map(int, i.split('\t'))) for i in f]

    clean_name = curr_file_name[:-4]
    genomeDict[clean_name] = curr_file_islands

print('genomeDict created')
print (genomeDict)
