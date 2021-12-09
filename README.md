# SI-507-final-project

SI 507 Final Project README

Pengfei Gao (pfgao,42511748)


# Project Description
This is a program that can show users top universities and information related to
these universities(such as Student/Faculty ratio, Location, Teaching Ranking, and
Research Ranking) according to their demands of world university ranking(or ranking
range).

Data Source:
Round Ranking: https://roundranking.com/ranking/world-university-rankings.html#world-2021

Required Package:

json

plotly

requests

bs4

time

geopy

pandas

webbrowser

datetime

# Instructions

1) Run data_access.py to get the data (This might take up to 15-20 minutes if there is no cache because there are 300 universities.)

2) Run main.py and enjoy! (When the plotly show plots, if the website loads for three seconds or longer, please refresh the page and then plots will be shown immediately!)

# Data Structure
I use a Binary Search Tree to store the information. The key of each node is the world rank of the university, and the value(info) of the node is a dictionary that contains all information of the university.
# How it works

1) The program scrapes top universities data from Round Ranking, caches the html, and stores the useful data into a json file ("CACHE.json").

2) The program will get data from "CACHE.json" and then convert the data to a tree and then store it in "univ_tree.json".

3) When you excute 'main.py', it will read data from 'univ_tree.json'. Then the program will use binary search Tree method to access specific information and use plotly to provide result.

# Program Structure 

1) data_access.py:

    a) request_with_cache(): It makes an online request and will cache anything that returns in every call

        parameters: url
                    cache dictionary
                    optional header
                    optional params
        
        returns: fetched data in whatever format it came in
        
    b) data_access(): The main function in data_access.py. It access data from CACHE.json(or from the website) and then it will convert the data to a tree and then store the tree in "univ_tree.json" file.

        parameter: None
        
        returns: None

2) BST.py:

    a) BSTNode Class: The class of BST Node. The __init__ function initiate the BST Node. The insert function can insert a specific element into a exist BST. The find function can find a specific element into a exist BST and then return it. The preorder_save function will save the tree to list in preorder sequence.

    insert():    
        
        parameter: 
        info: The dictionary contains all information of one university.
        val: The key of the node, which is also the world rank of the university.
        
        returns: nothing
    find():

        parameter:
        val: The key of the node, which is also the world rank of the university.

        returns: The information of the university.
    preorder_save():

        parameter:
        val: The key of the node, which is also the world rank of the university.

        returns: The list that store the tree.
        
3) visualization.py:

    a) table_show(): Show all information of one university in table format.
        
        Parameter: 
        univ: the dictionary of one university

        returns:
        None
    b) pie_show(): Show the Students/Faculty Ratio in pie chart format.
        
        Parameter: 
        univ: the dictionary of one university

        returns:
        tr: the trace of the chart
    c) bar_show(): Show the ranking in bar chart format.
        
        Parameter: 
        univ: the dictionary of one university

        returns:
        tr: the trace of the chart    
    d) map_show(): Show the location in map format.
        
        Parameter: 
        univ: the dictionary of one university

        returns:
        fig3: the figure of the map 
    c) show1(): Put all related figures into a html file and open it.

        Parameter: 
        univ: the dictionary of one university

        returns:
        None

4) univ_tree.py:

    a) save_BST(): Load the information of data, build a tree to store the data and then use a json file to store the tree.
        
        Parameter: 
        ori: the file that contains data

        dest: the file that will store the tree
        returns:
        None
5) read_tree.py:

    a) read_tree(): Read the tree data from a file and return the tree.

        Parameter:
        src: The file that contains the tree.

        returns:
        univ_tree: The tree that contains data.
6) util.py: Contains all pakages import.

7) main.py: Contains the main function which include the procedrue of program and the interaction with users.

# User Interactions

The program will first prompt the user to enter the rank or rank range of universities:
  - If the user input one number, we will ask the user choose text or plot.
  - If the user input two number, we will should the user all universities name in this number range and ask them to choose one university.
    - If the user choose one university, we will ask the user choose text or plot.

After the user choose text or plot:
- If the user choose text, we will build a table contains all information for user.
- If the user choose plot, we will build several plots contains all information for user.(4 kinds of Plots: table, pie chart, bar chart and map)

After that, we will ask the user if they want to search for another university.
- If the user enter 'yes', we let the user input a rank or rank range again.
- If the user enter 'no', the program exit.
