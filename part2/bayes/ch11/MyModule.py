import pymc as pymc
#import MyModule

#M = Model(MyModule)

def make_model(x):
    a = pymc.Exponential('a', beta=x, value=0.5)

    @pymc.deterministic
    def b(a=a):
        return 100-a

    @pymc.stochastic
    def c(value=.5, a=a, b=b):
        return (value-a)**2/b

    return locals()

M=pymc.Model(make_model(3))

print pymc.Model, M.a, M.c

#M.summary() 
#pymc.Matplot.plot(M)
