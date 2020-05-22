import os
import numpy as np
import pandas as pd


class GetSingleFeature:
    def __init__(self, data_path, store_path):
        self.data_path = data_path
        self.store_path = store_path
        self.pd_feature = pd.read_csv(self.data_path)
        self.feature_name = self.pd_feature.columns[1:]
        self.case_name = self.pd_feature["CaseName"]
        self.clinical_feature = ["sex", "age", "smoke", "label"]
        try:
            self.label = self.pd_feature["label"]
        except:
            print("please add label ! ")
        """
        在本次的实验中是有临床特征的因此，要添加临床特征
        如果没有临床特征，可以直接将此部分注释掉
        并将上面的列表置为空即可
        """
        try:
            self.sex = self.pd_feature["sex"]
            self.age = self.pd_feature["age"]
            self.smoke = self.pd_feature["smoke"]
        except:
            print("no clinical feaure!")

    def get_feature_class(self):
        feature_list = []
        for feature in self.feature_name:
            if feature not in self.clinical_feature:
                feature_list.append(feature.split("_")[-2])
        feature_list = set(feature_list)
        return feature_list

    def get_single_feaure(self, feature_name):
        feature_index = []
        for feature in self.feature_name:
            if feature not in self.clinical_feature:
                if feature.split("_")[-2] == feature_name:
                    feature_index.append(feature)
        pd_single = self.pd_feature[feature_index]

        pd_clinical = pd.concat([self.sex, self.age, self.smoke], axis=1)
        pd_single = pd.concat([self.case_name, self.label, pd_clinical, pd_single], axis=1)
        pd_single.to_csv(os.path.join(self.store_path, feature_name + ".csv"), index=None)


if __name__ == '__main__':
    get_single_feature = \
        GetSingleFeature(data_path=r"E:\EGFR TKI\feature_subtraction\sub_feature\ce_sub_c\clinical_ce_sub_c.csv",
                         store_path=r"E:\EGFR TKI\feature_subtraction\sub_feature\ce_sub_c")

    feature_list = get_single_feature.get_feature_class()
    for feaure in feature_list:
        get_single_feature.get_single_feaure(feature_name=feaure)

