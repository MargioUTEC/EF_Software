from datetime import datetime

# Contactos: Lista los contactos de un número de teléfono con sus nombres.
# Pagar: Transfiere un valor a otro número (debe ser un contacto). La cuenta debe tener saldo suficiente para hacer la transferencia
# Historial: Muestra el saldo y la lista de operaciones, tanto de envío como de recepción de dinero.


class operacion:
    def __init__(self, numorigen: str, numdestino: str, valor: int):
        self.numorigen = numorigen
        self.numdestino = numdestino
        self.fecha = datetime.now()
        self.valor = valor

class cuenta:
    def __init__(self, num: str, nombres: str, saldo: int, contactos):
        self.num = num
        self.nombres = nombres
        self.saldo = saldo
        self.contactos = contactos
        self.pagoshechos = []
        self.pagosrecibidos = []

    def pagar(self, destino: 'cuenta', valor: int) -> None:
        if (valor <= self.saldo) and (destino.num in self.contactos):
            Operacion = operacion(self.num, destino.num, valor)
            self.pagoshechos.append(Operacion)
            destino.pagosrecibidos.append(Operacion)
            self.saldo = self.saldo - valor
        else:
            print("Transferencia Rechazada")
            print()

    def historial(self):
        hpagoshechos = []
        hpagosrecibidos = []
        for pagohecho in self.pagoshechos:
            hpagoshechos.append({
                'valor': pagohecho.valor,
                'numdestino': pagohecho.numdestino,
                'fecha': pagohecho.fecha.strftime('%Y-%m-%d %H:%M:%S')
            })
        for pago_recibido in self.pagosrecibidos:
            hpagosrecibidos.append({
                'valor': pago_recibido.valor,
                'numorigen': pago_recibido.numorigen,
                'fecha': pago_recibido.fecha.strftime('%Y-%m-%d %H:%M:%S')
            })
        return {
            f'Saldo total de {self.nombres}': self.saldo,
            'Pagos_Hechos': hpagoshechos,
            'Pagos_Recibidos': hpagosrecibidos
        }

if __name__ == "__main__":
    Mcuenta = cuenta('2204', 'Margiory', 7000, ['0412'])
    Scuenta = cuenta('0412', 'Jin', 700, ['2204'])

    Scuenta.pagar(Mcuenta, 100)
    print(Mcuenta.historial())
    print(Scuenta.historial())


    Mcuenta.pagar(Scuenta, 2900)
    print(Mcuenta.historial())
    print(Scuenta.historial())