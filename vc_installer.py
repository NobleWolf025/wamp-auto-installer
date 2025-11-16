import subprocess
from utils.download import download_file
from languages import get_text

VC_DOWNLOADS = {
    "VC 2015-2022 x64": "https://aka.ms/vs/17/release/vc_redist.x64.exe",
    "VC 2015-2022 x86": "https://aka.ms/vs/17/release/vc_redist.x86.exe"
}

def install_vc(name):
    url = VC_DOWNLOADS.get(name)
    if not url:
        return False, get_text("vc_installed_fail").format(msg="URL bulunamadı.")

    filename = url.split("/")[-1]

    # indir
    ok = download_file(url, filename)
    if not ok:
        return False, get_text("vc_installed_fail").format(msg="İndirme başarısız.")

    # yükle
    try:
        print(get_text("vc_installing").format(package=name))
        subprocess.run([filename, "/install", "/quiet", "/norestart"], shell=True)
        return True, get_text("vc_installed_success").format(package=name)
    except Exception as e:
        return False, get_text("vc_installed_fail").format(msg=str(e))
