import os
import numpy as np
import pandas as pd


class DataFrame:
    """
    从特征表格中返回特征的名字，特征矩阵，Casename等信息
    """
    def __init__(self, pd_data_path):
        self.pd_data_path = pd_data_path
        self.pd_data = pd.read_csv(self.pd_data_path)

    def get_feature_name(self):

        feature_name = list(self.pd_data.columns)
        return feature_name[1:]

    def get_case_name(self):

        case_name = list(self.pd_data["CaseName"])
        return case_name

    def get_new_case_name(self):
        """
        用于完成相减后的特征表格的CaseName
        如果不需要新的casename就直接拿上面的casename就可以了
        :return: new case name
        """
        case_new_name = []
        for case in self.get_case_name():
            case_new_name.append(case.split("_")[0])
        return case_new_name

    def get_array(self):
        index_feature_name = self.get_feature_name()
        index_feature_name = index_feature_name
        array = np.asarray(self.pd_data[index_feature_name].values, dtype=np.float64)
        return array

    @staticmethod
    def update_feature_csv(feature_name, feature_array, case_name):
        data_frame = pd.DataFrame(data=feature_array, index=case_name, columns=feature_name)
        return data_frame

    @staticmethod
    def save_csv(pd_data_frame, store_path, frame_name):
        pd_data_frame.to_csv(os.path.join(store_path, frame_name), pd_data_frame)
        print("pd_data_frmae is saved !")




feature_1 = DataFrame(r"\feature_C.csv")
feature_2 = DataFrame(r"\feature_CE.csv")
feature_1_array = feature_c.get_array()
feature_2_array = feature_ce.get_array()

feature_array = feature_1_array - feature_2_array  # 此处可以有各种矩阵操作，注意维度匹配即可

pd_c_ce = pd.DataFrame(data=feature_array, index=feature_1.get_new_case_name(), columns=feature_1.get_feature_name())
pd_c_ce.to_csv(r"\sub_feature\c_ce.csv")
