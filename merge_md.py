import os
import glob

TYPE_DEF = {
    1: '[ 单选题 ] ',
    2: '[ 多选题 ] ',
    3: '[ 判断题 ] ',
    4: '[ 问答题 ] ',
    5: '[ 填空题 ] ',
}

path = '.\\md'
mds = glob.glob(path + r'/*/*.md')
mds = sorted(mds,
             key=(lambda x: int(x.strip().split('\\')[-1].split('.')[-2])))

if __name__ == '__main__':
    with open('all.md', 'w', encoding='utf-8') as f:
        #先遍历文件名
        f.writelines("[toc]\n\n")
        for filepath in mds:
            #遍历单个文件，读取行数
            with open(filepath, 'r', encoding='utf-8') as fmd:
                filename = filepath.strip().split('\\')[-1].split('.')[-2]
                for i, line in enumerate(fmd):
                    if i == 0:
                        line = int(line.strip())
                        if line == 4: break
                        f.writelines(f"#### {filename}\n\n{TYPE_DEF[line]} ")
                    else:
                        f.writelines(line)
                else:
                    f.write('\n---\n\n')
