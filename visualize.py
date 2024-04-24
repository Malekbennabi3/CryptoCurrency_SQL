# Data processing
import numpy as np
import pandas as pd

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Model performance evaluation
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

# Fichier csv
data = pd.read_csv('highs.csv')


#Caracteristiques
print(data.info())


'''
# Get the screen resolution
screen_dpi = {'width': 1280, 'height': 800}  # replace with your screen's width and height
plt.figure(figsize=(screen_dpi['width']/80, screen_dpi['height']/80))

# Now you can create your Seaborn plot
sns.lineplot(x=data.index, y=data['vol_ada'])
sns.lineplot(x=data.index, y=data['vol_avax'])
sns.lineplot(x=data.index, y=data['vol_bnb'])
sns.lineplot(x=data.index, y=data['vol_btc'])
sns.lineplot(x=data.index, y=data['vol_dot'])
sns.lineplot(x=data.index, y=data['vol_eth'])
sns.lineplot(x=data.index, y=data['vol_link'])
sns.lineplot(x=data.index, y=data['vol_ltc'])
sns.lineplot(x=data.index, y=data['vol_shib'])
sns.lineplot(x=data.index, y=data['vol_sol'])

plt.legend(['ada', 'avax', 'bnb', 'btc', 'dot', 'eth', 'link', 'ltc', 'shib', 'sol'])

# Show the plot
plt.show()

'''

# Visualize data using seaborn
sns.set(rc={'figure.figsize': (40, 7)})
sns.lineplot(x=data.index, y=data['high_ada'])
sns.lineplot(x=data.index, y=data['high_avax'])
sns.lineplot(x=data.index, y=data['high_bnb'])
sns.lineplot(x=data.index, y=data['high_btc'])
sns.lineplot(x=data.index, y=data['high_dot'])
sns.lineplot(x=data.index, y=data['high_eth'])
sns.lineplot(x=data.index, y=data['high_link'])
sns.lineplot(x=data.index, y=data['high_ltc'])
sns.lineplot(x=data.index, y=data['high_shib'])
sns.lineplot(x=data.index, y=data['high_sol'])

plt.legend(['ada', 'avax', 'bnb', 'btc', 'dot', 'eth', 'link', 'ltc', 'shib', 'sol'])

#plt.show()
plt.savefig("Rapport/highs.png")

