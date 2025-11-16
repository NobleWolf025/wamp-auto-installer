import winreg

def is_vc_installed(reg_path_list):
    for path in reg_path_list:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            value, _ = winreg.QueryValueEx(key, "Installed")
            if value == 1:
                return True
        except FileNotFoundError:
            continue
    return False

VC_LIST = {
    "VC 2015-2022 x64": [
        r"SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64",
        r"SOFTWARE\WOW6432Node\Microsoft\VisualStudio\14.0\VC\Runtimes\x64"
    ],
    "VC 2015-2022 x86": [
        r"SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x86",
        r"SOFTWARE\WOW6432Node\Microsoft\VisualStudio\14.0\VC\Runtimes\x86"
    ],
}

def get_missing_vc():
    missing = []
    for name, paths in VC_LIST.items():
        if not is_vc_installed(paths):
            missing.append(name)
    return missing
