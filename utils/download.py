import urllib.request
from languages import get_text

def download_file(url, filename):
    try:
        print(get_text("downloading_file").format(file=filename))
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        print(get_text("download_failed").format(file=filename, msg=str(e)))
        return False
