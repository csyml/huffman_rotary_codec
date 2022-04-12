# encoding=utf-8
"""
author:renyubin
date:20201212
function: 2 symbols rotary coe
"""

pre_nucleotides = ["AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT"]
map_dit = {0: ["AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA"],
           1: ["AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC"],
           2: ["AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG"],
           3: ["CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT"],
           4: ["CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA"],
           5: ["CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC"],
           6: ["CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG"],
           7: ["GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT"],
           8: ["GC", "GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA"],
           9: ["GG", "GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC"],
           10: ["GT", "TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG"],
           11: ["TA", "TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT"],
           12: ["TC", "TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA"],
           13: ["TG", "TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC"],
           14: ["TT", "AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG"]
           }
