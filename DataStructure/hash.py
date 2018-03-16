#coding=utf-8

class MyHash(object):
    '''
    哈希表设计
    '''

    def __init__(self,length=10):
        self.length = length
        self.slots = [[] for i in range(self.length)]
        self.datasize = 0

    def hash(self,k):
        return k % self.length

    def add(self,k,v):
        '''
        添加(k,v)
        '''
        if self.datasize >= len(self.slots):
            self.resize()
        index = self.hash(k)
        if self.slots[index] != []:
            # 先判断是否有内容在里面
            # 在判断是否有key重复
            for item in self.slots[index]:
                if k == item[0]:
                    self.slots[index].remove(item)

        #然后加入
        self.slots[index].append((k,v))
        self.datasize += 1

    def get(self,k):
        '''
        查找
        '''
        index = self.hash(k)
        if self.slots[index] != []:
            for item in self.slots[index]:
                if k == item[0]:
                    return item[1]

        raise KeyError

    def resize(self):
        '''
        当元素过多时，需要将slots的数量增加
        '''
        self.length *= 2
        new_slots = [[] for i in range(self.length)]
        for slot in self.slots:
            for item in slot:
                # print item
                index = self.hash(item[0])
                new_slots[index].append(item)
        self.slots = new_slots

    def __len__(self):
        return len(self.slots)


    def __str__(self):
        '''
        当采用print方法时，可以输出想要的内容
        '''
        return str(self.slots)

if __name__ == '__main__':
    h = MyHash()
    for i in range(23):
        h.add(i,i+1)

    print h.get(1)
    print h
    print len(h)
    print h.datasize