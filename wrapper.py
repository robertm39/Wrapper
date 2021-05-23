# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:55:04 2021

@author: rober
"""

global_store = list()

def unwrap(a):
    if type(a) is RecursiveWrapper:
        return a.__dict__['_RecursiveWrapper__________source']
    return a

def p_unwrap(a, b):
    return unwrap(a), unwrap(b)

BASE_TYPES = (str, int, float, complex, dict, set, list, tuple, chr, bool)

def o_wrap(a):
    if type(a) is RecursiveWrapper:
        return a
    #Some types we don't wrap
    if type(a) in BASE_TYPES:
        return a
    return RecursiveWrapper(a)

class RecursiveWrapper:
    def __init__(self, source):
        global_store.append(self)
        self.__________source = source
        #print('source type: ' + str(type(self.__________source)))
    
    def __getattr__(self, name):
        try:
            if name in ('__________source', '_RecursiveWrapper__________source'):
                return self.__dict__[name]
            val = getattr(self.__dict__['_RecursiveWrapper__________source'], name)
            #print('retrieved val')
            if type(val) is RecursiveWrapper:
                return val
    
            #Otherwise, replace it with a recursive wrapper
            new_val = o_wrap(val)
            # new_val = RecursiveWrapper(val)
            # new_val = RecursiveWrapper(val)
            try:
                setattr(self.__dict__['_RecursiveWrapper__________source'], name, new_val)
            except Exception:# as e:
                pass
                # print('Exception in setting:')
                # print(e)
                # print('**********')
                # a = 1/0
    
            #Now the val is a RecursiveWrapper
            return new_val
    
        except Exception:# as e:
            # print('Exception:')
            # print(e)
            # print('**********')
            # a = 1/0
            return None
    def __setattr__(self, name, val):
        try:
            
            if name in ('__________source', '_RecursiveWrapper__________source'):
                self.__dict__[name] = val
                return
    
            #Replace it with a RecursiveWrapper
            if type(val) is RecursiveWrapper:
                setattr(self.__________source, name, val)
                return
            
            # if type(val) is str:
            #     new_val = val
            # else:
            #     new_val = RecursiveWrapper(val)
            new_val = o_wrap(val)
            setattr(self.__dict__['_RecursiveWrapper__________source'], name, new_val)
        except Exception:
            pass
    
    def __call__(self, *args, **kwargs):
        return self.__dict__['_RecursiveWrapper__________source'](*args, **kwargs)
    
    def __iter__(self):
        return iter(self.__________source)
    
    def __getitem__(self, index):
        return self.__dict__['_RecursiveWrapper__________source'].__getitem__(index)
    
    def __setitem__(self, index, val):
        return self.__dict__['_RecursiveWrapper__________source'].__setitem__(index, val)
    
    #Comparison
    def __lt__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s < o)
    
    def __gt__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s > o)
    
    def __le__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s <= o)

    def __ge__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s >= o)
    
    def __eq__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s == o)
    
    def __ne__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s != o)
    
    #Math
    def __add__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s + o)
    
    def __sub__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s - o)
    
    def __mul__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s * o)

    def __matmul__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s @ o)
    
    def __floordiv__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s // o)
    
    def __div__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s / o)
    
    def __truediv__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s / o)
    
    def __mod__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s % o)
    
    def __pow__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s ** o)
    
    def __lshift__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s << o)
    
    def __rshift__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s >> o)

    def __and__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s & o)
    
    def __xor__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s ^ o)
    
    def __or__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(s | o)
    
    #Left math
    def __radd__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o + s)
    
    def __rsub__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o - s)
    
    def __rmul__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o * s)

    def __rmatmul__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o @ s)
    
    def __rfloordiv__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o // s)
    
    def __rdiv__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o / s)
    
    def __rmod__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o % s)
    
    def __rpow__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o ** s)
    
    def __rlshift__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o << s)
    
    def __rrshift__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o >> s)

    def __rand__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o & s)
    
    def __rxor__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o ^ s)
    
    def __ror__(self, other):
        s, o = p_unwrap(self, other)
        return o_wrap(o | s)
    
    #Assignment
    def __iadd__(self, other):
        s, o = p_unwrap(self, other)
        s += o
    
    def __isub__(self, other):
        s, o = p_unwrap(self, other)
        s -= o
    
    def __imul__(self, other):
        s, o = p_unwrap(self, other)
        s *= o
    
    def __idiv__(self, other):
        s, o = p_unwrap(self, other)
        s /= o
    
    def __ifloordiv__(self, other):
        s, o = p_unwrap(self, other)
        s //= o
    
    def __imod__(self, other):
        s, o = p_unwrap(self, other)
        s %= o
    
    def __ipow__(self, other):
        s, o = p_unwrap(self, other)
        s **= o

    def __ilshift__(self, other):
        s, o = p_unwrap(self, other)
        s <<= o
    
    def __irshift__(self, other):
        s, o = p_unwrap(self, other)
        s >>= o
    
    def __iand__(self, other):
        s, o = p_unwrap(self, other)
        s &= o
    
    def __ixor__(self, other):
        s, o = p_unwrap(self, other)
        s ^= o
    
    def __ior__(self, other):
        s, o = p_unwrap(self, other)
        s |= o
    
    #Unary
    def __neg__(self):
        s = unwrap(self)
        return o_wrap(-s)
    
    def __pos__(self):
        s = unwrap(self)
        return o_wrap(+s)
    
    def __abs__(self):
        s = unwrap(self)
        return o_wrap(abs(s))
    
    def __invert__(self):
        s = unwrap(self)
        return o_wrap(~s)
    
    def __complex__(self):
        s = unwrap(self)
        return o_wrap(complex(s))
    
    def __int__(self):
        s = unwrap(self)
        return o_wrap(int(s))
    
    # def __long__(self):
    #     s = unwrap(self)
    #     return o_wrap(long(s))
    
    def __float__(self):
        s = unwrap(self)
        return o_wrap(float(s))
    
    def __oct__(self):
        s = unwrap(self)
        return o_wrap(oct(s))
    
    def __hex__(self):
        s = unwrap(self)
        return o_wrap(hex(s))

# def wrap(name):
#     g = globals()
#     if not name in g:
#         #print('not found: {}'.format(name))
#         return
#     val = g[name]
#     if type(val) is RecursiveWrapper:
#         #print('already wrapper: {}'.format(name))
#         return
#     g[name] = RecursiveWrapper(val)

def source(i):
    return global_store[i]._RecursiveWrapper__________source

def print_sources():
    for i in range(len(global_store)):
        print(source(i))

#Not tested
def recursive_wrap(owner, name, levels=1):
    if levels==0:
        return
    
    d = owner if isinstance(owner, dict) else owner.__dict__
    if not name in d:
        #print('not found: {}'.format(name))
        return
    val = d[name]
    # if type(val) is RecursiveWrapper:
    #     #print('already wrapped: {}'.format(name))
    #     return

    #First, wrap the children
    #Wrap the parent last
    try:
        for sub_name in val.__dict__:
            recursive_wrap(val, sub_name, levels-1)
    except Exception:
        pass

    # wrapper = RecursiveWrapper(val)
    wrapper = o_wrap(val)
    try:
        d[name] = wrapper
    except Exception:
        pass