#!/usr/bin/env python
# -*- coding: utf-8 -*-
#first crack
import math
from turtle import *

G = 6.67428e-11
AU = (149.6e6 * 1000)
SCALE = 50 / AU #originally 250

class Orbiter(Turtle):
	name = 'Orbiter'
	mass = None
	vx = vy = 0.0
	px = py = 0.0
	
	def gravity(S,O):
		if S is O:
			raise ValueError("Gravity doesn't work like that" %s.name)
		sx, sy = S.px, S.py
		ox, oy = O.px, O.py
		dx = (ox-sx)
		dy = (oy-sy)
		d = math.sqrt(dx**2 + dy**2)
		if d == 0:
			raise ValueError("collision!" %(S.name, O.name))
		f = G * S.mass * O.mass / (d**2)
		theta = math.atan2(dy, dx)
		fx = math.cos(theta) * f
		fy = math.sin(theta) * f
		return fx, fy
		
def update_info(step, bodies):
	print('step#{}'.format(step))
	for body in bodies:
		s = '{:<8} pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(body.name, body.px/AU, body.py/AU, body.vx, body.vy)
		print(s)
	print()
	
def loop(bodies):
	timestep = 24*3600
	
	#for body in bodies:
		#body.penup()
		#body.hideturtle()
	
	step = 1
	
	while True:
		update_info(step, bodies)
		step += 1
		force = {}
		for body in bodies:
			total_fx = total_fy = 0.0
			for other in bodies:
				if body is other:
					continue
				fx, fy = body.gravity(other)
				total_fx += fx
				total_fy += fy
			force[body] = (total_fx, total_fy)
		for body in bodies:
			fx, fy = force[body]
			body.vx += fx / body.mass * timestep
			body.vy += fy / body.mass * timestep
			
			body.px += body.vx * timestep
			body.py += body.vy * timestep
			body.goto(body.px*SCALE, body.py*SCALE)
			

def main():
	sun = Orbiter()
	sun.name = 'Sun'
	sun.mass = 1.98892*10**30
	sun.pencolor("yellow")
	sun.dot(25, 'yellow')
	
	earth = Orbiter()
	earth.name = 'Earth'
	earth.mass = 5.9742*10**24
	earth.px = -1*AU
	earth.vy = -29.783 *1000
	earth.pencolor("blue")
	earth.dot(3, 'blue')
	
	venus = Orbiter()
	venus.name = 'Venus'
	venus.mass = 4.8685*10**24
	venus.px = -0.723*AU
	venus.vy = -35.02*1000
	venus.pencolor = ("orange")
	#venus.dot(3, 'blue')
	
	mars = Orbiter()
	mars.name = 'Mars'
	mars.mass = 6.4171*10**23
	mars.px = -1.523*AU
	mars.vy = -24.077*1000
	mars.pencolor('red')
	mars.dot(2, 'red')
	
	mercury = Orbiter()
	mercury.name = 'Mercury'
	mercury.mass = 3.3011*10**23
	mercury.px = -0.387098*AU
	mercury.vy = -47.362*1000
	mercury.pencolor('green')
	mercury.dot(1, 'green')
	
	planetx = Orbiter()
	planetx.name = 'nibiru'
	planetx.mass = 10*30
	planetx.px = 0.99*AU
	planetx.vy = 32*1000
	planetx.pencolor('purple')
	planetx.dot(3, 'purple')
	
	loop([sun, earth, venus, mars, mercury])#, planetx]) 

if __name__ == '__main__':
	main()
