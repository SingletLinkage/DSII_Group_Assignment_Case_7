import csv

reader = csv.reader(open('source_files/data_indonesia.csv', 'r'), delimiter=',')
header = next(reader)

latex_str = '''
\\newgeometry{left=1cm,right=1cm}
\\begin{table}[htbp]
\centering
\caption{change my description here}
\label{tab:change label here}
\\begin{tabular}{ccccc}        \hline
    '''

header_string = ' & '.join(map(lambda x: '\\textbf{'+x+'}', header)) + " \\\\ \hline \n"
latex_str += header_string

for row in reader:
    row = map(lambda x: x.replace('&', '\&'), row)
    latex_str += ' & '.join(row) + " \\\\ \n"

latex_str += '\\end{tabular}\n\\end{table}\n\\restoregeometry'

with open('scripts/table.tex', 'w') as f:
    f.write(latex_str)