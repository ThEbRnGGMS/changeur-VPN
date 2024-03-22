import pyautogui
import time

# Ouvrir les paramètres VPN
pyautogui.hotkey('win', 'i')
time.sleep(1)
pyautogui.write("VPN")
time.sleep(1)
pyautogui.press('enter')

# Sélectionner leNouveau serveur VPN VPN à changer
time.sleep(1)
pyautogui.click(x=100, y=200) # Coordonnées à ajuster en fonction de votre écran

# Modifier les paramètres VPN
time.sleep(1)
pyautogui.click(x=500, y=300) # Coordonnées à ajuster en fonction de votre écran

# Changer les paramètres VPN
time.sleep(1)
pyautogui.write("Nouveau serveur VPN")
time.sleep(1)
pyautogui.click(x=800, y=20) # Coordonnées à ajuster en fonction de votre écran

print("Paramètres VPN changés avec succès")