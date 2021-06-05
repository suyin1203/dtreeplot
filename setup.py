# from distutils.core import setup
from setuptools import setup
import setuptools 

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="dtreeplot",
    version="0.0.10",
    description="A Decision Tree Visualization Packages.",
    packages=setuptools.find_packages(),
    py_modules=["dtreeplot.plot", "dtreeplot.model_plot"],
        
    include_package_data=True,

    long_description="""A Decision Tree Visualization Packages.
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

```shell
pip3 install dtreeplot
```

    """,# 长描述
    url='', # 主页链接 
    author='suyin', # 作者名
    author_email='suyin1203@gmail.com', # 作者邮箱
    classifiers=[
        # 'Development Status :: latests',  # 当前开发进度等级（测试版，正式版等）

        # 'Intended Audience :: Developers', # 模块适用人群
        # 'Topic :: Decision Tree :: Visualization', # 给模块加话题标签

        'License :: OSI Approved :: MIT License', # 模块的license

        'Programming Language :: Python :: 3', # 模块支持的Python版本
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='decision tree Visualize',  # 模块的关键词，使用空格分割
    install_requires=[] # 依赖模块 'json', 'string', 'uuid', 'datetime', 'os'
    # extras_require={  # 分组依赖模块，可使用pip install sampleproject[dev] 安装分组内的依赖

    # },
    # package_data={  # 模块所需的额外文件
    #     'sample': [''],
    # },
    # data_files=[('', [''])], # 类似package_data, 但指定不在当前包目录下的文件
    )