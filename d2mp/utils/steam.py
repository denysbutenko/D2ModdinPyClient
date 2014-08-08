'''
Created on 01.06.2014

@author: Schleppi
'''
import psutil, sys
from d2mp.utils import log
from subprocess import call
from d2mp.core.mods import ModManager

def command(cmd):
    if sys.platform == "darwin":
        return call(["open", ModManager().steam_exe(), "steam://%s" %cmd])
    else:
        return call(["steam", "steam://%s" %cmd])

def launch_dota():
    if is_dota_running(): return
    print "launching dota"
    log.DEBUG("Launching dota")
    return command("rungameid/570")

def get_dota_process():
    for proc in psutil.process_iter():
        name = proc.as_dict(['name'])['name'] or ''
        if "dota" in name.lower(): return proc
    return None

def is_dota_running():
    return get_dota_process() is not None

def kill_dota():
    dota_proc = get_dota_process()
    if dota_proc is not None: dota_proc.kill()
    
def connect_dota(ip):
    print "connecting to " + ip 
    log.DEBUG("Told Steam to connect to %s." %(ip))
    command("connect/%s/" %(ip))


def spectate(ip):
    kill_dota()
    log.DEBUG("Told Steam to spectate at %s." %(ip))
    command("rungameid/570//+connect_hltv %s" %(ip))
        
