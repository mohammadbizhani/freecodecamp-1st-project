def arithmetic_arranger(list, answer = False):

  list1 = []
  list2 = []
def arithmetic_arranger(list, answer = False):

  list1 = []
  list2 = []
  list3 = []

  first_line = []
  second_line = []
  third_line = []
  fourth_line = []
  # check the size
  if len(list) > 5:
    return "ERROR: To many problems."

  for i in list:
    k = i.split()
    list1.append(k[0])
    list2.append(k[1])
    list3.append(k[2])

  # check the operator
  if "*" in list2 or "/" in list2:
    return "ERROR: You can just use '+' and '-'."

  # check the digits
  for i in range(len(list1)):
    if not (list1[i].isdigit() and list3[i].isdigit()):
      return "ERROR: Numbers must be digits."

  # check the length of numbers
  for i in range(len(list1)):
    if len(list1[i]) > 4 or len(list3[i]) > 4:
      return "ERROR: Numbers cannot be more than four digits."

  for i in range(len(list1)):
    if len(list1[i]) > len(list3[i]):
      first_line.append(" "*2 + list1[i])
    else:
      first_line.append(" "*(len(list3[i]) - len(list1[i]) + 2) + list1[i])

  for i in range(len(list1)):
    if len(list3[i]) > len(list1[i]):
      second_line.append(list2[i] + " " + list3[i])
    else:
      second_line.append(list2[i] + " "*(len(list1[i]) - len(list3[i]) + 1) + list3[i])

  for i in range(len(list1)):
    third_line.append("-"*(max(len(list1[i]), len(list3[i])) + 2))

  if answer:
    for i in range(len(list1)):
      if list2[i] == "+":
        ans = str(int(list1[i]) + int(list3[i]))
      else:
        ans = str(int(list1[i]) - int(list3[i]))

      if len(ans) <= max(len(list1[i]), len(list3[i])):
        fourth_line.append(" "*( max(len(list1[i]), len(list3[i])) - len(ans) + 2) + ans)
      else:
        fourth_line.append(" " + ans)

    arithmetic_arranger = print("    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line))
  
  else:
    arithmetic_arranger = print("    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n")

  return arithmetic_arranger


arithmetic_arranger(["8524 + 8388", "354 - 525", "9999 + 9999", "71 - 68"], True)
