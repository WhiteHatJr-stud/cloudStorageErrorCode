import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        
        dbx =  dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        print(f.read())

        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AwiGhdO02RNNjBWV_7XBYnfLPrYQYjk-VWmvgWv_rWplLZfEVTfrFm_5Z5XYpb9mw37j19wJjeXgHUVPVQRi-4tOm43ZyC-lSxw6SbCGjKy3mbzQMwG4No3nY331OCZvEj7c5Ww'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")
    transferData.upload_file(file_from, file_to)

main()