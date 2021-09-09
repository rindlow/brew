#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
import sys
import templates
from collections import defaultdict
import time

styles = {
    '7B-Amber Bitter European Beer-Altbier': ('11H', 'Rökig Alt'),
    '8A-English Pale Ale-Standard/Ordinary Bitter':
    ('3F', 'English ordinary bitter'),
    '8B-English Pale Ale-Special/Best/Premium Bitter':
    ('4A', 'English best bitter'),
    '8C-English Pale Ale-Extra Special/Strong Bitter':
    ('4B', 'English strong bitter - ESB'),
    '10A-American Ale-American Pale Ale': ('4C', 'American Pale Ale'),
    '12C-Pale Commonwealth Beer-English IPA': ('4E', 'English IPA'),
    '13B-Porter-Robust Porter': ('7D', 'Porter'),
    '13C-Porter-Baltic Porter': ('8C', 'Imperial Porter'),
    '14B-India Pale Ale(IPA)-American IPA': ('5C', '(Red) IPA'),
    '14C-India Pale Ale(IPA)-Imperial IPA': ('5E', 'DIPA'),
    '15C-German Wheat/Rye Beer-Weizenbock': ('6F', ''),
    '16C-Belgian And French Ale-Saison': ('9H', ''),
    '18B-Pale American Ale-American Pale Ale': ('4C', 'American Pale Ale'),
    '18E-Belgian Strong Ale-Belgian Strong Dark Ale': ('9K', 'Belgisk julöl'),
    '24B-Belgian Ale-Belgian Pale Ale': ('9A', 'Belgian Pale Ale'),
    '25C-Strong Belgian Ale-Belgian Golden Strong Ale':
    ('9D', 'Ljus stark belgisk ale'),
    '26C-Trappist Ale-Belgian Tripel': ('9C', 'Tripel'),
    '- No Style Chosen': ('-', '')
}

for fn in sys.argv[1:]:
    with open(fn) as f:
        soup = bs4.BeautifulSoup(f, features="html.parser")
    data = {}
    data['title'] = soup.title.text
    body = soup.body
    for child in body.children:
        if type(child) == bs4.element.NavigableString and child.strip() != '':
            data['style'] = child.strip()

    key = None
    ferm = None
    fermentables = []
    hop = None
    hops = []
    ing = None
    other = []
    yeast = None
    yeasts = []
    step = None
    steps = []
    skip = 0

    for td in body('td'):
        text = td.text.strip()
        if key is not None:
            data[key] = text

        if ferm is not None:
            if len(ferm) < 5:
                ferm.append(text)
            else:
                fermentables.append(ferm)
                ferm = []
                if text != 'Hops':
                    ferm.append(text)

        if hop is not None:
            if len(hop) < 6:
                hop.append(text)
            else:
                hops.append(hop)
                hop = []
                if text != 'Other Ingredients':
                    hop.append(text)

        if ing is not None:
            if len(ing) < 3:
                ing.append(text)
            else:
                other.append(ing)
                ing = []
                if text != 'Other Ingredients':
                    ing.append(text)

        if yeast is not None:
            if len(yeast) < 3:
                yeast.append(text)
            else:
                yeasts.append(yeast)
                yeast = []
                if text != 'Other Ingredients':
                    yeast.append(text)

        if step is not None:
            if skip > 0:
                skip -= 1
                continue
            if len(step) < 3:
                step.append(text)
            else:
                steps.append(step)
                step = []
                if text != 'General Notes':
                    step.append(text)

        if text == 'Date Brewed:':
            key = 'brewed'
        elif text == 'Target Volume Transferred:':
            key = 'transferred'
        elif text == 'Target OG:':
            key = 'og'
        elif text == 'Target FG:':
            key = 'fg'
        elif text == 'Target ABV:':
            key = 'abv'
        elif text == 'Target IBU:  (using Tinseth):':
            key = 'ibu'
        elif text == 'Target Color: (using Morey):':
            key = 'srm'
        elif text == 'Fermentables':
            ferm = []
        elif text == 'Hops':
            hop = []
            ferm = None
        elif text == 'Other Ingredients':
            ing = []
            hop = None
        elif text == 'Yeasts':
            yeast = []
            ing = None
        elif text == 'Water Profile':
            yeast = None
        elif text == 'Mash Schedule':
            step = []
            skip = 4
        elif text == 'General Notes':
            step = None
        else:
            key = None

    d = defaultdict(str)
    _, batch, name = data['title'].split(' ', 2)
    d['name'] = name
    d['author'] = 'Henrik Rindlöw'
    d['description'] = styles[data['style']][1]

    for name, amt, pct, mcu, when in fermentables[1:]:
        a, u = amt.split(' ')
        amount = float(a.replace(',', '.'))
        if u == 'g':
            amount /= 1000.0
        p, s = pct.split(' ')
        pc = float(p.replace(',', '.'))
        d['malt'] += templates.row3(name, f'{amount:.2f} kg', f'{pc:.0f} %')
    d['hops'] = ''
    for name, alpha, amt, ibu, form, when in hops[1:]:
        if ' ' in when:
            m, _ = when.split(' ', 1)
            m = f'{m} min'
        else:
            m = when
        m = m.replace('All', '60')
        d['hops'] += templates.row3(name, amt, m)
    d['yeast'] = ''
    for name, amt, used in yeasts[1:]:
        d['yeast'] += templates.row1(name)
    if len(other) > 1:
        other_rows = ''
        for name, amt, when in other[1:]:
            other_rows += templates.row3(name, amt, when)
        d['other'] = templates.other(other_rows)
    else:
        d['other'] = ''
    if len(steps) > 1:
        for stype, temp, dur in steps[1:]:
            if 'Rest' in stype:
                d['mash'] += templates.row3(stype, f'{dur} min', temp)
    else:
        d['mash'] += templates.row3('Saccharification rest',
                                    '60 min', '66 °C')

    t, _ = data['transferred'].split(' ')
    t = float(t.replace(',', '.'))
    d['stats'] += templates.row2('Batch size', f'{t:.1f} L')
    og, _ = data['og'].split(' ')
    og = float(og.replace(',', '.'))
    d['stats'] += templates.row2('Target OG', f'{og:.3f}')
    fg, _ = data['fg'].split(' ')
    fg = float(fg.replace(',', '.'))
    d['stats'] += templates.row2('Target FG', f'{fg:.3f}')
    abv, _ = data['abv'].split(' ')
    abv = float(abv.replace(',', '.'))
    d['stats'] += templates.row2('Target ABV', f'{abv:.1f} %')
    srm, _ = data['srm'].split(' ')
    srm = float(srm.replace(',', '.'))
    ebc = srm * 1.97
    d['stats'] += templates.row2('Target EBC', f'{ebc:.0f}')
    ibu, _ = data['ibu'].split(' ')
    ibu = float(ibu.replace(',', '.'))
    d['stats'] += templates.row2('Target IBU', f'{ibu:.0f}')
    d['stats'] += templates.row2('SHBF style', styles[data['style']][0])

    page = templates.page()

    batch = batch.strip(':')
    brewdate = time.strftime('%Y-%m-%d',
                             time.strptime(data['brewed'], '%d %b %Y'))
    filename = f'{batch}_{brewdate}_{d["name"]}.html'
    with open(filename, 'w') as f:
        f.write(page.format(**d))
