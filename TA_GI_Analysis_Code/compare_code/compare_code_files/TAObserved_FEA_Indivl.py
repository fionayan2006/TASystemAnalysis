##Count number of base pairs of TA systems that fall inside GI's

import pandas as pd
from partOne_code import genomeDict
df = pd.read_csv('/Users/siptest/SSG-LUGIA/codes/combined_csv.csv') ##CHANGE to combined_csv.csv during  actual run

#error_range = int(500) #(500 nucleotide buffer for genomic islands)
#1.1-1.2
row_index = 0 ##Is there a way to do this to find the row index that correspond to the contig?
list_of_TA_in_GI = []
##pd.DataFrame()#columns=['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end'])
#column_name = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']
###df_in_GI = pd.DataFrame()#column_name)
###df_notInGI = pd.DataFrame()

BP_TAInGI = 0
BP_TANotInGI = 0
TAInGI = 0
TANotInGI = 0
CbtA_InGI = 0
CbtA_notInGI = 0

##column_names = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']
##dfGI = dfGI.append(column_names)
for r in df['Contig']: ##goes through every row by contig
    ##print(df.iloc[row_index]['Upstream_length'])  ##test for getting the upstream length entry for this specific row
    
    #Get the TA sys. domain and upstream length
    curr_domain = df.iloc[row_index]['Domain'] 
    curr_upstream_length = df.iloc[row_index]['Upstream_length'] 
    ##print('domain= ' + str(curr_domain))##Test for correct identification of domain
    ##print('upstream length= '+ str(curr_upstream_length))##Test for correct identification of upstream length
    
    if (df.iloc[row_index]['Upstream_length']>1):
        ta_start = int(df.iloc[row_index]['Upstream_start'])
        ta_end = int(df.iloc[row_index]['Hit_stop'])
        print(curr_domain + ' ta_start= ' + str(ta_start) + 'ta_end= '+ str(ta_end) ) ##Test to see if the TA regions are identified correctly
    else:
        ta_start = int(df.iloc[row_index]['Hit_start'])
        ta_end = int(df.iloc[row_index]['Downstream_stop'])
        print(curr_domain+ ' ta_start= ' + str(ta_start) + 'ta_end= '+ str(ta_end) ) ##Test to see if the TA regions are identified correctly

    #Get the genomic regions
    list_of_regions = genomeDict[r]
    falls_in = False
    for this_tuple in list_of_regions:
        region_start = int(this_tuple[0])
        region_end = int(this_tuple[1])
        #print('region_start in  ' + r + ' is ' + str(region_start) + '. region_end is '  + str(region_end)) 
        #if (((region_start<ta_start) or (region_end>ta_end)) and ((ta_end-region_start>0) or (region_end-ta_start>0))):
        #if ((((region_start<ta_start) and (ta_end<region_end)) or ((ta_start>region_start) and (region_end>ta_start))) or ((ta_end>region_start) and (region_end>ta_end))):
        if (((ta_start>region_start) and (region_end>ta_start)) or ((ta_end>region_start) and (region_end>ta_end))):
            falls_in = True

            ##2/8: curr_ta_number_of_basepairs = ta_end-ta_start
            ##2/8: BP_TAInGI = BP_TAInGI + curr_ta_number_of_basepairs
            TAInGI = TAInGI + 1
            
            name_of_TA_Sys = curr_domain
            if (name_of_TA_Sys == 'CbtA'):
                CbtA_InGI = CbtA_InGI + 1
                ## add one to total count
            
            ##2/8: Name_of_chromo = r
            ###island_range = (region_start,region_end)
            ###distance_from_start = int(ta_start)-int(region_start)
            ###distance_from_end = int(region_end)-int(ta_end)
            ###data = [[name_of_TA_Sys,Name_of_chromo,island_range,distance_from_start,distance_from_end]]
            ###df_in_GI = df_in_GI.append(data,ignore_index=True)
            #, columns = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']


            #print(str(curr_domain)+' is in GI') ##replace with store in inGI dataframe with the correct info
            break ##break when falls into GI
        #else:
            #print('Not in this region')
    if (falls_in==False):
        #print(str(curr_domain)+' is NOT in GI') ##replace with store in inGI dataframe with the correct info
        name_of_TA_Sys = curr_domain
        if (name_of_TA_Sys == 'CbtA'):
            CbtA_notInGI = CbtA_notInGI+1
        Name_of_chromo = r
        #island_range = (region_start,region_end) ##FUTURE DIRECTION: CHECK HOW FAR THE TA IS FROM LANDING IN THE NEAREST GI
        ###data = [[name_of_TA_Sys,Name_of_chromo]]
        
        ###df_notInGI = df_notInGI.append(data,ignore_index=True)

        ##2/8: NotInGI_curr_ta_number_of_basepairs = ta_end-ta_start
        ##2/8:BP_TANotInGI = BP_TANotInGI + NotInGI_curr_ta_number_of_basepairs
        TANotInGI = TANotInGI+1

        ##test line to see if values in genomeDict are read in correctly
        ##HAVE TO MAKE IT SO THAT EVEN IF IT'S NOT IN THIS TUPLE, IT CHECKS FOR ALL THE TUPLES

    row_index += 1

#dfGI = pd.concat(list_of_TA_in_GI, names = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end'])

###df_in_GI = df_in_GI.rename(columns={0:'Domain',1:'Contig',2:'Island',3:'D From Start',4:'D From End'})

#print(dfGI)
#filepath_for_result='/Users/siptest/SSG-LUGIA/codes/compare_code'

###df_in_GI.to_csv('TA_In_GI_from_combined2.csv')

#dfGI.to_excel('TA_In_GI.xls')

###df_notInGI = df_notInGI.rename(columns={0:'Domain',1:'Contig'})

#print(df_notInGI)

###df_notInGI.to_csv('TA_NotIn_GI_from_combined2.csv')

#df_notInGI.to_excel('TA_In_GI.xls')

##2/8:total_TA_BP = BP_TAInGI+BP_TANotInGI
avg_size_chromo_bp = 4934898.5441558445 

##2/8: observed = BP_TAInGI/avg_size_chromo_bp * 100
##2/8: observed_absolute = TAInGI/(TAInGI+TANotInGI)*100

##2/8: observed_ta = BP_TAInGI/total_TA_BP*100

total_CbtA = CbtA_InGI+CbtA_notInGI
observed_CbtA = CbtA_InGI/total_CbtA*100
total_TA = TAInGI+TANotInGI
total_TA_ExcludingCbtA = total_TA-total_CbtA
total_TA_InGI_Excluding_CbtA = TAInGI - CbtA_InGI
observed_non_CbtA = total_TA_InGI_Excluding_CbtA/total_TA_ExcludingCbtA*100
 
print('The number of CbtA in GI = ' + str(CbtA_InGI))
print('The number of CbtA NOT in GI =  ' + str(CbtA_notInGI))
print('Total number of CbtA = ' + str(total_CbtA))
print("Observed_CbtA = "+ str(observed_CbtA))
print('Total number of non-CbtA TA = ' + str(total_TA_ExcludingCbtA))
print('Total number of non-CbtA in GI = ' + str(total_TA_InGI_Excluding_CbtA))
print('Observed non CbtA = ' + str(observed_non_CbtA))

print('done')

    



#entry = df.iloc[0][2]

#print (entry)
##print(df)