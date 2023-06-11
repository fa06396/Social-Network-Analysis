# Social Network Analysis - Pakistani National Assembly (2018)

This folder contains the data and scripts related to the social network analysis of the Pakistani National Assembly for the year 2018. The project focuses on extracting data from the Pakistani National Assembly website, manipulating the data, and constructing a social network graph based on the standing committees.

## Folder Structure

- [project_extraction_2.py]: This script was used for data extraction from the Pakistani National Assembly website for the year 2018.
- [combined.py]: This script was used for manipulating the extracted data.
- [individual_csvs]: Individual CSV files for each standing committee, containing the relevant data for the members.
- [combined.csv]: This file is a combined CSV that includes all the extracted data from the standing committees for the year 2018.
- [name_list]: This file contains the names of each member, where each line corresponds to a specific index used for network graph formation.
- [party_list]: This file contains the political party to which each member belongs, where each line corresponds to a specific index used for network graph formation.
- [edge_list]: This file contains the connections between different indices, indicating which index is connected to which index in the network graph.

## Usage

1. Explore the [project_extraction_2.py] to access the script used for data extraction from the Pakistani National Assembly website for the year 2018.
2. Explore the [combined.py] directory to access the script used for manipulating the extracted data.
3. Refer to the [individual_csvs] to access individual CSV files for each standing committee, containing the relevant data for the members.
4. The [combined.csv] file provides a consolidated view of all the extracted data from the standing committees for the year 2018.
5. The [name_list] file contains the names of each member, and the [party_list] file contains the political party to which each member belongs.
6. The [edge_list] file specifies the connections between different indices, facilitating the formation of the network graph.

Please note that the analysis and graph formation were done using R Studio, but unfortunately, the scripts are no longer available.
