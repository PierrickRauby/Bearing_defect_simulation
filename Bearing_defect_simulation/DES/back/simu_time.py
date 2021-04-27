## Direct copy from the Notebook
## https://stackoverflow.com/questions/279561/
##           what-is-the-python-equivalent-of-static-variables-inside-a-function
##TODO: not sure about that XD 
#def static_vars(**kwargs):
#    def decorate(func):
#        for k in kwargs:
#            setattr(func, k, kwargs[k])
#        return func
#    return decorate
#
## TODO: not sure about that either
#@static_vars(t=0)
#
#def init_time():
#    set_time(0)
#
#def now():
#       return now.t
#
#def set_time(t_new=0):
#    now.t = t_new
#    return now()
#
