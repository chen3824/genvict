# -*- coding: utf-8 -*-
"""判断层落盘前的数据整理：合并索引就位 + 写入 AI 判定的答案形态。"""
import os, json, shutil

WORK = r'E:\genvict\genvict\answers\_work'
HERE = os.path.dirname(os.path.abspath(__file__))

shutil.copyfile(os.path.join(WORK, 'merged_index.json'),
                os.path.join(HERE, 'notes_index.json'))

SHAPE = {
    '1':  '感想/求助 · 无清单',
    '3':  '求助帖 · 答案在评论区',
    '4':  '有文字清单 · 7 家（女装）',
    '5':  '清单在图里 · 正文仅声明',
    '8':  '风险提示 · 无清单',
    '10': '清单在图里 · 销售额榜',
    '11': '内容在图/视频 · 纯标签',
    '12': '单店比价 · 比价图在 p1/p2',
    '16': '清单在图里 · 正文仅感想',
    '18': '清单在图里 · 销售额榜',
    '24': '清单在图里 · 纯标签',
    '25': '有文字清单 · 1 家店名',
}
IN_IMAGE = {'5', '10', '11', '16', '18', '24'}

p = os.path.join(HERE, 'notes_content.json')
con = json.load(open(p, encoding='utf-8'))
for n in con:
    r = str(n['rank'])
    n['answer_shape'] = SHAPE.get(r, '短文')
    if r in IN_IMAGE:
        n['list_in_image'] = True
json.dump(con, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK notes_index.json + %d 篇 answer_shape' % len(con))
