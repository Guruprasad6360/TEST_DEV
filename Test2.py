@dlt.table(
    name=dlt_catalog.bronze.customer
)

def bronze_customer():
    df = spark.readStream.table('abfss://')
    return df