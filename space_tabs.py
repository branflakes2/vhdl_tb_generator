def tabs_to_spaces(string, num_spaces = 4):
    split_string = string.split('\t')
    return _tabs_to_spaces(split_string, num_spaces)    

def _tabs_to_spaces(split_string, num_spaces):
    if len(split_string) > 1:
        spaces = ""
        for i in range(0, num_spaces - (len(split_string[0]) % num_spaces)):
            spaces += " "
        split_string[0] = split_string[0] + spaces + split_string.pop(1)
        return _tabs_to_spaces(split_string, num_spaces)
    else:
        return split_string[0]

def allign_tabs(string, num_spaces = 4):
    lines = string.split('\n')
    split_lines = []
    for line in lines:
        split_lines.insert(0, line.split('\t'))
    
    #find the line with the minimum number of tabs
    min_tabs = len(split_lines[0])
    for line in split_lines[1:]:
        length = len(line)
        if length < min_tabs
            min_tabs = length
    
    #for each tab division, find the number of tabs needed so they allign
    for i in range(0, min_tabs):
        
        #find which line has the longest division
        max_tabs = len(line[i]) // num_spaces
        for line in split_lines[1:]:
            division_length = len(line[i]) // num_spaces
            if len(line[i]) // num_spaces > max_tabs
                max_tabs = division_length
            
            
