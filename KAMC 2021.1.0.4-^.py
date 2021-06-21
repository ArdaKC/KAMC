from io import StringIO
import os
import os.path

print("Gerekli Paketleri Kurmak İçin : 1")
print("Gerekli Paketleri Kurmak Ve Ardından Mac Değiştirmek İçin : 2")
print("Ağ Cihazını Kaydederek Daha Sonra Kullanmak İçin : 3")
print("Metin Belgesine Kayıt Edilmiş Ağ Cihazını Kullanmak İçin : 4")
print("Hakkında Kısmına Bakmak İçin : 5")
secenekler = input("")
if secenekler == "1":
    print("Hangi dağıtımı kullanıyorsunuz?")
    print("ARCH : 1")
    print("OPENSUSE : 2")
    print("Debian & Ubuntu : 3")
    print("Fedora : 4")
    dagitim = input("")
    if dagitim == "1":
     os.system("pacman -Syy")
     os.system("pacman -S net-tools-deprecated")
     os.system("pacman -S macchanger")


     print("İşlem tamamlandi!")
     
    if dagitim == "2":
     os.system("zypper refresh")
     os.system("zypper install net-tools-deprecated")
     os.system("zypper install macchanger")
   

     print("İşlem tamamlandi!")
  
  
    if dagitim == "3":
     os.system("apt update")
     os.system("apt install net-tools -y")
     os.system("apt install macchanger -y")
     print("İşlem tamamlandi!")
    if dagitim == "4":
     os.system("dnf upgrade --refresh")
     os.system("dnf install net-tools")
     os.system("dnf install net-tools-deprecated")
     os.system("dnf install macchanger")
     print("İşlem tamamlandi!")
if secenekler == "2":
    print("Hangi dağıtımı kullanıyorsunuz?")
    print("ARCH : 1")
    print("OPENSUSE : 2")
    print("Debian & Ubuntu : 3")
    print("Fedora : 4")

    dagitim = input("")
    if dagitim == "1":
     os.system("pacman -Syy")
     os.system("pacman -S net-tools-deprecated")
     os.system("pacman -S macchanger")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
     print("İşlem tamamlandi!")

    if dagitim == "2":
     os.system("zypper refresh")
     os.system("zypper install net-tools-deprecated")
     os.system("zypper install macchanger")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
     print("İşlem tamamlandi!")
  
  
    if dagitim == "3":
     os.system("apt update")
     os.system("apt install net-tools -y")
     os.system("apt install macchanger -y")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
     print("İşlem tamamlandi!")
    if dagitim == "4":
     os.system("dnf upgrade --refresh")
     os.system("dnf install net-tools")
     os.system("dnf install net-tools-deprecated")
     os.system("dnf install macchanger")
     print("İşlem tamamlandi!")
     os.system("ifconfig")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
     print("İşlem tamamlandi!")
if secenekler == "3":
  
    os.system("ifconfig")
    print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
    agcihazi = input("Ağ aygiti girin:")   
 
    os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
    print("İşlem tamamlandi!")
    os.system("exit")

if secenekler == "4":
     os.system("ifconfig")
     print("Kayıt edilecek ağ aygıtını girin.")
     print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
     agcihazi = input("Ağ aygiti girin:")   
     with open("agcihazi.txt", "w") as f:
         agcihazi2 = agcihazi
         f.write(agcihazi2)
         print("agcihazi.txt kayıt edildi.")
         os.system("exit")
if secenekler == "5":
   with open("agcihazi.txt","r") as f:
       icerik = f.read() 
       agcihazi = icerik
       os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
       print("İşlem tamamlandi!")

       os.system("exit")
       pass
if secenekler == "6":
 print("Yeni Yapımcı : Arda KC : Eski Yapımcı Furkan Karasu.")
pass
