from typing import Dict, List

# loops through classes to find class with key matching the keyword provided
# returns the class' value
def GetClass(keyword: str, classes: List[Dict]):
  for dict in classes:
    for key in dict.keys():
      if keyword == key:
        return dict[keyword]
  return None

# Loops through the provided dict and extract all keys into a list
# return the list
def GetListOfKeysFromDict(dict: dict) -> list[str]:
  listOfKeys = []
  for key in dict.keys():
    listOfKeys.append(key)
  return listOfKeys

# Loops through the provided dict and extract all keys that starts with a given keyword into a list
# return the list
def GetFilteredListOfKeysFromDict(dict: dict, keyword: str) -> list[str]:
  listOfKeys = []
  for key in dict.keys():
    if key.startswith(keyword) == True:
      listOfKeys.append(key)
  return listOfKeys

# Loops through the provided list and extract all values that starts with the given keyword into a list
# return the list of filtered values
def GetFilteredList(list: list, keyword: str) -> list[str]:
  listOfKeys = []
  for value in list:
    if value.startswith(keyword) == True:
      listOfKeys.append(value)
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
    if splitStatement[-1] == "":  # statement ends in period
      # if the statements value ends in period, it is a key to search for in classes
      splitStatement.pop()
      if len(splitStatement) == 1:
        # Loop through classes using the key found from statements
        classObjectValue = GetClass(splitStatement[-1], classes)
        if classObjectValue is None or classObjectValue == "":  # key not found in classes
          output[statement] = [""]
          continue
        else:  # key found
          if type(classObjectValue) == dict:
            # If the object found in classes has a Dict for value
            #  Extract the Key from the inner Dict into a list
            innerDictList = GetListOfKeysFromDict(classObjectValue)
            #  Sort the list in alphebatical order
            innerDictList.sort()
            #  add the top 5 from the list as output for the statement
            output[statement] = innerDictList[0:5]
            continue
          # check if object is list
          if type(classObjectValue) == list:
            # If the object found in classes has a list for value
            # sort list in alphebatical order
            classObjectValue.sort()
            # add the top 5 from the list for output
            output[statement] = classObjectValue[0:5]
            continue
      # This is a polymorphic type
      elif len(splitStatement) > 1:
        # returns empty list for output
        output[statement] = [""]
        continue
    else:
      # if the statements value does not end in period, it is a parameter to compare with
      if len(splitStatement) == 2:
        #  Find the word after the second period counting from the right for the key to search for in classes
        classObjectValue = GetClass(splitStatement[-2], classes)
        if classObjectValue is None or classObjectValue == "":  # key not found in classes
          output[statement] = [""]
          continue
        if type(classObjectValue) == dict:  # the inner object is a dict
          # Get the list of keys of the dict filtered by given parameter
          innerDictList = GetFilteredListOfKeysFromDict(
            classObjectValue, splitStatement[-1])
          # sort filtered list
          innerDictList.sort()
          # Only insert the top 5 words
          output[statement] = innerDictList[0:5]
          continue
        if type(classObjectValue) == list: # Object is a list
          # Filter the list with given parameter
          filteredList = GetFilteredList(classObjectValue, splitStatement[-1])
          # sort filter list
          filteredList.sort()
          # only insert the top 5 words
          output[statement] = filteredList[0:5]
          continue
      # If len more than 2 it is a polymorphic type
      elif len(splitStatement) > 2:
        # returns empty list for output
        output[statement] = [""]
        continue
  return output
