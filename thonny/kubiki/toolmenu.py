from thonny import get_workbench
from tkinter.messagebox import showinfo
import subprocess
from thonny import THONNY_USER_DIR
import os.path
import sys

template ="""\
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

"""

def insert_template():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    editor._code_view.text.insert(1.0, template)
    
def cmd_open_kubiki():
    subprocess.Popen(os.path.join(sys.prefix, "python") + " -m kubiki", shell=True)

def load_plugin():
    get_workbench().add_command(command_id="insert_template",
                                menu_name="tools",
                                command_label="Template",
                                handler=insert_template)
    
    get_workbench().add_command("open_kubiki", "tools",
                                "Open Kubiki world",
                                cmd_open_kubiki)

