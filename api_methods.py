import pandas as pd
import matplotlib.pyplot as plt

def anahtar_kelimeye_göre_ara(books_service, keywords):
    request = books_service.volumes().list(q=",".join(keywords))
    response = request.execute()
    return response.get("items", [])

def en_uretken_yil(books_info_df):
    books_info_df['PublishedDate'] = pd.to_datetime(books_info_df['PublishedDate'], errors='coerce')
    books_info_df['PublishedYear'] = books_info_df['PublishedDate'].dt.year
    en_uretken_yil = books_info_df['PublishedYear'].mode()[0]
    return en_uretken_yil

def plot_yillik_kitaplar(books_info_df):
    books_info_df['PublishedYear'] = pd.to_datetime(books_info_df['PublishedDate'], errors='coerce').dt.year
    yillik_kitaplar = books_info_df['PublishedYear'].value_counts().sort_index()
    yillik_kitaplar.plot(kind='bar', xlabel='Yıl', ylabel='Kitap Sayısı', title='Yıllara Göre Kitap Sayısı')
    plt.show()

def plot_tur_dagilimi(books_info_df):
    tur_dagilimi = books_info_df['Categories'].value_counts()
    tur_dagilimi.plot(kind='bar', xlabel='Kitap Türü', ylabel='Kitap Sayısı', title='Kitap Türlerine Göre Dağılım')
    plt.show()

def plot_yazar_basina_kitap(books_info_df):
    yazar_basina_kitap = books_info_df['Authors'].explode().value_counts()
    yazar_basina_kitap.plot(kind='bar', xlabel='Yazar', ylabel='Kitap Sayısı', title='Yazar Bazında Kitap Sayısı')
    plt.show()