import json
from urllib.parse import urlencode
from urllib.request import urlopen

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from models.Movie import Movie


class Fetcher(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)

    # search bar
        search_bar = Gtk.Box()

        self.entry = Gtk.SearchEntry(margin=3)
        self.entry.connect('activate', self.on_search)

        button = Gtk.Button(' Search ', margin=3)
        button.connect('clicked', self.on_search)

        search_bar.pack_start(self.entry, True, True, 0)
        search_bar.pack_end(button, False, True, 0)

    # pages
        pages = Gtk.Box()

        pages_label = Gtk.Label('page ')

        self.pages_counter = Gtk.SpinButton(margin=3)
        self.pages_counter.set_adjustment(Gtk.Adjustment(1, 1, 100, 1, 10, 0))
        self.pages_counter.set_value(1)
        self.pages_counter.connect('value-changed', self.do_fetch)

        pages.pack_end(self.pages_counter, False, True, 0)
        pages.pack_end(pages_label, False, True, 0)

    # results
        self.movies = Gtk.ListStore(str, str, str, str, str)
        self.results = Gtk.TreeView(self.movies)

        self.results.append_column(
            Gtk.TreeViewColumn('Title', Gtk.CellRendererText(), text=0))
        self.results.append_column(
            Gtk.TreeViewColumn('Year', Gtk.CellRendererText(), text=1))

    # packing
        self.pack_start(search_bar, False, True, 0)
        self.pack_end(pages, False, True, 0)
        self.pack_start(Gtk.Separator(), False, False, 0)
        self.pack_start(self.results, True, True, 0)


    def on_search(self, widget):
        self.pages_counter.set_value(1)
        self.do_fetch(widget)


    def do_fetch(self, widget):
        params = urlencode({'s': self.entry.get_text(),
                            'type': 'movie',
                            'page': self.pages_counter.get_value_as_int()})
        response = urlopen('https://www.omdbapi.com/?' + params)
        data = json.loads(response.read())

        self.movies.clear()

        if data['Response'] == 'True':
            for movie in data['Search']:
                self.movies.append(movie.values())


    def get_movie(self):
        return Movie(
            self.movies[self.results.get_cursor().path][0],
            self.movies[self.results.get_cursor().path][1]
        )
