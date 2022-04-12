#encoding=utf-8
"""
Author:renyubin
Datetime:20201212
Function:The main frame of text editing.
"""
from tools.filetools import FileTools
from Multi_Huffman.huffencoder import huffencode
from Multi_Huffman.huffdecoder import huffdecode
from Rotarycode.rotaryencoder import rotaryencode
from Rotarycode.rotarydecoder import rotarydecode
from text_editor.genalign import genalign
from os import path
import pandas as pd


def huffman_encode(bytefragment_list):
    huff_codewords_list = []
    huff_freq_dics = []
    for bytefragment in bytefragment_list:
        codewords, char_freq = huffencode(bytefragment)
        huff_codewords_list.append(codewords)
        huff_freq_dics.append(char_freq)
    return huff_codewords_list,huff_freq_dics

def rotary_encode(huff_codewords_list):
    rotary_codewords_list=[]
    for i in huff_codewords_list:
        rotary_codewords=rotaryencode(i)
        print(rotary_codewords)
        print(len(rotary_codewords))
        rotary_codewords_list.append(rotary_codewords)
    return rotary_codewords_list

def dna_store(dna_fragments,encoded_result_file):
    store_dic = {"dna_fragments": dna_fragments}
    store_df = pd.DataFrame(store_dic)
    for index, row in store_df['dna_fragments'].iteritems():
        store_df.loc[index, "length"] = len(row)
    # logging.info(store_df[['dna_fragments', 'length']])
    store_df.to_csv(encoded_result_file)

def evalue_efficiency(file_size,dna_fragments):
    total_dna = ''
    for fragment in dna_fragments:
        total_dna += fragment
    encoded_rate = file_size * 8 / len(total_dna)
    print("Coding rate is {}.".format(encoded_rate))

def rotary_decode(rotary_codewords_list):
    rotary_decoded_result = []
    for rotary_codeword in rotary_codewords_list:
        decoded_list = rotarydecode(rotary_codeword)
        rotary_decoded_result.append(decoded_list)
    return rotary_decoded_result

def huffman_decode(rotary_decoded_result,huff_freq_dics):
    huff_decoded_bytefragments=[]
    for rotary_codeword,freq_dic in zip(rotary_decoded_result,huff_freq_dics):
        huff_decoded_bytefragment=huffdecode(rotary_codeword,freq_dic)
        huff_decoded_bytefragments+=huff_decoded_bytefragment
    return huff_decoded_bytefragments

def main():
    input_file="test_file/symbol"
    encoded_result_file=path.splitext(input_file)[0]+"_encoded_result.csv"
    decoded_file=path.splitext(input_file)[0]+"_decoded"+path.splitext(input_file)[1]
    # The length of the recognition sequence before or after the crisper modification site
    identity_base_num = 24
    # The parameters of the file segmentation
    seg_parameter = 200

    file_tool=FileTools(seg_parameter)
    file_size = file_tool.get_file_size(input_file)
    print("The size of initial file is :{}".format(file_size))
    bytefragment_list=file_tool.read(input_file)

    #Convert the byte to the corresponding binary sequence
    bin_list=[format(x,'08b') for x in bytefragment_list[0]]

    #1.huffman encoding
    huff_codewords_list,huff_freq_dics=huffman_encode(bytefragment_list)
    #2.rotary encoding
    rotary_codewords_list=rotary_encode(huff_codewords_list)

    # 3.sequence alignment
    genalign(encoded_result_file,rotary_codewords_list,identity_base_num)

    #4.storing DNA coding sequence
    dna_store(rotary_codewords_list,encoded_result_file)
    #5.calculate the coding rate
    evalue_efficiency(file_size,rotary_codewords_list)

    #6.read the DNA coding sequence
    df=pd.read_csv(encoded_result_file)
    dna_fragments=df['dna_fragments'].values

    #7.rotary decoding
    rotary_decoded_result=rotary_decode(dna_fragments)

    #8.huffman decoding
    huff_decoded_bytefragments=huffman_decode(rotary_decoded_result, huff_freq_dics)
    file_tool.write(decoded_file,huff_decoded_bytefragments)

if __name__=="__main__":
    main()
