import importlib.resources


def page():
    return importlib.resources.read_text('brew', 'template.html')


def instructions():
    return importlib.resources.read_text('brew', 'instruction_template.html')


def other(rows):
    return f'''
      <h3>Other</h3>
      <table id="other">
{rows}
      </table>'''


def row1(cell1):
    return f'        <tr><td class="col123">{cell1}</td></tr>\n'


def row2(cell1, cell2):
    return f'        <tr><td class="col12">{cell1}</td>'\
        f'<td class="col3">{cell2}</td></tr>\n'


def row2b(cell1, cell2):
    return f'        <tr><td class="col1">{cell1}</td>'\
        f'<td class="col3" colspan="2">{cell2}</td></tr>\n'


def row3(cell1, cell2, cell3):
    return f'        <tr><td class="col1">{cell1}</td>' \
        f'<td class="col2">{cell2}</td><td class="col3">{cell3}</td></tr>\n'
