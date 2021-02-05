import numpy as np 
publishers = ['George Lucas', 'Dark Horse Comics', 'DC Comics', 'Marvel Comics', 'George Lucas']
heroes = ['Luke Skywalker', 'Abe Sapien', 'Abin Sur', 'Abomination', 'Darth Vader']

def get_publisher_heroes(heroes, publishers, desired_publisher):
  desired_heroes = [] 

  for i, pub in enumerate(publishers):
    if pub == desired_publisher:
      desired_heroes.append(heroes[i])

  return desired_heroes

def get_publisher_heroes_np(heroes, publishers, desired_publisher):
  heroes_np = np.array(heroes)
  pubs_np = np.array(publishers)

  desired_heroes = heroes[pubs_np == desired_publisher]

  return desired_heroes

# use get_publisher_heroes() to gather star wares heroes 
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')
print(star_wars_heroes)
