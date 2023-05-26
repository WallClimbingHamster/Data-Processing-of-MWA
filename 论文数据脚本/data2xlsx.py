
import numpy as np
import pandas as pd
import formula 
import prn2matrix
import constant



data_label = ["tanE","tanU","Zin","|Zin/Z0|","RL","衰减alpha","C0","涡流损耗"]




def get_all_ZinZ0(frequency,e1,e11,u1,u11,d):

    data = frequency / 10e8
    for i in np.arange(0.1,d,0.1):
        ZinZ0 = formula.get_ZinZ0(frequency,e1,e11,u1,u11,i)

        #data = np.hstack([data,ZinZ0])
        data = np.column_stack((data, ZinZ0))
    
    return data
# 0,0 frequency
# :,0 频率 1->18 Ghz
# 0,: 厚度 1->10 mm

# 用来保存 Zin/Z0 的代码！
def save2workbook2(workbookename,array,d):

    #写入数据
    df = pd.DataFrame(array)
    writer  = pd.ExcelWriter(workbookename)
    df.to_excel(writer,index=False)

    #写入字符串
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for i in np.arange(0,d,0.1):
        #worksheet.cell(1,i*10,str(i)+"mm")
        colum = i * 10 + 1
        worksheet.cell(1,int(colum),str(i)[:3])
    worksheet.cell(1,1,'frequency')
    writer.save()
    
def get_all_otherdata(frequency,e1,e11,u1,u11):

    # label3 = ["frequency","制图frequency","e\'","e\"","u\'","u\"","tanU","tanE","alpha衰减常数","C0","制图C0"]
    draw_picture_frequency = frequency / 10e8
    tanU = formula.get_tanU(u11,u1)
    tanE = formula.get_tanE(e11,e1)
    alpha = formula.get_Attenuation(frequency,e1,e11,u1,u11)
    C0 = formula.get_C0(u11,u1,frequency)
    draw_picture_C0 = C0 * 10e7
    
    data = np.column_stack((frequency,draw_picture_frequency,e1,e11,u1,u11,tanU,tanE,alpha,C0,draw_picture_C0))
    return data

#用来保存 otherdata 的代码
def save2workbook3(workbookename,array):
    
    df = pd.DataFrame(array)
    writer  = pd.ExcelWriter(workbookename)
    df.to_excel(writer,index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    for i in range(len(constant.label3)):
        
        # label3 = ["frequency","制图frequency","e\'","e\"","u\'","u\"","tanU","tanE","alpha衰减常数","C0","制图C0"]
        worksheet.cell(1,i+1,constant.label3[i])
    
    writer.save()


def get_all_reflection_loss(frequency,e1,e11,u1,u11,d):

    data = frequency / 10e8
    for i in np.arange(0.1,d,0.1):
        reflection_loss = formula.get_ReflectionLoss(frequency,e1,e11,u1,u11,i)

        #data = np.hstack([data,ZinZ0])
        data = np.column_stack((data, reflection_loss))
    
    return data
    

def save2workbook4(workbookename,array,d):

    
    df = pd.DataFrame(array)
    writer  = pd.ExcelWriter(workbookename)
    df.to_excel(writer,index=False)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    for i in np.arange(0,d,0.1):
        #worksheet.cell(1,i*10,str(i)+"mm")
        colum = i * 10 + 1
        worksheet.cell(1,int(colum),str(i)[:3])
    worksheet.cell(1,1,'frequency')
    writer.save()
    



if __name__ == "__main__":

    
    pass

    
