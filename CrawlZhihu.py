import requests
import json
import time
import re
import os
import pandas as pd
from openpyxl import load_workbook


def get_data(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：
        url ：目标网页的 url
    返回：目标网页的 html 内容
    '''
    headers = {
        'Referer': url,
        'content-type': 'application/json',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text

    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")


def parse_data(html):
    '''
    功能：提取 html 页面信息中的关键信息，并整合一个数组并返回
    参数：html 根据 url 获取到的网页内容
    返回：存储有 html 中提取出的关键信息的数组
    '''
    pattern = re.compile(r'<[^>]*>')  # 爬虫规则1
    pattern2 = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')  # 爬虫规则2
    json_data = json.loads(html)['data']

    try:
        dic = {'Name': [], 'Gender': [], 'AuthorURL': [], 'VoteupCount': [], 'CommentCount': [], 'Content': [],
               'URL': []}
        name_list = []
        gender_list = []
        author_url_list = []
        vote_list = []
        comment_count_list = []
        content_list = []
        url_list = []
        for item in json_data:
            content = re.sub(pattern, '', item['content']).replace('&#34;', '"')  # 正则匹配去重 回答内容
            name_list.append(item['author']['name'])
            gender_list.append(item['author']['gender'])
            author_url_list.append(item['author']['url'])
            vote_list.append(item['voteup_count'])
            comment_count_list.append(item['comment_count'])
            content_list.append(content)
            url_list.append(item['url'])
        dic['Name'] = name_list
        dic['Gender'] = gender_list
        dic['AuthorURL'] = author_url_list
        dic['VoteupCount'] = vote_list
        dic['CommentCount'] = comment_count_list
        dic['Content'] = content_list
        dic['URL'] = url_list
        return dic
    except Exception as e:
        print(dic)
        print(e)


def save_data(dic):
    '''
    功能：将comments中的信息输出到文件中/或数据库中。
    参数：comments 将要保存的数据
    '''
    try:
        filename = './albertZhihuMessage/comments.xlsx'
        if os.path.exists(filename):
            old_dataframe = pd.DataFrame(pd.read_excel(filename, sheet_name=0))  # 读取原数据文件和表
            new_dataframe = pd.DataFrame(dic)
            df_new = old_dataframe.append(new_dataframe, ignore_index=True)
            df_new.to_excel(filename, sheet_name='Sheet0', index=False, engine='openpyxl')
        else:
            dataframe = pd.DataFrame(dic)
            dataframe.to_excel(filename)
    except Exception as e:
        print(e)


# dataframe.to_csv(filename, mode='a', index=False, sep=',', header=False)
# dataframe.to_csv(filename, mode='a', index=False, sep=',',
# header=['name', 'gender', 'url', 'voteup_count', 'comment_count', 'content', 'url'])


def main():
    questionId = '361111920'
    url = f'https://www.zhihu.com/api/v4/questions/{questionId}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=5&platform=desktop&sort_by=default'

    # get total cmts number
    html = get_data(url)
    totals = json.loads(html)['paging']['totals']

    print(totals)
    print('---' * 10)

    page = 0

    while (page < totals):
        url = f'https://www.zhihu.com/api/v4/questions/{questionId}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=' + str(
            page) + '&platform=desktop&sort_by=default'

        html = get_data(url)
        dic = parse_data(html)
        print(dic)
        save_data(dic)

        print(page)
        page += 5
        time.sleep(1)


if __name__ == '__main__':
    main()
    print("完成！！")
