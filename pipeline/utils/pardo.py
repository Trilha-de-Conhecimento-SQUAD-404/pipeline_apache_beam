import os
import logging
from apache_beam import DoFn
from requests import get

# generate file with pipeline information
logging.basicConfig(
    level=logging.INFO, 
    filename="json_to_csv.log", 
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

