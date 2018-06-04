import os
import os.path as osp
import hashlib


def filehash(filepath):
    blocksize = 64 * 1024
    sha = hashlib.sha256()
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()


def get_recursive_hash(dir_root):
    print('size,sha256,filename')
    hash_list = []
    for root, dirs, files in os.walk(dir_root):
        for fpath in [osp.join(root, f) for f in files]:
            size = osp.getsize(fpath)
            sha = filehash(fpath)
            name = osp.relpath(fpath, dir_root)
            hash_list.append({'size': size, 'sha': sha, 'name':name})
    # print(hash_list)
    return hash_list


def compare_recursive_hash(dir1, dir2):
    hash_list1 = get_recursive_hash(dir1)
    hash_list2 = get_recursive_hash(dir2)
    print(len(hash_list1))
    print(len(hash_list2))
    y=0
    list_different=[]
    for i in  hash_list2:
        if i in hash_list1:
           y+=1
        else:
            list_different.append(i['name'])
    print("两者相同文件数为：" +str(y))
    print("两者不同文件数为：")
    print(list_different)
    print("差异或缺失的文件数目为" + str(len(list_different)))



compare_recursive_hash(r'E:\test\xianshang', r'E:\test\bendi')

# get_recursive_hash(r'E:\test\bendi')
# get_recursive_hash(r'E:\test\xianshang')