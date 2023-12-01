from flask import Flask, jsonify, request, make_response #Instalar flask con "pip install flask"
from methods import *


app = Flask(__name__)


#Creamos la data con los ejemplos presentados en el enunciado

Data = {
        '21345' : cuenta('21345', 'Arnaldo', 200, ['123', '456']), '123': cuenta('123','Luisa',450,['456']), '456': cuenta('456','Andrea','300',['21345'])
}

#Implementando endpoint 1 => /billetera/contactos?minumero=21345

@app.route('/billetera/contactos')
def contactos():
    num = request.args.get('minumero')
    if num in Data:
        cuenta = Data[num]
        contactos = cuenta.contactos
        return jsonify({numcontact: Data[numcontact].nombres for numcontact in contactos})
    else:
        response = jsonify({"Error 404!!!"})
        response.status_code = 404
        return make_response(response)
    
# Implementando endpoint 2 => /billetera/pagar?minumero=21345&numerodestino=123&valor=100
@app.route('/billetera/pagar')
def fechapago():
    num = request.args.get('minumero')
    numdestino = request.args.get('numerodestino')
    valor: int = int(request.args.get('valor'))
    if (num in Data) and (numdestino in Data):
        cuenta = Data[num]
        if (valor <= cuenta.saldo):
            cuenta_destino = Data[numdestino]
            cuenta.pagar(cuenta_destino, valor)
            return jsonify({"Realizado en": datetime.now()})
        else:
            response = jsonify({"No se pudo ver fecha de pago"})
            response.status_code = 404
            return make_response(response)
    else:
        response = jsonify({"Error 404!!!"})
        response.status_code = 404
        return make_response(response)
    
# Implementando endpoint 3 => /billetera/historial?minumero=123

@app.route('/billetera/historial')
def historial():
    num = request.args.get('minumero')
    if num in Data:
        cuenta = Data[num]
        return jsonify(cuenta.historial())
    else:
        response = jsonify({"No se pudo visualizar historial"})
        response.status_code = 404
        return make_response(response)


if __name__ == '__main__':
    app.run()