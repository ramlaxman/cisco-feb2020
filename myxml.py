#!/usr/bin/env python3


print(xml('foo'))               # first argument = tagname
# <foo></foo>

print(xml('foo', 'bar'))        # second (optional) argument = content
# # # # <foo>bar</foo>

print(xml('a',
          xml('b',
              xml('c', 'hello'))))
# # # # # # <a><b><c>hello</c></b></a>

# # # kwargs become attributes in opening tag

print(xml('tag', 'text', a=1, b=2, c=3))

# # # # <tag a="1" b="2" c="3">text</tag>

print(xml('tag', 'text', a=1, b=2))
# # # # <tag a="1" b="2">text</tag>

print(xml('tag', a=1, b=2))
# # # # # <tag a="1" b="2"></tag>
