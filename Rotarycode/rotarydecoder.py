# encoding=utf-8
"""
author:renyubin
date:20201212
function: ratary decoding
"""

from Rotarycode.rotary_param import *
import numpy as np

def rotarydecode(dna_str):

    if not isinstance(dna_str,str) or dna_str==[]:
        return []
    rotary_decoded_result=[]
    pre_nucleotide=''
    for i in range(0,len(dna_str),2):
        if pre_nucleotide == '':
            for key,value in map_dit.items():
                    if  dna_str[i:i+2]==value[0]:
                        rotary_decoded_result.append(key)
                        pre_nucleotide=dna_str[i:i+2]
                        break
        else:
            for key,value in map_dit.items():
                pre_nucleotide_index=pre_nucleotides.index(pre_nucleotide)
                if value[pre_nucleotide_index]==dna_str[i:i+2]:
                    rotary_decoded_result.append(key)
                    pre_nucleotide=dna_str[i:i+2]
    return rotary_decoded_result


if __name__=="__main__":
    dna_str1="ACATAGGCGACTCGCCCAATCGCCCAATCTCGCCCATAGTGGGCACAATTTGCCCAGCGACTCGCCCAGGGCGACTAAGGGCGAACGTGGGCGACTCGCCCAATAGACTAGACTCGCCCAATAGACAATTTGTCTAGTGGCCACTAGACTCGCCCAACTTTAGGCTCCAGAATCGTGGGCGACTCGCCCAATAATGGTGCCGCAACTTTAGGCTCCAGAATCGTGGGCGACTCAAGTTTC"
    dna_str2="ATCTGGTGACCCGATATTATCGGGTTCAGCTGACCCGATATTATGATCAGCTGGTGACCCGATAACCGGTAAATCTGGTGATGATCAGCTTAACCGGCTCAACAGCTGATGATCAGCCGCTAAAATCTTAACCAGAGTTTCAGCTGATCACGGTAACCGGTTCAGCTGATGATCAGCTTAACCGCTGCGGTATCTTAAAGATCCCGGATCAGATCCCGGAGCGTTATGTTACAGCACCCT"

    decoded_result=rotarydecode(dna_str2)
    print(decoded_result)
