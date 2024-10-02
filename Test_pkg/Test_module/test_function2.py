#This is a second test function for demonstration purposes
from IPython.display import HTML, display
from IPython import get_ipython
import pyspark.pandas as ps

def test_fn2(x,y):
    return (x + y)

def test_fn2_add(x,y,z):
    return (x + y + z)

def display1(df):
    display(df)

def display2(df):
    pdf = ps.DataFrame(df)
    shell = get_ipython().__class__.__name__
    if shell == 'DatabricksShell':
        display(HTML(pdf.to_html))

def display3(df):
    shell = get_ipython().__class__.__name__
    if shell == 'DatabricksShell':
        display(df)