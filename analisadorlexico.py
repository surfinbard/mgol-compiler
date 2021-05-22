import os.path
from typing import List
import numpy as np
from copy import deepcopy

i, j, cont = 0, 0, 0
ponteiro, contador_coluna, contador_linha, final_arquivo = 0, 0, 0, 0
palavra = ""
a = ""
retorno = ""

#          P' P    V    A    LV   D    L   TIPO ES   ARG  CMD  LD   OPRD COND CAB EXP_R CP   R    CP_R
GOTO = [[None,1   ,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #00
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #01
        [None,None,3   ,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #02
        [None,None,None,5   ,None,None,None,None,6   ,None,7   ,None,None,8   ,14  ,None, None,9  ,None], #03
        [None,None,None,None,17  ,18  ,None,20  ,None,None,None,None,None,None,None,None,None,None,None], #04
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #05
        [None,None,None,22  ,None,None,None,None,6   ,None,7   ,None,None,8   ,14  ,None,None,9   ,None], #06
        [None,None,None,23  ,None,None,None,None,6   ,None,7   ,None,None,8   ,14  ,None,None,9   ,None], #07
        [None,None,None,24  ,None,None,None,None,6   ,None,7   ,None,None,8   ,14  ,None,None,9   ,None], #08
        [None,None,None,25  ,None,None,None,None,6   ,None,7   ,None,None,8   ,14  ,None,None,9   ,None], #09
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #10
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #11
        [None,None,None,None,None,None,None,None,None,27  ,None,None,None,None,None,None,None,None,None], #12
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #13
        [None,None,None,None,None,None,None,None,33  ,None,34  ,None,None,35  ,14  ,None,32  ,None,None], #14
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #15
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #16
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #17
        [None,None,None,None,39  ,18  ,None,20  ,None,None,None,None,None,None,None,None,None,None,None], #18
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #19
        [None,None,None,None,None,None,41  ,None,None,None,None,None,None,None,None,None,None,None,None], #20
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #21
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #22
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #23
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #24
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #25
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #26
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #27
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #28
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #29
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #30
        [None,None,None,None,None,None,None,None,None,None,None,48  ,49  ,None,None,None,None,None,None], #31
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #32
        [None,None,None,None,None,None,None,None,33  ,None,34  ,None,None,35  ,14  ,None,52  ,None,None], #33
        [None,None,None,None,None,None,None,None,33  ,None,34  ,None,None,35  ,14  ,None,53  ,None,None], #34
        [None,None,None,None,None,None,None,None,33  ,None,34  ,None,None,35  ,14  ,None,54  ,None,None], #35
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #36
        [None,None,None,None,None,None,None,None,None,None,None,None,56  ,None,None,55  ,None,None,None], #37
        [None,None,None,None,None,None,None,None,None,None,None,None,56  ,None,None,57  ,None,None,None], #38
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #39
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #40
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #41
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #42
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #43
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #44
        [None,None,None,None,None,None,59  ,None,None,None,None,None,None,None,None,None,None,None,None], #45
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #46
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #47
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #48
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #49
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #50
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #51
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #52
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #53
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #54
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #55
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #56
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #57
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #58
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #59
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #60
        [None,None,None,None,None,None,None,None,None,None,None,None,65  ,None,None,None,None,None,None], #61
        [None,None,None,None,None,None,None,None,67  ,None,68  ,None,None,69  ,14  ,None,None,None,66  ], #62
        [None,None,None,None,None,None,None,None,None,None,None,None,71  ,None,None,None,None,None,None], #63
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #64
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #65
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #66
        [None,None,None,None,None,None,None,None,67  ,None,68  ,None,None,69  ,14  ,None,None,None,73  ], #67
        [None,None,None,None,None,None,None,None,67  ,None,68  ,None,None,69  ,14  ,None,None,None,74  ], #68
        [None,None,None,None,None,None,None,None,67  ,None,68  ,None,None,69  ,14  ,None,None,None,75  ], #69
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #70
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #71
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #72
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #73
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None], #74
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]] #75

            #inicio varinicio varfim int real lit leia escreva literal se entao fimse facaate fimfaca fim num id opr RCB OPM AB_P (	FC_P ) PT_V ; Vir , $
