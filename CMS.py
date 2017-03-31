import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from Cleaner import Cleaner
from Settings import Settings


class CMS(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Clean My Shit')
        self.connect('delete-event', Gtk.main_quit)

        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    # menu
        menu = Gtk.MenuBar()

        item_settings = Gtk.MenuItem('Settings')
        item_settings.connect(
            'activate', self.on_change_stack, 'settings')
        item_about = Gtk.MenuItem('About')
        item_about.connect('activate', self.on_about)

        menu.append(item_settings)
        menu.append(item_about)

    # stack
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(
            Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

        # cleaner
        cleaner = Cleaner()
        self.stack.add_named(cleaner, 'cleaner')

        # settings
        settings = Settings(self)
        self.stack.add_named(settings, 'settings')

    # packing
        layout.pack_start(menu, False, True, 0)
        layout.pack_start(Gtk.Separator(), False, False, 0)
        layout.pack_start(self.stack, True, True, 0)

        self.add(layout)
        self.show_all()


    def on_about(self, widget):
        about_dialog = Gtk.AboutDialog(transient_for=self, modal=True)

        # about_dialog.set_artists(['artists'])
        about_dialog.set_authors(['Benjamin Collet'])
        about_dialog.set_comments(
            'A program for naming and organizing media files.')
        about_dialog.set_copyright('Copyright © 2017 Benjamin Collet')
        # about_dialog.set_documenters(['documenters'])
        about_dialog.set_license_type(Gtk.License.MIT_X11)
        about_dialog.set_logo_icon_name('video-x-generic')
        about_dialog.set_program_name('CMS (Collection Management System)')
        # about_dialog.set_translator_credits('translator_credits')
        about_dialog.set_version('v0.0.1')
        about_dialog.set_website('https://github.com/TheMrBen/CMS')
        about_dialog.set_website_label('github.com/TheMrBen/CMS')

        about_dialog.present()

    def on_change_stack(self, widget, name):
        self.stack.set_visible_child_name(name)


if __name__ == '__main__':
    win = CMS()
    Gtk.main()


# TODO: make settings for: - path
#                          - filename
#                          - copy or move?
#                          - windows format (remove ":", "?" and other...)
#
#       fix errors when no selection
#
#       make a real Gtk Application menu (with actions and all that stuff)
#
#       make an Interface out of Fetcher
#
#       (low priority) a proper Python package
#
#       (low priority) a lot of doc
#
#       (low priority) a progress bar for copy/move
#
#       (low priority) use glade for building the GUI
