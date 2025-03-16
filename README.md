BLE Jammer Script

A Python script that scans for Bluetooth Low Energy (BLE) devices and attempts to flood a selected device with junk data.

⚠️ Disclaimer

This script is for educational and research purposes only. Unauthorized use of Bluetooth jamming or interference may be illegal in your country. Please use this responsibly.

🔧 Requirements

Before running this script, ensure your Kali Linux environment has the necessary dependencies.

1️⃣ Install Dependencies

Run the following command to install the required packages:

sudo apt update && sudo apt install -y python3-pip bluetooth libbluetooth-dev

pip3 install bluepy

2️⃣ Enable Bluetooth Interface

Ensure that your Bluetooth adapter is properly recognized by running:

hciconfig

If your adapter is listed but not up, enable it:

sudo hciconfig hci0 up

3️⃣ Clone the Repository

Download the script from GitHub:

git clone https://github.com/ekomsSavior/Ble_Jam
cd BLE-Jammer

4️⃣ Run the Script

Execute the Ble_jam.py script to scan for BLE devices:

python3 ble_jammer.py

The script will display a list of detected BLE devices. Choose the device index you want to attack.

5️⃣ Select Target Device

After scanning, enter the index number of the BLE device to start spamming:

[*] Enter the index of the device to spam: 0

The script will attempt to connect and send junk data.

🛑 Stop the Attack

Press CTRL + C to stop the script at any time.

🛠 Troubleshooting

✅ “bluepy not found” error

If bluepy is not installed correctly, try:

pip3 install --upgrade bluepy

✅ “Failed to connect to device” error

Ensure your Bluetooth adapter is working:

sudo hciconfig hci0 reset

Then restart the script.

📜 Legal & Ethical Considerations
	•	This script is meant for testing your own devices.
	•	DO NOT use this on unauthorized networks or devices.
	•	Use responsibly in controlled enviroments.
