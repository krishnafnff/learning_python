import os
import shutil
import re

WORKINGDIR = "/home/krishna/Downloads/orderv_admin"
os.chdir(WORKINGDIR)
CWD = os.listdir()


def SrtFileChecker(fileList):
    OnlySrtFiles = []
    for SrtFile in fileList:
        checkingExtention = re.search("(.srt)", SrtFile)
        if checkingExtention != None:
            OnlySrtFiles.append(SrtFile)
            # print(SrtFile)
    return OnlySrtFiles


def ZipFileChecker(fileList):
    OnlyZipFiles = []
    for ZipFile in fileList:
        checkingExtention = re.search("(.zip)", ZipFile)
        if checkingExtention != None:
            OnlyZipFiles.append(ZipFile)
            # print(ZipFile)
    return OnlyZipFiles


for folder in CWD:

    if os.path.isdir(folder):
        
        if len(os.listdir(folder)) != 0:
            # make sure at the end working directory will be change to default
            WD = os.chdir(WORKINGDIR+'/'+folder)

            os.mkdir("Mixes")

            listing = os.listdir()

            SrtFiles = SrtFileChecker(listing)
            ZipFiles = ZipFileChecker(listing)
            
            if len( SrtFiles ) != 0:
                os.mkdir("Mixes/SrtFiles")
                # print("srtfiles")
                # print(SrtFiles)
                for file in SrtFiles:
                    shutil.move(file,'Mixes/SrtFiles')

            if len( ZipFiles ) != 0:
                os.mkdir("Mixes/ZipFiles")
                # print("zipfiles")
                # print(ZipFiles)
                for file in ZipFiles:
                    shutil.move(file,'Mixes/ZipFiles')
            
            os.chdir(WORKINGDIR) #like this
            
