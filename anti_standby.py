import ctypes
import time
import sys

SPI_SET_SCREENSAVEACTIVE = 0x0011
ES_CONTINUOUS         = 0x80000000
ES_SYSTEM_REQUIRED    = 0x00000001
ES_DISPLAY_REQUIRED   = 0x00000002

def prevent_standby():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )
    ctypes.windll.user32.SystemParametersInfoA(
        SPI_SET_SCREENSAVEACTIVE, 0, None, 0
    )
    print("✅ Đã kích hoạt chế độ chống standby.")
    print("   Nhấn Ctrl+C để thoát và khôi phục trạng thái ban đầu.")

def restore_state():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
    ctypes.windll.user32.SystemParametersInfoA(
        SPI_SET_SCREENSAVEACTIVE, 1, None, 0
    )
    print("\n🔄 Đã khôi phục trạng thái. Máy tính có thể standby bình thường.")

if __name__ == "__main__":
    try:
        prevent_standby()
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        restore_state()
        sys.exit(0)