ACTION =   [['S2','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0','E0'], #0
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','Acc','E1','E1','E1','E1','E1'], #1
            ['E2','S4','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2','E2'], #2
            ['E3','E3','E3','E3','E3','E3','S11','S12','E3','S16','E3','E3','S15','E3','S10','E3','S13','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #3 
            ['E4','E4','S19','S42','S43','S44','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4'], #4
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','R2','E1','E1','E1','E1','E1'], #5
            ['E3','E3','E3','E3','E3','E3','S11','S12','E3','S16','E3','E3','S15','E3','S10','E3','S13','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #6                      
            ['E3','E3','E3','E3','E3','E3','S11','S12','E3','S16','E3','E3','S15','E3','S10','E3','S13','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #7
            ['E3','E3','E3','E3','E3','E3','S11','S12','E3','S16','E3','E3','S15','E3','S10','E3','S13','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #8
            ['E3','E3','E3','E3','E3','E3','S11','S12','E3','S16','E3','E3','S15','E3','S10','E3','S13','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #9
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','R38','E1','E1','E1','E1','E1'], #10
            ['E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','S26','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'], #11
            ['E6','E6','E6','E6','E6','E6','E6','E6','S28','E6','E6','E6','E6','E6','E6','S29','S30','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6','E6'], #12
            ['E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','S31','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7','E7'], #13
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','S36','E8','E8','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #14
            ['E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E','S37','E9','E9','E9','E9','E9','E9','E9','E9','E9'], #15
            ['E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E9','E','S38','E9','E9','E9','E9','E9','E9','E9','E9','E9'], #16
            ['E3','E3','E3','E3','E3','E3','R3','R3','E3','R3','E3','E3','R3','E3','R3','E3','R3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #17
            ['E4','E4','S19','S42','S43','S44','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4''E4','E4','E4','E4','E4'], #18
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','S40','E10','E10','E10','E10','E10','E10','E10'], #19
            ['E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','S21','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'], #20
            ['E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','E11','R8','S45','E11','E11','E11','E11','E11','E11','E11'], #21
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','R12','E1','E1','E1','E1','E1'], #22
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','R18','E1','E1','E1','E1','E1'], #23
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','R24','E1','E1','E1','E1','E1'], #24
            ['E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','R32','E1','E1','E1','E1','E1'], #25
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','S46','E10','E10','E10','E10','E10','E10','E10'], #26
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','S47','E10','E10','E10','E10','E10','E10','E10'], #27
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','R15','E10','E10','E10','E10','E10','E10','E10'], #28
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','R16','E10','E10','E10','E10','E10','E10','E10'], #29
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','R17','E10','E10','E10','E10','E10','E10','E10'], #30
            ['E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','S51','S50','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12'], #31
            ['E17','E17','E17','E17','E17','E17','R25','R25','E17','R25','E17','R25','R25','R25','R25','E17','R25','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #32
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','S36','E8','E8','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #33
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','S36','E8','E8','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #34
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','S36','E8','E8','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #35
            ['E17','E17','E17','E17','E17','E7','R31','R31','E17','R31','E17','R31','R31','R31','R31','E17','R31','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #36
            ['E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','S51','S50','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12'], #37
            ['E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','S51','S50','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12'], #38
            ['E3','E3','E3','E3','E3','E3','R4','R4','E3','R4','E3','E3','R4','E3','R4','R4','R4','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #39
            ['E3','E3','E3','E3','E3','E3','R5','R5','E3','R5','E3','E3','R5','E3','R5','R5','R5','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #40
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','S58','E10','E10','E10','E10','E10','E10','E10'], #41
            ['E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','R9','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'], #42
            ['E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','R10','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'], #43
            ['E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','R11','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'], #44
            ['E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','S21','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5','E5'], #45
            ['E17','E17','E17','E17','E17','E17','R13','R13','E17','R13','E17','R13','R13','R13','R13','E17','R13','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #46
            ['E17','E17','E17','E17','E17','E17','R14','R14','E17','R14','E17','R14','R14','R14','R14','E17','R14','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #47
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','S60','E10','E10','E10','E10','E10','E10','E10'], #48
            ['E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','E18','S61','E18','E18','R21','E18','E18','E18','E18','E18','E18','E18'], #49
            ['E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','R22','E19','R22','E19','R22','R22','E19','E19','E19','E19','E19','E19','E19'], #50
            ['E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','E19','R23','E19','R23','E19','R23','R23','E19','E19','E19','E19','E19','E19','E19'], #51
            ['E17','E17','E17','E17','E17','E17','R28','R28','E17','R28','E17','R28','R28','R28','R28','E17','R28','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #52
            ['E17','E17','E17','E17','E17','E17','R29','R29','E17','R29','E17','R29','R29','R29','R29','E17','R29','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #53
            ['E17','E17','E17','E17','E17','E17','R30','R30','E17','R30','E17','R30','R30','R30','R30','E17','R30','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #54
            ['E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','S62','E14','E14','E14','E14','E14','E14','E14','E14'], #55
            ['E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','S63','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15','E15'], #56
            ['E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','S64','E14','E14','E14','E14','E14','E14','E14','E14'], #57
            ['E4','E4','R6','R6','R6','R6','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4','E4'], #58
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','R7','E10','E10','E10','E10','E10','E10','E10'], #59
            ['E17','E17','E17','E17','E17','E17','R19','R19','E17','R19','E17','R19','R19','R19','R19','E17','R19','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17','E17'], #60
            ['E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','S51','S50','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12'], #61
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','E8','E8','S70','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #62
            ['E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','S51','S50','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12','E12'], #63
            ['E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','S72','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16','E16'], #64
            ['E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','E10','R20','E10','E10','E10'], #65
            ['E3','E3','E3','E3','E3','E3','R33','R33','E3','R33','E3','E3','R33','E3','R33','E3','R33','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #66
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','E8','E8','S70','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #67
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','E8','E8','S70','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #68
            ['E8','E8','E8','E8','E8','E8','S11','S12','E8','S16','E8','E8','E8','S70','E8','E8','S13','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #69
            ['E3','E3','E3','E3','E3','E3','R37','R37','E3','R37','E3','E3','R37','E3','R37','E3','R37','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #70
            ['E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','E14','R27','E14','E14','E14','E14','E14','E14','E14','E14'], #71
            ['E8','E8','E8','E8','E8','E8','R26','R26','E8','R26','E8','R26','E8','E8','E8','E8','R26','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8','E8'], #72
            ['E3','E3','E3','E3','E3','E3','R34','R34','E3','R34','E3','E3','R34','E3','R34','E3','R34','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #73
            ['E3','E3','E3','E3','E3','E3','R35','R35','E3','R35','E3','E3','R35','E3','R35','E3','R35','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3'], #74
            ['E3','E3','E3','E3','E3','E3','R36','R36','E3','R36','E3','E3','R36','E3','R36','E3','R36','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3','E3']] #75


terminais = [['inicio', 0],
             ['varinicio', 1],
             ['varfim', 2],
             ['inteiro', 3],
             ['real', 4],
             ['lit', 5],
             ['leia', 6],
             ['escreva', 7],
             ['literal', 8],
             ['se', 9],
             ['entao', 10],
             ['fimse', 11],
             ['facaate', 12],
             ['fimfaca', 13],
             ['fim', 14],
             ['num', 15],
             ['id', 16],
             ['opr', 17],
             ['rcb', 18],
             ['opm', 19],
             ['AB_P', 20],
             ['FC_P', 21],
             ['PT_V', 22],
             ['vir', 23],
             ['$', 24],
             ['ERRO1', 25],
             ['ERRO2', 26],
             ['ERRO3', 27],
             ['ERRO4', 28],
             ['ERRO5', 29],]

naoTerminais = [["P'", 0],
                ['P', 1],
                ['V', 2],
                ['A', 3],
                ['LV', 4],
                ['D', 5],
                ['L', 6],
                ['TIPO', 7],
                ['ES', 8],
                ['ARG', 9],
                ['CMD', 10],
                ['LD', 11],
                ['OPRD', 12],
                ['COND', 13],
                ['CAB', 14],
                ['EXP_R', 15],
                ['CP', 16],
                ['R', 17],
                ['CP_R', 18]]

gramatica =    [[],
                ["P'", "->", "P"],
                ["P", "->", "inicio", "V", "A"],
                ["V", "->", "varinicio", "LV"],
                ["LV", "->", "D", "LV"],
                ["LV", "->", "varfim", ";"],
                ["D", "->", "TIPO", "L", ";"],
                ["L", "->", "id", ",", "L"],
                ["L", "->", "id"],
                ["TIPO", "->", "inteiro"],
                ["TIPO", "->", "real"],
                ["TIPO", "->", "lit"],
                ["A", "->", "ES", "A"],
                ["ES", "->", "leia", "id", ";"],
                ["ES", "->", "escreva", "ARG", ";"],
                ["ARG", "->", "literal"],
                ["ARG", "->", "num"],
                ["ARG", "->", "id"],
                ["A", "->", "CMD", "A"],
                ["CMD", "->", "id", "RCB", "LD", ";"],
                ["LD", "->", "OPRD", "opm", "OPRD"],
                ["LD", "->", "OPRD"],
                ["OPRD", "->", "id"],
                ["OPRD", "->", "num"],
                ["A", "->", "COND",  "A"],
                ["COND", "->", "CAB", "CP"],
                ["CAB", "->", "se", "(", "EXP_R", ")", "entao"],
                ["EXP_R", "->", "OPRD", "opr", "OPRD"],
                ["CP", "->", "ES", "CP"],
                ["CP", "->", "CMD", "CP"],
                ["CP", "->", "COND", "CP"],
                ["CP", "->", "fimse"],
                ["A", "->", "R", "A"],
                ["R", "->", "facaAte", "(", "EXP_R", ")", "CP_R"],
                ["CP_R", "->", "ES", "CP_R"],
                ["CP_R", "->", "CMD", "CP_R"],
                ["CP_R", "->", "COND", "CP_R"],
                ["CP_R", "->", "fimFaca"],
                ["A", "->", "fim"]]

especificacaoErro = [["espera ser inserido 'inicio'"],                                                                                                  #erro 00 estado 00                               
                    ["esperava ser inserido '$'"],                                                                                                      #erro 01 estado 01, 05, 10, 24, 25, 26, 27
                    ["esperava ser inserido 'varinicio'"],                                                                                              #erro 02 estado 02
                    ["esperava ser inserido 'leia' ou 'escreva' ou  'id' ou 'se' ou 'facaate' ou 'fim'"],                                               #erro 03 estado 03, 06, 07, 08, 09 
                    ["esperava ser inserido 'varfim' ou 'inteiro' ou 'real' ou 'lit'"],                                                                 #erro 04 estado 04
                    ["esperava ser inserido 'id'"],                                                                                                     #erro 05 estado 11
                    ["esperava ser inserido 'literal' ou 'num' ou 'id'"],                                                                               #erro 06 estado 12
                    ["Esperava ser inserido '<-' (atribuição)"],                                                                                        #erro 07 estado 13
                    ["Esperava ser inserido 'leia' ou 'escreva' ou 'se' ou 'fimse' ou 'id'"],                                                           #erro 08 estado 14, 33, 34, 35, 62, 67, 68, 69
                    ["Esperava ser inserido '(' (abre parênteses)"],                                                                                    #erro 09 estado 15, 16
                    ["Esperava ser inserido ';' (ponto e vírgula)"],                                                                                    #erro 10 estado 19, 26, 27, 28, 29, 30, 41, 48
                    ["Esperava ser inserido ',' (vírgula) ou ';' (ponto e vírgula)"],                                                                   #erro 11 estado 21
                    ["Esperava ser inserido 'num' ou 'id'"],                                                                                            #erro 12 estado 31, 37, 38, 61, 63
                    ["Esperava ser inserido operadores aritméticos ('+', '-', '*' ou '/')"],                                                            #erro 13 estado 49
                    ["Esperava ser inserido ')' (fecha parênteses)"],                                                                                   #erro 14 estado 55, 57, 71
                    ["Esperava ser inserido operadores relacionais ('<', '>', '<=', '>=', '=' ou '<>')"],                                               #erro 15 estado 56
                    ["Esperava ser inserido 'entao'"],                                                                                                  #erro 16 estado 64 
                    ["Esperava ser inserido 'leia' ou 'escreva' ou  'id' ou 'se' ou 'fimse' ou 'facaate' ou 'fimfaca' ou 'fim'"],                       #erro 17 estado 32, 36, 46, 47, 52, 53, 54, 60
                    ["Esperava ser inserido operadores aritméticos ou ';' (ponto e vírgula)"],                                                          #erro 18 estado 49
                    ["Esperava ser inserido operadores relacionais ou operadores aritméticos ou ')' (fecha parênteses) ou ';' (ponto e vírgula)"],      #erro 19 estado 50, 51  
                    []]                                                                                       

tabeladeERRO = [['inicio'],                                                               #erro 00 estado 00
               ['$'],                                                                     #erro 01 estado 01, 05, 10, 24, 25, 26, 27
               ['varinicio'],                                                             #erro 02 estado 02
               ['leia', 'escreva', 'id', 'se', 'facaate', 'fim'],                         #erro 03 estado 03, 06, 07, 08, 09, 17, 39, 40, 66, 70, 73, 74, 75 
               ['varfim', 'inteiro', 'real', 'lit'],                                      #erro 04 estado 04, 18           
               ['id'],                                                                    #erro 05 estado 11, 20
               ['literal', 'num', 'id'],                                                  #erro 06 estado 12
               ['rcb'],                                                                   #erro 07 estado 13
               ['leia', 'escreva', 'se', 'fimse', 'id'],                                  #erro 08 estado 14, 33, 34, 35, 62, 67, 68, 69
               ['AB_P'],                                                                  #erro 09 estado 15, 16
               ['PT_V'],                                                                  #erro 10 estado 19, 26, 27, 28, 29, 30, 41, 48
               ['PT_V','vir'],                                                            #erro 11 estado 21
               ['num', 'id'],                                                             #erro 12 estado 31, 37, 38, 61, 63
               ['opm'],                                                                   #erro 13 estado 49
               ['FC_P'],                                                                  #erro 14 estado 55, 57, 71
               ['opr'],                                                                   #erro 15 estado 56
               ['entao'],                                                                 #erro 16 estado 64
               ['leia', 'escreva', 'id', 'se','fimse', 'facaate', 'fimfaca', 'fim'],      #erro 17 estado 32, 36, 46, 47, 52, 53, 54, 60
               ['opm', 'PT_V'],                                                           #erro 18 estado 49
               ['opr', 'opm', 'FC_P', 'PT_V'],                                            #erro 19 estado 50, 51 
                []]                            


class lista:
    def __init__(self):
        self.raiz = None

    def push(self, classe, lexema, tipo):
 
        novo_token = token(classe = classe, lexema = lexema, tipo = tipo)
        if(self.raiz == None):
            self.raiz = novo_token
            return

        self.raiz.anterior = novo_token
        novo_token.proximo = self.raiz
        self.raiz = novo_token

    def procura_na_lista(self, lexema):
        temp = self.raiz
        while temp:
            if temp.lexema == lexema:
                break
            temp = temp.proximo
        if temp == None:
            return False
        return temp

class token:
    def __init__(self, proximo=None, anterior=None, classe=None, lexema=None, tipo=None):
        self.proximo = proximo
        self.anterior = anterior
        self.classe = classe
        self.lexema = lexema
        self.tipo = "Nulo"

class analisador:

    def __init__(self, l, tabela_simbolos):
        self.l = l
        self.tabela_simbolos = tabela_simbolos

    def coluna (self, valor):
        global contador_coluna
        
        if valor == 0:
            contador_coluna = 0
        if valor ==1:
            contador_coluna += 1
        else:
            contador_coluna = contador_coluna + valor

    def linha (self):
        global contador_linha
        
        contador_linha += 1

    def scanner(self, arquivo_fonte, l, tabela_simbolos): 
        global j 
        global ponteiro
        j = ponteiro
        return self.q0(arquivo_fonte, l, tabela_simbolos)

    def Operadores(self, arquivo_fonte): #verifica se é operador
        global ponteiro
        operadores = "= + - * / ! > <"
        if arquivo_fonte[ponteiro] in operadores:
            return True
        return False

    def Delimitadores(self, arquivo_fonte):#verifica se é delimitador
        global ponteiro
        operadores = "; , ( ) { } [ ]"
        if arquivo_fonte[ponteiro] in operadores:
            return True
        return False
    def Delimitadores_ABP(self, arquivo_fonte):#verifica se é delimitador para abra parênteses
        global ponteiro
        operadores = "( ) { } [ ]"
        if arquivo_fonte[ponteiro] in operadores:
            return True
        return False
    def q0(self, arquivo_fonte, l, tabela_simbolos):
        global ponteiro
        global j
        global contador_coluna

        if '\n' == arquivo_fonte[ponteiro]:
            ponteiro += 1
            j = ponteiro
            self.coluna(0)
            self.linha()
            return self.q0(arquivo_fonte, l, tabela_simbolos)
        if '\t' == arquivo_fonte[ponteiro]:
            print("cheguei")
            ponteiro += 1
            self.coluna(1)
            j = ponteiro
            return self.q0(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[ponteiro].isspace():
            ponteiro+= 1
            j = ponteiro
            self.coluna(1)
            return self.q0(arquivo_fonte, l, tabela_simbolos)
        if arquivo_fonte[ponteiro].isdigit(): 
            return self.q1(arquivo_fonte, l, tabela_simbolos)
        elif '"' == arquivo_fonte[ponteiro]:
            return self.q7(arquivo_fonte, l, tabela_simbolos)
        elif '{' == arquivo_fonte[ponteiro]:
            return self.q9(arquivo_fonte, l, tabela_simbolos)
        elif '<' == arquivo_fonte[ponteiro]:
            return self.q12(arquivo_fonte, l, tabela_simbolos)
        elif '=' == arquivo_fonte[ponteiro]:
            return self.q16(arquivo_fonte, l, tabela_simbolos)
        elif '>' == arquivo_fonte[ponteiro]:    
            return self.q17(arquivo_fonte, l, tabela_simbolos)
        elif '+' == arquivo_fonte[ponteiro] or '-' == arquivo_fonte[ponteiro] or '*' == arquivo_fonte[ponteiro] or '/' == arquivo_fonte[ponteiro]:
            return self.q19(arquivo_fonte, l, tabela_simbolos)
        elif '(' == arquivo_fonte[ponteiro]:
            return self.q20(arquivo_fonte, l, tabela_simbolos)
        elif ')' == arquivo_fonte[ponteiro]:
            return self.q21(arquivo_fonte, l, tabela_simbolos)
        elif ';' == arquivo_fonte[ponteiro]: 
            return self.q22(arquivo_fonte, l, tabela_simbolos)
        elif ',' == arquivo_fonte[ponteiro]:
            return self.q23(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[ponteiro].isalpha():
            return self.q11(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[ponteiro] == '$':
            return self.q25(arquivo_fonte, l, tabela_simbolos)
        else:
            return self.q24(1, arquivo_fonte, l)

    def q1(self, arquivo_fonte, l, tabela_simbolos): # retorno_scanner *num*
        global ponteiro
        global j
        global ponteiro
        global palavra

        ponteiro +=1
        self.coluna(1)        
        if arquivo_fonte[ponteiro].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[ponteiro]=='\n': 
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('num', palavra, 'Nulo')
            return self.l.procura_na_lista(palavra)        
        if arquivo_fonte[ponteiro].isdigit():
            return self.q1(arquivo_fonte, l, tabela_simbolos)
        elif '.' == arquivo_fonte[ponteiro]:
            return self.q2(arquivo_fonte, l, tabela_simbolos)
        elif 'e' == arquivo_fonte[ponteiro] or 'E' == arquivo_fonte[ponteiro]: 
            return self.q4(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4,arquivo_fonte, l) 

    def q2(self, arquivo_fonte, l, tabela_simbolos):  
        global j 
        global ponteiro
        ponteiro += 1
        self.coluna(1)        
        if arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro].isdigit():
            return self.q3(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)

    def q3(self, arquivo_fonte, l, tabela_simbolos): # retorno_scanner *num*
        global j 
        global ponteiro
        global palavra
        ponteiro += 1
        self.coluna(1)        
        if arquivo_fonte[ponteiro].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[ponteiro]=='\n': 
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('num', palavra, 'Nulo')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[ponteiro].isdigit():
            return self.q3(arquivo_fonte, l, tabela_simbolos)
        elif 'e' == arquivo_fonte[ponteiro] or 'E' == arquivo_fonte[ponteiro]: 
            return self.q4(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)
 
    def q4(self, arquivo_fonte, l, tabela_simbolos):
        global j 
        global ponteiro
       
        ponteiro += 1
        self.coluna(1)        
        if arquivo_fonte[ponteiro].isdigit():
            return self.q6(arquivo_fonte, l, tabela_simbolos)
        elif '+' == arquivo_fonte[ponteiro] or '-' == arquivo_fonte[ponteiro]: 
            return self.q5(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)


    def q5(self, arquivo_fonte, l, tabela_simbolos): 
        global j 
        global ponteiro
       
        ponteiro += 1
        self.coluna(1)        
        if arquivo_fonte[ponteiro].isdigit():
            return self.q6(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)

    def q6(self, arquivo_fonte, l, tabela_simbolos): # retorno_scanner *num*
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1
        self.coluna(1)        
        if arquivo_fonte[ponteiro].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[ponteiro]=='\n': 
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('num', palavra, 'Nulo')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[ponteiro].isdigit():
            return self.q6(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)

    def q7(self, arquivo_fonte, l, tabela_simbolos): #começa lit
        global j
        global ponteiro
        
        while arquivo_fonte[ponteiro] !="\n":
            ponteiro +=1
            self.coluna(1)
            if arquivo_fonte[ponteiro] == '"':
                return self.q8(arquivo_fonte, l, tabela_simbolos)
            return self.q7(arquivo_fonte, l, tabela_simbolos)
        return self.q24(2, arquivo_fonte, l)
    
    def q8(self, arquivo_fonte, l, tabela_simbolos): # retorno_scanner *lit*
        global j
        global ponteiro
        global palavra

        ponteiro += 1
        self.coluna(1)
        if arquivo_fonte[ponteiro].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte):
            palavra = arquivo_fonte[j:ponteiro] 
            if not self.l.procura_na_lista(palavra):
                l.push('literal', palavra, 'Nulo')
            return self.l.procura_na_lista(palavra)
        else:
            return self.q24(2, arquivo_fonte, l)

    def q9(self, arquivo_fonte, l, tabela_simbolos): #Abre { comentário
        global j
        global ponteiro
        
        while arquivo_fonte[ponteiro] !="\n":
            ponteiro += 1
            self.coluna(1)
            if arquivo_fonte[ponteiro] == '}':
                return self.q10(arquivo_fonte, l, tabela_simbolos)
        return self.q24(3, arquivo_fonte, l)

    def q10(self, arquivo_fonte, l, tabela_simbolos): # fecha } comentário
        global j
        global ponteiro
        
        ponteiro += 1
        self.coluna(1)
        return self.q0(arquivo_fonte, l, tabela_simbolos)

    def q11(self, arquivo_fonte, l, tabela_simbolos): # reconhece *id*
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1
        self.coluna(1)
        i = 0
        erro = 0
        if not (arquivo_fonte[ponteiro].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[ponteiro] == '\n'):
            return self.q11(arquivo_fonte, l, tabela_simbolos)
        else:
            i = j
            while i < ponteiro:
                if arquivo_fonte[i].isdigit() or arquivo_fonte[i].isalpha() or arquivo_fonte[i] == '_':
                    i += 1
                else:
                    i += 1
                    erro = 1
            if erro == 0:
                palavra = arquivo_fonte[j:ponteiro]
                if self.tabela_simbolos.procura_na_lista(palavra):
                    return self.tabela_simbolos.procura_na_lista(palavra)
                if not self.l.procura_na_lista(palavra):
                    l.push('id', palavra, 'Nulo')
                return self.l.procura_na_lista(palavra)
            else:
                return self.q24(5, arquivo_fonte, l)

    def q12(self, arquivo_fonte, l, tabela_simbolos): # reconhece *<*
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1
        self.coluna(1)       
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace():
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opr', '<', 'Nulo')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[ponteiro] == '-':
            return self.q15(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[ponteiro] == '=':
            return self.q14(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[ponteiro] == '>':
            return self.q13(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q13(self, arquivo_fonte, l, tabela_simbolos): # diferente <>
        global j
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opr', '<>', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1,arquivo_fonte, l)

    def q14(self, arquivo_fonte, l, tabela_simbolos):  # menor igual <=
        global j
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opr', '<=', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1,arquivo_fonte, l)

    def q15(self, arquivo_fonte, l, tabela_simbolos): # atribuicao <-
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('rcb', '<-', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q16(self, arquivo_fonte, l, tabela_simbolos): # =
        global j 
        global ponteiro
        global palavra 
        
        ponteiro  += 1
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opr', '=', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            
            return self.q24(1, arquivo_fonte, l)

    def q17(self, arquivo_fonte, l, tabela_simbolos): # reconhece *>*
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opr', '>', 'Nulo')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[ponteiro] == '=':
            return self.q18(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q18(self, arquivo_fonte, l, tabela_simbolos): # maior igual >=
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opr', '>=', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q19(self, arquivo_fonte, l, tabela_simbolos): # operadores + - *  /
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte == '"' or arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro]=='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('opm', palavra, 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q20(self, arquivo_fonte, l, tabela_simbolos): # (
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte[ponteiro] == '"' or arquivo_fonte[ponteiro].isspace() or self.Delimitadores_ABP(arquivo_fonte) or arquivo_fonte[ponteiro] =='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('AB_P', '(', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q21(self, arquivo_fonte, l, tabela_simbolos): # )
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isalpha() or arquivo_fonte[ponteiro].isdigit() or arquivo_fonte[ponteiro] == '"' or arquivo_fonte[ponteiro].isspace() or self.Delimitadores_ABP(arquivo_fonte) or arquivo_fonte[ponteiro] =='\n':
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('FC_P', ')', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q22(self, arquivo_fonte, l, tabela_simbolos): # ;
        global j
        global palavra 
        global ponteiro
        global palavra
        
        ponteiro += 1
        self.coluna(1)

        if arquivo_fonte[ponteiro] == '\n': 
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('PT_V', ';', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else:
            return self.q24(1, arquivo_fonte, l)

    def q23(self, arquivo_fonte, l, tabela_simbolos): # ,
        global j 
        global ponteiro
        global palavra
        
        ponteiro += 1        
        self.coluna(1)
        if arquivo_fonte[ponteiro].isspace() or arquivo_fonte[ponteiro].isalpha():
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista(palavra):
                l.push('vir', ',', 'Nulo')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)


    def q24(self, cod, arquivo_fonte, l): # erro
        global palavra
        global j
        global ponteiro
        
        ponteiro+=1
        self.coluna(1)
        if cod ==2 or cod == 3 or cod ==5:
            palavra = arquivo_fonte[j:ponteiro-1]
            if not self.l.procura_na_lista (palavra):
                l.push('ERRO'+str(cod), palavra,'Nulo')
            return self.l.procura_na_lista(palavra)
        else:
            palavra = arquivo_fonte[j:ponteiro]
            if not self.l.procura_na_lista (palavra):
                l.push('ERRO'+str(cod), palavra, 'Nulo')
            return self.l.procura_na_lista(palavra)

    def q25(self, cod, arquivo_fonte, l): # $
        global ponteiro
        global final_arquivo
        global j
        global palavra
        if ponteiro == final_arquivo:
            if self.tabela_simbolos.procura_na_lista('$'):
                return self.tabela_simbolos.procura_na_lista('$')
        else:
            return self.q24(1, arquivo_fonte, l)

    def erro(self, cod):
        if(cod==2):
            print("Erro " + str(cod) + ". Aspas vêm ao final de constantes literais. Linha " + str(contador_linha) + ", coluna " + str(j+1) +" à coluna "+str(contador_coluna-1) +".")
        elif(cod==3):
            print("Erro " + str(cod) + ". Chaves devem fechar comentários. Linha " + str(contador_linha) + ", coluna " + str(j+1) +"  à coluna "+str(contador_coluna-1) +".")
        elif(cod==4):
            print("Erro " + str(cod) + ". Formato numérico permitido: D(.D)(e|E(+|-)D). Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        elif(cod==5):
            print("Erro " + str(cod) + ". Há pelo menos um caractere inválido no id. Linha " + str(contador_linha) + ", coluna " + str(j+1) +" à coluna "+str(contador_coluna-1) +".")
        else:
            print("Erro " + str(cod) + ". caractere inválido, linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
     
    def parser(self, ana, l, tabela_simbolos, fonte, retorno_scanner):    
        pilha: List[str] = []
        pilha.append(0)
        global a
        global palavra
        global final_arquivo
        
        arquivo_fonte = fonte.read()
        final_arquivo = len(arquivo_fonte)-1
        retorno_scanner = self.scanner(arquivo_fonte, l, tabela_simbolos)
        a = retorno_scanner.classe
        if str(retorno_scanner.classe)[0:4] == "ERRO":
            print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
            cod = int(retorno_scanner.classe[4:5])
            ana.erro(cod)
        
        for item in terminais:
            if item[0] == a:
                a = int(item[1])
        
        while True:
            pilha_copia = deepcopy(pilha)
            s = int(pilha_copia.pop())
            for item in terminais:
                if item[0] == a:
                    a = int(item[1])
            if ACTION[s][a][0] == 'S':
                t = int(ACTION[s][a][1:])
                pilha.append(t)
                retorno_scanner = self.scanner(arquivo_fonte, l, tabela_simbolos)
                a = retorno_scanner.classe
                if str(retorno_scanner.classe)[0:4] == "ERRO":
                    print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                    cod = int(retorno_scanner.classe[4:5])
                    ana.erro(cod)
            elif ACTION[s][a][0] == 'R':
                x = int(ACTION[s][a][1:])
                temp = 0
                tamanho = len(gramatica[x])-2
                while temp < tamanho:
                    pilha.pop()
                    temp += 1
                pilha_copia = deepcopy(pilha)
                t = int(pilha_copia.pop())
                A = gramatica[x][0]
                for item in naoTerminais:
                    if item[0] == A:
                        A = int(item[1])
                desvio = int(GOTO[t][A])
                pilha.append(desvio)
                imprimir = tuple(gramatica[x])
                imprimir = " ".join(imprimir)
                print("Regra "+str(x) +": "+str(imprimir))
            elif ACTION[s][a] == 'Acc':
                imprimir = tuple(gramatica[1])
                imprimir = " ".join(imprimir)
                print("Regra 1: "+str(imprimir))
                break
            else:
                if ACTION[s][a][0] == 'E':
                    pos_erro = int(ACTION[s][a][1:])
                    imprimir = tuple(especificacaoErro[pos_erro])
                    imprimir = "".join(imprimir)
                    self.imprime_erro(imprimir)
                    self.trata_erro(fonte, arquivo_fonte, ana, l, tabela_simbolos , pos_erro)

    def trata_erro(self, fonte, arquivo_fonte, ana, l, tabela_simbolos, pos_erro):
        global a
        while not a in tabeladeERRO[pos_erro]:
            if a !="$":
                retorno_scanner = self.scanner(arquivo_fonte, l, tabela_simbolos)
                a = retorno_scanner.classe   
                if str(retorno_scanner.classe)[0:4] == "ERRO":
                    print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                    cod = int(retorno_scanner.classe[4:5])
                    ana.erro(cod)
            else:
                break 
        if a in tabeladeERRO[pos_erro]:
            print("Análise estabelicida. Token: '{}' foi econtrado na linha {}, coluna {}.".format(a, contador_linha, contador_coluna-len(palavra) +1))           

    def imprime_erro(self, imprimir):
        print("Erro: "+ imprimir + ". Linha " + str(contador_linha) + ', coluna ' + str(contador_coluna -len(palavra) +1) + '.')

def main():
    if not os.path.exists('fonte.txt'):
        print("Arquivo não encontrado.\n")
    else: 
        #fonte = open('f.txt', 'a+') #abre arquivo
        #fonte.write(" $")
        #fonte.close()
        l = lista()
        tabela_simbolos = lista()
        ana = analisador(l, tabela_simbolos)
        retorno_scanner = token()

        tabela_simbolos.push('inicio', 'inicio', 'Nulo')
        tabela_simbolos.push('varinicio', 'varinicio', 'Nulo')
        tabela_simbolos.push('varfim', 'varfim', 'Nulo')
        tabela_simbolos.push('escreva', 'escreva', 'Nulo')
        tabela_simbolos.push('leia', 'leia', 'Nulo')
        tabela_simbolos.push('se', 'se', 'Nulo')
        tabela_simbolos.push('entao', 'entao', 'Nulo')
        tabela_simbolos.push('fimse', 'fimse', 'Nulo')
        tabela_simbolos.push('facaate', 'facaate', 'Nulo')
        tabela_simbolos.push('fimfaca', 'fimfaca', 'Nulo')
        tabela_simbolos.push('fim', 'fim', 'Nulo')
        tabela_simbolos.push('inteiro', 'inteiro', 'int')
        tabela_simbolos.push('lit', 'lit', 'lit')
        tabela_simbolos.push('real', 'real', 'real')
        tabela_simbolos.push('$', '$', 'Nulo')

        ana.coluna(0)
        ana.linha()
        
        fonte = open('fonte.txt', 'r+')
        ana.parser(ana, l, tabela_simbolos, fonte, retorno_scanner)
        fonte.close()
        
if __name__ == '__main__':
    main()