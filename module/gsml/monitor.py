from win32api import EnumDisplayMonitors, GetMonitorInfo

def get_monitors(n):
    monitors = [GetMonitorInfo(monitor[0]) for monitor in EnumDisplayMonitors()]
    screen_size = (monitors[n-1]['Monitor'][2] - monitors[n-1]['Monitor'][0],
                   monitors[n-1]['Monitor'][3] - monitors[n-1]['Monitor'][1])
    return screen_size