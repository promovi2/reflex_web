# rxconfig.py

import os
import reflex as rx

# Obtén el puerto desde la variable de entorno PORT (por defecto 10000 si no está configurado)
port = int(os.environ.get('PORT', 10000))

config = rx.Config(
    app_name="your_app_name",  # Cambia esto al nombre de tu aplicación
    api_url=f"http://localhost:{port}",  # Asegúrate de que el backend esté configurado para escuchar en este puerto
)
