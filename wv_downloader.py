import os
from time import sleep


print ("Welcome to WM downloader \n")
sleep (0.7)
os.system ("clear")
print ("<Step 1> \n")
print (" The proggram will download some packs \n")
sleep (1.2)
os.system ("clear")
print ("Downloading sddm <display manager> \n")
print ("If a popup window comes up <select sddm > <NOT! light> \n")
nothing = input ("Press [Enter] to continue")
os.system ("clear")
print ("Please put your password")
os.system ("clear")
os.system ( "sudo apt install sddm")
os.system ("clear")
print ("Done !")
sleep (1.2)
os.system ("clear")
print ("<Step 2> \n")

print ("<Kali> <Ubuntu>")
select_distro = input ("~> ")

print ("<Xfce4> <KDE plasma> <GNOME> <i3> <Awesome> \n")
select_wm = input ("~> ")



if select_distro == ("Kali") or ("kali"):
    if select_wm == ("Xfce4") or ("Xfce"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies kali-desktop-xfce")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("KDE plasma") or ("KDE"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install kali-desktop-kde")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("GNOME") or ("gnome"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install kali-desktop-gnome")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("i3") or ("I3"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt-get -y install i3")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("awesome") or ("Awesome"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install awesome")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")
    else:
        print ("something went wrong \n")
        print ("the proggram will restart ")
        os.system (" /bin/python wv_downloader.py")
        exit()

elif select_distro == ("Ubuntu") or ("ubuntu"):
    if select_wm == ("Xfce4") or ("Xfce"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install xfce4")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("KDE plasma") or ("KDE"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install kde-full")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("GNOME") or ("gnome"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install ubuntu-gnome-desktop")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("i3") or ("I3"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt install i3")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")

    elif select_wm == ("awesome") or ("Awesome"):
        os.system ("clear")
        print ("Sure")
        os.system ("sudo apt-get install awesome")
        os.system ("clear")
        print ("Done")
        sleep (1.2)
        print ("<Step 3> \n")
        print ("Reconfigure files \n")
        os.system ("sudo dpkg-reconfigure lightdm")
        print ("Done !")
        sleep (1.2)
        os.system ("clear")
        print ("<Step finall> \n")
        print ("The system will restart in 5.2 sec \n")
        print ("Goodbye")
        sleep (5.2)
        os.system("sudo init 6")
    else:
        print ("something went wrong \n")
        print ("the proggram will restart ")
        os.system (" /bin/python wv_downloader.py")
        exit()


else:
    print ("something went wrong \n")
    print ("the proggram will restart ")
    os.system (" /bin/python wv_downloader.py")
    exit()

