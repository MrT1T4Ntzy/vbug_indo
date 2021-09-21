#coding=utf-8
import os
import sys
import time
import random
import socket
import zipfile
import webbrowser

from urllib.request import urlopen as request
from urllib.error import URLError as SocketError

if 'linux' in sys.platform:
  r = "\033[91m" # Red
  g = "\033[92m" # Green
  y = "\033[93m" # Yellow
  p = "\033[94m" # Purple
  P = "\033[95m" # Pink
  c = "\033[96m" # Cyan
  w = "\033[97m" # White
  a = "\033[0m"  # Reset
else:
  # Convert String To Variabel Name
  for i in ['r','g','y','p','P','c','w','a']:
    globals()[i] = ""

# Last Update
UPDATE = "07-07-2021 19:26"

# Random ANSI Code
colors = lambda : random.choice([r,g,y,p,P,c,w])

#
add = [i for i in range(1,60)]

# Logo
logo = f"{r}****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n{p}╔═════════════════════════════════════╗\n║[{y}•{p}] {c}Author : {g}Mr T1T4N Cyber Hood             {p}║\n║[{y}•{p}] {c}GitHub : {w}github.com/MrT1T4N  {p}║\n║[{y}•{p}] {c}WA.    : {y}+62 81219410786        {p} ║\n║[{y}•{p}] {c}UPDATE : {UPDATE}      {p}  ║\n║[{y}•{p}] {c}Python : {colors()}{sys.version[0:6]}                {p}  ║\n║[{y}•{p}] {c}OS     : {colors()}{sys.platform}{' '*(23 - len(sys.platform))}{p} ║\n║[{y}•{p}] {c}Host   : {colors()}{socket.gethostname()}{' '*(24 - len(socket.gethostname()))}{p}║\n║[{y}•{p}] {c}Team.  : {colors()}TNT {colors()}ANONYMOUS {r}INDO{w}NESIA{p} ║\n╚═════════════════════════════════════╝{a}"

# VBUG Menu
virtex= f"""{p} ANVIMA/n {w} Linvima/n {w} PonVima/n{p}] {y}KEMBALI KE MENU UTAMA\n{p}[{r}00{p}] {r}KELUAR DARI PROGRAM{a}"""


# Download File
def Download(path):
  total = 0
  print ("%s[%s!%s] %sDownloading %s%s%s" % (p,y,p,y,c,path,a))
  while 1:
    try:
      data = request("https://sfile.mobi"+path)
      print ("%s[%s✓%s] %sURL : %s" % (p,y,p,y,data.geturl()))
      print ("%s[%s✓%s] %sStatus : %s" % (p,y,p,y,data.status))
      fopen = os.open(path,os.O_WRONLY | os.O_CREAT)
      os.write(fopen,data.read())
      os.close(fopen)
      print ("%s[%s✓%s] %sFile Name : %s" % (p,y,p,g,os.path.basename(path)))
      byte = os.stat(path).st_size
      for b in ['B','KB','MB','GB','TB']:
        if byte < 1024.0:
          byte = "%3.1f %s" % (byte,b)
          break
        else:
          byte /= 1024.0
      print ("%s[%s✓%s] %sFile Size : %s" % (p,y,p,g,byte))
      print ("%s[%s✓%s] %sFile Path : %s" % (p,y,p,g,os.path.realpath(path)))
      var = input('%s[%s?%s] %sLihat VirusNya Di File[%sY%s/%sn%s]%s ' % (p,y,p,w,g,w,r,w,P)).lower()
      if var == 'y':
        os.system ("xdg-open --view "+path)
        break
      else:
        break
    except SocketError as Soc:
      total += 1
      if total == 5:
        print ("%s[%s!%s] %sGagal Terhubung Ke Server\n\n\tCoba :\n\t\t• Nonaktifkan mode pesawat\n\t\t• Aktifkan data seluler atau Wi-Fi\n\t\t• Periksa sinyal di area Anda\n%s%s" % (p,y,p,y,Soc,a))
        exit()
      else:
        print ("%s[%s!%s] %sMencoba menghubungkan ulang ke server" % (p,y,p,y))
        time.sleep(1.5)

