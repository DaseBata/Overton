from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import numpy as np

app = Flask(__name__, static_url_path='/static')

df = pd.read_json("overton.jsonl", lines=True)

fig_tab = df[['es_score', 'citation_count', 'citation_count_including_self']].describe()

# Calculer les percentiles
percentiles = np.linspace(0, 100, 100)
citation_count_percentiles = np.percentile(df['citation_count'], percentiles)

# Créer un DataFrame pour les données
data = {'percentiles': percentiles, 'citation_count_percentiles': citation_count_percentiles}
df_percentiles = pd.DataFrame(data)

# Tracer la courbe jusqu'au centiles
fig_affichage = px.line(df_percentiles, x='percentiles', y='citation_count_percentiles', title='Répartition des données de la variable "citation_count" jusqu\'au 100e percentile')
fig_affichage.update_layout(xaxis_title='Percentiles', yaxis_title='Nombre de citations')


# Analyse temporelle
df['published_on'] = pd.to_datetime(df['published_on'], errors='coerce')
temporal_analysis = df.set_index('published_on').resample('M').size().reset_index(name='Number of Publications')

figure_temp=px.line(temporal_analysis, x='published_on', y='Number of Publications',
                       labels={'Number of Publications': 'Nombre de publications', 'published_on': 'Mois'},
                       title='Nombre de publications par mois')


# Analyse des sources
source_df = pd.json_normalize(df['source'])
source_distribution = source_df['title'].value_counts()

figure_sources = px.bar(source_distribution,
             title='Distribution des sources')


# Analyse des topics
keywords_count = df['topics'].explode().value_counts()
keywords_count = keywords_count[:15]

figure_topics = px.bar(keywords_count,
             title='DTop 10 des topics')


# Relations entre les variables
correlation_matrix = df[['es_score', 'citation_count']].corr()
figure_relations = px.imshow(correlation_matrix, color_continuous_scale='Viridis')

figure_relations.update_layout(
    title='Heatmap de la matrice de corrélation',
)


# Analyse des classifications
classifications_count = df['classifications'].explode().value_counts()
classifications_count = classifications_count[:14]

figure_classifications = px.bar(classifications_count,
             title='Analyse des classifications')


# Langues
languages_count = df['languages'].explode().value_counts()
languages_count = languages_count[:15]

figure_langues = px.bar(languages_count, log_y=True,
             title='Langues')


# Analyse des auteurs
authors_count = df['authors'].explode().value_counts()
authors_count = authors_count[:10]

figure_auteurs = px.bar(authors_count,
             title='Auteurs')

"""
# Analyse des citations
citation_df = pd.json_normalize(df['cites'])
citations_count = citation_df['scholarly'].explode().value_counts()
citations_count = citations_count[:10]

figure_citations = px.bar(citations_count,
             title='Citations')
"""

@app.route('/')
def index():
    return render_template('index.html', plot0=fig_tab.to_html(), plot0_5 = fig_affichage.to_html(), plot1=figure_temp.to_html(), plot2=figure_sources.to_html(), plot3=figure_topics.to_html(), plot4=figure_relations.to_html(), plot5=figure_classifications.to_html(), plot6=figure_langues.to_html(), plot7=figure_auteurs.to_html())

if __name__ == '__main__':
    app.run(debug=True)
