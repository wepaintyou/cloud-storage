from google.cloud import storage
import os


class GCStorage:
    def __init__(self, bucket_name, project_id=None):
        self.client = storage.Client(project=project_id)
        self.bucket = self.client.get_bucket(bucket_name)

    def set_bucket(self, bucket_name):
        self.bucket = self.client.get_bucket(bucket_name)

    def upload_file(self, blob_destination, file_path):
        blob = self.bucket.blob(blob_destination)
        blob.upload_from_filename(file_path)

    def download_file(self, destination_filename, blob_name):
        blob = self.bucket.blob(blob_name)
        blob.download_to_filename(destination_filename)

    def list_blobs(self, folder=None):
        return self.bucket.list_blobs(prefix=folder)

    def download_files_from_folder(self, folder, destination_folder):
        blobs = self.list_blobs(folder)
        for blob in blobs:
            if not blob.name.endswith("/"):
                # This blob is not a directory!
                print(f"Downloading file [{blob.name}]")
                filename = blob.name.split("/")[-1]
                blob.download_to_filename(os.path.join(destination_folder, filename))


if __name__ == "__main__":

    bucket_name = "dreambooth-bucket"
    project_id = "bionic-repeater-368120"

    # Construct GCStorage instance
    gcs = GCStorage(bucket_name, project_id)

    # List files
    blobs = gcs.list_blobs()
    print([b for b in blobs])
