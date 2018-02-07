import port as p
import space_tabs as st

#extracts the entity string (entity declaration to end <entity_name>)
def get_entity(filename):
    entity_string = ""
    entity_flag = 0
    infile = open(filename)
    for line in infile:
        if len(line.strip()) > 6 and line.strip()[0:6] == "entity":
            entity_flag = 1
        if len(line.strip()) > 4 and line.strip()[0:3] == "end":
            entity_flag = 0
            entity_string += line
            break
        if entity_flag:
            entity_string += line
    infile.close()
    return entity_string.strip()

#extracts port info from the entity string
#currently only works with std_logic and std_logic_vectors
def create_ports(entity_string):
    ports = []
    lines = entity_string.split("\n")
    for line in lines:
        if ":" in line:
            words = line.strip().split(" ")
            words = clear_empty_strings(words)
            name = words[0]
            data_type = "std_logic"
            direction = words[2]
            if "std_logic_vector" in words[3]:
                data_type = "std_logic_vector"
            size = 1
            if data_type == "std_logic_vector":
                lenstring = clear_empty_strings\
                    (line.split("(")[1].split(")")[0].strip().split(" "))
                size = abs(int(lenstring[0]) - int(lenstring[2])) + 1
            a = p.port(data_type, direction, size, name)
            ports.append(a)
    return ports

#clears empty entries out of a list of strings
def clear_empty_strings(str_list):
    j = 0
    for i in range(0, len(str_list)):
        if len(str_list[j]) == 0:
            del str_list[j]
            j-=1
        j+=1
    return str_list

def get_entity_name(entity_string):
    return clear_empty_strings(entity_string.split(" "))[1]

def entity_test_string(entity_name):
    return "entity " + entity_name + "_test is\nend " + entity_name + "_test;"

def component_string(entity_name, ports):
    ret = "\tcomponent " + entity_name + "\n\tport(\n"
    port_num = 1 
    for port in ports:
        if port.data_type == "std_logic_vector":
            upper_bound = port.size - 1
            ret += "\t\t" + port.name + "\t:\t" + port.direction + "\tstd_logic_vector(" + str(upper_bound) + " downto 0)"
        else:
            ret += "\t\t" + port.name + "\t:\t" + port.direction + "\tstd_logic"
        if port_num != len(ports):
            ret += ";\n"
        else:
            ret += "\n"
            ret += "\t);\n"
            ret += "\tend component;\n"
        port_num += 1

    #allign tabs of port declaration
    split = ret.split('\n')
    split[2:(2 + len(ports))] = st.allign_tabs(split[2:(2 + len(ports))])
    ret = ""
    for line in split:
        ret += line + '\n'
    return ret

def signal_string(ports):
    ret = ""
    for port in ports:
        if port.data_type == "std_logic_vector":
            upper_bound = port.size - 1
            ret += "\tsignal\ts_" + port.name + "\t:\t" + port.data_type + "(" + str(upper_bound) + " downto 0);\n"
        else:
            ret += "\tsignal\ts_" + port.name + "\t:\t" + port.data_type + ";\n"
    split = ret.rstrip().split('\n')
    split = st.allign_tabs(split)
    ret = ""
    for line in split:
        ret += line + '\n'
    return ret 

def main():
    filename = "count_decoder.vhd"
    entity_string = get_entity(filename)
    entity_name = get_entity_name(entity_string)
    ports = create_ports(entity_string)
    print(st.tabs_to_spaces(component_string(entity_name, ports)))
    print(st.tabs_to_spaces(signal_string(ports)))

main()
