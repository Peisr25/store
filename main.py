import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.models.product import Product
from src.models.order import Order, OrderItem
from src.routes.user import user_bp
from src.routes.product import product_bp
from src.routes.order import order_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Habilitar CORS para permitir requisições do frontend
CORS(app)

# Registrar blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(product_bp, url_prefix='/api')
app.register_blueprint(order_bp, url_prefix='/api')

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Criar tabelas e dados iniciais
with app.app_context():
    db.create_all()
    
    # Verificar se já existem produtos, se não, criar alguns produtos de exemplo
    if Product.query.count() == 0:
        sample_products = [
            Product(
                name="Vape Pod Premium",
                description="Pod system premium com excelente qualidade de vapor e sabor intenso.",
                price=89.90,
                original_price=119.90,
                category="Pod System",
                image_url="/static/vape-products-1.jpg",
                stock_quantity=50,
                rating=4.8,
                reviews_count=124
            ),
            Product(
                name="Kit Iniciante Completo",
                description="Kit completo para iniciantes com tudo que você precisa para começar.",
                price=149.90,
                original_price=199.90,
                category="Kit Completo",
                image_url="/static/vape-products-2.jpg",
                stock_quantity=30,
                rating=4.9,
                reviews_count=89
            ),
            Product(
                name="Vape Descartável Mix",
                description="Vape descartável com sabores variados, prático e conveniente.",
                price=29.90,
                original_price=39.90,
                category="Descartável",
                image_url="/static/vape-products-3.jpg",
                stock_quantity=100,
                rating=4.7,
                reviews_count=256
            ),
            Product(
                name="Mod Avançado Pro",
                description="Mod avançado para usuários experientes com controle total.",
                price=299.90,
                original_price=399.90,
                category="Mod Avançado",
                image_url="/static/vape-products-4.jpg",
                stock_quantity=20,
                rating=4.9,
                reviews_count=67
            )
        ]
        
        for product in sample_products:
            db.session.add(product)
        
        db.session.commit()
        print("Produtos de exemplo criados!")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
