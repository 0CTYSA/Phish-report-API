# Phish Report Automation Tool

## Descripción

Este script en Python está diseñado para automatizar el proceso de reportar URLs potencialmente maliciosas a través de la API de Phish.Report. Facilita el envío de informes de phishing en masa y almacena los resultados en archivos JSON dentro de una carpeta local.

## Características

- **Reporte en Masa**: Permite reportar hasta 10 URLs a la vez.
- **Automatización de Takedowns**: Inicia automáticamente los procesos de takedown para URLs identificadas como maliciosas.
- **Almacenamiento Local de Resultados**: Guarda la información de contacto de abuso y las respuestas del takedown en archivos JSON.

## Pre-requisitos

Para utilizar este script, necesitas lo siguiente:

- Python 3
- `requests` biblioteca instalada en Python (instala usando `pip install requests`)
- `json` bibliteca instalada en python (instala usando `pip install json`)
- Una clave API válida de Phish.Report

## Configuración

1. Clona este repositorio o descarga los archivos en tu máquina local.
2. Abre el script en tu IDE o editor de texto favorito y reemplaza `'your_real_api_key_here'` con tu clave API real.
3. Asegúrate de que las bibliotecas `requests` y `json` esten instaladas.

## Uso

Para ejecutar el script, sigue estos pasos:

1. Abre una terminal o línea de comandos.
2. Navega hasta el directorio donde se encuentra el script.
3. Ejecuta el script con `python repph.py`.
4. Sigue las instrucciones en pantalla para ingresar las URLs que deseas reportar.
5. Revisa la carpeta "resultados" para ver los archivos JSON con los detalles de los reportes.

## `.gitignore` Configuración

Se ha configurado un archivo `.gitignore` para excluir la carpeta 'resultados' y su contenido del repositorio.

## Advertencia

Utiliza este script con cautela y asegúrate de que solo se reporten URLs que hayas verificado como maliciosas.

## Soporte

Si encuentras algún problema o tienes alguna sugerencia, por favor abre un issue en este repositorio.
