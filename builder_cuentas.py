# Patrón Builder: sistema de cuentas bancarias


class CuentaBancaria:
    def __init__(
        self,
        titular,
        dni,
        tipo_cuenta,
        moneda,
        tarjeta_debito=False,
        chequera=False,
        home_banking=False,
        limite_extraccion=0,
    ):
        self.titular = titular
        self.dni = dni
        self.tipo_cuenta = tipo_cuenta
        self.moneda = moneda
        self.tarjeta_debito = tarjeta_debito
        self.chequera = chequera
        self.home_banking = home_banking
        self.limite_extraccion = limite_extraccion

    def mostrar_datos(self):
        print("\n==============================")
        print("DATOS DE LA CUENTA")
        print("==============================")
        print(f"Titular: {self.titular}")
        print(f"DNI: {self.dni}")
        print(f"Tipo: {self.tipo_cuenta}")
        print(f"Moneda: {self.moneda}")
        print(f"Tarjeta Débito: {self.tarjeta_debito}")
        print(f"Chequera: {self.chequera}")
        print(f"Home Banking: {self.home_banking}")
        print(f"Límite extracción: ${self.limite_extraccion}")


class CuentaBancariaBuilder:
    def __init__(self):
        self.titular = None
        self.dni = None
        self.tipo_cuenta = None
        self.moneda = None
        self.tarjeta_debito = False
        self.chequera = False
        self.home_banking = False
        self.limite_extraccion = 0

    def con_titular(self, titular):
        self.titular = titular
        return self

    def con_dni(self, dni):
        self.dni = dni
        return self

    def con_tipo_cuenta(self, tipo):
        self.tipo_cuenta = tipo
        return self

    def con_moneda(self, moneda):
        self.moneda = moneda
        return self

    def con_tarjeta_debito(self):
        self.tarjeta_debito = True
        return self

    def con_chequera(self):
        self.chequera = True
        return self

    def con_home_banking(self):
        self.home_banking = True
        return self

    def con_limite_extraccion(self, limite):
        self.limite_extraccion = limite
        return self

    def construir(self):
        return CuentaBancaria(
            self.titular,
            self.dni,
            self.tipo_cuenta,
            self.moneda,
            self.tarjeta_debito,
            self.chequera,
            self.home_banking,
            self.limite_extraccion,
        )


def main():
    cuenta_basica = (
        CuentaBancariaBuilder()
        .con_titular("Fede")
        .con_dni("12345678")
        .con_tipo_cuenta("Caja de Ahorro")
        .con_moneda("ARS")
        .con_home_banking()
        .con_tarjeta_debito()
        .construir()
    )

    cuenta_premium = (
        CuentaBancariaBuilder()
        .con_titular("Ana")
        .con_dni("87654321")
        .con_tipo_cuenta("Cuenta Corriente")
        .con_moneda("USD")
        .con_home_banking()
        .con_tarjeta_debito()
        .con_chequera()
        .con_limite_extraccion(2000000)
        .construir()
    )

    cuenta_basica.mostrar_datos()
    cuenta_premium.mostrar_datos()


if __name__ == "__main__":
    main()