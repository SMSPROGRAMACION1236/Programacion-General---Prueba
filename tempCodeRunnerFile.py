
while True: 
  subjects = ["math", "physic", "chemistry", "history", "literature"]
  for subject in subjects:
    grades = int(input(f"How is your grade in {subject}: "))
    print(f"I took{grades} in {subject}")
  break