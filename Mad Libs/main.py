import random
import argparse

def get_blanks(story):
  # print "story", story
  blanks = []

  while len(story) > 0:
    start = story.find("{{")
    end = story.find("}}")
    if start == -1:
      break

    blank = story[start + 2 : end]
    blanks.append(blank)
    # print "found blank word:", blank

    story = story[end + 2 : ]
    # print "story sliced to:", story


  return blanks

def main():
  parser = argparse.ArgumentParser(description="""This project is a mad lib, which is a story with some
   words missing that you need to fill in.
   There are descriptions telling you whether
   the word needs to be a noun, adjective, etc.""")
  args = parser.parse_args()
  story = random.choice(stories)

  blanks = get_blanks(story)

  for blank in blanks:
    answer = input(blank + ":")

    story = story.replace("{{" + blank + "}}", answer, 1)

  print
  print(story)

main()
