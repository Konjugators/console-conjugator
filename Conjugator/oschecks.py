import platform


def getColorAvailability() -> bool:
    return platform.system() != "Windows"
