#coding=utf-8
"""
Datetime:20210214
Author:renyubin
function:The sequencing results were compared with the coding sequences.
The missing base was filled with specific bases to make the length of the
sequencing results consistent with the length of coding sequence.
"""

def pre_format(coding_seq,sequenced_seq):
    coding_seq_len=len(coding_seq)
    sequenced_seq_len=len(sequenced_seq)
    left_index = 0
    right_index = 0
    #determine the position of the missing bases
    if coding_seq_len!=sequenced_seq_len:
        for i,j in zip(coding_seq,sequenced_seq):
            if i!=j:
                break
            left_index += 1
        for i,j in zip(coding_seq[::-1],sequenced_seq[::-1]):
            if i!=j:
                break
            right_index += 1

        #确定缺失位置及长度
        missing_len=coding_seq_len-right_index-left_index
        #进行填充
        filled_seq=sequenced_seq[:left_index]+"A"*missing_len+sequenced_seq[-right_index:]
        return filled_seq

    else:
        if coding_seq==sequenced_seq:
            print("equal sequence!")
        else:
            print("only equal length!")


if __name__=="__main__":
    symbol_seq="TGTCGTGGGACTCCCAAGTGGTGCGAATCAATTGAATTGGTCTAGGCGATACAAGTTTTGGCTGTCGATGTCGTCTCAAGACTACGACGAATTCGAAAGTCCAAGCGACGAGTTTCTAGGGCCTCGCAATACTCGG"
    squenced_seq="TGTCGTGGGACTCCCAAGTGGTGCGAATCAATTGAATTGGTCTAGGCGATACAAGTTTTGGCTGTCGATGTCGTCTCAAGACTACGACGACTAGTACTTTTGGCATTGCTCGCAAATCGTGGGACTCCCAAGACTTGTGA"

    filled_seq=pre_format(symbol_seq,squenced_seq)
    print("The filled sequence of the sequenced sequence with missing bases:{}.".format(filled_seq))