# Main Program
def main():
   while 1:
    os.system('clear')
    print (logo)
    try:
      print ("%sPILIH JENIS VIRUSNYA" % (g))
      print ("%s%s%s" % (c,'='*43,a))
      print (virtex)
      v = int(input("%s>>>> %s" % (g,c)))
      if v == 99:
        menu() ; break
      elif v == 0:
        os.abort()
      elif v == 60:
        try:
          print ("%s[%s!%s] %sDownloading elite.apk" % (p,y,p,y))
          data = request("https://sfile.mobi/8h0Ul09NduQ").read()
          shifa = os.open("vbug.apk",os.O_WRONLY | os.O_CREAT)
          os.write(shifa,data)
          os.close(shifa)
          Apk = apkfile.AipFile("vbug.apk")
          print ("%s[✓] File Name : %s" % (g,apk.filename))
          print ("%s[✓] File Path : %s" % (g,os.path.realpath(apk.filename)))
          for file in zip.namelist():
            zip.extract(file)
            print ("%s[✓] %s" % (g,file))
          else:
            print (r + "[!] Exit!")
            break
        except SocketError:
          print ("%s[%s!%s] %sTidak Ada Koneksi%s" % (p,y,p,y,a))
          break
      elif v in add:
        Download("v%d.txt" % (v))
      else:
        raise ValueError
    except ValueError:
      print ("%s[!] Invalid Input!" % (y))
      time.sleep(1.5)

# Menu
def menu():
  os.system('clear')
  print (logo)
  print (g + "MENU UTAMA")
  print ("%s%s" % (c,"="*37))
  print (f'{p}[{y}1{p}] {g}DOWNLOAD FILE VBUG\n{p}[{y}2{p}] {y}LAPORKAN BUG\n{p}[{y}3{p}] {y}ABOUT\n{p}[{y}0{p}] {r}KELUAR')
  choice = input("%s>>> %s" % (y,c))
  if choice == '1' or choice == '01':
    main()
  elif choice == '2' or choice == '02':
    url = "https://wa.me/6281219410786"
    code = webbrowser.open(url)
    if code:
      time.sleep(0.9)
      memu()
    else:
      os.system ("xdg-open "+url)
  elif choice == '3' or choice == '03':
    os.system('clear')
    print (f"{logo}\n{g}INFO SCRIPT\n========================\n{p}[{y}✓{p}] {c}Author: {g}Rahmat adha\n{p}[{y}✓{p}] {c}Team  : {colors()}TNT {colors()}ANONYMOUS {r}INDO{w}NESIA\n{p}[{y}✓{p}] {c}Script: {colors()}{os.path.basename(sys.argv[0])}\n{p}[{y}✓{p}] {c}Path  : {os.path.realpath(sys.argv[0])}\n{p}[{y}✓{p}] {c}Size  : {os.stat(os.path.realpath(sys.argv[0])).st_size} Byte\n{p}[{y}✓{p}] {c}Link  : {colors()}https://github.com/MR-X-Junior/Virtex\n{p}[{y}✓{p}] {c}Update: {colors()}{UPDATE}\n{p}[{y}✓{p}] {c}Versi : 1.1\n\n{g}Contact Me ^_^\n==================\n{p}[{y}✓{p}] {c}Github: {colors()}https://github.com/MR-X-Junior/\n{p}[{y}✓{p}] {c}Fb.   : {colors()}https://www.facebook.com/Anjay.pro098\n{p}[{y}✓{p}] {c}Wa.   : {colors()}+62 85754629509\n{p}[{y}✓{p}] {c}Email : {colors()}termux.indonesia01@gmail.com\n{a}")
  elif choice == '00' or choice == '0':
    os.abort()
  else:
    print ("%s[!] Invalid Input!" % (y))
    time.sleep(0.9)
    menu()

if __name__ == "__main__":
  menu()
