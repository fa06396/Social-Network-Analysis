import csv


def readCSV(combined, file_name):
    temp = file_name
    file_name = file_name + '.csv'
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            # print(row)
            if row[1] in combined:
                combined[row[1]]["Committees"].append(temp)
            else:
                combined[row[1]] = {"Party": row[2],
                                    "Committees": [temp], "NA": row[3]}
                # partyDict[row[1]] = row[2]
        csv_file.close()


def refined(combined, s_no):
    refined = {}
    for i in combined:
        refined[str(s_no)] = {i: combined[i]}
        s_no += 1
    return refined


def __helper_edgeList__(edgeList):
    with open('combined_edge_list.txt', 'w') as txt_file:
        for i in edgeList:
            for j in edgeList[i]:
                writeLine = i + ' ' + j + '\n'
                txt_file.write(writeLine)
        txt_file.close


def create_edgeList(refined):
    edgeList = {}
    for i in refined:
        edgeList[i] = []
        for j in refined:
            if i != j:
                for k in refined[i]:
                    for l in refined[i][k]['Committees']:
                        # print(f'l = {l}')
                        for m in refined[j]:
                            if l in refined[j][m]['Committees']:
                                edgeList[i].append(j)
                        # print(f'j,m = {refined[j][m]}')
                        # if l in m['Committees']:
    __helper_edgeList__(edgeList)


def createCSV(combined):
    header = ["S.no", "Name", "Party", "Committees", "NA"]
    file_name = 'Combined.csv'
    with open(file_name, 'w', newline='') as f:
        counter = 1
        writer = csv.writer(f)
        writer.writerow(header)
        for i in combined:
            data = []
            data.append(counter)
            data.append(i)
            data.append(combined[i]["Party"])
            temp = '['
            for j in combined[i]["Committees"]:
                temp += j + ','
            temp = temp.strip(',') + ']'
            data.append(temp)
            data.append(combined[i]["NA"])
            # data.append(combined[i][0])
            # for j in combined[i]:
            #     data.append(j)
            counter += 1
            writer.writerow(data)
        f.close()


def nameFile():
    nameList = []
    partyList = []
    with open("Combined.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            nameList.append(row[1])
            partyList.append(row[2])
        csv_file.close()

    with open("namelist.txt", 'w') as txt_file:
        for i in nameList:
            writeLine = i + '\n'
            txt_file.write(writeLine)
        txt_file.close()

    with open("party.txt", 'w') as txt_file:
        for i in partyList:
            writeLine = i + '\n'
            txt_file.write(writeLine)
        txt_file.close()


def naFile():
    naList = []
    with open("Combined.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            naList.append(row[4])
        csv_file.close()

    with open("na_list_2013.txt", 'w') as txt_file:
        for i in naList:
            writeLine = i + '\n'
            txt_file.write(writeLine)
        txt_file.close()


# def partyFile(dct):
#     with open("partylist.txt", 'w') as txt_file:
#         for i in dct:
#             writeLine = dct[i] + '\n'
#             txt_file.write(writeLine)
#         txt_file.close()


def main():
    # NAME_LIST = [
    #     'Aviation', 'Cabinet Secretariat', 'Climate Change',
    #     'Commerce', 'Communications', 'Defence Production',
    #     'Defence', 'Economic Affairs Division', 'Energy',
    #     'Federal Education, Professional Training, National Heritage and Culture'
    # ]
    NAME_LIST = ['Cabinet Secretariat', 'Climate Change', 'Commerce and Textile', 'Communications', 'Defence', 'Defence Production',
                 'Energy', 'Federal Education and Professional Training',
                 'Finance, Revenue and Economic Affairs', 'Foreign Affairs', 'Housing and Works', 'Human Rights', 'Industries and Production',
                 'Information Technology and Telecommunication', 'Information, Broadcasting, National History and Literary Heritage',
                 'Inter-Provincial Coordination', 'Interior', 'Kashmir Affairs and Gilgit-Baltistan', 'Law and Justice', 'Maritime Affairs', 'Narcotics Control',
                 'National Food Security and Research', 'National Health Services, Regulations and Coordination',
                 'Overseas Pakistanis and Human Resource Development', 'Parliamentary Affairs',
                 'Planning and Development', 'Postal Services', 'Privatization', 'Railways',
                 'Religious Affairs and Inter-faith Harmony', 'Science and Technology',
                 'States and Frontier Regions', 'Statistics', 'Water Resources']

    combined = {}
    partyDct = {}
    s_no = 1
    for i in NAME_LIST:
        readCSV(combined, i)
    createCSV(combined)
    naFile()
    # refinedDct = refined(combined, s_no)
    # print(refinedDct)
    # create_edgeList(refinedDct)
    # print(refinedDct)
    # nameFile()
    # partyFile(partyDct)


if __name__ == '__main__':
    main()
