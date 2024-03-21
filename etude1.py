
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

import sys 

def ParsePartitions(inputLines):
    outputLines = []
    hasValidPartition = False
    inScenario = False 

    #Function to standardise partition when found 
    def StandardisePartition(partition):
        parts = sorted(map(int, partition.replace(',', ' ').split()), reverse=True)
        return ' '.join(map(str, parts))
    
    # Function to handle mixed separators incases like '1, 2 3' in example input 1
    def isMixedSeparationInPartition(line):
        if ',' in line:
            partsWithComma = line.split(',')
            for part in partsWithComma:
                if ' ' in part.strip() and ',' not in part:
                    return True
        return False
    
    # Each line processed 
    for line in inputLines:

        # each line stripped of whitespace 
        line = line.rstrip()

        # handle separators 
        if len(line) >= 3 and all(c == '-' for c in line):

            if inScenario and not hasValidPartition:
                outputLines.append("# INVALID SCENARIO")
                outputLines.append("--------")
            elif inScenario:
                outputLines.append("--------")
            hasValidPartition = False
            inScenario = False 
            continue

        # track scenarios 
        if line or inScenario:
            inScenario = True

        # handle empty lines - ensuring only one empty line added between content (avoid multiple empty lines)
        if not line:
            if outputLines and outputLines[-1] != "":
                outputLines.append("") 
            continue
         
        # handle comments, echoing them in output
        if line.startswith('#'):
            outputLines.append(line)
            continue

        # if any invalid partitions, mark invalid. Invalid can be by mixed separators, alphabetic chars, or special chars
        # if any valid partitions, standardise it.
        if isMixedSeparationInPartition(line) or any(c.isalpha() for c in line) or any(c in "!@#$%^&*()" for c in line):
            outputLines.append(f"# INVALID: {line}")
        else:
            try:
                line_preprocessed = line.replace(', ', ' ').replace(',', ' ')
                standardisedPartition = StandardisePartition(line_preprocessed)
                outputLines.append(standardisedPartition)
                hasValidPartition = True
            except ValueError:
                outputLines.append(f"# INVALID: {line}")
    # end of line loop
                
    # Final scenario check 
    if inScenario and not hasValidPartition:
        outputLines.append("# INVALID SCENARIO")
    elif inScenario:
        outputLines.append("--------")

    while outputLines and (not outputLines[-1] or outputLines[-1] == "# INVALID SCENARIO"):
        outputLines.pop() 

    return outputLines


if __name__ == "__main__":
    input_lines = sys.stdin.readlines()
    output = ParsePartitions(input_lines)
    for line in output:
        print(line)