##Count number of base pairs of TA systems that fall inside GI's
##useless file? done in TAObserved_FEA
import pandas as pd
from partOne_code import genomeDict
df = pd.read_csv('/Users/siptest/SSG-LUGIA/codes/combined_csv.csv') ##change to combined_csv.csv during  actual run

#error_range = int(500) #(500 nucleotide buffer for genomic islands)
#1.1-1.2
row_index = 0 ##Is there a way to do this to find the row index that correspond to the contig?
list_of_TA_in_GI = []
##pd.DataFrame()#columns=['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end'])
#column_name = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']
df_in_GI = pd.DataFrame()#column_name)
df_notInGI = pd.DataFrame()
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
        region_start = int(this_tuple[0]-500)
        region_end = int(this_tuple[1]+500)
        #print('region_start in  ' + r + ' is ' + str(region_start) + '. region_end is '  + str(region_end)) 
        #if (((region_start<ta_start) or (region_end>ta_end)) and ((ta_end-region_start>0) or (region_end-ta_start>0))):
        #if ((((region_start<ta_start) and (ta_end<region_end)) or ((ta_start>region_start) and (region_end>ta_start))) or ((ta_end>region_start) and (region_end>ta_end))):
        if (((ta_start>region_start) and (region_end>ta_start)) or ((ta_end>region_start) and (region_end>ta_end))):
            falls_in = True
            name_of_TA_Sys = curr_domain
            Name_of_chromo = r
            island_range = (region_start,region_end)
            distance_from_start = int(ta_start)-int(region_start)
            distance_from_end = int(region_end)-int(ta_end)
            data = [[name_of_TA_Sys,Name_of_chromo,island_range,distance_from_start,distance_from_end]]
            df_in_GI = df_in_GI.append(data,ignore_index=True)
            #, columns = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end']


            #print(str(curr_domain)+' is in GI') ##replace with store in inGI dataframe with the correct info
            break ##break when falls into GI
        #else:
            #print('Not in this region')
    if (falls_in==False):
        #print(str(curr_domain)+' is NOT in GI') ##replace with store in inGI dataframe with the correct info
        name_of_TA_Sys = curr_domain
        Name_of_chromo = r
        #island_range = (region_start,region_end) ##FUTURE DIRECTION: CHECK HOW FAR THE TA IS FROM LANDING IN THE NEAREST GI
        data = [[name_of_TA_Sys,Name_of_chromo]]
        df_notInGI = df_notInGI.append(data,ignore_index=True)
        
        ##test line to see if values in genomeDict are read in correctly
        ##HAVE TO MAKE IT SO THAT EVEN IF IT'S NOT IN THIS TUPLE, IT CHECKS FOR ALL THE TUPLES

    row_index += 1

#dfGI = pd.concat(list_of_TA_in_GI, names = ['name of TA', 'Contig', 'Island', 'Distance from start', 'Distance from end'])
df_in_GI = df_in_GI.rename(columns={0:'Domain',1:'Contig',2:'Island',3:'D From Start',4:'D From End'})
#print(dfGI)
#filepath_for_result='/Users/siptest/SSG-LUGIA/codes/compare_code'
df_in_GI.to_csv('TA_In_GI_from_combined2.csv')
#dfGI.to_excel('TA_In_GI.xls')
df_notInGI = df_notInGI.rename(columns={0:'Domain',1:'Contig'})
#print(df_notInGI)
df_notInGI.to_csv('TA_NotIn_GI_from_combined2.csv')
#df_notInGI.to_excel('TA_In_GI.xls')
print('done')

    



#entry = df.iloc[0][2]

#print (entry)
##print(df)