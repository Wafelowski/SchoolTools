import requests, os

api_key = input("Enter your API key: ")


if not os.path.isfile("ip_addresses.txt"):
    with open("ip_addresses.txt", "w") as f:
        f.write("")
    print("A text file has been created for you. Please paste all the IP addresses there. Divide them by commas or newlines.")
else:
    print("Put the IP addresses inside the text file.")
input("Press Enter to continue...")

with open("ip_addresses.txt", "r") as f:
    addresses = f.read()

def vpn_check(api_key, addresses):
        
    if "," in addresses:
        addresses = addresses.split(",")
    elif "\n" in addresses:
        addresses = addresses.split("\n")
            
    if len(addresses) > 500: # VPNAPI.io allows only 1000 IPs per day in their free plan.
        print("You have entered too many IPs. Please try again with less than 500 IPs.")
        return

    print("\n📡 | Checking IP Adress(es)...")
    vpns = []
    proxy = []
    tor = []

    for ip in addresses:
        try:
            api = requests.get(f"https://vpnapi.io/api/{ip}?key={api_key}")
            api = api.json()
            print(api)

            if api['message'] == 'You have exceeded the maximum daily limit for this API key. Please upgrade your plan.':
                print("\nYou have exceeded the maximum daily limit for this API key!")
                return
            
            if api['security']['vpn'] == True:
                vpns.append(ip)
            if api['security']['proxy'] == True:
                proxy.append(ip)
            if api['security']['tor'] == True:
                tor.append(ip)
        except Exception as e:
            print("VPNCheck error: " + str(e))
            print(f"Error encountered while checking IP {ip}. Cancelling... \nError: {e}")
            return

    print("📡 | VPN \n\n{}\n".format('\n'.join(vpns)))
    print("🌐 | Proxy \n\n{}\n".format('\n'.join(proxy)))
    print("🧅 | Tor \n\n{}\n".format('\n'.join(tor)))

    print("\n Done!")

if __name__ == "__main__":
    vpn_check(api_key, addresses)