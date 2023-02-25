from partOne_code import genomeDict

##test for looping through a dictionary
test_dictionary = genomeDict ##genomeDict
list_of_values = list(test_dictionary.values()) ##list of islands
##print (list_of_values)
size_of_list = len(list_of_values)
print(size_of_list) ##should be 770
index = 0 
bp_sum = 0
while index < size_of_list: ##loops through every value in the genomeDict
    current_value = list_of_values[index] ##the current island
    if isinstance(current_value,list): ##if the current key contains a list of values (which it should)
        index_for_current_value = 0
        size_of_current_value = len(current_value)
        while index_for_current_value < size_of_current_value: ##loops through each individual island in the chromosome
            start_test = current_value[index_for_current_value][0] ##start sequence
            end_test = current_value[index_for_current_value][1] ##end sequence
            print("the tuple is " + str(current_value[index_for_current_value])) 
            print("start value is a "+ str(start_test)) 
            print("end value is a "+ str(end_test))
            current_island_size = end_test - start_test+1
            bp_sum = bp_sum + current_island_size
            index_for_current_value += 1
            
       ## print(str(current_value) + " is a list")
    else:
        start_test = current_value[0]
        end_test = current_value[1]
        print("the tuple is " + str(current_value))
        print("start value is "+ str(start_test))
        print("end value is "+ str(end_test))
        current_island_size = end_test - start_test +1
        bp_sum = bp_sum + current_island_size
    index = index+1

print("total number of genomic island base pairs in all 770 chromosmes =  " + str(bp_sum)) ##sum should be 23

AveSizeGI = bp_sum/770
print("AveSizeGI = " + str(AveSizeGI))

avg_size_chromo_bp = 4934898.5441558445 
AveSizeChromo_NoGI = avg_size_chromo_bp - AveSizeGI
calculated_FEA = AveSizeGI / avg_size_chromo_bp*100

calculated_FEA_BeforeAve = bp_sum/(avg_size_chromo_bp*770)
print('average bp of chromosomes - average bp of GI = ' + str(AveSizeChromo_NoGI))
print('The calculated chance for FEA = ' + str(calculated_FEA))
print('The calculated chance for FEA 2 = ' + str(calculated_FEA_BeforeAve))
print("done")