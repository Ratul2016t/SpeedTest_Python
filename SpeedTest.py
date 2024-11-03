import speedtest
import requests
import subprocess
import platform

def get_public_ip():
    # Fetch the public IP address
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except requests.RequestException as e:
        print("Error fetching IP address:", e)
        return None

def test_internet_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()
    
    # Get download and upload speeds (in bits per second)
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    
    # Display the results
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

def get_ipconfig():
    # Determine OS and execute appropriate command
    try:
        if platform.system() == "Windows":
            # Run `ipconfig` on Windows
            result = subprocess.check_output("ipconfig", text=True)
        else:
            # Run `ifconfig` on Unix-based systems
            result = subprocess.check_output("ifconfig", text=True)
        print("\nNetwork Configuration:")
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error fetching network configuration:", e)

def main():
    # Get and display the IP address
    ip_address = get_public_ip()
    if ip_address:
        print("Your Public IP Address:", ip_address)
    
    # Perform the speed test
    print("\nTesting internet speed...")
    test_internet_speed()
    
    # Display ipconfig or ifconfig information
    print("\nFetching network configuration...")
    get_ipconfig()

if __name__ == "__main__":
    main()
