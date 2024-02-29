import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import ListedColormap

from sklearn.linear_model import LogisticRegression

# For df_candidate
df_candidate = pd.read_csv('candidate_no_fada.csv', encoding='iso-8859-1')

print(df_candidate.head())

df = df_candidate.groupby(["Constituency", "Party Id"]).agg({"Votes": "sum"}).reset_index()

df['Vote Fraction'] = df['Votes'] / df.groupby('Constituency')['Votes'].transform('sum')

print(df.head())

urban_constituencies = [
    "Dublin Bay North", "Dublin Bay South", "Dublin Central", "Dublin Fingal", "Dublin Mid-West",
    "Dublin North West", "Dublin Rathdown", "Dublin South Central", "Dublin South West", "Dublin West",
    "Dun Laoghaire", "Cork North Central", "Cork South Central", "Limerick City"
]

mixed_constituencies = [
    "Cork East", "Cork North West", "Cork South West", "Limerick County", "Galway West",
    "Kildare North", "Kildare South", "Louth", "Waterford", "Wicklow"
]


# Adding a new column for the constituency type
df['Type'] = df['Constituency'].apply(
    lambda x: "urban" if x in urban_constituencies else ("mixed" if x in mixed_constituencies else "rural")
)

old_df=df.copy()

df=df[df['Type'] != "mixed"]

# Preparing the plot data

x1=np.array(df[df["Party Id"]=="Fianna Fa/il"]["Vote Fraction"])
x2=np.array(df[df["Party Id"]=="Fine Gael"]["Vote Fraction"])
x =np.array(list(zip(x1,x2)))
y=np.array(df[df["Party Id"]=="Fianna Fa/il"]["Type"])

clf = LogisticRegression(penalty='none')
clf.fit(x, y)

new_y=clf.predict(x)

b0 = clf.intercept_[0]
b1, b2 = clf.coef_[0]
c = -b0/b2
m = -b1/b2

print(m,c)

#x_values = np.linspace(x1.min(),x1.max(), 400)
x_values = np.linspace(0.15,0.22, 400) 

# Calculating the corresponding y values using y = mx + c
y_values = m * x_values + c


df_pivot = old_df.pivot_table(index=['Constituency', 'Type'], columns='Party Id', values='Vote Fraction').reset_index()

colors = {'urban': 'red', 'rural': 'green', 'mixed': 'gray'}
alphas =  {'urban': 0.6, 'rural': 0.6, 'mixed': 0.2}


# Plotting

plt.figure(figsize=(3.5, 2.5))

for ctype, group in df_pivot.groupby('Type'):
    plt.scatter(group['Fianna Fa/il'], group['Fine Gael'], color=colors[ctype], label=ctype, alpha=alphas[ctype])

#for i in range(len(y)):
#    plt.scatter(x1[i],x2[i],color=colors[y[i]])

xlim = plt.xlim()
ylim = plt.ylim()


plt.plot(x_values,y_values)

plt.xlim(xlim)
plt.ylim(ylim)

plt.xlabel('FF fraction')

plt.ylabel('FG fraction')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1),title='Type')

plt.tight_layout()
plt.grid(True)
plt.savefig('../02.5_ffVfg_linear.png', dpi=300)
plt.show()


# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Coefficients


# Generating a grid of x and y values
x = np.linspace(0, 0.5, 100)
y = np.linspace(0,0.5, 100)
x_grid, y_grid = np.meshgrid(x, y)

# Computing sigma(beta0 + beta1*x + beta2*y)
z = sigmoid(b0 + b1*x_grid + b2*y_grid)

# Creating a custom color map: red for 0, green for 1
cmap = ListedColormap(['red', 'green'])


plt.figure(figsize=(3.5, 2.5))


for ctype, group in df_pivot.groupby('Type'):
    plt.scatter(group['Fianna Fa/il'], group['Fine Gael'], color=colors[ctype], alpha=alphas[ctype])


#for i in range(len(y)):
#    plt.scatter(x1[i],x2[i],color=colors[y[i]])

xlim = plt.xlim()
ylim = plt.ylim()

contour = plt.contourf(x_grid, y_grid, z, 50, cmap='RdYlGn_r', vmin=0, vmax=1) 


for ctype, group in df_pivot.groupby('Type'):
    plt.scatter(group['Fianna Fa/il'], group['Fine Gael'], color=colors[ctype], label=ctype, alpha=alphas[ctype])


plt.xlim(xlim)
plt.ylim(ylim)

plt.xlabel('FF fraction')

plt.ylabel('FG fraction')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1),title='Type')

plt.tight_layout()
plt.grid(True)
plt.savefig('../02.5_ffVfg_heatmap.png', dpi=300)
plt.show()

