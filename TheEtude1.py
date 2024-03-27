# Author: Blake Leahy 

import sys

def main():
    
    allScenarios = []
    currentScenario = []
    scenarioHasPartition = False

    for line in sys.stdin:

        line = line.rstrip('\n')

        if isBlank(line):

            if currentScenario and currentScenario[-1] != "":
                currentScenario.append("")
            continue

        elif isComment(line):

            currentScenario.append(line)

        elif isPartition(line):

            line = standardisePartition(line)
            currentScenario.append(line)
            scenarioHasPartition = True

        elif isSeparator(line):
            
            if currentScenario: 
                if not scenarioHasPartition:
                    currentScenario.insert(0, "# INVALID SCENARIO") 
                allScenarios.append(currentScenario)
                # Reset for next scenario as isSeparator true 
                currentScenario = []  
                scenarioHasPartition = False
        else:
            # if line not blank,comment,partition or separator, INVALID 
            currentScenario.append(f"# INVALID: {line}")

    # If the file ends without a separator, finalise the last scenario
    if currentScenario:
        if not scenarioHasPartition:
            currentScenario.insert(0, "# INVALID SCENARIO")
        allScenarios.append(currentScenario)

    # output all scenarios except the last one
    for scenario in allScenarios[:-1]:
        print("\n".join(scenario).strip())
        print("--------")  

    # Print the last scenario - don't add an extra separator
    print("\n".join(allScenarios[-1]).strip())

def standardisePartition(partition):
    parts = sorted(map(int, partition.replace(',', ' ').split()), reverse=True)
    return ' '.join(map(str, parts))

def isPartition(line):
    if isMixedSeparationInPartition(line):
        return False
    elif ',,' in line:
        return False
    elif line.endswith(','):
        return False
    parts = line.replace(',', ' ').split()
    return all(part.isdigit() and int(part) > 0 and str(int(part)) == part for part in parts)
    #return all(part.isdigit() for part in line.replace(',', ' ').split())


def isMixedSeparationInPartition(line):
        if ',' in line:
            partsWithComma = line.split(',')
            for part in partsWithComma:
                if ' ' in part.strip() and ',' not in part:
                    return True
        return False

def isComment(line):
    return line.startswith('#')

def isBlank(line):
    return not line.strip()

def isSeparator(line):
    return set(line.strip()) == {'-'} and len(line.strip()) >= 3


if __name__ == "__main__":
    main()
