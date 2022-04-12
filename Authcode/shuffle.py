#encoding=-utf-8
"""
author:renyubin
function:string reversible shuffle
datetime:20200112
"""
import random
class Shuffle:

    def get_shuffle_exc(self,size,key):
        exchanges=['']*(size-1)
        random.seed(key)
        for i in range(1,size)[::-1]:
            n = random.randint(0, i+1)
            exchanges[size-1-i]=n
        return exchanges

    def shuffle(self,src_str,key):
        size=len(src_str)
        chars=[s for s in src_str]
        exchanges=self.get_shuffle_exc(size,key)
        for i in range(1,size)[::-1]:
            n=exchanges[size-1-i]
            tmp_char=chars[i]
            chars[i]=chars[n]
            chars[n]=tmp_char
        return "".join(chars)

    def deshuffle(self,shuffled_str,key):
        size=len(shuffled_str)
        chars=[s for s in shuffled_str]
        exchanges=self.get_shuffle_exc(size,key)
        for i in range(1,size):
            n=exchanges[size-i-1]
            tmp_char=chars[i]
            chars[i]=chars[n]
            chars[n]=tmp_char
        return "".join(chars)

if __name__=="__main__":
    src_str="CGACGACGA"
    shuffe=Shuffle()
    shuffed_str=shuffe.shuffle(src_str,123)
    deshuffed=shuffe.deshuffle(shuffed_str,123)
    print(shuffed_str)
    print(deshuffed)