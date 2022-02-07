# old way %s(string), %d(digit), %f(floating ), %r(repr)
print('%s %s' % ('two', 'one'))
print('{} {}'.format('two', 'one'))  # new way [placeholders]

print('%d %d' % (1, 2))      # old way
print('{} {}'.format(1, 2))  # new way

print('{1} {0}'.format('one', 'two'))  # new way {index}

print('%10s' % ('test',))      # old way
print('{:>10}'.format('test'))  # new way {padding}
