import os
import logging
from apache_beam import DoFn
from requests import get

# Generate file with pipeline information
logging.basicConfig(
    level=logging.INFO, 
    filename="json_to_csv.log", 
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

class PublicApis(DoFn): 
    def process(self, element):    
        url = "https://api.publicapis.org/entries"
        response = get(url)
        public_apis = response.json().get("entries")

        try:                
            logging.info(f"API retornou o status code: {response.status_code}")
            
            # If sucess, return separately each api json 
            if response.status_code == 200: 
                for api in public_apis:
                    yield api
                    
        except Exception as e:
            logging.error(f"Erro na requisição: {e}")