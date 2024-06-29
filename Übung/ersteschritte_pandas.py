import pandas as pd

excel_file_path = r"C:\Users\MichalRontsinsky\OneDrive - beyondBIM\Dokumente\VS_Projects\HSLU_CAS2_FS24\Raumliste_Demo.xlsx"

# excel_file_path = "Raumliste_Demo.xlsx"

base_df = pd.read_excel(excel_file_path, sheet_name="Sheet1")

#print(base_df)


# Iteration über die einzelnen Reihen, Option in Klammer Spaltenname eingeben

sig_code_lst = []

for index,row in base_df.iterrows():

    act_raumcode = row["Raumcode"]
    act_storeycode = row["Geschosscode"]

    sig_code = "{}__{}".format(act_storeycode, act_raumcode)

    sig_code_lst.append(sig_code)

base_df["Signaletik"] = sig_code_lst

export_df = base_df.loc[ :, ["Raumcode","Geschosscode","Signaletik","SIA416"]]



filt_df_iloc = base_df.iloc[ 0 : 10, base_df.columns.get_loc('SIA416')]


export_df.to_excel("Raumliste_Signaletik.xlsx", sheet_name="daten", index= False)


#hnf_df = base_df.loc[base_df["SIA416"] == "HNF"]

#raum_flaeche_hnf = hnf_df["Raumflaeche [m²]"].sum()

#print(raum_flaeche_hnf)

#filt_df = base_df.loc[ : ,["SIA416", "Bodenmaterial"]]

#print(filt_df)


