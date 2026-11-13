# -*- coding: utf-8 -*-
"""合并两轮搜索的索引，按 note_id 去重、按赞数降序，标出来源搜索词。"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
Q1 = '抖音男装 性价比 好店'
Q2 = '抖音靠谱的男装店铺'

a = json.load(open(os.path.join(BASE, 'probe_index.json'), encoding='utf-8'))
b = json.load(open(os.path.join(BASE, 'index2.json'), encoding='utf-8'))
for n in a:
    n['queries'] = [Q1]
for n in b:
    n['queries'] = [Q2]

seen = {}
for n in a + b:
    k = n['note_id']
    if k in seen:
        seen[k]['queries'] = sorted(set(seen[k]['queries'] + n['queries']))
    else:
        seen[k] = n

notes = sorted(seen.values(), key=lambda x: -x['likes'])
for i, n in enumerate(notes, 1):
    n['rank'] = i

out = os.path.join(BASE, 'merged_index.json')
json.dump(notes, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('TOTAL', len(notes), '->', out)
for n in notes:
    print('%2d. %6d  %s | %s | %s' % (
        n['rank'], n['likes'], n['title'][:38], n['author'][:12],
        '+'.join(n['queries'])))
