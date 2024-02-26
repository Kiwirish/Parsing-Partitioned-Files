
# Partition is a way of writing a positive integer as a sum of positive integers
# eg 5 has paritions: (5),(4,1),(3,2),(2,2,1), etc 

# What i must do 
# Must differentiate between:
#       -comment lines starting with '#' 
#       -Empty lines 
#       -Partition lines, so a sequence of positive integers 
#        separated by commas or whitespace 
#       -Separator lines with 3 hyphens '---'
# Standardisation output requirements:
#       -Partitions in non-increasing order, separated by whitespace
#       -separation lines exactly 8 hyphens 
#       -If a line isn't the expected format, mark as invalid w # INVALID 
#       -If a scenario has no valid partitions, mark w # INVALID SCENARIO

# I must write a program that reads input from stdin,
# process the content (identify types of lines, check validty as partition, applys standardisation),
# then write standardised content to stdout 

# approach: read and classify inputs lines and determines types 
#           (comment, empty, partition or separator)
#  will need: 
# scenario_valid boolean 
# output_lines array 
# ^^ in function process_input 
# Functions: isPartitionLine, ProcessPartitionLine, isSeparatorLine - all called in ProcessInput. 
# In main, i must sys.stdin.readlines() then call processInput function set to standardisedOutput then print new standardised output
#  psuedocode: 
#   for all lines in input_lines
#   if current line is separator line 
#     then append 8 hyphens to output_lines 
#   elseif current line is '' or whiteSpace 
#     then append "" empty line to output_lines 
#   elseif current line starts with '#'
#   also if current lines scenario is valid
#     then append current line to output_lines
#   else current line's not valid, append f"# INVALID: {line}" to output_lines
#   elseif current line is a partition line (partition function call),
#     then ProcessPartitionLine function called with partition line 
#     and appended to output_lines
#   else it must be an invalid line so append f"# INVALID: {line}" to output_lines
#   if NOT scenario_valid, append # INVALID SCENARIO to output_lines