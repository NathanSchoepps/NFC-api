import requests
from app.schemas import Token, NFCData

EXTERNAL_AUTH_URL = "https://example.com/api/authenticate"

def authenticate_with_external_service(nfc_data: NFCData) -> Token:
    response = requests.post(EXTERNAL_AUTH_URL, json=nfc_data.dict())
    response.raise_for_status()
    token_data = response.json()
    return Token(**token_data)
