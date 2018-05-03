

import urllib.request

webpage = urllib.request.urlopen('http://www.baidu.com')
print(webpage.status)
print(webpage.read())

#下载文件到本地 并指定别名
urllib.request.urlretrieve("http://www.baidu.com", 'baidu.html')

#在不指定下载文件别名的情况下，可用于清理文件
# urllib.request.urlcleanup()