import jsonpath
import json

page = input('输入想要的页码1~12')
page_list = []
for i in range(13):
    page_list.append(str(i))
if page in page_list:
    result = json.load(open(r'D:\CodeOfPython\Code_python_normal\spider_Code\spider_day3\zhilianzhaopian_json\shanghai_1.json', 'r',encoding='utf-8'))
    jobName_list = jsonpath.jsonpath(result, '$..jobName')
    company_name_list = jsonpath.jsonpath(result, '$..company.name')
    salary_list = jsonpath.jsonpath(result, '$..salary')

    print(jobName_list)  # 爬取到的职位
    print(company_name_list)  # 爬取到的公司
    print(salary_list)  # 爬取到的薪资

else:
    print('输入有误')