# Create OR'd PMID list from txt file
with open('pmids.txt', 'r') as input_file: 
    pmid_str=input_file.read().replace('\n', 'OR ')

# Append OR'd PMID list for WoS Advanced Search to txt file
with open('pmids.txt', 'a') as input_file: 
    input_file.write('\n' + '\n' + 'PMID = (' + pmid_str +')')
