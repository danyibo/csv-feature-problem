import pandas as pd
import os




class CombineFeature:
    """

           这个类是将平扫和增强数据的特征进行拼接
           由于数据的case是不同的，因此，拼接出来后就会有空值
           再将空值drop掉

       """
    def __init__(self, all_data_path):
        self.all_data_path = all_data_path

    def store_folder(self):
        store_folder_path = os.path.join(self.all_data_path, "平扫和增强拼接")
        if not os.path.exists(store_folder_path):
            os.makedirs(store_folder_path)
        return store_folder_path

    def change_row(self, pd_data, clas):
        pd_new_row = []
        pd_header_list = list(pd_data.loc[[]])
        for feature in pd_header_list:
            x = feature.split("roi")[-1]
            if x == "CaseName":
                pass
            else:
                x = clas + x
            pd_new_row.append(x)
        pd_data.columns = pd_new_row

        return pd_data

    def make_same_case_name(self, pd_data):
        pd_list = list(pd_data["CaseName"])
        pd_case_name_list = []
        for case_name in pd_list:
            x = case_name.split("_")[0]
            pd_case_name_list.append(x)
        pd_data["CaseName"] = pd_case_name_list
        pd_new_data = pd_data
        return pd_new_data

    def get_csv(self):
        folder_P = os.path.join(self.all_data_path, "平扫数据特征")
        folder_Z = os.path.join(self.all_data_path, "增强数据特征")
        folder_P_list = os.listdir(folder_P)
        folder_Z_list = os.listdir(folder_Z)
        P_1 = pd.read_csv(os.path.join(folder_P, folder_P_list[0]))
        P_2 = pd.read_csv(os.path.join(folder_P, folder_P_list[1]))
        P_2 = self.make_same_case_name(P_2)
        P_3 = pd.read_csv(os.path.join(folder_P, folder_P_list[2]))
        P_3 = self.make_same_case_name(P_3)
        Z_1 = pd.read_csv(os.path.join(folder_Z, folder_Z_list[0]))
        Z_2 = pd.read_csv(os.path.join(folder_Z, folder_Z_list[1]))
        Z_3 = pd.read_csv(os.path.join(folder_Z, folder_Z_list[2]))

        P_1 = self.change_row(P_1, "P")
        P_2 = self.change_row(P_2, "P")
        P_3 = self.change_row(P_3, "P")
        Z_1 = self.change_row(Z_1, "Z")
        Z_2 = self.change_row(Z_2, "Z")
        Z_3 = self.change_row(Z_3, "Z")
        return P_1, P_2, P_3, Z_1, Z_2, Z_3


    def combin_two(self):
        P_1, P_2, P_3, Z_1, Z_2, Z_3 = self.get_csv()
        P_Z_1 = pd.merge(P_1, Z_1, how='left', on="CaseName")
        P_Z_1 = P_Z_1.dropna(how="any", axis=0)

        P_Z_2 = pd.merge(P_2, Z_2, how='left', on="CaseName")
        P_Z_2 = P_Z_2.dropna(how="any", axis=0)

        P_Z_3 = pd.merge(P_3, Z_3, how='left', on="CaseName")
        P_Z_3 = P_Z_3.dropna(how="any", axis=0)

        store_path = self.store_folder()
        P_Z_1.to_csv(os.path.join(store_path, "alk.csv"), index=None)
        P_Z_2.to_csv(os.path.join(store_path, "egfr.csv"), index=None)
        P_Z_3.to_csv(os.path.join(store_path, "negative.csv"), index=None)

if __name__ == "__main__":
        combine_feture = CombineFeature(all_data_path=r"E:\gao_lung_data")
        P_1, P_2, P_3, Z_1, Z_2, Z_3 = combine_feture.get_csv()
        combine_feture.combin_two()