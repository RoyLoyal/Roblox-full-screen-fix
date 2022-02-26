import shutil, os

#Constant variable
RBX_VER_PATH = os.environ['USERPROFILE'] + "\AppData\Local\Roblox\Versions"
FINAL_FOLDER_NAME = "\\ClientSettings"
CLIENT_SET = __file__.rsplit('\\', maxsplit=1)[0] + FINAL_FOLDER_NAME

#returns bulain value(true) of string that start with "version"
def does_start_with_version(rbx_ver):
    return rbx_ver.startswith('version')

#takes strings and adds "path string"
def add_string(path):
    return (RBX_VER_PATH + "\\" + path)
 
#creates list of directoris(files)
rbx_ver_lst = os.listdir(RBX_VER_PATH)
#filters list to strings that start with version
rbx_ver_lst = list(filter(does_start_with_version, rbx_ver_lst))
#adds paths to folders in list
rbx_ver_lst = list(map(add_string, rbx_ver_lst))
#returns the folder that was last modified
last_mod_ver = max(rbx_ver_lst, key=os.path.getmtime)

shutil.copytree(CLIENT_SET, last_mod_ver + FINAL_FOLDER_NAME)