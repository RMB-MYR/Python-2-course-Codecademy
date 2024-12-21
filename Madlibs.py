"""
Description: Mad Libs
Author: RemboMaster
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s\s ruled the world."

print "The Game Mad Libs has started"

name = raw_input("Enter a name: ")

print "We need three adjective from you"
adj_1 = raw_input("Enter an adjektive: ")
adj_2 = raw_input("Enter a second adjektive: ")
adj_3 = raw_input("Enter one more adjektive: ")

print "We also need a verb"
verb = raw_input("Please enter a verb: ")

print "Finally, we also. need two nouns"
noun_1 = raw_input("Enter the first noun: ")
noun_2 = raw_input("Now ennter the second noun: ")

print "We need some additional inforamtion..."
animal = raw_input("Enter an Animal: ")
food = raw_input("Enter a food of your choosing: ")
fruit = raw_input("Enter a fruit you don't like?: ")
superhero = raw_input("Whats your favourite superhero?: ")
country = raw_input("Which country won the last world football cup?:  ")
dessert = raw_input("Enter yout favourite dessert: ")
year = raw_input("Enter a year between 1400 and 1988: ")

print "The Stroy is now in progress..."

print STORY % (name, adj_1, adj_2, animal, food, verb, noun_1, fruit, adj_3, name, superhero, name, country, name, dessert, name, year, noun_2)













