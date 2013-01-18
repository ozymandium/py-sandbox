#!/usr/bin/env python
"""
Decorator for making python function call graphs
Does not terminate after single iteration
currently Python v2.7.3
"""
try:
    import pycallgraph, sys
except ImportError:
    print('You do not have pycallgraph installed')
    sys.exit()
import pdb


def callgraph(outfile='/tmp/pycallgraph.png'):
    def argwrapper(fn):
        def callwrapper(*args, **kwargs):
            if not outfile: # allow deactivating
                return fn(*args, **kwargs)
            pycallgraph.start_trace()
            fn_output = fn(*args, **kwargs)
            pycallgraph.stop_trace()
            pycallgraph.make_dot_graph(outfile)
            return fn_output
        return callwrapper
    return argwrapper


# Example of usage with an output
@callgraph(outfile='./test_pycallgraph_decorator.png')
def example_fn1(x):
    print('this will create a call graph')
    print(x)

# if you want to leave the decorator but only use it conditionally
@callgraph(outfile=None)
def example_fn2():
    print('This will not')

if __name__ == '__main__':
    example_fn1(2)
    example_fn2()
