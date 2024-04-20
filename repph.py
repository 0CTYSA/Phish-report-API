import requests
import json
import os

# Función para obtener la información de contacto de abuso para múltiples URLs


def get_abuse_contact_info_bulk(api_key, urls):
    contact_info_results = {}
    for url in urls:
        headers = {
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.get(
            f'https://phish.report/api/v0/hosting', params={'url': url}, headers=headers)
        if response.ok:
            contact_info_results[url] = response.json()
        else:
            contact_info_results[url] = {'error': response.text}
    return contact_info_results

# Función para iniciar la baja de múltiples URLs


def start_takedown_bulk(api_key, urls):
    takedown_responses = {}
    for url in urls:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            'url': url,
            'ignore_duplicates': True
        }
        response = requests.post(
            f'https://phish.report/api/v0/cases', json=payload, headers=headers)
        if response.ok:
            takedown_responses[url] = response.json()
        else:
            takedown_responses[url] = {'error': response.text}
    return takedown_responses

# Función para guardar los resultados en archivos JSON dentro de una carpeta 'resultados'


def save_results_to_files(results, folder='resultados'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for url, data in results.items():
        # Extraer el dominio de la URL
        domain = url.split('//')[-1].split('/')[0]
        file_path = os.path.join(folder, f"{domain}.json")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


# Solicitar al usuario que ingrese las URLs a través de la terminal
urls_to_check = []
print("Por favor, ingrese las URLs que desea verificar (máximo 10). Escriba 'done' cuando haya terminado:")
while len(urls_to_check) < 10:
    url_input = input("Ingrese URL o 'done' para terminar: ")
    if url_input.lower() == 'done':
        break
    urls_to_check.append(url_input)

# Suponiendo que ya tenemos la API key
api_key = 'your_real_api_key_here'  # Reemplaza esto con la clave de API real

# Obtener información de contacto para abuso en masa y guardar resultados
contact_info_bulk = get_abuse_contact_info_bulk(api_key, urls_to_check)
save_results_to_files(contact_info_bulk)

# Iniciar proceso de baja para múltiples URLs maliciosas y guardar resultados
takedown_responses_bulk = start_takedown_bulk(api_key, urls_to_check)
save_results_to_files(takedown_responses_bulk)
