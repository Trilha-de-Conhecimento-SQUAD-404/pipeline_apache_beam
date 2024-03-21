import apache_beam as beam
from utils.pardo import PublicApis 
from utils.method import json_to_csv_row


with beam.Pipeline() as pipeline:
    api_csv = (
        pipeline
        | "Trigger Pipeline" >> beam.Create([None])
        | "Api request" >> beam.ParDo(PublicApis())
        | "JSON to csv" >> beam.Map(json_to_csv_row)
        | "Write pages in a folder" >> beam.io.WriteToText("data/public_apis", file_name_suffix='.csv',
                                                           header="API, Description, Auth, HTTPS, Cors, Link, Category",  num_shards=1)
    )