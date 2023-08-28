from typing import Dict, List

def GetClass(keyword: str, classes: List[Dict]):
  for dict in classes:
    for key in dict.keys():
      if keyword == key:
        return dict[keyword]
  return None

def GetListOfKeysFromDict(dict):
  listOfKeys = []
  for key in dict.keys():
    listOfKeys.append(key)
  return listOfKeys

def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  # Fill in your solution here and return the correct output based on the given input
  output = {}
  # Loop through statements
  # For each str value in statements
  for statement in statements:
    splitStatement = statement.split(".")
    # Check if the statements value ends in period
    if splitStatement[-1] == "": # statement ends in period
      # if the statements value ends in period, it is a key to search for in classes
      splitStatement.pop()
      if len(splitStatement) == 1:
        # Loop through classes using the key found from statements
        classObjectValue = GetClass(splitStatement[-1],classes)
        if classObjectValue is None: # key not found in classes
          output[splitStatement[-1]] = ""
          continue
        else: # key found
          if type(classObjectValue) == dict: 
            # If the object found in classes has a Dict for value
            #  Extract the Key from the inner Dict into a list
            innerDictList = GetListOfKeysFromDict(classObjectValue)
            #  Sort the list in alphebatical order
            innerDictList.sort()
            #  add the top 5 from the list as output for the statement
            output[splitStatement[-1]] = innerDictList[0:5]
            continue

          # check if object is list
          if type(classObjectValue) == list:
            # If the object found in classes has a list for value
            # sort list in alphebatical order
            classObjectValue.sort()
            # add the top 5 from the list for output
            output[splitStatement[-1]] = classObjectValue[0:5]
            continue
      # This is a polymorphic type
      elif len(splitStatement) > 1:
        # returns empty list for output
        output[splitStatement[-1]] = ""
        continue
    else:  
      # if the statements value does not end in period, it is a parameter to compare with
      #  Find the word after the second period counting from the right for the key to search for in classes
      classObjectValue = GetClass(splitStatement[-2],classes)
      if classObjectValue is None: # key not found in classes
        output[splitStatement[-2]] = ""
        continue
      else:
        print()
  



  print(output)
  return output
