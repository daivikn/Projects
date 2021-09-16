questions = {
  "When was the last year Neptune made a full orbit around the sun?": "2011",
  "Is Pluto a dwarf planet?": "yes",
  "What is the asteroid belt located past Neptune called?": "kuiper belt",
  "How many phases does the Earth's moon have?": "8",
  "How many Earths would fit inside Jupiter?": "1300",
}

for question,correctanswer in questions.items():

  answer = input(question + ": ").lower()

  if answer == correctanswer:
    print("Nice job!")
  else:
    print("WRONG!!!!")
