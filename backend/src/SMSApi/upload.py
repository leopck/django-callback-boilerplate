from rest_framework.decorators import api_view

class Upload:

    def __init__(self, args):
        pass

    def create_upload(self, file):
        print(file)

        return "A file is uploaded"

    def create_upload_http(self, http_link):
        return "A http is uploaded"