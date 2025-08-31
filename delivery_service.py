import requests
import os
from datetime import datetime

class DeliveryService:
    def __init__(self):
        # Configurações das APIs de entrega
        self.uber_api_key = os.getenv('UBER_API_KEY', 'YOUR_UBER_API_KEY_HERE')
        self.uber_customer_id = os.getenv('UBER_CUSTOMER_ID', 'YOUR_UBER_CUSTOMER_ID_HERE')
        self.uber_api_url = 'https://api.uber.com/v1/deliveries'
        
        # Para 99, não há API pública oficial, então vamos simular
        self.moto99_api_key = os.getenv('MOTO99_API_KEY', 'YOUR_99_API_KEY_HERE')
        
        # Endereço da loja (origem das entregas)
        self.store_address = {
            'street': 'Rua das Flores, 123',
            'city': 'São Paulo',
            'state': 'SP',
            'postal_code': '01234-567',
            'latitude': -23.5505,
            'longitude': -46.6333
        }
    
    def get_delivery_quote(self, delivery_address, delivery_method):
        """Obtém cotação de entrega"""
        try:
            if delivery_method == 'pickup':
                return {
                    'method': 'pickup',
                    'name': 'Retirada na Loja',
                    'price': 0.0,
                    'estimated_time': '0 min',
                    'available': True
                }
            elif delivery_method == 'uber':
                return self._get_uber_quote(delivery_address)
            elif delivery_method == '99moto':
                return self._get_99moto_quote(delivery_address)
            else:
                return None
                
        except Exception as e:
            print(f"Error getting delivery quote: {str(e)}")
            return None
    
    def request_delivery(self, order):
        """Solicita entrega para um pedido"""
        try:
            if order.delivery_method == 'pickup':
                return {'success': True, 'tracking_id': None}
            elif order.delivery_method == 'uber':
                return self._request_uber_delivery(order)
            elif order.delivery_method == '99moto':
                return self._request_99moto_delivery(order)
            else:
                return {'success': False, 'error': 'Método de entrega não suportado'}
                
        except Exception as e:
            print(f"Error requesting delivery: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def _get_uber_quote(self, delivery_address):
        """Obtém cotação do Uber Direct"""
        try:
            # Se não tiver API key configurada, retornar valores simulados
            if self.uber_api_key == 'YOUR_UBER_API_KEY_HERE':
                return {
                    'method': 'uber',
                    'name': 'Uber Entrega',
                    'price': 9.50,
                    'estimated_time': '25-40 min',
                    'available': True
                }
            
            headers = {
                'Authorization': f'Bearer {self.uber_api_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'pickup_address': self.store_address,
                'dropoff_address': self._parse_address(delivery_address)
            }
            
            response = requests.post(f'{self.uber_api_url}/quote', 
                                   headers=headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'method': 'uber',
                    'name': 'Uber Entrega',
                    'price': data.get('fee', 9.50),
                    'estimated_time': f"{data.get('duration', 30)} min",
                    'available': True
                }
            else:
                print(f"Uber API error: {response.status_code}")
                return self._get_fallback_uber_quote()
                
        except Exception as e:
            print(f"Error getting Uber quote: {str(e)}")
            return self._get_fallback_uber_quote()
    
    def _get_99moto_quote(self, delivery_address):
        """Obtém cotação da 99 Moto (simulado)"""
        try:
            # Como não há API pública da 99, vamos simular baseado na distância
            # Em uma implementação real, seria necessário integrar com a API corporativa
            
            base_price = 8.50
            distance_factor = self._estimate_distance(delivery_address)
            final_price = base_price + (distance_factor * 0.5)
            
            return {
                'method': '99moto',
                'name': '99 Moto Entrega',
                'price': round(final_price, 2),
                'estimated_time': '30-45 min',
                'available': True
            }
            
        except Exception as e:
            print(f"Error getting 99 Moto quote: {str(e)}")
            return {
                'method': '99moto',
                'name': '99 Moto Entrega',
                'price': 8.50,
                'estimated_time': '30-45 min',
                'available': True
            }
    
    def _request_uber_delivery(self, order):
        """Solicita entrega via Uber Direct"""
        try:
            if self.uber_api_key == 'YOUR_UBER_API_KEY_HERE':
                # Simulação
                return {
                    'success': True,
                    'tracking_id': f'UBER_{order.id}_{datetime.now().strftime("%Y%m%d%H%M")}',
                    'estimated_delivery': '25-40 min'
                }
            
            headers = {
                'Authorization': f'Bearer {self.uber_api_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'pickup_address': self.store_address,
                'dropoff_address': self._parse_address(order.delivery_address),
                'pickup_name': 'VapeStore',
                'pickup_phone': '+5511999999999',
                'dropoff_name': order.customer_name,
                'dropoff_phone': order.customer_phone,
                'external_delivery_id': str(order.id),
                'manifest_items': [
                    {
                        'name': item.product_name,
                        'quantity': item.quantity,
                        'size': 'small'
                    } for item in order.items
                ]
            }
            
            response = requests.post(f'{self.uber_api_url}/deliveries', 
                                   headers=headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'tracking_id': data.get('delivery_id'),
                    'estimated_delivery': data.get('estimated_delivery_time')
                }
            else:
                print(f"Uber delivery request error: {response.status_code}")
                return {'success': False, 'error': 'Falha na solicitação Uber'}
                
        except Exception as e:
            print(f"Error requesting Uber delivery: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def _request_99moto_delivery(self, order):
        """Solicita entrega via 99 Moto (simulado)"""
        try:
            # Simulação da solicitação de entrega
            tracking_id = f'99MOTO_{order.id}_{datetime.now().strftime("%Y%m%d%H%M")}'
            
            return {
                'success': True,
                'tracking_id': tracking_id,
                'estimated_delivery': '30-45 min'
            }
            
        except Exception as e:
            print(f"Error requesting 99 Moto delivery: {str(e)}")
            return {'success': False, 'error': str(e)}
    
    def _parse_address(self, address_string):
        """Converte string de endereço para formato estruturado"""
        # Em uma implementação real, seria necessário usar um serviço de geocoding
        return {
            'street': address_string,
            'city': 'São Paulo',
            'state': 'SP',
            'postal_code': '00000-000'
        }
    
    def _estimate_distance(self, delivery_address):
        """Estima distância baseada no endereço (simulado)"""
        # Em uma implementação real, usaria Google Maps API ou similar
        # Por enquanto, retorna um valor aleatório entre 1 e 10 km
        import random
        return random.uniform(1, 10)
    
    def _get_fallback_uber_quote(self):
        """Retorna cotação padrão do Uber em caso de erro"""
        return {
            'method': 'uber',
            'name': 'Uber Entrega',
            'price': 9.50,
            'estimated_time': '25-40 min',
            'available': True
        }
    
    def get_all_delivery_options(self, delivery_address):
        """Retorna todas as opções de entrega disponíveis"""
        options = []
        
        # Retirada na loja
        pickup = self.get_delivery_quote(delivery_address, 'pickup')
        if pickup:
            options.append(pickup)
        
        # 99 Moto
        moto99 = self.get_delivery_quote(delivery_address, '99moto')
        if moto99:
            options.append(moto99)
        
        # Uber
        uber = self.get_delivery_quote(delivery_address, 'uber')
        if uber:
            options.append(uber)
        
        return options

# Instância global do serviço
delivery_service = DeliveryService()

