# 转换成 ["frequency","制图frequency","e\'","e\"","u\'","u\"","tanU","tanE","alpha衰减常数","C0","制图C0"] 的脚本
import get_prn_DirFile
import prn2matrix
import data2xlsx
import formula


suffix = "__otherdata"

# xlsx 目标文件路径

prn_xlsx_filename = get_prn_DirFile.process(suffix)

#这是所有prn路径列表
#print(prn_xlsx_filename[0])


#这是xlsx文件保存路径
#print(prn_xlsx_filename[1])

for i in range(len(prn_xlsx_filename[0])):

    print(i)
    numpyarry = prn2matrix.process(prn_xlsx_filename[0][i])

    frequency = prn2matrix.get_frequency(numpyarry)
    e1 = prn2matrix.get_e1(numpyarry)
    e11 = prn2matrix.get_e11(numpyarry)
    u1 = prn2matrix.get_u1(numpyarry)
    u11 = prn2matrix.get_u11(numpyarry)

    all_otherdata = data2xlsx.get_all_otherdata(frequency,e1,e11,u1,u11)

    

    # d 为毫米
    data2xlsx.save2workbook3(prn_xlsx_filename[1][i],all_otherdata)

    
