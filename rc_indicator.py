#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator

import os
import sys
import signal
import subprocess
import psutil


parentPath = os.path.dirname(os.path.realpath(__file__))
server_process = None
indicator = None

START_LABEL = "Start server"
STOP_LABEL = "Stop server"


def kill_all(process):
    pp = psutil.Process(process.pid)
    for child in pp.children(recursive=True):
        child.send_signal(signal.SIGINT)
    pp.send_signal(signal.SIGINT)


def toggle_service(w):
    global server_process
    global indicator

    if w.get_label() == START_LABEL:
        server_process = subprocess.Popen("python3 " + os.path.join(parentPath, "manage.py") + " runserver 0.0.0.0:8000", shell=True)
        w.set_label(STOP_LABEL)
        indicator.set_icon("remote-control-icon-running")
    else:
        kill_all(server_process)
        w.set_label(START_LABEL)
        indicator.set_icon("remote-control-icon")


def main():
    # Allow Ctrl+C like signals while running in terminal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Create the app indicator
    global indicator
    indicator = appindicator.Indicator.new_with_path(
                          "Remote Control Server",
                          "remote-control-icon",
                          appindicator.IndicatorCategory.APPLICATION_STATUS,
                          parentPath)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

    menu = Gtk.Menu()
    mitem = Gtk.MenuItem(START_LABEL)
    mitem.connect("activate", toggle_service)
    menu.append(mitem)

    mitem = Gtk.MenuItem("Exit")
    mitem.connect("activate", lambda w: sys.exit(0))
    menu.append(mitem)

    menu.show_all()
    indicator.set_menu(menu)
    Gtk.main()


if __name__ == "__main__":
    main()
