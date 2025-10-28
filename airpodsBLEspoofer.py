import subprocess
import time
import sys

def airpods_spoofer(message, duration=10):
    print(f"Starting AirPods prank: '{message}'")
    
    # Reset Bluetooth interface
    subprocess.run(['sudo', 'hciconfig', 'hci0', 'down'], capture_output=True)
    subprocess.run(['sudo', 'hciconfig', 'hci0', 'up'], capture_output=True)
    
    subprocess.run(['sudo', 'hciconfig', 'hci0', 'name', message], 
                   capture_output=True)
    
    # Apple AirPods advertisement pattern (simplified)
    apple_pattern = "1e ff 4c 00 07 19 01 02 03 04 05 06"
    
    # Set advertising data
    subprocess.run([
        'sudo', 'hcitool', '-i', 'hci0', 'cmd',
        '0x08', '0x0008', apple_pattern
    ], capture_output=True)
    
    subprocess.run([
        'sudo', 'hcitool', '-i', 'hci0', 'cmd', '0x08', '0x000a', '01'
    ], capture_output=True)
    
    print(f"Prank active for {duration} seconds...")
    time.sleep(duration)
    
    subprocess.run([
        'sudo', 'hcitool', '-i', 'hci0', 'cmd', '0x08', '0x000a', '00'
    ], capture_output=True)

if __name__ == "__main__":
    message = "Banned from using Airpods for participation in the 9/11 attacks"
    airpods_spoofer(message, duration=15)
