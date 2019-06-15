import sys



def main(): 
    filename = str(sys.argv[1])
    print(filename)
    with open(filename, "r") as f:
        online_lines = f.readlines()
        online_lines = online_lines
        online_lines = set(online_lines)
        parsed_lines = list()
        for element in online_lines:
            element = "'" + element.rstrip(" \xa0\n") + "'" + ",\n"
            if element != "":
                parsed_lines.append(element)
        

    with open(filename, "w") as f:
        f.writelines(parsed_lines)
    return
        #f.writelines(parsed_list)

    
if __name__ == "__main__":
    main()
