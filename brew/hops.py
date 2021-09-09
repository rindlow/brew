from .recipe import dryhop, firstwort
from . import templates


class Hop:

    minutes = 0
    name = '<hop>'

    def __init__(self, amount, minutes, alpha=None):
        self.amount = amount
        self.minutes = minutes
        if alpha is not None:
            self.alpha = alpha

    def html(self):
        if self.minutes == 0:
            when = 'Flame Out'
        elif self.minutes == dryhop:
            when = 'Dry Hop'
        elif self.minutes == firstwort:
            when = 'First Wort'
        else:
            when = f'{self.minutes} min'
        return templates.row3(self.name, f'{self.amount} g', when)

    def instructions(self):
        if self.minutes == dryhop:
            when = 'Dry Hop'
        elif self.minutes == firstwort:
            when = 'First Wort'
        else:
            when = f'{self.minutes} min'
        return templates.row3(when, self.name, f'{self.amount} g')

    def fermenter(self):
        return templates.row1(f'{self.name}, {self.amount} g')


class Amarillo(Hop):
    name = 'Amarillo'
    alpha = 10


class Bobek(Hop):
    name = 'Bobek (Styrian Goldings)'
    alpha = 5.0


class BramblingCross(Hop):
    name = 'Brambling Cross'
    alpha = 6.0


class Cascade(Hop):
    name = 'Cascade'
    alpha = 5.8


class Cluster(Hop):
    name = 'Cluster'
    alpha = 6.9


class EastKentGoldings(Hop):
    name = 'East Kent Goldings'
    alpha = 4.8


class Ekuanot(Hop):
    name = 'Ekuanot'
    alpha = 15


class Enigma(Hop):
    name = 'Enigma'
    alpha = 16


class Fuggle(Hop):
    name = 'Fuggle'
    alpha = 5.0


class Galaxy(Hop):
    name = 'Galaxy'
    alpha = 13.5


class HallertauerMittelfruh(Hop):
    name = 'Hallertauer Mittelfruh'
    alpha = 3.7


class Magnum(Hop):
    name = 'Magnum'
    alpha = 12.0


class Perle(Hop):
    name = 'Perle'
    alpha = 8.0


class NorthernBrewer(Hop):
    name = 'Northern Brewer'
    alpha = 8.0


class Saaz(Hop):
    name = 'Saaz'
    alpha = 3.0


class Simcoe(Hop):
    name = 'Simcoe'
    alpha = 13.5


class Willamette(Hop):
    name = 'Willamette'
    alpha = 4.3
