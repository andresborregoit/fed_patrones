# Patrones de diseño: Builder y Singleton

Este repositorio contiene dos ejemplos ejecutables de patrones creacionales en Python.

## Archivos

- `builder_cuentas.py`: aplica Builder para crear cuentas bancarias básicas y premium. El builder permite configurar los datos obligatorios y habilitar servicios opcionales mediante llamadas encadenadas antes de construir la cuenta.
- `singleton_logs.py`: aplica Singleton para compartir una única instancia de `Logger` entre los servicios de login, transferencias y consultas de cuenta. Al final comprueba que los servicios usan el mismo objeto.

## Requisitos y ejecución

Se requiere Python 3.10 o superior. No hay dependencias externas.

Desde una terminal ubicada en la carpeta del proyecto, ejecutar:

```bash
python builder_cuentas.py
python singleton_logs.py
```