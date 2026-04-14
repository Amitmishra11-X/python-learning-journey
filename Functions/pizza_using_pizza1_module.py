import pizza1

pizza1.pizza_make(16, 'chesse','pepperoni' )
pizza1.pizza_make(10, 'chesse')

from pizza1 import pizza_make as mp
mp(16, 'chesse','pepperoni' )
mp(10, 'chesse')

