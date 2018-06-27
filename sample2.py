def show_staffs(names = None):
    if type(names) == list:
        for name in names:
            print("今日出勤する人は、{}さんです。".format(name))
    elif type(names) == str:
        print("今日出勤する人は、{}さんです。".format(names))
    else:
        print("今日出勤する人はいません。")
show_staffs()
show_staffs('一郎')
workers = ["一郎", "次郎", "三郎"]
show_staffs(workers)
