from typing import Dict, List


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
  # Fill in your solution here and return the correct output based on the given input

  # Loop through statements
  # For each str value in statements
  # Check if the statements value ends in period
  # if the statements value does not end in period, it is a parameter to compare with
  #  Find the word after the second period counting from the right for the key to search for in classes
  # if the statements value ends in period, it is a key to search for in classes
  # Loop through classes using the key found from statements
  # If the Dict found in classes using the key has a Dict for value
  #  Extract the Key from the inner Dict into a list
  #  Sort the list in alphebatical order
  #  If a parameter was provided compare the parameter with each word in the sorted list
  #  Return the top 5 from the list as output for the statement
  # If the Dict found in classes has a list for value
  #  Check if list is a enum or polymorphic type
  #  If string in list are found as key in classes, it is a polymorphic type
  #   return empty list for polymorphic type
  #  Else the list is enum
  #   Sort the list in alphebatical order
  #   If parameter was provided, compare the parameter with each word in the sorted list
  #   return top 5 in the list as output for the statement
  
  return {}
