##By Fiona Yan July,2022

import pandas as pd
from partOne_code import genomeDict
df_A = pd.read_csv('/Users/siptest/SSG-LUGIA/codes/compare_code/E.coli_Comp_trn_A.csv') ##change to combined_csv.csv during  actual run
df_B = pd.read_csv('/Users/siptest/SSG-LUGIA/codes/compare_code/E.coli_Comp_trn_B.csv')

BP_TspInGI = 0
BP_TspNotInGI = 0
TspInGI = 0
TspNotInGI = 0
#error_range = int(500) #(500 nucleotide buffer for genomic islands)
#1.1-1.2
row_index_tsp = 0 ##Is there a way to do this to find the row index that correspond to the contig?
list_of_tsp_in_GI = [] ##MAYBE not needed?
##pd.DataFrame()#columns=['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end'])
#column_name = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']
df_tsp_in_GI = pd.DataFrame()#column_name)
df_tsp_notInGI = pd.DataFrame()
##column_names = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']
##dfGI = dfGI.append(column_names)

for r_tsp in df_A['Contig']: ##goes through every row by contig
    ##print(df.iloc[row_index]['Upstream_length'])  ##test for getting the upstream length entry for this specific row
    
    #Get the TA sys. domain and upstream length
    curr_type = df_A.iloc[row_index_tsp]['Type'] 
    #curr_upstream_length = df.iloc[row_index]['Upstream_length'] 
    ##print('domain= ' + str(curr_domain))##Test for correct identification of domain
    ##print('upstream length= '+ str(curr_upstream_length))##Test for correct identification of upstream length
    
    tsp_start = df_A.iloc[row_index_tsp]['Position']
    tsp_end = df_B.iloc[row_index_tsp]['Position']
    #if (df.iloc[row_index]['Upstream_length']>1):
        #ta_start = int(df.iloc[row_index]['Upstream_start'])
        #ta_end = int(df.iloc[row_index]['Hit_stop'])
        #print(curr_domain + ' ta_start= ' + str(ta_start) + 'ta_end= '+ str(ta_end) ) ##Test to see if the TA regions are identified correctly
    #else:
        #ta_start = int(df.iloc[row_index]['Hit_start'])
        #ta_end = int(df.iloc[row_index]['Downstream_stop'])
        #print(curr_domain+ ' ta_start= ' + str(ta_start) + 'ta_end= '+ str(ta_end) ) ##Test to see if the TA regions are identified correctly

    #Get the genomic regions
    list_of_regions = genomeDict[r_tsp]
    falls_in_tsp = False
    for this_tuple in list_of_regions:
        region_start = int(this_tuple[0])
        region_end = int(this_tuple[1])
        #print('region_start in  ' + r + ' is ' + str(region_start) + '. region_end is '  + str(region_end)) 
        #if (((region_start<ta_start) or (region_end>ta_end)) and ((ta_end-region_start>0) or (region_end-ta_start>0))):
        #if ((((region_start<ta_start) and (ta_end<region_end)) or ((ta_start>region_start) and (region_end>ta_start))) or ((ta_end>region_start) and (region_end>ta_end))):
        if (((tsp_start>region_start) and (region_end>tsp_start)) or ((tsp_end>region_start) and (region_end>tsp_end))):
            falls_in_tsp = True
            name_of_tsp = curr_type
            Name_of_chromo_tsp = r_tsp
            island_range_tsp = (region_start,region_end)
            distance_from_start_tsp = int(tsp_start)-int(region_start)
            distance_from_end_tsp = int(region_end)-int(tsp_end)

            curr_tsp_number_of_basepairs = tsp_end-tsp_start
            BP_TspInGI = BP_TspInGI + curr_tsp_number_of_basepairs
            TspInGI = TspInGI + 1

            data = [[name_of_tsp,Name_of_chromo_tsp,island_range_tsp,distance_from_start_tsp,distance_from_end_tsp]]
            df_tsp_in_GI = df_tsp_in_GI.append(data,ignore_index=True)
            #, columns = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']


            #print(str(curr_domain)+' is in GI') ##replace with store in inGI dataframe with the correct info
            break ##break when falls into GI
        #else:
            #print('Not in this region')
    if (falls_in_tsp==False):
        #print(str(curr_domain)+' is NOT in GI') ##replace with store in inGI dataframe with the correct info
        name_of_tsp = curr_type
        Name_of_chromo_tsp = r_tsp
        ####### ADD curr_tsp_number_of_basepairs
        NotInGI_curr_tsp_number_of_basepairs = tsp_end-tsp_start
        BP_TspNotInGI = BP_TspNotInGI + NotInGI_curr_tsp_number_of_basepairs
        TspNotInGI = TspNotInGI + 1
        # BP_TspInGI = BP_TAInGI + curr_ta_number_of_basepairs
        #island_range = (region_start,region_end) ##FUTURE DIRECTION: CHECK HOW FAR THE TA IS FROM LANDING IN THE NEAREST GI
        data = [[name_of_tsp,Name_of_chromo_tsp]]
        df_tsp_notInGI = df_tsp_notInGI.append(data,ignore_index=True)
        
        ##test line to see if values in genomeDict are read in correctly
        ##HAVE TO MAKE IT SO THAT EVEN IF IT'S NOT IN THIS TUPLE, IT CHECKS FOR ALL THE TUPLES

    row_index_tsp += 1

#dfGI = pd.concat(list_of_TA_in_GI, names = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end'])
df_tsp_in_GI = df_tsp_in_GI.rename(columns={0:'Domain',1:'Contig',2:'Island',3:'D From Start',4:'D From End'})
#print(dfGI)
#filepath_for_result='/Users/siptest/SSG-LUGIA/codes/compare_code'
df_tsp_in_GI.to_csv('TSP_In_GI_from_E.Coli_Comp_trn.csv')
#dfGI.to_excel('TA_In_GI.xls')
df_tsp_notInGI = df_tsp_notInGI.rename(columns={0:'Type',1:'Contig'})
#print(df_notInGI)
df_tsp_notInGI.to_csv('TSP_NotIn_GI_from_.Coli_Comp_trn.csv')
#df_notInGI.to_excel('TA_In_GI.xls')

##2/10: total_Tsp_BP = BP_TspInGI+BP_TspNotInGI
##2/10: avg_size_chromo_bp = 4934898.5441558445 

total_Tsp=TspInGI+TspNotInGI
observed = TspInGI/total_Tsp * 100

print("The observed chance of TSP falling in GI is "+ str(observed))
print('done')

    



#entry = df.iloc[0][2]

#print (entry)
##print(df)