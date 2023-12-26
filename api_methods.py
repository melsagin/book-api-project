import pandas as pd

def get_book_info(books, book_ids):
    all_data = []

    """request = books.volumes().list(
        q=",".join(book_ids)
    )

    response = request.execute()

    # loop through items in response
    for item in response.get("items", []):
        volume_info = item.get("volumeInfo", {})"""

    for book_id in book_ids:
        request = books.volumes().get(volumeId=book_id)
        response = request.execute()

        volume_info = response.get("volumeInfo", {})

        data = {
            'title': volume_info.get('title', 'N/A'),
            'authors': volume_info.get('authors', 'N/A'),
            'publishedDate': volume_info.get('publishedDate', 'N/A'),
            'description': volume_info.get('description', 'N/A'),
            'pageCount': volume_info.get('pageCount', 'N/A'),
            'categories': volume_info.get('categories', 'N/A'),
        }
        all_data.append(data)

    return pd.DataFrame(all_data)


def get_popular_books_by_category(books, category):
    # Fonksiyon, belirli bir kategorideki popüler kitapları almak için kullanılır.
    all_data = []

    # Google Books API'ye bir sorgu yapılıyor.
    request = books.volumes().list(
        q=f"subject:{category}",  # Belirli bir kategoriye ait kitapları sorgulamak için kullanılan sorgu ifadesi.
        orderBy="relevance",  # Kitapların sıralama ölçütü. "relevance" en ilgili olanları ön plana çıkarır.
        maxResults=40  # En fazla alınacak kitap sayısı.
    )

    # API'ye yapılan sorgu sonucunda gelen yanıt alınıyor.
    response = request.execute()

    # Gelen yanıt içindeki her bir kitap için bir döngü oluşturuluyor.
    for item in response.get("items", []):
        # Kitap bilgilerini içeren kısmı alıyoruz.
        volume_info = item.get("volumeInfo", {})

        # Kitap bilgileri bir sözlük içinde düzenleniyor.
        data = {
            'title': volume_info.get('title', 'N/A'),
            'authors': volume_info.get('authors', ['N/A']),
            'publishedDate': volume_info.get('publishedDate', 'N/A'),
            'description': volume_info.get('description', 'N/A'),
            'pageCount': volume_info.get('pageCount', 'N/A'),
            'categories': volume_info.get('categories', ['N/A']),
        }
        
        # Kitap bilgileri listeye ekleniyor.
        all_data.append(data)

    # Oluşturulan kitap bilgileri listesi bir Pandas DataFrame'e dönüştürülüyor ve geri döndürülüyor.
    return pd.DataFrame(all_data)
