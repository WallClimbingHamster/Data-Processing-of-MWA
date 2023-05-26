# 转换成 ["frequency","制图frequency","e\'","e\"","u\'","u\"","tanU","tanE","alpha衰减常数","C0","制图C0"] 的脚本
import get_prn_DirFile
import prn2matrix
import data2xlsx
import formula


suffix = "__RLoss"
suffix1 = "__RLoss__width"

# xlsx 目标文件路径

prn_xlsx_filename = get_prn_DirFile.process(suffix)
#prn_xlsx_filename_of_RL_width = get_prn_DirFile.process(suffix1)

#这是所有prn路径列表
#print(prn_xlsx_filename[0])


#这是xlsx文件保存路径
#print(prn_xlsx_filename[1])

for i in range(len(prn_xlsx_filename[0])):

    print(prn_xlsx_filename[0][i])
    numpyarry = prn2matrix.process(prn_xlsx_filename[0][i])

    frequency = prn2matrix.get_frequency(numpyarry)
    e1 = prn2matrix.get_e1(numpyarry)
    e11 = prn2matrix.get_e11(numpyarry)
    u1 = prn2matrix.get_u1(numpyarry)
    u11 = prn2matrix.get_u11(numpyarry)

    all_reflection_loss = data2xlsx.get_all_reflection_loss(frequency,e1,e11,u1,u11,10)

    

    # d 为毫米
    data2xlsx.save2workbook4(prn_xlsx_filename[1][i],all_reflection_loss,10)

    #RL宽度

    #data2xlsx.save2workbook4(prn_xlsx_filename_of_RL_width[1][i], ,10)

input("\npress enter to close\n")
