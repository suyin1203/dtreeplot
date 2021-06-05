#!/usr/bin/env python
# coding=utf-8
lang = "python"



import json
import string
import uuid
import datetime
import os


# cop from https://www.kaggle.com/bhavesh09/titanic-decision-tree-visual-with-d3-js
def _tree_to_json(clf, features, labels, node_index=0):
    """Structure of rules in a fit decision tree classifier

    Parameters
    ----------
    clf : DecisionTreeClassifier
        A tree that has already been fit.

    features, labels : lists of str
        The names of the features and labels, respectively.

    Returns
    ----------
    	Decision tree json.

    """
    
    
    node = {}
    if clf.tree_.children_left[node_index] == -1:  # indicates leaf, leaf noode
        num_examples = clf.tree_.n_node_samples[node_index]
        value = clf.tree_.value[node_index, 0].tolist()
        distribution = [round(i/num_examples, 4) for i in value]
        
        node['value'] = {'type': 'PROBABILITY', 
                         'distribution': distribution,
                         'num_examples': f"{num_examples},{format(distribution[-1], '.2%')}"
                        }
        
        
    else: # split node
        feature = features[clf.tree_.feature[node_index]]
        threshold = clf.tree_.threshold[node_index]
        num_examples = clf.tree_.n_node_samples[node_index]
        value = clf.tree_.value[node_index, 0].tolist()
        distribution = [round(i/num_examples, 4) for i in value]
        node['value'] = {'type': 'PROBABILITY', 
                         'distribution': distribution,
                         'num_examples': f"{num_examples},{format(distribution[-1], '.2%')}"
                        }
        node['condition'] = {'type': 'NUMERICAL_IS_HIGHER_THAN', 
                             'attribute': feature,
                             'threshold': round(threshold, 4)
                            }
        left_index = clf.tree_.children_left[node_index]
        right_index = clf.tree_.children_right[node_index]
        
        node['children'] = [_tree_to_json(clf, features, labels, right_index),
                            _tree_to_json(clf, features, labels, left_index)]
        
    return node




# copy from https://github.com/tensorflow/decision-forests
def _plot_tree(tree, features, labels) -> str:
    """Plots a decision tree.
    
    Parameters
    ----------
    tree: A decision tree.
    features: 
    labels: 

    Returns:
      The html content displaying the tree.

    """
    
    '''
    todo:
        max_depth: Maximum plotting depth. Makes the plot more readable in case of
            large trees.
    
    '''

    # Plotting library.
    basepath = os.path.abspath(__file__)
    folder = os.path.dirname(basepath)
    plotter_js_path = os.path.join(folder, 'js/plotter.js')

    # print(plotter_js_path)

    with open(plotter_js_path) as f:
        plotter_js_content = f.read()


    container_id = "tree_plot_contid_" + uuid.uuid4().hex

    # Converts the tree into its json representation.
    json_tree = _tree_to_json(tree, features, labels)
    
    
    # Display options.
    options = {}

#     if tree.label_classes is not None:
#         options["labels"] = json.dumps(tree.label_classes) # json.dumps(tree.label_classes)

# <script src="https://d3js.org/d3.v6.min.js"></script>
    
    basepath = os.path.abspath(__file__)
    folder = os.path.dirname(basepath)
    d3_js_path = os.path.join(folder, 'js/d3.v6.min.js')
    # print(d3_js_path)

    html_content = string.Template("""
<script src="${d3_pkg}"></script>
<script src="https://d3js.org/d3.v6.min.js"></script>
<div id="${container_id}"></div>
<script>
${plotter_js_content}
display_tree(${options}, ${json_tree_content}, "#${container_id}")
</script>
""").substitute(
  options=json.dumps(options),
  plotter_js_content=plotter_js_content,
  container_id=container_id,
  json_tree_content=json_tree,# json.dumps(json_tree)
  d3_pkg=d3_js_path
  ) 

    return html_content



def model_plot(model, features, labels, width=950, height=350, show_notebook=True):
    """Plots a decision tree structure in Jupyter notebook.

    Parameters
    ----------
    model: DecisionTreeClassifier
        A tree that has already been fit.
    features: lists of str
        The names of the features and labels, respectively.
    labels: lists of str
        The names of the features and labels, respectively.
    width: number
    	The width of HTML element in notebook. eg.950
    height: number
    	The height of HTML element in notebook. eg.350
    show_notebook: True or False
    	If True, plot displayed in the notebook. If False, return file name.

    Returns:
      A Notebook HTML element showing the model.
    
    """


    html = _plot_tree(tree=model, features=features, labels=labels)

    uid = uuid.uuid4().hex
    now = datetime.datetime.now()
    dt = str(now.date()).replace('-', '_')
    html_file_name = f'tree_plot_{dt}_{uid}.html'

    with open(f'{html_file_name}', 'w') as f:
        f.write(html)
    
    if show_notebook:
        from IPython.display import IFrame, display
        display(IFrame(src=html_file_name, width=width, height=height))

    if show_notebook == False:
        return f'可视化文件名：{html_file_name}'




