# Idle Economy Model

## Version 0.1: Fixed-cost single producer

The simulation has:

- one currency
- one producer type
- fixed producer cost
- fixed income per producer
- automatic buying when affordable

## Variables

B = balance  
n = producers owned  
C = producer cost  
p = income per producer per second  
t = time  

## Equations

income_per_second = n * p

time_to_next_purchase = (C - B) / income_per_second

After purchase:

B = B - C  
n = n + 1  

## Simulation method

Use event-based simulation.

Instead of ticking every frame, jump directly to the next purchase event.