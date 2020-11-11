# Action Contre la Faim - Système d'Alerte

Objectif : construire un tableau de bord permettant le suivi des situations humanitaires en Birmanie (pays pilote) et dans le monde, à partir de données publiques. En particulier, suivre l'évolution de ces situations en lien avec l'épidémie de Covid-19.

## Etapes
- Identifier et prioriser les indicateurs d'intérêt
- Identifier les sources de données correspondantes et les évaluer
- Développer le code d'acquisition et de structuration des données (notebooks)
- Industrialiser ce code et planifier des runs périodiques (scripts et *cron jobs*)
- Documenter les caractéristiques de chaque source de données et de ses transformations
- Développer un dashboard de suivi des indicateurs consolidés (Power BI) 

## Structure du répertoire
- `src/` : contient le code de développement (`src/notebooks/`) et de production (`src/scripts/`) nécessaire à la consolidation des données
- `data/` : contient les sources de données scrapées (`data/sources/`) et transformées (`data/clean/`) ; non suivi par git.
- `docs/` : contient la documentation du code ainsi que celle des sources de données.

## Environnement de développement
### Langage
- python 3.8.2
- Convention PEP-8. Black est utilisé pour l'assurer dans les notebooks: l'activer avec la commande
```
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip
jupyter nbextension enable jupyter-black-master/jupyter-black
```
puis cliquer sur le bouton "Jupyter Black" en sélectionnant les cellules concernées
 
### Notebooks
- Collection de chaque source dans un notebook individuel Jupyter, ce qui permet de maintenir plus aisément le code.
- Chaque notebooks peut être converti en un script à l'aide de la commande:
```
# run from repository root
jupyter nbconvert --config "./config/notebooks_conversion_cfg.py" --to script --output-dir "./src/scripts/collection/"
```
- Pour ignorer les cellules de tests/developpement lors de la conversion, il suffit de les marquer du tag 'dev'. 
Les tags peuvent être activés dans les notebooks en allant à "View - Cell Toolbar - Tags".
