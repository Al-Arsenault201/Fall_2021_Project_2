
def read_a_file(filename):
    with open(filename,"r") as infile:
        infile.readline()
        infile.readline()
        data = infile.read()
        data_list = data.split('\n')
        for i in range(len(data_list)):
            if data_list[i] == "":
                data_list.pop(i)
        for i in range(len(data_list)):
            data_list[i] = data_list[i].split(',')

        return data_list


def insert_new_columns(two_d_list):
    for i in range(len(two_d_list)):
        ptot = int(two_d_list[i][3]) + int(two_d_list[i][4]) + int(two_d_list[i][5])
        two_d_list[i].insert(6,ptot)
        class_tot = ptot + int(two_d_list[i][7]) + int(two_d_list[i][8]) + int(two_d_list[i][9])
        two_d_list[i].insert(10,class_tot)
    return two_d_list

if __name__ == "__main__":
    main_db =[]
    n_files = int(input("How many files are to be read?"))
    for i in range(n_files):
        fn = input("Enter the full path to the file to be read")
        fdb = read_a_file(fn)
        new_fdb = insert_new_columns(fdb)
        main_db.append(new_fdb)

    for i in range(n_files):
#        print(main_db[i])



        for j in range(len(new_fdb)):
            for k in range(len(new_fdb[j])):
                print(new_fdb[j][k], end = '\t')
            print('\n')
