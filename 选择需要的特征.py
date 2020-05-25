import os
import pandas as pd


def remove_one_feature(feature_path, data_path, store_path, store_name):
    pd_feature = pd.read_csv(feature_path)
    feature_list = pd_feature["feature_name"]
    pd_data = pd.read_csv(data_path)
    feature_name = pd_data.columns[2:]
    case_name = pd_data["CaseName"]
    label = pd_data["label"]
    pd_new = pd_data[feature_list]
    pd_new = pd.concat([case_name, label, pd_new], axis=1)
    pd_new.to_csv(os.path.join(store_path, store_name + ".csv"), index=None)



select_feature = r"D:\lung_C_feature\alk_one_feature\新建文本文档.csv"
data_path = r"D:\lung_P_feature\test.csv"
store_path = r"D:\lung_P_feature"
store_name = "test_somte"
remove_one_feature(feature_path=select_feature, data_path=data_path, store_path=store_path, store_name=store_name)