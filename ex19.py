# define a function "cheese_and_cracker" with two arguments "cheese_count and boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print number of cheese using digit formatter
	print "you have %d cheeses!" % cheese_count
# print number of boxes of crackers using digit formatter
	print "you have %d boxes of crackers!" % boxes_of_crackers
# print a string
	print "Man that's enough for a party!"
#print a string
	print "Get a blanket.\n"
# print a string
print "We can just give the function numbers directly:"
# call function cheese_and_crackers with value 20, 30
cheese_and_crackers(20, 30) 
#print a string
print "OR, we can use variables from our script:"
# variable created
amount_of_cheese = 10
# variable created
amount_of_crackers = 50
# call function cheese_and_crackers with value amount_of_cheese, amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print a string
print "we can even do maths inside too:"
# call function cheese_and_crackers with mathematical value 10 + 20, 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)
#print a string
print "And we can combine the two, variables and math:"
# call function cheese_and_crackers with variable and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)