from metadata.settings import Settings
from parse.parser import Parser
from plot.printer import show_max_percent_parties_bar, show_pie_chart_results


if __name__ == "__main__":
    with open(Settings.election_file, 'r') as election:
        parties = Parser.import_data(election)
        show_max_percent_parties_bar(parties)
        show_pie_chart_results(parties)
