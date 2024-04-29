import re
import json

#pattern = ['{','}', '[', ']','"',',']
pattern = ['{}[]\"']

def load_merge(merge_file):
    with open(merge_file, "r") as f:
        merged_words = list(f.read().splitlines())
    return merged_words

def load_chi(chi_file):
    #with open(chi_file, "r") as f:
    #    chi_data = list(f.read().split('null\t'))
    chi_data = []
    with open(chi_file, 'r+') as f:
        for line in f:
            chi_data.append(json.loads(line.replace('null','').strip()))
    return chi_data

if __name__ == "__main__":
    merge_str = ""
    merge_file = load_merge("merged.txt")
    for item in merge_file:
        merge_str = merge_str + " " + item

    chi_str = ""
    chi_file = load_chi("chi_output.txt")
    
    for item in chi_file:
        for key, value in item.items():
            chi_str = chi_str + key + ": " + ''.join(' '+x+' '+str(y)+','  for x,y in value) + '\n'

    print(chi_str + merge_str)
        
    
    
    