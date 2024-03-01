import apache_beam as beam

with beam.Pipeline() as pipeline:
    api_csv = (
        pipeline
        | "Trigger Pipeline" >> beam.Create([])
        | "Api request" >> beam.ParDo()
        | "JSON to csv" >> beam.Map()
        | "Write pages in a folder" >> beam.io.WriteToText("public_apis", 
                                                           header="API, Description, Auth, HTTPS, Cors, Link, Category")
    )