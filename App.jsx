import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { ShoppingCart, Menu, X, Star, Heart, Search } from 'lucide-react'
import vapeProducts1 from './assets/vape-products-1.jpg'
import vapeProducts2 from './assets/vape-products-2.jpg'
import vapeProducts3 from './assets/vape-products-3.jpg'
import vapeProducts4 from './assets/vape-products-4.jpg'
import './App.css'

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [cartItems, setCartItems] = useState(0)

  const products = [
    {
      id: 1,
      name: "Vape Pod Premium",
      price: 89.90,
      originalPrice: 119.90,
      image: vapeProducts1,
      rating: 4.8,
      reviews: 124,
      category: "Pod System"
    },
    {
      id: 2,
      name: "Kit Iniciante Completo",
      price: 149.90,
      originalPrice: 199.90,
      image: vapeProducts2,
      rating: 4.9,
      reviews: 89,
      category: "Kit Completo"
    },
    {
      id: 3,
      name: "Vape Descartável Mix",
      price: 29.90,
      originalPrice: 39.90,
      image: vapeProducts3,
      rating: 4.7,
      reviews: 256,
      category: "Descartável"
    },
    {
      id: 4,
      name: "Mod Avançado Pro",
      price: 299.90,
      originalPrice: 399.90,
      image: vapeProducts4,
      rating: 4.9,
      reviews: 67,
      category: "Mod Avançado"
    }
  ]

  const addToCart = (product) => {
    setCartItems(cartItems + 1)
    // Aqui seria implementada a lógica real do carrinho
    console.log('Produto adicionado ao carrinho:', product)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <header className="bg-black/20 backdrop-blur-md border-b border-white/10 sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            {/* Logo */}
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">V</span>
              </div>
              <h1 className="text-2xl font-bold text-white">VapeStore</h1>
            </div>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex items-center space-x-8">
              <a href="#" className="text-white hover:text-purple-300 transition-colors">Início</a>
              <a href="#" className="text-white hover:text-purple-300 transition-colors">Produtos</a>
              <a href="#" className="text-white hover:text-purple-300 transition-colors">Categorias</a>
              <a href="#" className="text-white hover:text-purple-300 transition-colors">Sobre</a>
              <a href="#" className="text-white hover:text-purple-300 transition-colors">Contato</a>
            </nav>

            {/* Search and Cart */}
            <div className="flex items-center space-x-4">
              <div className="hidden md:flex items-center bg-white/10 rounded-lg px-3 py-2">
                <Search className="w-4 h-4 text-white/70 mr-2" />
                <input 
                  type="text" 
                  placeholder="Buscar produtos..." 
                  className="bg-transparent text-white placeholder-white/70 outline-none w-40"
                />
              </div>
              
              <Button 
                variant="outline" 
                size="sm" 
                className="relative bg-white/10 border-white/20 text-white hover:bg-white/20"
              >
                <ShoppingCart className="w-4 h-4" />
                {cartItems > 0 && (
                  <span className="absolute -top-2 -right-2 bg-purple-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                    {cartItems}
                  </span>
                )}
              </Button>

              {/* Mobile Menu Button */}
              <Button
                variant="ghost"
                size="sm"
                className="md:hidden text-white"
                onClick={() => setIsMenuOpen(!isMenuOpen)}
              >
                {isMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
              </Button>
            </div>
          </div>

          {/* Mobile Navigation */}
          {isMenuOpen && (
            <nav className="md:hidden mt-4 pb-4 border-t border-white/10 pt-4">
              <div className="flex flex-col space-y-3">
                <a href="#" className="text-white hover:text-purple-300 transition-colors">Início</a>
                <a href="#" className="text-white hover:text-purple-300 transition-colors">Produtos</a>
                <a href="#" className="text-white hover:text-purple-300 transition-colors">Categorias</a>
                <a href="#" className="text-white hover:text-purple-300 transition-colors">Sobre</a>
                <a href="#" className="text-white hover:text-purple-300 transition-colors">Contato</a>
              </div>
            </nav>
          )}
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-20 px-4">
        <div className="container mx-auto text-center">
          <h2 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            Sua Loja de
            <span className="bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent"> Vapes</span>
            <br />Online
          </h2>
          <p className="text-xl text-white/80 mb-8 max-w-2xl mx-auto">
            Descubra os melhores produtos de vaping com qualidade premium, 
            entrega rápida e atendimento especializado via WhatsApp.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white px-8 py-3">
              Ver Produtos
            </Button>
            <Button size="lg" variant="outline" className="border-white/30 text-white hover:bg-white/10 px-8 py-3">
              Falar no WhatsApp
            </Button>
          </div>
        </div>
      </section>

      {/* Products Section */}
      <section className="py-16 px-4">
        <div className="container mx-auto">
          <div className="text-center mb-12">
            <h3 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Produtos em Destaque
            </h3>
            <p className="text-white/70 text-lg">
              Selecionamos os melhores produtos para você
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {products.map((product) => (
              <div key={product.id} className="bg-white/10 backdrop-blur-md rounded-xl p-6 border border-white/20 hover:border-purple-400/50 transition-all duration-300 group">
                <div className="relative mb-4">
                  <img 
                    src={product.image} 
                    alt={product.name}
                    className="w-full h-48 object-cover rounded-lg"
                  />
                  <Button
                    size="sm"
                    variant="ghost"
                    className="absolute top-2 right-2 text-white hover:text-pink-400 bg-black/20 hover:bg-black/40"
                  >
                    <Heart className="w-4 h-4" />
                  </Button>
                  {product.originalPrice > product.price && (
                    <div className="absolute top-2 left-2 bg-red-500 text-white text-xs px-2 py-1 rounded">
                      -{Math.round(((product.originalPrice - product.price) / product.originalPrice) * 100)}%
                    </div>
                  )}
                </div>

                <div className="space-y-2">
                  <span className="text-purple-300 text-sm">{product.category}</span>
                  <h4 className="text-white font-semibold text-lg">{product.name}</h4>
                  
                  <div className="flex items-center space-x-1">
                    {[...Array(5)].map((_, i) => (
                      <Star 
                        key={i} 
                        className={`w-4 h-4 ${i < Math.floor(product.rating) ? 'text-yellow-400 fill-current' : 'text-gray-400'}`} 
                      />
                    ))}
                    <span className="text-white/70 text-sm ml-2">({product.reviews})</span>
                  </div>

                  <div className="flex items-center space-x-2">
                    <span className="text-2xl font-bold text-white">R$ {product.price.toFixed(2)}</span>
                    {product.originalPrice > product.price && (
                      <span className="text-white/50 line-through">R$ {product.originalPrice.toFixed(2)}</span>
                    )}
                  </div>

                  <Button 
                    className="w-full bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 text-white mt-4"
                    onClick={() => addToCart(product)}
                  >
                    Adicionar ao Carrinho
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 px-4 bg-black/20">
        <div className="container mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <ShoppingCart className="w-8 h-8 text-white" />
              </div>
              <h4 className="text-xl font-semibold text-white mb-2">Entrega Rápida</h4>
              <p className="text-white/70">Entrega via 99 Moto e Uber em até 1 hora na sua região</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <Heart className="w-8 h-8 text-white" />
              </div>
              <h4 className="text-xl font-semibold text-white mb-2">Qualidade Premium</h4>
              <p className="text-white/70">Produtos selecionados com garantia e qualidade certificada</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full flex items-center justify-center mx-auto mb-4">
                <Search className="w-8 h-8 text-white" />
              </div>
              <h4 className="text-xl font-semibold text-white mb-2">Atendimento WhatsApp</h4>
              <p className="text-white/70">Suporte especializado via WhatsApp para tirar suas dúvidas</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-black/40 py-12 px-4">
        <div className="container mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold text-lg">V</span>
                </div>
                <h5 className="text-xl font-bold text-white">VapeStore</h5>
              </div>
              <p className="text-white/70">
                Sua loja online de vapes com os melhores produtos e atendimento especializado.
              </p>
            </div>
            
            <div>
              <h6 className="text-white font-semibold mb-4">Produtos</h6>
              <ul className="space-y-2 text-white/70">
                <li><a href="#" className="hover:text-white transition-colors">Pod Systems</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Mods</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Descartáveis</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Acessórios</a></li>
              </ul>
            </div>
            
            <div>
              <h6 className="text-white font-semibold mb-4">Atendimento</h6>
              <ul className="space-y-2 text-white/70">
                <li><a href="#" className="hover:text-white transition-colors">WhatsApp</a></li>
                <li><a href="#" className="hover:text-white transition-colors">FAQ</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Trocas e Devoluções</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Garantia</a></li>
              </ul>
            </div>
            
            <div>
              <h6 className="text-white font-semibold mb-4">Contato</h6>
              <ul className="space-y-2 text-white/70">
                <li>WhatsApp: (11) 99999-9999</li>
                <li>Email: contato@vapestore.com</li>
                <li>Horário: 9h às 18h</li>
              </ul>
            </div>
          </div>
          
          <div className="border-t border-white/20 mt-8 pt-8 text-center">
            <p className="text-white/70">
              © 2025 VapeStore. Todos os direitos reservados.
            </p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App

