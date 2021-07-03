from io import StringIO
import os
import os.path
print("KCS Auto MacChanger 2021.1.0.3-^")
print("Gerekli paketleri kurdukdan sonra macı değiştirmek için 1 yazın. : Sadece Mac Değiştirmek İçin 2 Yazın : Metin belgesine ağ aygıtını kaydetmek için 3 : Kayıt Edilmiş Ağ Cihazını Kullanmak için 4 : Hakkında Kısmına Bakmak İçin 5 Yazın.")
secenekler = input("")

if secenekler == "1":


 

 os.system("apt update")
 os.system("apt install net-tools")
 os.system("apt install macchanger")
 os.system("ifconfig")
 print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
 agcihazi = input("Ağ aygiti girin:")   
 os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
 print("İşlem tamamlandi!")

if secenekler == "2":
  
 os.system("ifconfig")
 print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
 agcihazi = input("Ağ aygiti girin:")   
 
 os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
 print("İşlem tamamlandi!")

 os.system("exit")
 pass
if secenekler == "3":
  os.system("ifconfig")
  print("Kayıt edilecek ağ aygıtını girin.")
  print("Ağcihazi komutu şuna benzer wlp3s0 wlp2s0 veya wlan0 ağ aygıtı kısmına benzer kodu girin.")
  agcihazi = input("Ağ aygiti girin:")   
  with open("agcihazi.txt", "w") as f:
        agcihazi2 = agcihazi
        f.write(agcihazi2)
        print("agcihazi.txt kayıt edildi.")
os.system("exit")
if secenekler == "4":
 with open("agcihazi.txt","r") as f:
   icerik = f.read() 
   agcihazi = icerik
   os.system("sudo ifconfig "+ agcihazi + " down && sudo service NetworkManager stop && sudo macchanger -r "+ agcihazi+" && sudo ifconfig "+ agcihazi +" up && sudo service NetworkManager start")
   print("İşlem tamamlandi!")

 os.system("exit")
 pass
if secenekler == "5":
 print("Yapımcı : Yeni Yapımcı : Arda KC : Eski Yapımcı Furkan Karasu.")
 