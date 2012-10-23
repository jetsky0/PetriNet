import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

n = PetriNet('N') #creando una red petri

n.add_place(Place('v0')) #declarando estado inicial reposo del abanico
n.add_transition(Transition('t0')) #declarar primera transicion al accionar interruptor
n.add_place(Place('v1')) #declarando estado de velocidad uno del abanico
n.add_transition(Transition('t1')) #declarando segunda transicion al accionar el interruptor otra vez
n.add_place(Place('v2')) #declaracion del estado de velocidad maxima del abanico
n.add_transition(Transition('t2')) #delcaracion ultima transicion donde de velocidad maxima vuelve al estado de reposo
n.add_input('v0', 't0', Variable('x0')) #del estado de reposo pasa a la primera transicion (t0)
n.add_output('v1', 't0', Expression('x1')) #una vez pasando la primera transicion llega a la v1
n.add_input('v1', 't1', Variable('x2')) #accionando el interruptor llega a la segunda transicion (t1)
n.add_output('v2', 't1', Expression('x3')) #despues de t1 llega la velocidad aumenta a v2
n.add_input('v2', 't2', Variable('x4')) #finalmente al volver a accionar el interruptor llega a la tercera transicion (t2) 
n.add_output('v0', 't2', Expression('x5')) #una vez pasando t2 regresa al estado inicial v0

for engine in ('neato', 'dot', 'circo', 'twopi', 'fdp') :     
	n.draw(',redpetri-%s.png' % engine, engine=engine)

s = StateGraph(n)
s.build()
s.draw(',redpetri.png')

for node in sorted(n.node(), key=str) :
	node.pos.moveto(-100, -100)
n.layout()
any(node.pos == (-100, -100) for node in sorted(n.node(), key=str))
False
