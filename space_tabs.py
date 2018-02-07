def tabs_to_spaces(string, num_spaces = 4):
    lines = string.split('\n')
    ret = ""
    for i in range(0, len(lines)):
        split_string = lines[i].split('\t')
        lines[i] = _tabs_to_spaces(split_string, num_spaces)    
    for line in lines:
        if len(line) > 0:
            ret += line + "\n"
    return ret    

def _tabs_to_spaces(split_string, num_spaces):
    if len(split_string) > 1:
        spaces = ""
        #if len(split_string[0]) > 0:
        #    for i in range(0, num_spaces):
        #        spaces += " "
        #else:
        for i in range(0, num_spaces - (len(split_string[0]) % num_spaces)):
            #print(str(len(split_string[0]) % num_spaces))
            spaces += " "
        split_string[0] = split_string[0] + spaces + split_string.pop(1)
        return _tabs_to_spaces(split_string, num_spaces)
    else:
        return split_string[0]

#alligns tabs on seperate lines
def allign_tabs(lines, num_spaces = 4):
    split_lines = []
    for line in lines:
        split_lines.append(line.split('\t'))
    
    #find the line with the minimum number of tabs
    min_tabs = len(split_lines[0])
    for line in split_lines[1:]:
        length = len(line)
        if length < min_tabs:
            min_tabs = length

    #for each tab division, find the number of tabs needed so they allign
    for i in range(0, min_tabs):
        
        #find which line has the longest division
        max_tabs = len(line[i]) // num_spaces
        for line in split_lines:
            division_length = len(line[i]) // num_spaces
            if len(line[i]) // num_spaces > max_tabs:
                max_tabs = division_length
        
        #add the correct amount of tabs
        for j in range(0, len(split_lines)):
            for k in range(0, max_tabs - len(split_lines[j][i]) // num_spaces):
                split_lines[j][i] += '\t'
                
    #recombine lines
    for i in range(0, len(lines)):
        new_line = ""
        for j in range(0, len(split_lines[i]) - 1):
            new_line += split_lines[i][j] + '\t'
        new_line += split_lines[i][len(split_lines[i]) - 1] 
        lines[i] = new_line

    return lines
                   
