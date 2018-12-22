#!/usr/bin/env python
from functools import reduce
import os
import random
import sys

class DicewarePhrase:
  NUM_ROLLS = 5
  NUM_SIDES = 6
  DEFAULT_NUM_WORDS_IN_PHRASE = 5
  def __init__(self):
    self.initialize_data()
    self.r = random.Random()

  def word(self):
    num = 0
    for i in range(self.NUM_ROLLS):
      num = num * 10 + self.r.randint(1, self.NUM_SIDES)
    return self.data[num]

  def phrase(self, n=None):
    if not n:
      n = self.DEFAULT_NUM_WORDS_IN_PHRASE
    return reduce(lambda s1, s2: s1 + ' ' + s2, [self.word() for i in range(n)])

  def initialize_data(self):
    script_dir = os.path.dirname(__file__)
    wordlist_path = os.path.join(script_dir, 'eff_large_wordlist.txt')
    fp = open(wordlist_path, 'r')
    self.set_message_bounds(fp)
    self.data = { }
    fp.seek(self.offset[0])
    while fp.tell() < self.offset[1]:
      s = fp.readline().strip()
      if s == '':
        continue
      # print(s)
      num, word = s.split()
      self.data[int(num)] = word
    fp.close()

  def set_message_bounds(self, fp):
    starting_offset = 0
    ending_offset = 0
    s = fp.readline()
    while s and '-----BEGIN PGP SIGNED MESSAGE-----' not in s:
      s = fp.readline()
    if '-----BEGIN PGP SIGNED MESSAGE-----' not in s:
      self.offset = (0, fp.tell())
      return

    starting_offset = fp.tell()

    while s and '-----BEGIN PGP SIGNATURE-----' not in s:
      s = fp.readline()
    if '-----BEGIN PGP SIGNATURE-----' not in s:
      ending_offset = fp.tell()
    else:
      ending_offset = fp.tell() - len(s)

    self.offset = (starting_offset, ending_offset)

if __name__ == '__main__':
  dp = DicewarePhrase()
  # print(sys.argv)
  n = 5
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
  print(dp.phrase(n))
