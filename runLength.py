def RunLength(strParam):

  e_string = ""
  i = 0

  while (i <= len(strParam)-1):
    count = 1
    ch = strParam[i]
    j = i

    while (j < len(strParam) - 1):
      if (strParam[j] == strParam[j+1]):
        count = count + 1
        j = j + 1
      else:
        break

    e_string = e_string + str(count) + ch 
    i = j + 1

  return e_string

print(RunLength(input()))