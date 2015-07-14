def lessThan4(aList):
       '''
    aList: a list of strings
    '''
       join = []
       smaller = 4
       count = 0
       for index in aList:
 ##             print index
              count = len(index)
 ##             print count
              if count < 4:
                     join.append(index)
 ##                    print join

       return join
