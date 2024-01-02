## **Unilever Satış Verileri Üzerinde Net Maliyet Tahmini Analizi**

### **Başlangıç:**
Bu proje, Unilever'in 8 aylık süre zarfında Food (Gıda), HC (Ev Bakımı) ve PC (Kişisel Bakım) kategorilerindeki satış verilerini kullanarak, çeşitli düzeltmelerle ve ürün gruplarına özgü değişkenlikleri içeren net maliyeti tahmin etmeyi amaçlamaktadır. Analiz, işletme için maliyet etkinliği ve karlılık açısından önemli bilgiler sağlayabilir.

### **Veri Seti Özellikleri:**
- KOD (Ürün Kodu/Referans Numarası)
- BARKOD (Barkod Numarası)
- MAMUL (Ürün Adı/Tanımı)
- K.İÇİ (Birim İçeriği)
- GR (Ağırlık)
- LİSTE (Liste Fiyatı)
- FATURA ALTI % (Fatura Altı İndirim Oranı)
- DÖNEM SONU % (Dönem Sonu İndirim Oranı)
- KDV (Katma Değer Vergisi Oranı)
- NET MALİYET
- Ö.RAF (Öneri Raf Fiyatı)
- KATEGORİ ( Ürünün Ait Olduğu Kategori (Food, HC, PC))
- AY (Satışın Gerçekleştiği Ay, Mart- Ekim)

### **Veri Seti Görselleştirmesi:**
Projede Seaborn kütüphanesi kullanılarak yapılan grafiklerle veri setinin istatistiksel gösterimi sunulmuştur.

### **Regresyon Model Performansı:**
Z-score ve IQR veri ön işlemesi ile eğitilen modelin performans karşılaştırması.

| Değer\Yöntem | Z-score veri ön işlemesi | IQR veri ön işlemesi |
|--------------|-------------------------|----------------------|
| MSE          | 32.6917                 | 37.8279              |
| RMSE         | 5.7176                  | 6.1504               |
| R2           | 0.9470                  | 0.9194               |
| MAE          | 4.1301                  | 4.603                |


### **Gereksinimler:**
- Python 3.11 (https://www.python.org/downloads/)
- Jupyter Notebook (https://jupyter.org/install)
- NumPy (pip install numpy)
- Pandas (pip install pandas)
- Matplotlib (pip install matplotlib)
- Seaborn (pip install seaborn)
- Scikit-learn (pip install scikit-learn)

### **Kurulum:**
1. Python 3.11'i [indirin ve yükleyin](https://www.python.org/downloads/).
2. Jupyter Notebook'u [indirin ve yükleyin](https://jupyter.org/install).
3. Proje dosyalarını indirin veya kopyalayın.
4. Jupyter Notebook ile proje dosyalarını açın.
5. `init.ipynb` dosyasını çalıştırarak regresyon modelinin sonuçlarını gözlemleyin.
6. `analysis.ipynb` dosyasını çalıştırarak veri analizini ve grafikleri gözlemleyin.

<hr /> 

### **Örnek Görselleştirme:**
<div style="display: flex; align-items: center; justify-content: center; gap: 1rem; flex-wrap: wrap;">
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/1e915ca2-e2af-4408-92c1-832102e97b80" alt="1" width="500" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/f95455c0-1af0-43af-b974-dbe6b83acb26" alt="2" width="300" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/5392b625-3b8a-44a5-a344-95137371e8eb" alt="3" width="300" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/aed6a96c-5a8c-4825-8106-1ca19d3d79c5" alt="4" width="300" height="auto" >
<img src="https://github.com/Mstfucrr/Veri-Madenciligi-Proje/assets/76887611/61d70a41-285b-4ba8-a1d6-b7be1f79215a" alt="4" width="300" height="auto" >


</div>



**Kullanım:**
Proje dosyalarını Jupyter Notebook ile açarak, regresyon modelini değerlendirebilir ve veri analizini gerçekleştirebilirsiniz.

