**Data Science Approaches to Data Analysis and Net Cost Prediction**

### **Start:**
This project aims to estimate the net cost of Unilever's Food, HC (Home Care) and PC (Personal Care) categories over a period of 8 months, using sales data, with various adjustments and including variations specific to the product groups. The analysis can provide important information for the business in terms of cost effectiveness and profitability.

**Data Set Characteristics:**
- CODE (Product Code/Reference Number)
- BARKOD (Barcode Number)
- PRODUCT (Product Name/Description)
- INSIDE (Unit Content)
- GR (Weight)
- LIST (List Price)
- UNDER INVOICE % (Under Invoice Discount Rate)
- PERIOD END % (End of Period Discount Rate)
- VAT (Value Added Tax Rate)
- NET COST
- S.RAF (Suggested Shelf Price)
- CATEGORY (Category to which the product belongs (Food, HC, PC))
- MONTH (Month of Sale, March-October)

**Data Set Visualisation:**
In the project, statistical representation of the data set is presented with graphs made using the Seaborn library.

### **Regression Model Performance:**
Performance comparison of the model trained with Z-score and IQR data preprocessing.

| Value\Method | Z-score data preprocessing | IQR data preprocessing |
|--------------|-------------------------|----------------------|
| MSE | 32.6917 | 37.8279 |
| RMSE | 5.7176 | 6.1504 |
| R2 | 0.9470 | 0.9194 |
| MAE | 4.1301 | 4.603 |


### **Requirements:**
- Python 3.11 (https://www.python.org/downloads/)
- Jupyter Notebook (https://jupyter.org/install)
- NumPy (pip install numpy)
- Pandas (pip install pandas)
- Matplotlib (pip install matplotlib)
- Seaborn (pip install seaborn)
- Scikit-learn (pip install scikit-learn)

### **Installation:**
1. [Download and install](https://www.python.org/downloads/) Python 3.11.
2. [Download and install](https://jupyter.org/install) the Jupyter Notebook.
3. Download or copy the project files.
4. Open the project files with Jupyter Notebook.
5. `init.ipynb` dosyasını çalıştırarak regresyon modelinin sonuçlarını gözlemleyin.
6. `analysis.ipynb` dosyasını çalıştırarak veri analizini ve grafikleri gözlemleyin.

<hr /> 

### **Sample Visualisation:**
<div style="display: flex; align-items: center; justify-content: center; gap: 1rem; flex-wrap: wrap;">
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/1e915ca2-e2af-4408-92c1-832102e97b80" alt="1" width="500" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/f95455c0-1af0-43af-b974-dbe6b83acb26" alt="2" width="300" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/5392b625-3b8a-44a5-a344-95137371e8eb" alt="3" width="300" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/aed6a96c-5a8c-4825-8106-1ca19d3d79c5" alt="4" width="300" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/61d70a41-285b-4ba8-a1d6-b7be1f79215a" alt="4" width="300" height="auto" >


</div>



**Usage:**
By opening the project files with Jupyter Notebook, you can evaluate the regression model and perform data analysis.
