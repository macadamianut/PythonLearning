print "Let's practice evrything."
print "You\'d need to know \ about escapes with \\ that do \n newlines and \t tabs."

poem = """
\t The lovely world
with logic so firmlay planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "______________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret-formula(started):
	jelly-beans = started * 500
	jars = jelly_beans / 100
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret-formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)