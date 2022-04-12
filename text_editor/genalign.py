#encoding=utf-8
"""
Author:renyubin
datetime:20200122
function:sequence alignment
"""
import logging
import pandas as pd
from tools.stringcmp import stringcmp
import os

def genalign(pre_modify_file,current_dna_fragments,identity_base_num):
    # compare the contents before and after the file modification to determine the modified DNA sequence
    if os.path.exists(pre_modify_file) and os.path.getsize(pre_modify_file) :
        df1 = pd.read_csv(pre_modify_file)
        pre_file_dna_fragments = list(df1['dna_fragments'].values)
        # modifying the content of the file will only change the local bases of the encoded DNA strand.
        if len(pre_file_dna_fragments) == len(current_dna_fragments):
            # obtain the index of the DNA strand whose base has changed
            changed_indexs = [pre_file_dna_fragments.index(i) for i, j in zip(pre_file_dna_fragments, current_dna_fragments) if i != j and isinstance(i,str) and isinstance(j,str)]
            for i in changed_indexs:
                left_identity_bases, before_modify_part, after_modify_part, right_identity_bases = stringcmp( pre_file_dna_fragments[i], current_dna_fragments[i], identity_base_num)
                logging.info("The original sequence of the [{}] chain: [{}] is modified to: [{}].".format(i, pre_file_dna_fragments[i], current_dna_fragments[i]))
                logging.info("[{}]chain:[{}]--->[{}],{}recognition bases before modification site: [{}], {} recognition bases after modification site:[{}].".format(i, before_modify_part,
                                                                                                after_modify_part,
                                                                                                identity_base_num,
                                                                                                left_identity_bases,
                                                                                                identity_base_num,
                                                                                                right_identity_bases))
        # The modification of the content will lead to the increase of DNA strands and the internal change of some DNA strands.
        elif len(pre_file_dna_fragments) < len(current_dna_fragments):
            # DNA strand added after modification
            add_dna_fragments = [fragment for fragment in current_dna_fragments if fragment not in pre_file_dna_fragments]
            logging.info("DNA coding strand added:{}.".format(add_dna_fragments))
            # the index of the added DNA,the index is based on final_dna_fragments
            add_dna_fragments_index = [current_dna_fragments.index(add_dna_fragment) for add_dna_fragment in
                                       add_dna_fragments]
            # DNA strand unchanged
            not_add_dna_fragments = [x for x in current_dna_fragments if current_dna_fragments.index(x) not in add_dna_fragments_index]
            # The local base changes of the DNA chain, the index is based on pre_file_dna_fragments
            changed_indexs = [pre_file_dna_fragments.index(i) for i, j in zip(pre_file_dna_fragments, not_add_dna_fragments) if i != j and isinstance(i,str) and isinstance(j,str)]
            for i in changed_indexs:
                left_identity_bases, before_modify_part, after_modify_part, right_identity_bases = stringcmp(pre_file_dna_fragments[i], not_add_dna_fragments[i], identity_base_num)
                logging.info("[{}]chain:[{}]--->[{}],{}recognition bases before modification site: [{}], {} recognition bases after modification site:[{}].".format(i, before_modify_part,
                                                                                                after_modify_part,
                                                                                                identity_base_num,
                                                                                                left_identity_bases,
                                                                                                identity_base_num,
                                                                                                right_identity_bases))

        # The modification of the content will lead to the reduction of the DNA chain and the internal change of some DNA chains
        elif len(pre_file_dna_fragments) > len(current_dna_fragments):
            #  DNA strand reduced after modification
            decrease_dna_fragments = [fragment for fragment in pre_file_dna_fragments if fragment not in current_dna_fragments]
            logging.info("DNA strand reduced:{}.".format(decrease_dna_fragments))
            # Determine the index of the reduced DNA strand
            decrease_dna_fragments_index = [pre_file_dna_fragments.index(decrease_dna_fragment) for decrease_dna_fragment in decrease_dna_fragments]
            # Determine unchanged DNA strand index
            not_decreased_dna_fragments = [x for x in pre_file_dna_fragments if pre_file_dna_fragments.index(x) not in decrease_dna_fragments_index]
            changed_indexs = [current_dna_fragments.index(i) for i, j in zip(not_decreased_dna_fragments, current_dna_fragments) if i != j and isinstance(i,str) and isinstance(j,str)]
            for i in changed_indexs:
                left_identity_bases, before_modify_part, after_modify_part, right_identity_bases = stringcmp( not_decreased_dna_fragments[i], current_dna_fragments[i], identity_base_num)
                logging.info("[{}]chain:[{}]--->[{}],{}recognition bases before modification site: [{}], {} recognition bases after modification site:[{}].".format(i, before_modify_part,
                                                                                                after_modify_part,
                                                                                                identity_base_num,
                                                                                                left_identity_bases,
                                                                                                identity_base_num,
                                                                                                right_identity_bases))

if __name__=="__main__":
    pre_modify_file= "test_file/eternity_and_a_Day_encoded_result.csv"
    aft_modify_file= "test_file/reverse_eternity_encoded_result.csv"
    identity_base_num=24
    genalign(pre_modify_file, aft_modify_file, identity_base_num)
