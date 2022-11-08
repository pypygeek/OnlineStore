from .mongodb import conn_mongodb
from datetime import datetime

class Product():
    @staticmethod
    def insert_one(product, thumbnail_img_url, detail_img_url):
        db = conn_mongodb()
        db.products.insert_one({
            'name': product['name'],
            'price': product['price'],
            'description': product['description'],
            'thumbnail_img_url': thumbnail_img_url,
            'detail_img_url': detail_img_url,
            'user': 'admin',
            'created_at': int(datetime.now().timestamp()),
            'updated_at': int(datetime.now().timestamp()),
        })

        # db.products.insert_one({
        #     'name': name,
        #     'price': price,
        #     'description': description
        # })