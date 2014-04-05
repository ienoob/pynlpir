# -*- coding: utf-8 -*-
"""A part of speech map for NLPIR/ICTCLAS."""

from __future__ import unicode_literals


POS_MAP = {
    'n': ('名词', 'noun', {
        'nr': ('人名', 'personal name', {
            'nr1': ('汉语姓氏', 'Chinese surname'),
            'nr2': ('汉语名字', 'Chinese given name'),
            'nrj': ('日语人名', 'Japanese personal name'),
            'nrf': ('音译人名', 'transcribed personal name')
        }),
        'ns': ('地名', 'toponym', {
            'nsf': ('音译地名', 'transcribed toponym'),
        }),
        'nt': ('机构团体名', 'organization/group name'),
        'nz': ('其它专名', 'other proper noun'),
        'nl': ('名词性惯用语', 'noun phrase'),
        'ng': ('名词性语素', 'noun morpheme'),
    }),
    't': ('时间词', 'time word', {
        'tg': ('时间词性语素', 'time morpheme'),
    }),
    's': ('处所词', 'locative word'),
    'f': ('方位词', 'noun of locality'),
    'v': ('动词', 'verb', {
        'vd': ('副动词', 'auxiliary verb'),
        'vn': ('名动词', 'nounal verb'),
        'vshi': ('动词"是"', 'verb 是'),
        'vyou': ('动词"有"', 'verb 有'),
        'vf': ('趋向动词', 'directional verb'),
        'vx': ('行事动词', 'performative verb'),
        'vi': ('不及物动词', 'intransitive verb'),
        'vl': ('动词性惯用语', 'verb phrase'),
        'vg': ('动词性语素', 'verb morpheme'),
    }),
    'a': ('形容词', 'adjective', {
        'ad': ('副形词', 'auxiliary adjective'),
        'an': ('名形词', 'nounal adjective'),
        'ag': ('形容词性语素', 'adjective morpheme'),
        'al': ('形容词性惯用语', 'adjective phrase'),
    }),
    'b': ('区别词', 'distinguishing word', {
        'bl': ('区别词性惯用语', 'distinguishing phrase'),
    }),
    'z': ('状态词', 'status word'),
    'r': ('代词', 'pronoun', {
        'rr': ('人称代词', 'personal pronoun'),
        'rz': ('指示代词', 'demonstrative pronoun', {
            'rzt': ('时间指示代词', 'temporal demonstrative pronoun'),
            'rzs': ('处所指示代词', 'locative demonstrative pronoun'),
            'rzv': ('谓词性指示代词', 'predicate demonstrative pronoun'),
        }),
        'ry': ('疑问代词', 'interrogative pronoun', {
            'ryt': ('时间疑问代词', 'temporal interrogative pronoun'),
            'rys': ('处所疑问代词', 'locative interrogative pronoun'),
            'ryv': ('谓词性疑问代词', 'predicate interrogative pronoun'),
        }),
        'rg': ('代词性语素', 'pronoun morpheme'),
    }),
    'm': ('数词', 'numeral', {
        'mq': ('数量词', 'numeral-plus-classifier compound'),
    }),
    'q': ('量词', 'classifier', {
        'qv': ('动量词', 'verbal classifier'),
        'qt': ('时量词', 'temporal classifier'),
    }),
    'd': ('副词', 'adverb'),
    'p': ('介词', 'preposition', {
        'pba': ('介词“把”', 'preposition 把'),
        'pbei': ('介词“被”', 'preposition 被'),
    }),
    'c': ('连词', 'conjunction', {
        'cc': ('并列连词', 'coordinating conjunction'),
    }),
    'u': ('助词', 'particle', {
        'uzhe': ('着', '着'),
        'ule': ('了／喽', '了/喽'),
        'uguo': ('过', '过'),
        'ude1': ('的／底', '的/底'),
        'ude2': ('地', '地'),
        'ude3': ('得', '得'),
        'usuo': ('所', '所'),
        'udeng': ('等／等等／云云', '等/等等/云云'),
        'uyy': ('一样／一般／似的／般', '一样/一般/似的/般'),
        'udh': ('的话', '的话'),
        'uls': ('来讲／来说／而言／说来', '来讲/来说/而言/说来'),
        'uzhi': ('之', '之'),
        'ulian': ('连', '连'),
    }),
    'e': ('叹词', 'interjection'),
    'y': ('语气词', 'modal particle'),
    'o': ('拟声词', 'onomatopoeia'),
    'h': ('前缀', 'prefix'),
    'k': ('后缀' 'suffix'),
    'x': ('字符串', 'string', {
        'xe': ('Email字符串', 'email address'),
        'xs': ('微博会话分隔符', 'hashtag'),
        'xm': ('表情符合', 'emoticon'),
        'xu': ('网址URL', 'URL'),
    }),
    'w': ('标点符号', 'punctuation mark', {
        'wkz': ('左括号', 'left parenthesis/bracket'),
        'wky': ('右括号', 'right parenthesis/bracket'),
        'wyz': ('左引号', 'left quotation mark'),
        'wyy': ('右引号', 'right quotation mark'),
        'wj': ('句号', 'period'),
        'ww': ('问号', 'question mark'),
        'wt': ('叹号', 'exclamation mark'),
        'wd': ('逗号', 'comma'),
        'wf': ('分号', 'semicolon'),
        'wn': ('顿号', 'enumeration comma'),
        'wm': ('冒号', 'colon'),
        'ws': ('省略号', 'ellipsis'),
        'wp': ('破折号', 'dash'),
        'wb': ('百分号千分号', 'percent/per mille sign'),
        'wh': ('单位符号', 'unit of measure sign'),
    }),
}


def _get_pos_name(pos_code, parents=False, english=True, pos_map=POS_MAP):
    """Gets the part of speech name for *pos_code*."""
    for i in range(1, len(pos_code) + 1):
        try:
            pos_key = pos_code[0:i]
            pos_entry = pos_map[pos_key]
            break
        except KeyError:
            if i == len(pos_code):
                raise ValueError("part of speech not recognized: '%s'" %
                                 pos_code)
    pos = (pos_entry[1 if english else 0], )
    if len(pos_entry) == 3 and pos_key != pos_code:
        sub_map = pos_entry[2]
        sub_pos = _get_pos_name(pos_code, parents, english, sub_map)
        pos = pos + sub_pos if parents else (sub_pos, )
    return pos if parents else pos[-1]


def get_pos_name(pos_code, parents=False, english=True):
    """Gets the part of speech name for *pos_code*."""
    return _get_pos_name(pos_code, parents, english)
