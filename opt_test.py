from pyomo.environ import *

model = ConcreteModel()
model.x = Var()
model.y = Var()
def rosenbrock(m):
    return (m.x)+ 100.0*(m.y - m.x)

def con_x(m):
    return -100,m.x,100

def con_y(m):
    return -29,m.y,29

model.conx = Constraint(rule=con_x)
model.cony = Constraint(rule=con_y)
model.obj = Objective(rule=rosenbrock, sense=minimize)
solver = SolverFactory('gurobi')
solver.solve(model, tee=True)
print("Optimisation problem solved sucessfully")
print()
print('*** Solution *** :')
print('x:', value(model.x))
print('y:', value(model.y))
