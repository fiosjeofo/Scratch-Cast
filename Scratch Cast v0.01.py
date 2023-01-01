print("Setting up scratchattach and other libaries, Please wait.")
with open("config.txt", "r") as config:
    config = (config.readlines())
    import os
    import time
    #import system libs
    
    if (config[9].replace("\n", "") == "n"):
        os.system("pip install scratchattach")
        os.system("pip install pillow")
        os.system("pip install Image")
        os.system("pip install pyautogui")
    else:
        print("Skipping downloads...")
    #skip if config calls it
    from PIL import Image
    import scratchattach as scratch3
    import pyautogui
    from scratchattach import Encoding
    input("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to Scratch Cast! this program will cast your screen to the broad web. This script was made my Anonymous_cat1 on scratch.\n\nPlease be aware that that Scratch Team does not take too kindly to cloud projects that allow unmoderated content to be shown.\n\nAnonymous_cat1 is NOT responsible for any Account Blocks, Project Takedowns or Instantaneous Death that may result by using this program.\n\nClick ENTER to continue.")
    #setup stuff
    
    print('\nThe config file contains the username "' + config[12].replace("\n", "") +  '"')
    print('The config file contains the password "' + config[15].replace("\n", "") +  '"')
    print('The config file says the project ID you want to connect to is "' + config[18].replace("\n", "") +  '"\n')
    input("If these are NOT correct, please update them in the 'config.txt' file.\nIf these ARE correct, press ENTER to continue.")
    loginuser = config[12].replace("\n", "")
    loginpass = config[15].replace("\n", "")
    #notify user prompt
    try:
        print("\nAttempting to login...")
        session = scratch3.login(loginuser, loginpass)
    except:
        input("\nLogin details are inccorect, the account is banned, or you might be having issues connecting to Scratch. press Enter to exit.")
        exit()
    #Attempt to log in as user
    print("Connecting to cloud...")
    try:
        conn = session.connect_cloud(config[18].replace("\n", ""))
    except:
        input("Failed to connect... Press ENTER to exit, you might have put an unshared or invalid project ID.")
        exit(1)
    while True:
        try:
            sleeptime = (1 / int(input("\nLogged in!\n\nHow many fps do you want the stream to run at?\n(for best results, put 2 - 5. anything higher may result you hitting the update rate limit.) ")))
            break
        except:
            print("Invalid Input. Try Again.")
    print("Alright! now casting to project '" + config[18].replace("\n", "") + "'. please be respectful to what you show.")
    
pyautogui.screenshot('temp.png')

while True:
    with Image.open('temp.png') as im:
        im = im.resize((57, 43))
        im = im.convert("L")
        im.save('temp.png')
        #convert screenshot
        i = 1
        try:
            contrastmod = int(config[21].replace("\n", ""))
        except:
            print("Failed to apply Contrast mod. setting to 1")
            contrastmod = 1
        #ii = X cord, i = Y cord
        temp = ""
        while (i < 43):
            ii = 1
            while (ii < 57):
                val = ((im.getpixel((ii, i)) / 255))
                val = round(contrastmod * ((val * 9)))
                if val <= 0 :
                    val = 1
                if val > 9:
                    val = 9
                    #jussst in case
                temp = temp + str(val)
                #val = brightnees value. it rounds the brightness to the closet whole number from 0 - 9
                ii += 1
            i += 1
            continue
        #converts screeshot into text format
        ii = 0
        iii = 0
        #iii = current split list index
        split = ['','','','','','','','','','']
        while (ii < len(temp)):
            i = 0
            temp2 = ''
            while (i < 256):
                try:
                    temp2 = temp2 + str(temp[ii])
                    i += 1
                    ii += 1
                except:
                    break
                #splits video data if it's longer than a 256 char byte
                #i and ii are now counters
            split[iii] = temp2
            iii += 1
        i = 0
        #setup  for encoding ans sending data
        config = open("config.txt", "r")
        config = (config.readlines())
        #update current config in ram
        if (len(config[22].replace("\n", "")) <= 100):
            captionline = (Encoding.encode(config[24].replace("\n", "")))
        else:
            print("Captions are too long! removing extra chars.")
            captionline = config[22].replace("\n", "")
            temp2 = ""
            while (i < 100):
                temp2 = temp2 + captionline[i]
                i += 1
            captionline = temp2
            captionline = (Encoding.encode(captionline))
        captionline = str(captionline + ("0" * abs(200 - len(captionline))))
        #convert captions + error correction
        while (i < 10):
                try:
                    if (i == 9):
                        temp = ''
                        temp = str(split[i] + captionline)
                        temp = temp + str("0" * (3 - len(str(round(((pyautogui.position()[0] / pyautogui.size()[0]) * 480)))  )))
                        temp = temp + str(round(((pyautogui.position()[0] / pyautogui.size()[0]) * 480)))       
                        temp = temp + str("0" * (3 - len(str((abs(round(((pyautogui.position()[1] / pyautogui.size()[1]) * 360) - 360)))))))
                        temp = temp + str(abs(round(((pyautogui.position()[1] / pyautogui.size()[1]) * 360) - 360)))
                        #caption, mousedata encoding stuff here
                        conn.set_var("VIDEOSTREAM INPUT 10" ,int(temp))
                        #encodes ALL metadata into the 10th string: rest of video data, caption data, and converted mouse pos data.
                        i += 1
                    else:
                        conn.set_var("VIDEOSTREAM INPUT " + str(i + 1), int(split[i]))
                        i += 1
                except:
                    print("Framedata failed to send! aborting frame.")
                    break
        time.sleep(sleeptime)
        open
        pyautogui.screenshot('temp.png')

    




