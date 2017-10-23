import math
from bokeh.plotting import figure, show, output_file
from functools import reduce
from metadata.keys import Keys as K
from bokeh.models import ColumnDataSource


def show_max_percent_parties_bar(parties, max_percent=1):
    if not parties:
        parties = []

    percent_votes = (__get_total_votes(parties) / 100) * 1

    percent_parties = sorted(filter(lambda party: party[K.votes_key] <= percent_votes, parties),
                             key=lambda party: party[K.votes_key],
                             reverse=True)
    colors = []
    labels = []
    votes = []
    for party in percent_parties:
        colors.append(party[K.color_key])
        labels.append(party[K.short_key])
        votes.append(party[K.votes_key])

    one_percent_parties_count = len(percent_parties)

    p = figure(x_range=labels, x_axis_label='Parties', y_axis_label='Votes',
               title=f"Election Results for max {max_percent}% votes parties")
    p.xaxis.major_label_orientation = math.pi / 2

    p.vbar(x=range(1, one_percent_parties_count + 1),
           top=votes,
           fill_color=colors,
           tags=labels,
           width=0.7)
    output_file("max_percent_parties.html")
    show(p)


def show_pie_chart_results(parties):
    if not parties:
        parties = []

    parties = sorted(parties, key=lambda party: party[K.votes_key], reverse=True)
    total_votes = __get_total_votes(parties)

    colors = []
    labels = []
    votes = []
    starts = []
    ends = []
    next_start = math.pi / 2
    next_end = next_start

    for party in parties:
        next_end -= party[K.votes_key] / total_votes * 2 * math.pi
        ends.append(next_end)
        starts.append(next_start)
        next_start = next_end

        colors.append(party[K.color_key])
        labels.append(party[K.short_key])
        votes.append(party[K.votes_key])

    src = ColumnDataSource(data={
        'start': starts,
        'end': ends,
        'color': colors,
        'label': labels})

    p = figure(title="Election Results")
    p.wedge(x=0, y=0, radius=0.5,
            start_angle='start',
            end_angle='end',
            color='color',
            legend='label',
            source=src,
            direction='clock', )
    output_file("election_results.html")
    show(p)


def __get_total_votes(parties):
    return reduce(lambda x, party: x + party[K.votes_key], parties, 0)
