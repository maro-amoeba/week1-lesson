"""
以下のように出力させるプログラムを作成してください。
また、次の日の授業は前日の最後の次の授業から始まることに注意してください。

期待する結果
_________________
月曜日は、3時間勉強する予定です。
1限目 数学
2限目 機械学習
3限目 深層学習
~~省略~~
木曜日は、お休みです。
~~
日曜日は、2時間勉強する予定です。
1限目 エンジニアプロジェクト
2限目 Python
~~
_________________
"""

WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']
save_subject_list = 1

def output_schedule(study_time_list):
    '''今週の勉強予定を出力します'''
    global save_subject_list #無いとprint後?ローカル変数と判定されてしまう
    for day, study_time in zip(WEEK_LIST, study_time_list):
        if study_time == 0:
            print("{}曜日は、お休みです。".format(day))
        else:
            print("{}曜日は、{}時間勉強する予定です。".format(day, study_time))
        for time_count in range(study_time):
            print("{}限目 {}".format(time_count+1, SUBJECT_LIST[save_subject_list]))
            save_subject_list += 1
            if save_subject_list == 5:
                save_subject_list = 0


def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    output_schedule(study_time_list)


if __name__ == '__main__':
    main()

"""
[my メモ]
WEEK_LISTを順に取得 @1
study_study_time_listを順に取得 @1に連動　_もし値が0ならholidayにする。
取得した回数分だけSUBJECT_LISTを順に取得する
＿なぜか数学から順にスタートして最後までいったら頭に戻る
次の日の授業は前日の最後の次の授業から始まる
"""
