# 1. TODO import all resource classes here
# 2. TODO get count of each resource
# 3. TODO get "singular" resource urls of each resource
# 4. TODO pull data from random 3 "singular" resource URLs
# 5. TODO convert swapi project into CLI application
      # task1 task2 task3

from reso.characters import Characters
from reso.planets import Planets
from reso.spaceships import Spaceship
from reso.vehicles import Vehicle

import argparse

a = Characters()
b = Planets()
c = Spaceship()
d = Vehicle()


# Character
developers = a.get_count()
developers_1 = a.get_urls_random(1)
developers_2 = a.get_resource_urls()

# Planet
developers1 = b.get_count()
developers_11 = b.get_urls_random(1)
developers_12 = b.get_resource_urls()
#
developers2 = c.get_count()
developers_21 = c.get_urls_random(1)
developers_22 = c.get_resource_urls()
#
developers3 = d.get_count()
developers_31 = b.get_urls_random(1)
developers_32 = b.get_resource_urls()

parser = argparse.ArgumentParser(
    description="handy tool to greet of developers")

#print(parser)
#print(type(parser))  # object of class `<class 'argparse.ArgumentParser'>`


parser.add_argument("developer1", type=str,)
parser.add_argument("developer2", type=str,)

args = parser.parse_args()

# import pdb;pdb.set_trace()

if args.developer1 == "count" :
    print(f"count of characters -\n {developers.get(args.developer1)}")
    print(f"count of planets -\n {developers1.get(args.developer1)}")
    print(f"count of Spacships -\n {developers2.get(args.developer1)}")
    print(f"count of Vehicles -\n {developers3.get(args.developer1)}")

if args.developer2 == "url":
    print(f" single url of characters -\n {developers_1.get(args.developer2)}")
    print(f" Random Three url of characters -\n {developers_2.get(args.developer2)}")
    print(f" single url of Planet -\n {developers_11.get(args.developer2)}")
    print(f" Random Thdirree url of Planet -\n {developers_12.get(args.developer2)}")
    print(f" single url of Spaceship -\n {developers_21.get(args.developer2)}")
    print(f" Random Three url of Spaceships -\n {developers_22.get(args.developer2)}")
    print(f" single url of Vehicles -\n {developers_31.get(args.developer2)}")
    print(f" Random Three url of Vehicles -\n {developers_32.get(args.developer2)}")



