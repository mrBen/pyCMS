import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Settings(Gtk.Box):

    def __init__(self, main):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)

    # stuff
        stuff = Gtk.Label('Settings')

    # buttons
        buttons = Gtk.Box()

        # save = Gtk.Button('Save', margin=3)
        # save.connect('clicked', main.on_change_stack, 'cleaner')
        cancel = Gtk.Button('Cancel', margin=3)
        cancel.connect('clicked', main.on_change_stack, 'cleaner')

        # buttons.pack_end(save, False, True, 0)
        buttons.pack_end(cancel, False, True, 0)

    # packing
        self.pack_start(stuff, True,  True, 0)
        self.pack_end(buttons, False, True, 0)
