import numpy as np
from constant import *
#用来计算各项实验数据的函数

# tan(u''/u')
def get_tanU(u11,u1):

    tanu = np.tan(u11/u1)

    return tanu

# tan(e''/e')
def get_tanE(e11,e1):

    tane = np.tan(e11/e1)

    return tane
    
# Zin
def get_Zin(frequency,e1,e11,u1,u11,d):
    # Zin 为材料阻抗 d 为厚度

    # sqrt((u'+u''j)/(e'+e''j))
    Ur = u1 - u11 * 1j
    Er = e1 - e11 * 1j

    formula_part1 = Z0*np.sqrt( Ur / Er )
    formula_part2 = np.tanh(1j * 2 * pi * frequency * d / cmm * np.sqrt(Ur * Er))
    # d =>> mm  c =>> m 此处用 cmm =>> mm
    Zin = formula_part1 * formula_part2

    return Zin

# Z0
def get_Z0():  

    return 377

# |Zin/Z0| 
def get_ZinZ0(frequency,e1,e11,u1,u11,d):  
    # Zin 包含乘数因子Z0
    Ur = u1 - u11 * 1j
    Er = e1 - e11 * 1j

    formula_part1 = np.sqrt( Ur / Er )
    formula_part2 = np.tanh(1j * 2 * pi * frequency * d / cmm  * np.sqrt(Ur * Er))
    Zin_divide_Z0 = np.abs(formula_part1 * formula_part2)

    return Zin_divide_Z0

# ReflectionLoss
def get_ReflectionLoss(frequency,e1,e11,u1,u11,d):
    
    Zin = get_Zin(frequency,e1,e11,u1,u11,d)
    Z0 = get_Z0()
    T = (Zin - Z0) / (Zin + Z0)
    RL = 20 * np.log10(np.abs(T))

    return RL

# alpha 衰减特性
def get_Attenuation(frequency,e1,e11,u1,u11):
    #参数都是numpy的列数组

    a1 = pi*frequency/c
    a2 = 2 * (u11*e11-u1*e1)
    a3 = np.sqrt(np.power(u11*e11-u1*e1,2)+np.power(u1*e11+u11*e1,2))
    alpha = a1*np.sqrt(a2+2*a3)

    return alpha

# C0
def get_C0(u11,u1,f):
    C0 = u11*np.power(u1,-2)*np.power(f,-1)
    return C0

############################################################


import numpy as np

def find_frequency_ranges(freq, RL,d,RL_effect):
    """
    Find frequency ranges where RL is less than -10 dB.
    
    Args:
    - frequency (numpy array): Array of frequency values.
    - RL (numpy array): Array of reflection loss values.
    
    Returns:
    - freq_ranges (list of lists): List of lists where each sublist contains 
      [min_freq, max_freq, width] for each frequency range where RL is less than -10 dB.
    """

    freq_ranges = []
    freq_ranges_txt = []
    start_idx = None
    end_idx = None
    frequency = freq/10e8
    for RL_min in RL_effect:
        for i in range(len(RL)):
            if RL[i] <= RL_MIN and start_idx is None:
                start_idx = i
            elif RL[i] <= RL_MIN and start_idx is not None:
                end_idx = i
                if end_idx == len(RL):
                    freq_ranges.append([frequency[start_idx], frequency[end_idx], frequency[end_idx] - frequency[start_idx]])
            elif RL[i] > RL_MIN and start_idx is not None and end_idx is not None:
                freq_ranges.append([frequency[start_idx], frequency[end_idx], frequency[end_idx] - frequency[start_idx]])
                start_idx = None
                end_idx = None
            
    # Add range if last value is less than -10
    #if start_idx is not None and end_idx is None:
    # freq_ranges.append([frequency[start_idx], frequency[-1], frequency[-1] - frequency[start_idx]])
   
        
# 输出结果
        if len(freq_ranges) == 0:
            #print("No frequency range found with RL less than -10 dB.")
            pass
        else:
        #print("Frequency ranges with RL less than -10 dB:")
            for i, fr in enumerate(freq_ranges):
                freq_range_txt = f"d(mm):{d:.2f}\tRL_effective<{RL_MIN}\tRange {i+1}: {fr[0]:.2f} - {fr[1]:.2f} GHz,\twidth = {fr[2]:.2f} GHz."
                freq_ranges_txt.append(freq_range_txt)
            
    return freq_ranges_txt


