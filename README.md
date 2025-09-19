# 🏥 Analyse des ventes d'une pharmacie avec PySpark

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python) ![PySpark](https://img.shields.io/badge/PySpark-3.5-orange?logo=apache-spark) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-red?logo=matplotlib)

Ce projet analyse les ventes d'une pharmacie en utilisant **PySpark** pour le traitement de données massives et **Matplotlib** pour la visualisation. Il fournit des insights utiles pour la gestion du stock et la planification des ventes.

---

## 📊 Fonctionnalités
- Analyse du **médicament le plus vendu**
- Analyse de la **catégorie la plus demandée** (antibiotiques, vitamines, antidouleurs, etc.)
- Calcul du **revenu par jour**
- Visualisation graphique des ventes :
  - **Histogramme** : Top 5 médicaments vendus  
  - **Pie chart** : Répartition des ventes par catégorie  
  - **Histogramme** : Revenu par jour  
  - **Stacked bar chart** : Quantité vendue par catégorie chaque jour  

---

### Top 5 médicaments vendus
![Top 5 Médicaments](figures/top5_medicaments.png)

### Répartition des ventes par catégorie
![Répartition par catégorie](figures/repartition_categories.png)

### Revenu par jour
![Revenu par jour](figures/revenu_par_jour.png)

### Quantité vendue par catégorie par jour
![Quantité par catégorie par jour](figures/quantite_par_categorie_par_jour.png)

---

## 💡 Insights possibles
- Identifier **les produits les plus rentables** pour optimiser les commandes.
- Repérer **les jours avec le plus de ventes** afin d'ajuster le personnel.
- Observer les **tendances saisonnières** des ventes par catégorie.
- Aider à la **planification du stock** pour éviter les ruptures ou surplus.

---

## 🚀 Lancer le projet
1. Cloner le dépôt
   ```bash
   git clone https://github.com/aleeaouini/pharmacy-analysis.git
   cd pharmacy-analysis
