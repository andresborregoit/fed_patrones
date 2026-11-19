# Patrón Singleton: sistema de logs bancarios


class Logger:
    # Guarda la única instancia permitida.
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            print("Creando Logger...")
            cls._instancia = super().__new__(cls)
        else:
            print("Ya existe Logger. Reutilizando.")
        return cls._instancia

    def log(self, mensaje):
        print(f"[INFO] {mensaje}")


class LoginService:
    def __init__(self):
        self.logger = Logger()

    def iniciar_sesion(self, usuario):
        self.logger.log(f"Usuario {usuario} inició sesión")

    def cerrar_sesion(self, usuario):
        self.logger.log(f"Usuario {usuario} cerró sesión")


class TransferService:
    def __init__(self):
        self.logger = Logger()

    def transferir(self, monto):
        self.logger.log(f"Transferencia realizada por ${monto}")


class AccountService:
    def __init__(self):
        self.logger = Logger()

    def consultar_saldo(self):
        self.logger.log("Consulta de saldo realizada")


def main():
    login_service = LoginService()
    transfer_service = TransferService()
    account_service = AccountService()

    login_service.iniciar_sesion("fede")
    transfer_service.transferir(50000)
    account_service.consultar_saldo()
    login_service.cerrar_sesion("fede")

    print("\n==============================")
    print("VERIFICACIÓN SINGLETON")
    print("==============================")
    print(login_service.logger is transfer_service.logger)
    print(transfer_service.logger is account_service.logger)

    print("\nID LOGIN LOGGER:")
    print(id(login_service.logger))
    print("\nID TRANSFER LOGGER:")
    print(id(transfer_service.logger))
    print("\nID ACCOUNT LOGGER:")
    print(id(account_service.logger))


if __name__ == "__main__":
    main()