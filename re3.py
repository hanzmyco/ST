import re

'''
p=re.compile('(?!:)')
print p.match('abcd:ab')
print p.match(' a  ')
print p.match('abcd')
print '1111  '

'''
p=re.compile('^(?!(\s|:))(?!.*(:|\s$))')
print p.match('ab:cd:ab')
print p.match('a ')
print p.match(' a  ')
print p.match(' a')
print p.match('')
print p.match('abcd')
print p.match(':ab1')
print p.match('abc:')
print 'lol  '

'''
p=re.compile('^\S\S$')
print p.match('abcd:ab')
print p.match(' a  ')
print p.match('a')


print '66666'
p2=re.compile('^\S(?!.*:).*(?!.*:).*\S$')
print p2.search('abcd:cde')
print p2.match(' a ')
print p2.match('a')
print p2.match(':abc')
'''