import subprocess
import shlex
 

def check_ip_ping(ip):
    cmd = 'ping -c 1' + ip
    args = shlex.split(cmd)
    try:
	    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    return u"%s is up!"%ip
    except subprocess.CalledProcessError:
        return u"??%s is down!"%ip