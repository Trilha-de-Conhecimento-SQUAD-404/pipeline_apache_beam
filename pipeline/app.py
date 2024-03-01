import apache_beam as beam
from utils.pardo import PublicApis 

with beam.Pipeline() as pipeline:
    api_csv = (
        pipeline
        | "Trigger Pipeline" >> beam.Create([])
        | "Api request" >> beam.ParDo(PublicApis())
        | "JSON to csv" >> beam.Map()
        | "Write pages in a folder" >> beam.io.WriteToText("public_apis", 
                                                           header="API, Description, Auth, HTTPS, Cors, Link, Category")
    )