import os


def create_target_directory():
    """Fetch .BatteryMonitor folder inside User folder to save audio files generated by GTTS"""
    home_dir = os.path.expanduser("~")
    target_directory = f"{home_dir}/.BatteryMonitor"
    if not os.path.exists(target_directory):
        os.mkdir(target_directory)
    os.chdir(target_directory)

    try:
        import ctypes

        hide_file_flag = 0x02
        ctypes.windll.kernel32.SetFileAttributesW(
            target_directory, hide_file_flag)

    except:
        pass
