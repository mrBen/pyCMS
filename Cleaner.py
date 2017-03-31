import shutil
import os.path
from pathlib import Path

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from Fetcher import Fetcher


class Cleaner(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)

    # pane
        pane = Gtk.Paned()
        pane.set_wide_handle(True)

        # file chooser
        self.file_chooser = Gtk.FileChooserWidget()

        # fetcher
        self.fetcher = Fetcher()

        pane.pack1(self.file_chooser, True, False)
        pane.pack2(self.fetcher, True, False)

    # status
        status = Gtk.Box()

        self.info = Gtk.Label(margin=3)

        rename_button = Gtk.Button(' Rename ', margin=3)
        rename_button.connect('clicked', self.on_rename)

        status.pack_start(self.info, False, True, 0)
        status.pack_end(rename_button, False, True, 0)

    # packing
        self.pack_start(pane, True,  True, 0)
        self.pack_start(Gtk.Separator(), False, False, 0)
        self.pack_start(status, False, True, 0)


    def on_rename(self, widget):
        filename = self.file_chooser.get_filename()
        movie = self.fetcher.get_movie()

        dst = '/home/user/Videos/test/' + movie.path

        if not os.path.exists(os.path.dirname(dst)):
            Path(os.path.dirname(dst)).mkdir(parents=True)

        src = filename
        dst += os.path.splitext(filename)[1]

        shutil.move(src, dst)

        text = '<small>The file <tt>{}</tt>'.format(os.path.basename(src))
        text += ' have been moved to\n<tt>{}</tt></small>'.format(dst)
        self.info.set_markup(text)
