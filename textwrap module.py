import textwrap

letters="abcdefghijklmnopqrstuvwxyz"

print(dir(textwrap))
print(len(dir(textwrap)))

print(textwrap.__all__)


print(textwrap.wrap(letters,5))
print(textwrap.fill(letters,5))
print(textwrap.indent(letters,"---"))

print(textwrap.shorten(letters,25))
print(textwrap.shorten(letters,26))

print(textwrap.dedent(letters))