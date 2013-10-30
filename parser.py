import sys
from bs4 import BeautifulSoup

class Parser:

  def clean(self, tag): 
    title = tag.get('data-grabthis')
    content = tag.text.lstrip('***GRAB THIS: {{%s}}*** ' % title)
    tagtype = tag.name
    position = self.position(tag)
    return (title, content, tagtype, position)

  def position(self, tag, pos=[]):
    if not tag.parent:
      pos.reverse()
      return pos
    else:
      pos.append((tag.name, tag.attrs))
      return self.position(tag.parent, pos)

  def submit(self, html):
    soup = BeautifulSoup(html)
    # grab all the elements that we added
    # find out what type of data makes most sense to extract 
    # apply different strategies depending on attributes surrounding, 
    # i.e., from the first row in a tables, get the column (how is this represented?)
    grabthis = [ self.clean(tag) for tag in soup.find_all() if tag.has_attr('data-grabthis')]
    print grabthis


def main(filename):
  parser = Parser()
  with open(filename, 'r') as html:
    parser.submit(html.read())


if __name__ == '__main__':
  if len(sys.argv) > 1:
    print 'Parsing ' + sys.argv[1]
    main(sys.argv[1])
  else: 
    print 'You might want some sample files to go with that...'