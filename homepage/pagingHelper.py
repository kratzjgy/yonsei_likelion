class pagingHelper:
    def getTotalPageList(self, totalCnt, rowsPerPage):
        if ((totalCnt % rowsPerPage) == 0):
            self.total_pages = totalCnt / rowsPerPage;
            #print 'getTotalPage #1'
        else:
            self.total_pages = (totalCnt / rowsPerPage) + 1;
            #print 'getTotalPage #2'
            
        self.totalPageList = []
        for i in range(self, total_pages):
            self.totalPageList.append(i + 1)
                
        return self.totalPageList{'total_pages' : total_pages}
            
    def __init__(self):
        self.total_pages = 0
        self.totalPageList = 0