#!/usr/bin/python

import sys
sys.path.insert(0, '../')

import gobject
import gtk
import unittest
from AppInstall.activation import *
from AppInstall.AppInstall import AppInstall

class FakeOptions(object):
    def __init__(self):
        self.datadir = "data/"
        self.desktopdir = "test/data/desktop"
        self.cachedir = "test/data/cache"
        self.transient_for = None
        self.addon_cd = None
        self.mime_type = "text/plain"
        self.test_mode = True

class TestMimeSearch(unittest.TestCase):
    def setUp(self):
        options = FakeOptions()
        uri = "file:/etc/fstab"
        style = MimeSearchActivationStyle(options, uri, uri)
        style.isInstallerOnly = False
        style.preRun()
        self.app = AppInstall(options, style)

    def testHasItems(self):
       self.assert_(len(self.app.menu.treeview_packages.get_model()) > 0,
                     "no mime-data found")

    def testRun(self):
        gobject.timeout_add(100, gtk.main_quit)
        self.app.run()

    def tearDown(self):
        self.app.window_main.destroy()
        del(self.app)

if __name__ == '__main__':
    unittest.main()

