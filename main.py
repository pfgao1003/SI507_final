import util
import BST
import data_access
import visualization
import read_tree

def main():
    univ_tree = read_tree.read_tree('univ_tree.json')
    print ('-------------------------Welcome--------------------------')
    print('This system can show information of top 300 universities.')
    while True:
        print('Please enter the rank(or rank range) of universities you want to search.')
        print('(If you want to see the universities which ranking between 40 and 60, please enter: 41 60.')
        ans = input()
        nums = ans.split(' ')
        if len(nums) == 1:
            univ = univ_tree.find(int(nums[0]))
            print ("The university is " + univ['name'])
        else:
            univs = []
            for i in range(int(nums[0]),int(nums[1])+1):
                univs.append(univ_tree.find(i))
            print('Here are universities in this range, choose one to look at.')
            for i in range(len(univs)):
                print(int(nums[0]) + i, univs[i]['name'])
            print('Please enter a number.')
            num = input()
            univ = univ_tree.find(int(num))
        print('Please choose a format of information.')
        print('1. text')
        print('2. plot')
        option = input()
        print("Please wait...")
        if option == '1':
            visualization.table_show(univ)
        else:
            visualization.show1(univ)
        print('The information has been shown in website.')
        print('Do you want to select another university?(yes/no)')
        ans = input()
        if ans == 'no':
            print('bye!')
            return
if __name__ == '__main__':
    main()
