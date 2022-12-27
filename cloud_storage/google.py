from google.cloud import storage
import os

class GCStorage:
    def __init__(self, project_id=None):
        self.client = storage.Client(project=project_id)

    def get_bucket(self, bucket_name):
        return self.client.bucket(bucket_name)

    def upload_model(self, bucket, blob_destination, model_path):
        model_name = model_path.split('/')[-1]
        blob_destination += model_name
        blob = bucket.blob(blob_destination)
        blob.upload_from_filename(model_path)
        return blob

    def list_blobs(self, bucket, folder=None):
        return bucket.list_blobs(prefix=folder)

    def download_files_from_folder(self, bucket, folder, destination_folder):
        blobs = self.list_blobs(bucket, folder)
        for blob in blobs:
            if not blob.name.endswith('/'):
                # This blob is not a directory!
                print(f'Downloading file [{blob.name}]')
                filename = blob.name.split("/")[-1]
                blob.download_to_filename(os.path.join(destination_folder, filename))

if __name__ == "__main__":
    
    bucket_name = "dreambooth-bucket"
    project_id = "bionic-repeater-368120"

    # Construct GCStorage instance
    gcs = GCStorage(project_id)

    # Cloud Storage bucket
    bucket_gcs = gcs.get_bucket(bucket_name)
    
    # List files
    blobs = gcs.list_blobs(bucket_gcs)
    print([b for b in blobs])
