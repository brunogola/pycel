'''
Simple example file showing how a spreadsheet can be translated to python and executed
'''


from pycel.excelutil import *
from pycel.excellib import *
import os
from pycel.excelcompiler import ExcelCompiler
from os.path import normpath,abspath

if __name__ == '__main__':
    
    fname = normpath(abspath("../example/example.xlsx"))
    
    print("Loading %s..." % fname)
    
    # load  & compile the file to a graph, starting from D1
    c = ExcelCompiler(filename=fname)
    
    print("Compiling..., starting from D1")
    sp = c.gen_graph('D1',sheet='Sheet1')
    
    # test evaluation
    print("D1 is %s" % sp.evaluate('Sheet1!D1'))
    
    print("Setting A1 to 200")
    sp.set_value('Sheet1!A1',200)
    
    print("D1 is now %s (the same should happen in Excel)" % sp.evaluate('Sheet1!D1'))
    
    # show the graph usisng matplotlib
    print("Plotting using matplotlib...")
    sp.plot_graph()

    # export the graph, can be loaded by a viewer like gephi
    print("Exporting to gexf...")
    sp.export_to_gexf(fname + ".gexf")
    
    print("Serializing to disk...")
    sp.save_to_file(fname + ".pickle")

    print("Done")