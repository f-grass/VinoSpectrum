import os
import pandas as pd


lst_47 = [f"data/47grad_nah_TIFF/{file}" for file in os.listdir('data/47grad_nah_TIFF')]
df_47 = pd.DataFrame({'tiff_filename': lst_47})
df_47["category"] = "47_grad"
df_47["id"] = df_47["tiff_filename"].apply(lambda file: file.split("/")[-1][:-5])

lst_90 = [f"data/90grad_nah_TIFF/{file}" for file in os.listdir('data/90grad_nah_TIFF')]
df_90 = pd.DataFrame({'tiff_filename': lst_90})
df_90["category"] = "90_grad"
df_90["id"] = df_90["tiff_filename"].apply(lambda file: file.split("/")[-1][:-5])

df_relevant = pd.concat([df_47, df_90], ignore_index=True)

df_all = pd.read_csv('data/all_image_gps.csv')
df_all['id'] = df_all['image_name'].apply(lambda file: file[4:-4])

df_relevant = pd.merge(left=df_relevant, right=df_all, on='id', how='left')

df_relevant.to_csv(path_or_buf='data/relevant_images_gps.csv', index=False)
