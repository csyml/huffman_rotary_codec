#encoding=utf-8
"""
author:renyubin
date:20201210
function:huffman encoding

"""
from Multi_Huffman.huffman import *
import copy
def huffencode(bytefragment):
    """
    function:huffman encode
    :param bytefragment_list
    :return:
    """
    # Count the frequency of ASCII value of byte
    if bytefragment==[]:
        return [],{}

    char_freq={}
    bytes=[]
    for i in range(len(bytefragment)):
        byte=bytefragment[i]
        bytes.append(byte)
        if byte in char_freq.keys():
            char_freq[byte]+=1
        else:
            char_freq[byte]=1
    # print("bytes:{}".format(bytes))
    #print the statistics result
    # for byte in char_freq.keys():
    #     print("{}:{}".format(byte,char_freq[byte]))

    char_weight = copy.deepcopy(char_freq)
    # print("char_weight:{}".format(char_weight))
    #build the array of huffman tree for the huffman encode
    hufftrees_list=[] #huffman trees list
    for symbol in char_weight.keys():
        tem_tree=HuffTree(0,symbol,char_weight[symbol],None,None,None
                          ,None,None,None,None,None,None,None,None
                          ,None,None,None,None)
        hufftrees_list.append(tem_tree)
    # start the huffman encode and count the leaf node number
    leaf_node_num=len(char_weight.keys())
    #build the huffman tree,and acquire the huffman code for source symbol
    hufftree=build_huff_tree(hufftrees_list,len(char_weight.keys()))
    # print(hufftree)
    hufftree.recursive_trav_tree(hufftree.get_root(),char_weight,[])

    # huffman encode
    codewords=[]
    for i in range(len(bytefragment)):
        key=bytefragment[i]
        codewords+=char_weight[key]

    return codewords,char_freq



