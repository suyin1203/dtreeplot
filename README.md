### Dtreeplot

A python library for decision tree visualization and model.

```python
# import dtreeplot package model_plot function
from dtreeplot import model_plot

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 

X, y = datasets.make_classification(n_samples=30000, n_features=10, weights=[0.96, 0.04])
features = [f'Var{i+1}' for i in range(X.shape[1])]


clf = DecisionTreeClassifier(criterion='gini',
                             max_depth=3, 
                             min_samples_split=30, 
                             min_samples_leaf=10, 
                             random_state=1234)
model = clf.fit(X, y)

# visualize tree model
model_plot(model, features, labels=y, height=530)
```

![image-20210605204143475](/Users/suyin/Library/Application Support/typora-user-images/image-20210605204143475.png)



#### install

```
pip3 install dtreeplot
```

