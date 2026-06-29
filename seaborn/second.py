import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(style="whitegrid")

sns.histplot(
    data=tips,
    x="total_bill",
    kde=True
)

plt.title("Distribution of Total Bill")

plt.show()