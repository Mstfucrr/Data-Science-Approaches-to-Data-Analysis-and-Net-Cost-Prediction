import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_excel('excles/Data.xlsx')

conditions = {
    "calve": "1",
    "knorr": "2",
    "lipton": "3",
    "LİPTON": "3",
    "omo": "4",
    "rinso": "5",  
    "yumos": "6",
    "yumoş": "6",  
    "signal": "7",
    "SİGNAL": "7",
    "white": "7",  
    "şampuan": "8",
    "dove": "9",
    "elidor": "10",
    "ELİDOR": "10",
    "clear": "11",
    "domestos": "12",
    "vim": "13",
    "cif": "14",
    "CİF": "14",
    "yüzey": "15",
    "rexona": "16",
    "axe": "17",
    "lux": "18",  
    "pure": "19",  
    "VASELİNE": "20" 
}


# "MAMUL" sütununu içinde koşulların ve eşleşmelerin bir sözlük listesiyle değiştirin
for i, row in dataset.iterrows():
    mamul = row['MAMUL']
    for key in conditions:
        if key in mamul.lower() or key in mamul:
            dataset.at[i, 'MAMUL'] = conditions[key]

dataset["MAMUL"] = pd.to_numeric(dataset["MAMUL"], downcast="integer")

# Eşik değer 100 olarak tanımlandı
threshold = 100
inval = dataset["MAMUL"].value_counts() 
for i,v in zip(inval.index, inval.values): 
    if v < threshold:
        dataset = dataset.drop(dataset[dataset["MAMUL"] == i].index)


# Yeni veri setini excel dosyasına yazdırın
with pd.ExcelWriter("vm_dataset.xlsx") as writer:
    dataset.to_excel(writer, index=False)

