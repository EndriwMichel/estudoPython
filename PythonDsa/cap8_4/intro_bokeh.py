# Utilizando boke para apreentação dos dados

import bokeh
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

from bokeh.sampledata.iris import flowers

# Arquivo gerado para visualização
# out_file('bokeh-grafico.html')


""" Grafico exemplo """
# p = figure()

# p.line([1, 2, 3, 4, 5],
#        [6, 7, 2, 4, 5],
#        line_width=2)

# show(p)

""" Exemplo grafico de barras """
# output_file('Exemplo-grafico-barras.html')

# fruits = ['Maças', 'Peras', 'Tangerinas', 'Uvas', 'Mlancias', 'Morangos']
# counts = [5, 3, 4, 2, 4, 6]

# source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

# p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title='Contagem de frutas')

# p.vbar(x='fruits',
#        top='counts',
#        width=0.9,
#        source=source,
#        legend='fruits',
#        line_color='white',
#        fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))

# p.xgrid.grid_line_color = None
# p.y_range.start = 0
# p.y_range.end = 9
# p.legend.orientation = 'horizontal'
# p.legend.location = 'top_center'

# show(p)

""" Exemplo scatterplot """
# colormap = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
# colors = [colormap[x] for x in flowers['species']]

# p = figure(title='Iris morphology')
# p.xaxis.axis_label = 'Petal length'
# p.yaxis.axis_label = 'Petal width'

# p.circle(flowers['petal_length'], flowers['petal_width'], color=colors, fill_alpha=0.2, size=10)

# show(p)