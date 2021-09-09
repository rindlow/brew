#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-

import glob
import os.path

files = []
for f in glob.glob('*.html'):
    fn, ext = os.path.splitext(f)
    b, d, n = fn.split('_')
    b = int(b)
    files.append((b, d, n, f))

print('''Content-Type: text/html

<!DOCTYPE html>
<html lang="sv">
  <head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="style.css"/>
    <title>Björkebys brygder</title>
  </head>
  <body>
    <div id="brewery"><span id="breweryname">Björkeby</span></div>
    <div id="basics">
      <h1>Björkebys brygder</h1>
      <table id="list">''')

for b, d, n, f in sorted(files, reverse=True):
    print('       '
          '<tr><td class="list1">{b}</td>'
          '<td class="list3"><a href="{f}">{n}</a></td>'
          '<td class="list2">{d}</td></tr>'
          .format(b=b, d=d, f=f, n=n))

print('''      </table>
    </div>
  </body>
</html>''')
    
