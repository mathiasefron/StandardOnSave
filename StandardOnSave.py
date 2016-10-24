import sublime_plugin
import re
import subprocess
import os.path

class SublimeOnSaveBuild(sublime_plugin.EventListener):
    def on_post_save(self, v):

        if os.path.splitext(v.file_name())[1] != '.js':
            return

        path = v.file_name()
        parent = False
        i = 0
        while not parent and i < 5:
            i = i+ 1
            path = path.rsplit("/", 1)[0]
            if path == "":
                return
            if os.path.isfile(path + "/package.json"):
                parent = True
        
        standard = path + "/node_modules/.bin/standard" 
        
        if os.path.isfile(standard):
            print(subprocess.check_output([standard, "--fix", v.file_name()], cwd=path))