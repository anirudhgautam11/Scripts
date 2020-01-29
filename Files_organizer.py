# Python script to move all files in Category folders
#Name of category folder is the value of the key in dictionary 'extensions' to which file belongs
# This script affects files only, folders are excluded
# This script is portable, run this script from the directory you want to organize

import os,shutil


extensions={'audio': ['.aif', '.cdale', '.midio', '.mp3', '.ogg', '.wav', '.wpl'], 
'compressed': ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
 'discImage': ['.bin','.iso', '.dmg', '.toast', '.vcd'],
  'database': ['.csv', '.dat', '.db', '.dbf', '.log','.xlsx' ,'.mdb', '.sav', '.sql', '.tar', '.xml'],
   'image': ['.ai', '.bmp','.BMP', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff'],
    'documents': ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wks', '.wps', '.wpd'], 
    'videos': ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'], 
     'sourceCode': ['.py', '.c', '.class', '.cpp', '.cs', '.h', '.java', '.sh', '.swift', '.vb'],
      'spreadsheet ': ['.ods', '.xlr', '.xls', '.xlsx'],
        'executables': ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.wsf'], 
         'presentations': ['.key', '.odp', '.pps', '.ppt', '.pptx'],'Torrent Files':['.torrent'] ,'internetFiles': ['.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php', '.rss', '.xhtml'], 'systemFiles': ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp']}
cwd = os.getcwd() 

def makedir(folderName):   #function to make category directories
    if not os.path.exists(cwd+"\\"+folderName):
        
        try:
            os.mkdir(os.path.join(cwd,folderName))
            return (cwd+"\\"+folderName)
        except:
            print("Directory %s cannot be created" ,folderName)
        else:
            print(folderName,"created Successfully!")
    
    else:
        print("Dir already exists")
        return (os.path.join(cwd,folderName))
      
def movein(filePath,destPath):   #function to move files.
    try:
        shutil.move(filePath,destPath)
    except:
        print(filePath,"cannot be moved")
    else:
        print("success!")

filesAndFolders = os.listdir(cwd)   #Will return a list of all files and folders in perticular directory

keys=list(extensions.keys())

for i in filesAndFolders:
    
    filepath = os.path.abspath(i)
    file_name=(__file__.split("\\"))[-1]  #extracting name of python script
    
    if i==file_name:  #To avoid moving our python script
        continue
    
    elif os.path.isfile(i):
        
        # extension of file
        tempLt = i.split('.')  
        ext = "."+tempLt[-1] 

        for k in keys:
            ext_list = extensions[k]
            if ext in ext_list:
                dest_path = makedir(k)
                movein(filepath,str(dest_path))
                
   
