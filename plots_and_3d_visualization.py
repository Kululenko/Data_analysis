import pandas 
import seaborn 
import matplotlib.pyplot as plt

#load dataset
iris = seaborn.load_dataset("iris")
print(iris.head())   # runs 5 first rows 

#check for missing values
missing_values = iris.isnull().sum()
print(missing_values)

print(iris.describe()) # shows a lot of crucial information about the dataset (min,max,mean etc.)

#histogram plot
#iris.hist()
#plt.show()

#boxplot
#iris.boxplot()
#plt.show()


#trying subplots
fig, axs = plt.subplots(2,1, figsize=(10, 8))

for col in iris.columns[:-1]:                                 #slicing the last column because its "species"
    seaborn.histplot(iris[col], ax=axs[0], kde=True)

for col in iris.columns[:-1]:
    seaborn.boxplot(x="species",y=col, data=iris, ax=axs[1])

plt.tight_layout()
plt.show()

#streudiagramm und länge und breite der blüte entgegengestellt für cluster erkennung
plt.figure(figsize=(10, 6))
seaborn.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)

plt.title("Streudiagramm Sepal length gegen Sepal width")
plt.xlabel("Sepal length in [cm]")
plt.ylabel("Sepal width in [cm]")
plt.legend(title="species")

#plt.show()

#korrelationsanalyse
numerical_data = iris.select_dtypes(include=["float64","int64"])   #64 wird angegben für die Genauigkeit der zahlen wegen 64bit
korrelationsmatrix = numerical_data.corr()

plt.figure(figsize=(8,6))
seaborn.heatmap(korrelationsmatrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("korrelationsmatrix der Iris Datensatz Merkmale")
plt.show()

#Konklusion der Korrelationsanalyse
#Interessanterweise gibt es eine extrem starke korrelation (0.96) zwischen der Blüttenblatt länge und Breite, sowie eine starke Korrelation der Blüttenblatt breite (0.82) 
# und Länge (0.87) mit der Kelchblattlänge. Aber dafür gibt es eine negative korrelation bei der kelchblattbreite (Blütenblatt länge -0.43) (blüttenblatt breite -0.37) 

# Zusammenfassend kann man schlussfolgern: Je größer und breiter die Blüttenblätter und die Kelchblattlänge, desto kleiner die Kelchblattbreite.


#Facetgrid
grid = seaborn.FacetGrid(iris, col="species")
grid.map(plt.hist, "sepal_length")
plt.show()

#Durch die mehreren Subplots erkennt man die Unterschiedliche Sepal_length der unterschiedlichen Arten


#violinplot
plt.figure(figsize=(8,6))
seaborn.violinplot(x="species", y="petal_width", data=iris)
plt.title("Violinplot nach petal_width für Irisblütten arten")
plt.show()

#pairplot
seaborn.pairplot(iris, hue="species")
plt.suptitle("pairplot für den iris datensatz",verticalalignment="baseline")
plt.show()


#Multivariate Analyse

#Figur und 3d achse
fig = plt.figure(figsize=(10,7))
axe = fig.add_subplot(111, projection="3d")

colors = {"setosa": "r","versicolor": "g", "virginica": "b"}

#3d model scatter plots für alle arten
for species, group in iris.groupby("species"):
    axe.scatter(group["sepal_length"], group["sepal_width"], group["petal_length"], c=colors[species], label=species, edgecolors="k", depthshade=False)

axe.set_xlabel("sepal_lenght")
axe.set_ylabel("sepal_width")
axe.set_zlabel("petal_length")

axe.set_title('3D-Scatter-Plot des Iris-Datensatzes')
axe.legend()

plt.show() 





