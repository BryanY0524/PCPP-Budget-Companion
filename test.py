import budget_Formula
import pcpp_Filter
import pcpp_Scrape

MASTER_LIST = pcpp_Scrape.read_JSON()
testvalues = [['2', 3000, 1, 1, 3, 3], ['2', 3000, 1, 2, 3, 3],
              ['2', 3000, 1, 3, 3, 3], ['2', 3000, 2, 1, 3, 3],
              ['2', 3000, 2, 2, 3, 3], ['2', 3000, 2, 3, 3, 3],
              ['2', 3000, 3, 1, 1, 3], ['2', 3000, 3, 2, 1, 3],
              ['2', 3000, 3, 3, 1, 3]]

for i in range(0, 9):
    for testsubject in testvalues:
        compList = budget_Formula.giveFormula(testsubject[0], testsubject[1])
        pcpp_Filter.grabBuilds(compList, testsubject, MASTER_LIST)
