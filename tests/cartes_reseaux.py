import re

def obtenir_interfaces_reseau():
    interfaces = []

    try:
        with open('/proc/net/dev', 'r') as f:
            network_info = f.read()

        interfaces_match = re.findall(r'(\w+):\s+\d+', network_info)

        for interface in interfaces_match:
            if interface != 'lo':
                interfaces.append(interface)

    except FileNotFoundError:
        print("Le fichier /proc/net/dev n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

    return interfaces
