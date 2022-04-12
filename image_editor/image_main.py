#encoding=utf-8
"""
Author:renyubin
Datetime:20201212
Function:The main frame of image editing.
"""
from tools.filetools import FileTools
from Multi_Huffman.huffencoder import huffencode
from Multi_Huffman.huffdecoder import huffdecode
from Rotarycode.rotaryencoder import rotaryencode
from Rotarycode.rotarydecoder import rotarydecode
from image_editor.genalign import genalign
from os import path
import pandas as pd
from image_editor.image_edit import modify_color



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


def store_result(target_file,byte_fragment_lens,dna_fragments):
    store_dic = {"byte_fragment_lens":byte_fragment_lens,"dna_fragments": dna_fragments}
    store_df = pd.DataFrame(store_dic)
    for index, row in store_df['dna_fragments'].iteritems():
        store_df.loc[index, "dna_length"] = len(row)
    # logging.info(store_df[['dna_fragments', 'length']])
    store_df.to_csv(target_file)


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
    huff_decoded_bytefragments=bytes()
    for rotary_codeword,freq_dic in zip(rotary_decoded_result,huff_freq_dics):
        huff_decoded_bytefragment=huffdecode(rotary_codeword,freq_dic)
        huff_decoded_bytefragments+=huff_decoded_bytefragment
    return huff_decoded_bytefragments

def main():
    # The length of the recognition sequence before or after the crisper modification site
    identity_base_num = 24
    # The parameters of the file segmentation
    seg_parameter = 2000
    file_tool = FileTools(seg_parameter)
    init_img = "img_file/apple.bmp"
    modify_img = path.splitext(init_img)[0] + "_modify" + path.splitext(init_img)[1]
    # modify_img="img_file2/red_app.bmp"
    #image editing
    color_green = [60, 255, 124]
    modify_color(init_img, modify_img, color_green)

    # encoding the initial image
    init_encoded_result_file=path.splitext(init_img)[0]+"_encoded_result.csv"
    init_decoded_file=path.splitext(init_img)[0]+"_decoded"+path.splitext(init_img)[1]
    init_file_size = file_tool.get_file_size(init_img)
    print("The file size is :{}".format(init_file_size))
    init_bytefragment_list=file_tool.read(init_img)
    init_bytefragment_lens=[len(x) for x in init_bytefragment_list]
    init_huff_codewords_list,init_huff_freq_dics=huffman_encode(init_bytefragment_list)
    init_rotary_codewords_list=rotary_encode(init_huff_codewords_list)
    # store_result(init_encoded_result_file,init_bytefragment_lens,init_rotary_codewords_list)
    # calculate the coding rate
    evalue_efficiency(init_file_size, init_rotary_codewords_list)
    #encoding the image modified
    modify_encoded_result_file=path.splitext(modify_img)[0]+"_encoded_result.csv"
    modify_decoded_file=path.splitext(modify_img)[0]+"_decoded"+path.splitext(modify_img)[1]
    modify_file_size = file_tool.get_file_size(modify_img)
    print("The file size is :{}".format(modify_file_size))
    modify_bytefragment_list=file_tool.read(modify_img)
    modify_bytefragment_lens=[len(x) for x in modify_bytefragment_list]
    modify_huff_codewords_list,modify_huff_freq_dics=huffman_encode(modify_bytefragment_list)
    modify_rotary_codewords_list=rotary_encode(modify_huff_codewords_list)
    store_result(modify_encoded_result_file, modify_bytefragment_lens, modify_rotary_codewords_list)
    # calculate the coding rate
    evalue_efficiency(modify_file_size, modify_rotary_codewords_list)

    # 3.sequence alignment
    genalign(init_encoded_result_file,modify_encoded_result_file,identity_base_num)

    #4.decoding the initial image
    initdf=pd.read_csv(init_encoded_result_file)
    init_dna_fragments=initdf['dna_fragments'].values
    rotary_decoded_result=rotary_decode(init_dna_fragments)
    huff_decoded_bytefragments=huffman_decode(rotary_decoded_result, init_huff_freq_dics)
    file_tool.write(init_decoded_file,huff_decoded_bytefragments)

    #5.decoding the image modified
    modifydf=pd.read_csv(modify_encoded_result_file)
    modify_dna_fragments=modifydf['dna_fragments'].values
    rotary_decoded_result=rotary_decode(modify_dna_fragments)
    huff_decoded_bytefragments=huffman_decode(rotary_decoded_result, modify_huff_freq_dics)
    file_tool.write(modify_decoded_file,huff_decoded_bytefragments)


if __name__=="__main__":
    main()
