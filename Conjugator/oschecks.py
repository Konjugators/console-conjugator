import platform


def getColorAvailability() -> bool:
    if platform.system() not in ["Linux", "Darwin"]: return False
    return True
