# encoding=utf-8
"""
author:renyubin
date:20201212
function: rotary encoding
"""
from Rotarycode.rotary_param import *

def rotaryencode(codelist):
    if codelist==[]:
        return []

    encoded_result = ''
    pre_nucleotide=''
    for i in codelist:
        for key,value in map_dit.items():
            if i ==key and pre_nucleotide=='':
                encoded_result+=value[0]
                pre_nucleotide=value[0]
                break
            elif i==key:
                pre_nucleotide_index=pre_nucleotides.index(pre_nucleotide)
                encoded_result+=value[pre_nucleotide_index]
                pre_nucleotide=value[pre_nucleotide_index]
                break
    return encoded_result

if __name__=="__main__":


    list2=[2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 4, 4, 4, 2, 3, 2, 3, 2, 3, 4, 4, 4, 4, 2, 3, 2, 3, 2, 3, 4, 4, 4, 4, 2, 3,
     2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 2, 3, 2, 3, 4, 4, 4, 4, 4, 4, 2, 3, 2, 3, 2, 3, 4, 4, 2, 3, 2, 3, 4, 4, 4, 4, 0, 1,
     4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 4, 4, 0, 1, 0, 1, 0, 1, 0, 1,
     0, 1, 0, 1, 0, 1]

    encoded_result=rotaryencode(list2)
    print(encoded_result)
