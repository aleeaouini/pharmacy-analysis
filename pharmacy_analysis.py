from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum
import matplotlib.pyplot as plt

# Créer une session Spark
spark = SparkSession.builder.appName("PharmacyAnalysis").getOrCreate()

# Charger le dataset
df = spark.read.csv("data/ventes.csv", header=True, inferSchema=True)

print("==== Données brutes ====")
df.show()

# Calcul du revenu (quantité * prix)
df = df.withColumn("revenu", col("quantite") * col("prix"))

# 🔹 Médicament le plus vendu
medicament_plus_vendu = (
    df.groupBy("medicament")
    .agg(_sum("quantite").alias("total_vendu"))
    .orderBy(col("total_vendu").desc())
)
print("==== Médicament le plus vendu ====")
medicament_plus_vendu.show(5)

# 🔹 Catégorie la plus demandée
categorie_plus_demandee = (
    df.groupBy("categorie")
    .agg(_sum("quantite").alias("total_vendu"))
    .orderBy(col("total_vendu").desc())
)
print("==== Catégorie la plus demandée ====")
categorie_plus_demandee.show()

# 🔹 Revenu par jour
revenu_par_jour = (
    df.groupBy("date")
    .agg(_sum("revenu").alias("revenu_total"))
    .orderBy("date")
)
print("==== Revenu par jour ====")
revenu_par_jour.show()

# Conversion en Pandas pour les figures
med_pd = medicament_plus_vendu.limit(5).toPandas()
cat_pd = categorie_plus_demandee.toPandas()

# 🔹 Histogramme : Top 5 médicaments
plt.figure(figsize=(8,5))
plt.bar(med_pd["medicament"], med_pd["total_vendu"], color="skyblue")
plt.title("Top 5 Médicaments Vendus")
plt.xlabel("Médicament")
plt.ylabel("Quantité vendue")
plt.savefig("figures/top5_medicaments.png")
plt.close()

# 🔹 Pie chart : Répartition par catégorie
plt.figure(figsize=(6,6))
plt.pie(cat_pd["total_vendu"], labels=cat_pd["categorie"], autopct="%1.1f%%", startangle=140)
plt.title("Répartition des ventes par catégorie")
plt.savefig("figures/repartition_categories.png")
plt.close()

print("✅ Analyse terminée. Graphiques sauvegardés dans le dossier 'figures/'")

# Arrêter Spark
spark.stop()
