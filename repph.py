import requests

# Funciones para interactuar con la API de Phish Report

def get_abuse_contact_info(api_key, url):
    """
    Obtiene la información de contacto para reportar abusos para una URL/IP dada.
    
    :param api_key: Clave API del usuario para la autenticación.
    :param url: La URL, dominio o dirección IP para la cual se busca información de contacto.
    :return: Un diccionario con la respuesta de la API.
    """
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(f'https://phish.report/api/v0/hosting', params={'url': url}, headers=headers)
    
    if response.ok:
        return response.json()
    else:
        return {'error': response.text}

def start_takedown(api_key, url, ignore_duplicates=False):
    """
    Inicia el proceso de baja de una URL maliciosa.
    
    :param api_key: Clave API del usuario para la autenticación.
    :param url: La URL maliciosa que se quiere dar de baja.
    :param ignore_duplicates: Si se debe ignorar si ya hay un caso abierto para esa URL.
    :return: Un diccionario con la respuesta de la API.
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    payload = {
        'url': url,
        'ignore_duplicates': ignore_duplicates
    }
    response = requests.post(f'https://phish.report/api/v0/cases', json=payload, headers=headers)
    
    if response.ok:
        return response.json()
    else:
        return {'error': response.text}

# Ejemplo de uso de las funciones

# Reemplazar con tu clave API real
api_key = 'your_real_api_key_here'
url_to_check = 'http://suspicious.url.here'

# Obtener información de contacto para abuso
contact_info = get_abuse_contact_info(api_key, url_to_check)
print(contact_info)

# Iniciar proceso de baja para una URL maliciosa
takedown_response = start_takedown(api_key, url_to_check)
print(takedown_response)
