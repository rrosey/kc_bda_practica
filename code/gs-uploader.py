# Imports the Google Cloud client library
from google.cloud import storage

def upload_blob(bucket_name, blob_name, file_name):
    """Uploads a file to the bucket."""

    # Explicitly use service account credentials by specifying the private key file.
    storage_client = storage.Client.from_service_account_json("key.json")
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_name)

    print(f'File {file_name} uploaded to {bucket_name}')


def main():

    # Para subirlo a una carpeta del bucket se lo indicaremos en el blob name.
    bucket_name = 'gs-kc-airbnb'
    file_name = 'airbnb-listings-lite.csv'
    blob_name = 'datasets/airbnb/airbnb-listings-lite.csv'

    # Ahora cogemos el fichero de airbnb y lo subimos al bucket
    upload_blob(bucket_name=bucket_name, blob_name=blob_name, file_name=file_name)

    # Para subirlo a una carpeta del bucket se lo indicaremos en el blob name.
    file_name = 'idealista-locales_20190912.csv'
    blob_name = 'datasets/idealista/' + file_name

    # Ahora cogemos el fichero del resultado del scraping y lo subimos al bucket
    upload_blob(bucket_name=bucket_name, blob_name=blob_name, file_name=file_name)

    print('Upload completo')

if __name__ == "__main__":
    main()