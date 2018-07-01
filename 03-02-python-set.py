"""
@受講生がどのコースに在籍しているかを出力する。

期待する結果
______________________________
探したい人: {'Aさん', 'Cさん'}
AIコースに{'Aさん', 'Cさん'}は在籍しています。
Railsコースに{'Cさん'}のみ在籍しています。
Railsチュートリアルコースに{'Aさん', 'Cさん'}は在籍していません。
JSに{'Aさん'}のみ在籍しています。
______________________________
"""

course_dict = {
    'AIコース': {'Aさん', 'Cさん', 'Dさん'},
    'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
    'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
}


def find_person(want_to_find_person):
    for key in course_dict:
        if len(course_dict[key] & want_to_find_person) == 0:
            print("{0}に{1}は在籍していません。".format(key, want_to_find_person))
        elif len(course_dict[key] & want_to_find_person) == 1:
            print("{0}に{1}のみ在籍しています。".format(key, want_to_find_person))
        else:
            print("{0}に{1}は在籍しています。".format(key, want_to_find_person))

def main():
    want_to_find_person = {'Cさん', 'Aさん'}
    print('探したい人: {}'.format(want_to_find_person))
    find_person(want_to_find_person)


if __name__ == '__main__':
    main()
