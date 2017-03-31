# NOT USED YET

import configparser


class Conf():

    path = 'settings.conf'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Conf.path)

        self.keep_original = config.getboolean('global', 'keep_original',
            fallback=False)
        self.windows_compatibility = config.getboolean('global', 'windows_compatibility',
            fallback=True)

        self.movies_directory = config.get('movies', 'directory',
            fallback='$HOME/Videos/films')
        self.movies_filename = config.get('movies', 'filename',
            fallback='{title} ({year})')

        self.series_directory = config.get('series', 'directory',
            fallback='$HOME/Videos/series')
        self.series_filename = config.get('series', 'filename',
            fallback='{ShowName}/Season {XX}/{ShowName} - s{XX}e{YY} - {Optional_Info}')

    def save(self):
        config = configparser.ConfigParser()

        config['global'] = {}
        config['global']['keep_original'] = 'yes' if self.keep_original else 'no'
        config['global']['windows_compatibility'] = 'yes' if self.windows_compatibility else 'no'

        config['movies'] = {}
        config['movies']['directory'] = self.movies_directory
        config['movies']['filename'] = self.movies_filename

        config['series'] = {}
        config['series']['directory'] = self.series_directory
        config['series']['filename'] = self.series_filename

        with open(Conf.path, 'w') as configfile:
            config.write(configfile)
