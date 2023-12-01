import unittest as ut
import json
from flask.testing import FlaskClient
from pregunta1 import app

app.testing = True
client = FlaskClient(app)

#CASO UNO (ÉXITO)


class TestAPI(ut.TestCase):
    def setUp(self):
        self.app = app.test_client()


    #Caso de prueba exitoso: Obtiene todos los contactos de de cierto numero
    def test_contactos(self):
        response = self.app.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'123': 'Luisa', '456': 'Andrea'})

    #Caso de prueba erróneo 1 (PAGA A ALGUIEN QUE NO ESTÁ EN SUS CONTACTOS)
    def test_pagar(self):
        response = self.app.get('/billetera/pagar?minumero=21345&numerodestino=123456&valor=10')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'Error 404'})

    #Caso de prueba erróneo 2 (CUENTA NUMERO 7 NO EXISTE, POR ESO DA ERROR)
    def test_historial(self):
        response = self.app.get('/billetera/historial?minumero=7')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"Error": "Transacción no encontrada"})

    #Caso de prueba erróneo 3 (Testeando función no definida)
    def test_saldo(self):
        response = self.app.get('/billetera/saldo?minumero=123')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'Error': 'Error interno del servidor'})

if __name__ == '__main__':
    ut.main()