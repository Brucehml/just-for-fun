import zipfile,os,shutil
import subprocess
import xml.etree.ElementTree as ET
filename = ''
    
def jieya(filename):  
    with zipfile.ZipFile(filename, 'r') as zipf:
        zipf.extractall('officecpassword')

    
def cancel_p(path):
    f_p = path+'\\officecpassword\\ppt\\presentation.xml'
    # 解析XML文件
    tree = ET.parse(f_p)
    root = tree.getroot()
    #recursive_print(root)
    for child in root:
        if 'modifyVerifier' in str(child):
            root.remove(child)

    # 保存修改后的XML文件
    tree.write(f_p)

def yasuo(fp,path,name):
    shutil.make_archive(fp,'zip',path+'\\officecpassword\\')
    os.rename(fp+'.zip', path+'\\unlocked'+name)
    shutil.rmtree(path+'\\officecpassword\\')
    os.system('explorer /select, '+path+"\\unlocked"+name)
    
filename = 'C:\\Users\\admin\\Desktop\\2024年江苏纲要（选择“只读打开”).pptx'
jieya(filename)
(path, name) = os.path.split(filename)
cancel_p(path)
yasuo(filename,path,name)
