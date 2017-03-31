import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from models.Conf import Conf


class Settings(Gtk.Box):

    def __init__(self, win):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)

        self.win = win
        self.config = Conf()

    # settings
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # keep original
        self.check_copy = Gtk.CheckButton('Keep the original file (make a copy insted of rename)')
        self.check_copy.set_active(self.config.keep_original)

        # windows compatibility
        self.check_windows = Gtk.CheckButton('Use a Windows compatible filename (use _ to replace < > : " / \ | ? *)')
        self.check_windows.set_active(self.config.windows_compatibility)

        layout.pack_start(self.check_copy, False, True, 0)
        layout.pack_start(self.check_windows, False, True, 0)

    # buttons
        buttons = Gtk.Box()

        save = Gtk.Button('Save', margin=3)
        save.connect('clicked', self.on_save)
        cancel = Gtk.Button('Cancel', margin=3)
        cancel.connect('clicked', self.on_save)

        buttons.pack_end(save, False, True, 0)
        buttons.pack_end(cancel, False, True, 0)

    # packing
        self.pack_start(layout, True,  True, 0)
        self.pack_end(buttons, False, True, 0)


    def on_save(self, widget):
        self.config.keep_original = self.check_copy.get_active()
        self.config.windows_compatibility = self.check_windows.get_active()

        self.config.save()
        self.win.config = self.config
        self.win.on_change_stack(self, 'cleaner')

    def on_cancel(self, widget):
        self.config = Conf()
        self.win.on_change_stack(self, 'cleaner')
