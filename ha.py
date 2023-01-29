import re

#Finds a substring using a regex and returns the match in a dictionary used as replacement map. 
#Returns an empty string if a match is not found
def find_and_replace(string: str, pattern: str, repl_map_dict: dict):
  # Compile the regular expression pattern
  regex = re.compile(pattern)
  
  # Define the replacement function
  def replacement(match):
    # Get the matched string
    matched_string = match.group()
    
    # Check if the matched string is in the replacement dictionary
    if matched_string in repl_map_dict:
      # Return the corresponding replacement from the dictionary
      return repl_map_dict[matched_string]
    else:
      # Return the original matched string if it's not in the dictionary
      return matched_string
  
  # Use the sub() function to find and replace the pattern
  modified_string = regex.sub(replacement, string)
  
  #Returns an empty string if a match is not found
  if modified_string == string:
    modified_string = ""

  # Return the modified string
  return modified_string

#Given a devcie name, find the HA peer, assuming they follow a specific naming convention (ie. pattern)
def getHApeer(device: str, pattern: str, haMap: dict):    
    haPair = find_and_replace(device, pattern, haMap)
    if haPair == "":
        print('Pair not found')
    
    return haPair
