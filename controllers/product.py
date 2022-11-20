# 상품과 관련된 API
from flask import request, render_template
from .blueprint import product

from models.product import Product

from datetime import datetime
from werkzeug.utils import secure_filename
import os


@product.route('/form')
def form():
    return render_template('product_form.html')


@product.route('/regist', methods=['POST'])
def regist():
    # 전달받은 상품 정보
    form_data = request.form
    thumbnail_img = request.files.get('thumbnail_img')
    detail_img = request.files.get('detail_img')
    thumbnail_img_url = _upload_file(thumbnail_img)
    detail_img_url = _upload_file(detail_img)
    Product.insert_one(form_data, thumbnail_img_url, detail_img_url)

    return "상품 등록 API 입니다."

# 상품 리스트 조회 API
@product.route('/list')
def get_products():
    # 상품 리스트 정보를 mongo db products 컬렉션에 있는 documents
    products = Product.find()

    return render_template('products.html', products=products)

def _upload_file(img_file):
    timestamp = str(datetime.now().timestamp())
    filename = timestamp + '_' + secure_filename(img_file.filename)
    image_path = f'./static/uploads'
    os.makedirs(image_path, exist_ok=True)
    img = os.path.join(image_path, filename)
    img_file.save(img)

    return f'/static/uploads/' + filename
