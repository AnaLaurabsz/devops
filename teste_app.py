import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug 
if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        # Criação do cliente de teste 
        cls.client = app.test_client()
        
    def test_login_token_generation(self):
        
        response = self.client.post('/login') # Testa se a rota de login gera um token de acesso válido
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('access_token', data)
        
        token = data['access_token'] # Verifica se o token é uma string não vazia
        self.assertTrue(isinstance(token, str))
        self.assertTrue(len(token) > 0)        
    
    
    
    def test_protected_route_message_content(self):  # Testa se o conteúdo da mensagem na rota protegida está correto.
        
        auth_response = self.client.post('/login')
        access_token = auth_response.json['access_token']
        
        headers = {'Authorization': f'Bearer {access_token}'}
        
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)

        esperado = "Protected route"
        obtido = response.json['message']
        
        self.assertEqual(obtido, esperado, f"A mensagem deveria ser '{esperado}', mas veio '{obtido}'")
        
        
    def test_swagger_ui_accessible(self):  # Testa se a interface Swagger está acessível.

        response = self.client.get('/swagger/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Swagger UI', response.data)

if __name__ == '__main__':
    unittest.main()
    