import requests
import os
from datetime import datetime

class WhatsAppService:
    def __init__(self):
        # Configurações da WhatsApp Business API
        self.access_token = os.getenv('WHATSAPP_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_HERE')
        self.phone_number_id = os.getenv('WHATSAPP_PHONE_NUMBER_ID', 'YOUR_PHONE_NUMBER_ID_HERE')
        self.business_phone = os.getenv('WHATSAPP_BUSINESS_PHONE', '+5511999999999')
        self.api_url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
        
    def send_order_notification(self, order):
        """Envia notificação de pedido via WhatsApp"""
        try:
            # Formatar mensagem do pedido
            message = self._format_order_message(order)
            
            # Enviar para o número de negócios (lojista)
            success = self._send_message(self.business_phone, message)
            
            if success:
                print(f"WhatsApp notification sent successfully for order {order.id}")
                return True
            else:
                print(f"Failed to send WhatsApp notification for order {order.id}")
                return False
                
        except Exception as e:
            print(f"Error sending WhatsApp notification: {str(e)}")
            return False
    
    def send_order_confirmation_to_customer(self, order):
        """Envia confirmação de pedido para o cliente"""
        try:
            if not order.customer_phone:
                return False
                
            message = self._format_customer_confirmation(order)
            
            # Limpar e formatar número do cliente
            customer_phone = self._format_phone_number(order.customer_phone)
            
            success = self._send_message(customer_phone, message)
            
            if success:
                print(f"Customer confirmation sent successfully for order {order.id}")
                return True
            else:
                print(f"Failed to send customer confirmation for order {order.id}")
                return False
                
        except Exception as e:
            print(f"Error sending customer confirmation: {str(e)}")
            return False
    
    def _send_message(self, phone_number, message):
        """Envia mensagem via WhatsApp Cloud API"""
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'messaging_product': 'whatsapp',
                'to': phone_number,
                'type': 'text',
                'text': {
                    'body': message
                }
            }
            
            # Se não tiver token configurado, apenas simular o envio
            if self.access_token == 'YOUR_ACCESS_TOKEN_HERE':
                print("=== SIMULAÇÃO DE ENVIO WHATSAPP ===")
                print(f"Para: {phone_number}")
                print(f"Mensagem: {message}")
                print("===================================")
                return True
            
            response = requests.post(self.api_url, headers=headers, json=payload)
            
            if response.status_code == 200:
                return True
            else:
                print(f"WhatsApp API error: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"Error in _send_message: {str(e)}")
            return False
    
    def _format_order_message(self, order):
        """Formata mensagem de pedido para o lojista"""
        message = f"""🛍️ *NOVO PEDIDO - VapeStore*

📋 *Pedido:* #{order.id}
👤 *Cliente:* {order.customer_name}
📞 *Telefone:* {order.customer_phone}
📧 *Email:* {order.customer_email or 'Não informado'}

📍 *Endereço de Entrega:*
{order.delivery_address}

🚚 *Método de Entrega:* {self._get_delivery_method_name(order.delivery_method)}
💳 *Pagamento:* {order.payment_method}

📦 *Itens do Pedido:*"""
        
        for item in order.items:
            message += f"\n• {item.product_name} x{item.quantity} - R$ {item.subtotal:.2f}"
        
        message += f"""

💰 *Subtotal:* R$ {order.total_amount - order.delivery_fee:.2f}
🚚 *Taxa de Entrega:* R$ {order.delivery_fee:.2f}
💰 *Total:* R$ {order.total_amount:.2f}

📝 *Observações:* {order.notes or 'Nenhuma'}

⏰ *Data do Pedido:* {order.created_at.strftime('%d/%m/%Y %H:%M')}

🔗 *Link do Pedido:* https://vapestore.com/admin/orders/{order.id}"""
        
        return message
    
    def _format_customer_confirmation(self, order):
        """Formata mensagem de confirmação para o cliente"""
        message = f"""✅ *Pedido Confirmado - VapeStore*

Olá {order.customer_name}! Seu pedido foi confirmado com sucesso.

📋 *Pedido:* #{order.id}
💰 *Total:* R$ {order.total_amount:.2f}
🚚 *Entrega:* {self._get_delivery_method_name(order.delivery_method)}

📦 *Seus itens:*"""
        
        for item in order.items:
            message += f"\n• {item.product_name} x{item.quantity}"
        
        message += f"""

📍 *Endereço de entrega:*
{order.delivery_address}

⏰ *Tempo estimado:* {self._get_estimated_delivery_time(order.delivery_method)}

Obrigado por escolher a VapeStore! 🙏

Para dúvidas, responda esta mensagem."""
        
        return message
    
    def _format_phone_number(self, phone):
        """Formata número de telefone para o padrão internacional"""
        # Remove caracteres especiais
        phone = ''.join(filter(str.isdigit, phone))
        
        # Se não começar com código do país, adicionar +55 (Brasil)
        if not phone.startswith('55'):
            phone = '55' + phone
        
        return '+' + phone
    
    def _get_delivery_method_name(self, method):
        """Retorna nome amigável do método de entrega"""
        methods = {
            'pickup': 'Retirada na Loja',
            '99moto': '99 Moto Entrega',
            'uber': 'Uber Entrega'
        }
        return methods.get(method, method)
    
    def _get_estimated_delivery_time(self, method):
        """Retorna tempo estimado de entrega"""
        times = {
            'pickup': 'Disponível para retirada',
            '99moto': '30-45 minutos',
            'uber': '25-40 minutos'
        }
        return times.get(method, '30-60 minutos')

    def send_status_update_to_customer(self, order, old_status):
        """Envia atualização de status do pedido para o cliente"""
        try:
            if not order.customer_phone:
                return False
                
            message = self._format_status_update_message(order, old_status)
            
            # Limpar e formatar número do cliente
            customer_phone = self._format_phone_number(order.customer_phone)
            
            success = self._send_message(customer_phone, message)
            
            if success:
                print(f"Status update sent successfully for order {order.id}")
                return True
            else:
                print(f"Failed to send status update for order {order.id}")
                return False
                
        except Exception as e:
            print(f"Error sending status update: {str(e)}")
            return False
    
    def _format_status_update_message(self, order, old_status):
        """Formata mensagem de atualização de status"""
        status_messages = {
            'confirmed': f'✅ Seu pedido #{order.id} foi confirmado e está sendo preparado!',
            'preparing': f'👨‍🍳 Seu pedido #{order.id} está sendo preparado com carinho!',
            'delivering': f'🚚 Seu pedido #{order.id} saiu para entrega! Chegará em breve.',
            'delivered': f'🎉 Seu pedido #{order.id} foi entregue! Obrigado por escolher a VapeStore!'
        }
        
        main_message = status_messages.get(order.status, f'📋 Status do seu pedido #{order.id} foi atualizado.')
        
        message = f"""🔔 *Atualização do Pedido - VapeStore*

{main_message}

📋 *Pedido:* #{order.id}
📊 *Status:* {self._get_status_name(order.status)}
💰 *Total:* R$ {order.total_amount:.2f}

Para dúvidas, responda esta mensagem.

VapeStore - Sua satisfação é nossa prioridade! 🙏"""
        
        return message
    
    def _get_status_name(self, status):
        """Retorna nome amigável do status"""
        status_names = {
            'pending': 'Pendente',
            'confirmed': 'Confirmado',
            'preparing': 'Preparando',
            'delivering': 'Em Entrega',
            'delivered': 'Entregue',
            'cancelled': 'Cancelado'
        }
        return status_names.get(status, status)

# Instância global do serviço
whatsapp_service = WhatsAppService()

