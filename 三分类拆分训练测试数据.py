import os
import pandas as pd
from sklearn.model_selection import train_test_split


def split_train_test(pd_file):
    """按比例拆分数据，返回两个pd对象"""
    train, test = train_test_split(pd_file)
    return train, test


def give_path_of_file(folder_path, file_name_list):

    """需要表格放在一个文件夹下，并给出每个表格的名称"""
    if len(file_name_list) != 3:
        print("本文档仅支持三个表格的拆分！")
    file_path_1 = os.path.join(folder_path, file_name_list[0] + ".csv")
    file_path_2 = os.path.join(folder_path, file_name_list[1] + ".csv")
    file_path_3 = os.path.join(folder_path, file_name_list[2] + ".csv")

    # 利用pandas读取路径
    pd_file_1 = pd.read_csv(file_path_1)
    pd_file_2 = pd.read_csv(file_path_2)
    pd_file_3 = pd.read_csv(file_path_3)

    # 进行拆分
    train_1, test_1 = split_train_test(pd_file=pd_file_1)
    train_2, test_2 = split_train_test(pd_file=pd_file_2)
    train_3, test_3 = split_train_test(pd_file=pd_file_3)
    # 进行拼接
    train = train_1.append(train_2).append(train_3)
    test = test_1.append(test_2).append(test_3)

    return train, test


def precess_csv_feature(folder_path, file_name_list, store_path):
    """传入文件所在的路径，需要处理的表格名称，以及"""
    train_store_path = os.path.join(store_path, "train.csv")
    test_store_path = os.path.join(store_path, "test.csv")
    train, test = give_path_of_file(folder_path, file_name_list)
    train_csv = train.to_csv(train_store_path, index=0)
    test_csv = test.to_csv(test_store_path, index=0)


if __name__ == "__main__":
    folder_path = r"E:\gao_lung_data\p_feature"
    file_name_list = ["alk", "egfr", "negative"]
    store_path = r"E:\gao_lung_data\p_feature\train_test"
    precess_csv_feature(folder_path, file_name_list, store_path)