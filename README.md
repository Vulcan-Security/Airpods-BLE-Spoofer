# AirPods BLE Spoofer 🎧

A Bluetooth Low Energy (BLE) spoofing tool that makes fake AirPods popup appear on iPhones with custom messages.

## ⚠️ Disclaimer
**For educational and authorized testing purposes only.** Only use on devices you own or have explicit permission to test. Vulcan Security is not responsible for misuse.

## 🎯 What It Does
- Spoofs Apple AirPods BLE advertisements
- Makes iPhones show the familiar AirPods connection popup
- Displays custom messages (you can change the defualt one I set)
- Completely harmless - no actual connection occurs

## 🛠️ Supported Hardware

### Broadcasters (Devices that send the packets):
- ✅ Raspberry Pi (all models with Bluetooth)
- ✅ Linux computers with Bluetooth
- ✅ ESP32 microcontrollers
- ✅ Flipper Zero
- ✅ Rooted Android phones

### Targets (Devices that see the popup):
- ✅ iPhones (iOS 10+)
- ✅ iPads
- ✅ MacBooks (shows connection dialog)

## 🚀 Quick Start

### On Raspberry Pi:
```bash
# Install dependencies
sudo apt update
sudo apt install bluez bluez-tools python3 python3-pip

# Clone repository
git clone https://github.com/yourusername/airpods-prank.git
cd airpodsBLEspoofer

# Run the prank
sudo python3 airpodsBLEspoofer.py
