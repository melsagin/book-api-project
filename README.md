# Google Book API
Bu Python kodu, Book API ile client kütüphanesi kullanılarak web kazıma (web scraping) yapmayı amaçlayan bir projedir.Proje, Google Book içerisindeki verileri almaya, işlemeye ve görselleştirmeye yarar.

## Gereksinimler
Scripti çalıştırmadan önce, Book API kimlik bilgilerinizi ayarlamanız gerekiyor. Bir Google Geliştirici hesabı oluşturun ve şu kimlik bilgilerini edinin (ücretsiz bir şekilde alabilirsiniz):

- Geliştirme Yaparken Yararlanılabilecek Kaynak: https://developers.google.com/books/docs/v1/using?hl=tr
- Google Geliştirici Hesabı: https://console.cloud.google.com/apis/api/books.googleapis.com/metrics?project=daring-slice-408613
- config.py içeren bir config dosyası oluşturun
    -  **BOOK_API_KEY** bilginizi config.py içerisine ekleyin

## Kurulum
* Depoyu klonlayın:
- `git clone https://github.com/melsagin/book-api-project.git`

* Gerekli Python paketlerini yükleyin:
- `pip install -r requirements.txt`

# Google Book API
This Python code is a project aiming to perform web scraping using the Book API with the help of the client library. The project is designed to retrieve, process, and visualize data from Google Books.

## Requirements
Before running the script, you need to set up your Book API credentials. Create a Google Developer account and obtain the following credentials (you can obtain them for free):

- Useful Resource for Development: https://developers.google.com/books/docs/v1/using
- Google Developer Account: https://console.cloud.google.com/apis/api/books.googleapis.com/metrics?project=daring-slice-408613
- Create a config file containing config.py
    - Add your **BOOK_API_KEY** inside config.py

## Installation
* Clone the repository:
- `git clone https://github.com/melsagin/book-api-project.git`
* Install the required Python packages:
- `pip install -r requirements.txt`