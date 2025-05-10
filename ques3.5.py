with open("D:\\students.csv", "w", newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Name", "Age", "Score"])
  writer.writerow(["Alice", 20, 85])
  writer.writerow(["Bob", 22, 78])
  writer.writerow(["Charlie", 23, 90])


with open("D:\\students.csv", "r") as file:
  reader = csv.reader(file)
  next(reader)
  for row in reader:
    name, age, score = row
    if int(score) > 80:
      print(f"{name} scored {score}.")