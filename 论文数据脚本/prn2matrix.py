from csv import reader
import get_prn_DirFile
import numpy

#get_prn_DirFile 会获得 只有一个prn的列表 或者 多个 prn的列表

def read_prn_data(prn_file):
    prn_data = []
    with open(prn_file) as f:
        data =  reader(f)
        #reader() 返回一个迭代器 用for 访问
        for i in data:
            prn_data.append(i)

    return prn_data[1:]


            

def prndata2matrix(prn_data):
    #将prn文件内的数据转换成python的矩阵，之后进行计算或者其他操作
    matrix = []
    for line in prn_data:
        if line:
            nums = line[0].split('\t')
            row = [float(num) for num in nums]
            matrix.append(row)
    return matrix


def build_numpy_array(matrix):
    numpyarry = numpy.array(matrix)
    #通过numpy建立数组
    return numpyarry

def get_frequency(numpyarry):
    #从数组中获得frequency
    return numpyarry[:,0]

def get_e1(numpyarry):
    #从数组中获得e'
    return numpyarry[:,1]

def get_e11(numpyarry):
    #从数组中获得e''
    return numpyarry[:,2]
    
def get_u1(numpyarry):
    #从数组中获得u'
    return numpyarry[:,3]

def get_u11(numpyarry):
    #从数组中获得u''
    return numpyarry[:,4]



def process(prn_file):
    
    prn_data = read_prn_data(prn_file)
    matrix = prndata2matrix(prn_data)
    numpyarry = build_numpy_array(matrix)
    
    return numpyarry


if __name__ == "__main__":
    #测试用例 可以直接运行
    
    prn_file = r'C:\Users\97250\Desktop\论文数据脚本\CuSn 1_3.27mm-.prn'
    

    
