import os
#get_prn_DirFile 会获得 只有一个prn的列表 或者 多个 prn的列表

def get_all_prn(dir):
    #这里扫描路径下的所有prn文件列表

    all_file = os.listdir(dir)
    all_prn = []

    for i in all_file:
        if ".prn" in i:
            all_prn.append(dir + '\\' + i)

    return all_prn
    #dir 应该是个prn文件list


def get_a_prn(file):
    #这里是获取单个prn文件路径
    return [file]
    #file因该是个单独的prn文件路径字符串

def get_xlsx_name(all_prn,suffix):
    #返回一个xlsx文件名
    all_xlsx = []
    for i in all_prn:
        all_xlsx.append(i[:-4] + suffix + r".xlsx")
    return all_xlsx


def get_a_file_or_dir():

    #这里获得文字输入，拖拽即可
    file_or_dir = input(r"拖拽放置prn的文件夹||拖拽prn文件")
    
    if " " in file_or_dir:
        file_or_dir1 = file_or_dir[3:-1]
        return file_or_dir1
    else:
        return file_or_dir


def judge_file_or_dir(file_or_dir):

    if os.path.isdir (file_or_dir):
        #判断是否是文件夹

        print("isdir")
        return get_all_prn(file_or_dir)

    elif os.path.isfile(file_or_dir):
        #判断是否是prn文件

        print("isfile")
        return get_a_prn(file_or_dir)

    
    

def process(suffix):

    file_or_dir = get_a_file_or_dir()
    all_prn = judge_file_or_dir(file_or_dir)
    xlsx_name = get_xlsx_name(all_prn,suffix)

    # process 该函数 从输入获得 prn文件路径 返回 xlsx目标文件啊路径
    return all_prn,xlsx_name

    


if __name__ == '__main__':
    process()
