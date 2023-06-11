import requests
from bs4 import BeautifulSoup
import re
import csv


def CSVWriter(dct, file_name):
    header = ["S.no", "Name", "Party", "Constituency"]
    file_name = file_name + '.csv'
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in dct:
            data = []
            data.append(i)
            for j in dct[i]:
                data.append(dct[i][j])
            writer.writerow(data)
        f.close()


def combined_dataframe(combined, dataframe):
    for i in dataframe:
        combined[dataframe[i]['$name']] = [dataframe[i]['$party']]


def extraction(url, file_name, combined):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    partyList = ['PTI', 'PPPP', 'PML-N', 'MQMP',
                 'MMAP', 'GDA', 'PML', 'Ind', 'BNP', 'BAP', 'JWP']
    dataframe = {}
    s_no = '0'
    isRepeat = False
    party = ''
    constituency = ''
    table = soup.find('table')
    rows = table.find_all('tr')
    for i in rows:
        col = i.find_all('tr')
        for j in col:
            name = ''
            partyFound = False
            text = j.getText()
            result = re.sub(r'\s+', ' ', text)
            temp = result.split()
            if len(temp) >= 7 and len(temp) <= 15:
                if temp[0].strip('.').isnumeric():
                    s_no = temp[0].strip('.')
                    if isRepeat and s_no == '1':
                        break
                    for data in range(1, len(temp)):
                        if temp[data] in partyList:
                            partyFound = True
                            party = temp[data]
                        elif not partyFound:
                            name += temp[data] + ' '
                        elif data == len(temp) - 1:
                            constituency = temp[data]
                    name = name.strip()
                    dataframe[s_no] = {
                        "$name": name,
                        "$party": party,
                        "$constituency": constituency
                    }
                    isRepeat = True
    CSVWriter(dataframe, file_name)
    combined_dataframe(combined, dataframe)


def get_edgeList(dct):
    newDct = {}
    for i in dct:
        localList = []
        for j in dct:
            if i != j:
                if dct[i][1] == dct[j][1]:
                    localList.append(j)
        newDct[i] = localList
    with open('combined.txt', 'w') as txt_file:
        for nodes in newDct:
            for edges in newDct[nodes]:
                writeLine = nodes + ' ' + edges + '\n'
                txt_file.write(writeLine)
        txt_file.close()


def main():
    URL_LIST = [
        'https://na.gov.pk/en/cmen.php?comm=MTU2',
        'https://na.gov.pk/en/cmen.php?comm=MQ==',
        'https://na.gov.pk/en/cmen.php?comm=ODY=',
        'https://na.gov.pk/en/cmen.php?comm=Mg==',
        'https://na.gov.pk/en/cmen.php?comm=Mw==',
        'https://na.gov.pk/en/cmen.php?comm=Ng==',
        'https://na.gov.pk/en/cmen.php?comm=Nw==',
        'https://na.gov.pk/en/cmen.php?comm=MTY0',
        'https://na.gov.pk/en/cmen.php?comm=MzA=',
        'https://na.gov.pk/en/cmen.php?comm=NTg=',
        'https://na.gov.pk/en/cmen.php?comm=MTQ=',
        'https://na.gov.pk/en/cmen.php?comm=MjA=',
        'https://na.gov.pk/en/cmen.php?comm=MjU=',
        'https://na.gov.pk/en/cmen.php?comm=OTE=',
        'https://na.gov.pk/en/cmen.php?comm=Mjg=',
        'https://na.gov.pk/en/cmen.php?comm=Mjk=',
        'https://na.gov.pk/en/cmen.php?comm=NA==',
        'https://na.gov.pk/en/cmen.php?comm=OA==',
        'https://na.gov.pk/en/cmen.php?comm=MTA=',
        'https://na.gov.pk/en/cmen.php?comm=MTM=',
        'https://na.gov.pk/en/cmen.php?comm=MTY=',
        'https://na.gov.pk/en/cmen.php?comm=MzE=',
        'https://na.gov.pk/en/cmen.php?comm=MTA5',
        'https://na.gov.pk/en/cmen.php?comm=NjI=',
        'https://na.gov.pk/en/cmen.php?comm=MjM=',
        'https://na.gov.pk/en/cmen.php?comm=MTE=',
        'https://na.gov.pk/en/cmen.php?comm=NzI=',
        'https://na.gov.pk/en/cmen.php?comm=ODA=',
        'https://na.gov.pk/en/cmen.php?comm=MTY3',
        'https://na.gov.pk/en/cmen.php?comm=MTQz',
        'https://na.gov.pk/en/cmen.php?comm=MTEw',
        'https://na.gov.pk/en/cmen.php?comm=MzU=',
        'https://na.gov.pk/en/cmen.php?comm=MzY=',
        'https://na.gov.pk/en/cmen.php?comm=Mzg=',
        'https://na.gov.pk/en/cmen.php?comm=NDE=',
        'https://na.gov.pk/en/cmen.php?comm=NDQ='
    ]

    NAME_LIST = ['Aviation', 'Cabinet Secretariat', 'Climate Change', 'Commerce', 'Communications', 'Defence', 'Defence Production',
                 'Economic Affairs Division', 'Energy', 'Federal Education, Professional Training, National Heritage and Culture',
                 'Finance and Revenue', 'Foreign Affairs', 'Housing and Works', 'Human Rights', 'Industries and Production',
                 'Information and Broadcasting', 'Information Technology and Telecommunication', 'Inter-Provincial Coordination',
                 'Interior', 'Kashmir Affairs and Gilgit-Baltistan', 'Law and Justice', 'Maritime Affairs', 'Narcotics Control',
                 'National Food Security and Research', 'National Health Services, Regulations and Coordination',
                 'Overseas Pakistanis and Human Resource Development', 'Parliamentary Affairs',
                 'Planning, Development and Special Initiatives', 'Poverty Alleviation and Social Safety Division', 'Power',
                 'Privatization', 'Railways', 'Religious Affairs and Inter-faith Harmony', 'Science and Technology',
                 'States and Frontier Regions', 'Water Resources']

    combined_dataFrame = {}

    for i in range(len(URL_LIST)):
        extraction(URL_LIST[i], NAME_LIST[i], combined_dataFrame)

    # refined_dataframe = {}
    # counter = 1
    # for i in combined_dataFrame:
    #     refined_dataframe[str(counter)] = [i, combined_dataFrame[i]]
    #     counter += 1
    # get_edgeList(refined_dataframe)


if __name__ == '__main__':
    main()
