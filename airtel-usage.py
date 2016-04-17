#! /usr/bin/env python

import urllib2
import re
import os
import subprocess

def main():
	#The IP hasn't changed in the last 30 days. Hope it stays the same.
	r = urllib2.urlopen('http://122.160.230.125:8080/planupdate/');
	page = r.read();

	#Quick regex. Will break with a even a minor change of the source website.
	m = re.search("<p>You are left with only <span>(\d+\.\d+) GB</span> of high-speed data limit.", page);
	if m != None:
		p = subprocess.Popen("""eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)"; /usr/bin/notify-send "airtel-usage: You are left with {0} GB this month." """.format(m.group(1)), shell=True);
		os.waitpid(p.pid, 0);
	else:
		p = subprocess.Popen("""eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)"; /usr/bin/notify-send Something went wrong.""", shell=True);
                os.waitpid(p.pid, 0);
		exit();



if __name__ == "__main__":
	main();
