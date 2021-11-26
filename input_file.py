input_file = open("dataset_isp.csv", "r", encoding = "utf-8")
output_files = open("url_data.csv","w", encoding="utf-8")
input_lines = input_file.readlines()
input_file.close()


for line in range(0,len(input_lines)):
    line_mass = input_lines[line].split(",")
    if line_mass[3] == "legit":
        line_bool_dga = 1
    else:
        line_bool_dga = -1

    output_files.writelines(line_mass[2] +","+ str(line_bool_dga) + "\n")


