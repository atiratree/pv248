from metadata.Settings import Settings
from parse.Parser import Parser
from chart.Printer import show_max_percent_parties_bar


if __name__ == "__main__":
    with open(Settings.election_file, 'r') as election:
        parties = Parser.import_data(election)
        show_max_percent_parties_bar(parties)
