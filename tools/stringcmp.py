# encoding=utf-8
import numpy as np
def stringcmp(str1, str2,identity_base_num=0):
    """
    功能：从字符串的两端出发进行字符串的比较，查找出修改后的位置及内容
    :param str1: 修改之前的字符串
    :param str2: 修改之后的字符串
    :return:left_identity_bases(左侧识别碱基序列）,before_modify_part（修改之前的部分），
            after_modify_part(修改之后的部分）,right_identity_bases（右侧识别碱基序列）
    """
    left_index=0
    right_index=0
    for i,j in zip(str1,str2):
        if i!=j:
            break
        left_index += 1
    for i,j in zip(str1[::-1],str2[::-1]):
        if i!=j:
            break
        right_index += 1
    before_modify_part=str1[left_index:len(str1)-right_index]
    after_modify_part=str2[left_index:len(str2)-right_index]

    #获取修改位点两侧二十多个碱基序列用于crisper的碱基识别
    left_identity_bases=''
    if identity_base_num<left_index:
        left_identity_bases=str1[left_index-identity_base_num:left_index]
    else:
        left_identity_bases=str1[:left_index]

    right_identity_bases=''
    if identity_base_num<len(str1)-right_index:
        right_identity_bases=str1[len(str1)-right_index:len(str1)-right_index+identity_base_num]
    else:
        right_identity_bases=str1[len(str1)-right_index:]
    return left_identity_bases,before_modify_part,after_modify_part,right_identity_bases


if __name__ == "__main__":
    str1 = "ATATATATATATCATATATATAAA"
    str2 = "ATATATATATATAAAAATATATATAAA"
    identity_base_num=3
    left_identity_bases,before_modify_part,after_modify_part,right_identity_bases=stringcmp(str1, str2,identity_base_num)
    print("left_identity_bases:{}".format(left_identity_bases))
    print("before_modify_part:{}".format(before_modify_part))
    print("after_modify_part:{}".format(after_modify_part))
    print("right_identity_bases:{}".format(right_identity_bases))
