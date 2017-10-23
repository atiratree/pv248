from bokeh.plotting import figure, show
from functools import reduce
from metadata.Keys import Keys as K
import math


def show_max_percent_parties_bar(parties, max_percent=1):
    if not parties:
        parties = []

    total_votes = reduce(lambda x, party: x + party[K.votes_key], parties, 0)
    percent_votes = (total_votes / 100) * 1

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

    p = figure(x_range=labels, x_axis_label='Parties', y_axis_label='Votes')
    p.xaxis.major_label_orientation = math.pi / 2

    p.vbar(x=range(1, one_percent_parties_count + 1),
           top=votes,
           fill_color=colors,
           tags=labels,
           width=0.7)
    show(p)
