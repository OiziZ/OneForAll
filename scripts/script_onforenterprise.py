import os
import urllib.request
import urllib.parse
import re

def get_file_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error from this URL {url}: {e}")
        return None

def write_to_output_file(content):
    with open('../oneforenterprise.txt', 'a') as file:
        file.write(content + '\n')

def clean_line(line):
    regex = r"([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)|((?:[0-9]{1,3}\.){3}[0-9]{1,3})|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
    matches = re.findall(regex, line)
    if matches:
        return matches[0][0] or matches[0][1] or matches[0][2]
    return None

links = [
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_21.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_53.txt"
]

for link in links:
    content = get_file_content(link)
    if content is not None:
        lines = content.split('\n')
        for line in lines:
            if not line.strip().startswith('#'):
                clean_line_result = clean_line(line)
                if clean_line_result:
                    write_to_output_file(clean_line_result)

print("Files oneforenterprise.txt ok")