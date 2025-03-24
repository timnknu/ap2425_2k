a = "HELLO"
#s = f'here is the value: {a} !!'
#print(s)
s = 'here is the value: {a}, or {next_val}!!'
#print(s.format(**{'a': 'abcd'}))
print(s.format(a = 'abcd', next_val = 123))

