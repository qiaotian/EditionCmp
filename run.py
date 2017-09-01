import os
import sys
import re
from sets import Set

def parse_input(filename):
    '''
    DES: Input the file directory and output the resource list,
         whose key is device name, and value is the software list
         installed on this device

    DATA STRUCTURE:
         software_dict --
                        - device 1 : [s1, s2, s3]
                        - device 2 : [s2, s3]
                        - device 3 : [s3, s4, s5]
    '''
    software_dict = {}
    with open(filename) as f:
        isfirstline = True
        for i in f:
            if isfirstline:
                isfirstline = False
                continue
            i = i.strip().lower()
            if i == '':
                continue
            device, software = i.split(',')[0:2]
            #print device, software
            if not software_dict.has_key(device):
                software_dict[device] = []
            software_dict[device].append(software)

    return software_dict


def split_software_string(software_string):
    '''
    DES: Input the softwware string, for example, 'Visual Studio 2015', then
         output the software name, version, and suffix, like 'Visual Studio', '2015' and ''.
         First, this function find the version string with greedy mode, then split software_string
         into three parts according to this version string.

    >> 'Visual Studio 2015'
    'Visual Studio', '2015', ''

    >> 'rabbitmq 2.2.0 ENV'
    'rabbitmq', '2.2.0', 'ENV'
    '''
    #pattern = re.compile(r'((\s|\S)+)(\d+.){1,8}(\d+)(\w*)')
    pattern = re.compile(r'(\d+\.)(\d+\.){0,8}(\d+)')
    match = pattern.search(software_string)

    version = ''
    name = ''
    suffix = ''
    if match:
        name = software_string[ : match.start()].strip() if match.start() > 0 else ''
        version = software_string[match.start() : match.end()].strip()
        suffix = software_string[match.end() : ].strip() if match.end() < len(software_string) else ''

    return name, version, suffix

def generate_expected_data(software_dict):
    '''
    convert software dict to a new one (ans)
    get software list
    '''
    ans = {}
    software_set = Set([])
    for device in software_dict:
        if not ans.has_key(device):
            ans[device] = {}
        for s in software_dict[device]:
            name, version, suffix = split_software_string(s)
            if len(name.strip())==0:
                continue
            software_set.add(name)
            ans[device][name] = {}
            ans[device][name]['version'] = version
            ans[device][name]['suffix'] = suffix

    software_list = []
    for i in software_set:
        i = i.strip()
        if i != '':
            software_list.append(i)
    return software_list, ans

def get_device_list():
    return ['prism-ba01', 'prism-ba02', 'prism-ba03', 'prism-ba04', 'prism-ba05']

def final_process(mdict, slist, dlist):
    '''
    PARAMS:
        slist: software list
        dlist: device list

    RETURN:
    {
        software1 : {
            device1 : {
                version:
                suffix:
            }
            device2 : {
                version:
                suffix
            }
            device3 : None
            device4 : None
            device5 : {
                version:
                suffix
            }
        }
        software2 : {
            device1 : {
                version:
                suffix:
            }
            device2 : {
                version:
                suffix
            }
            device3 : None
            device4 : None
            device5 : {
                version:
                suffix
            }
        }
        ...
    }
    '''

    ### init the ans
    ans = {}
    for s in slist:
        # for every software
        if not ans.has_key(s):
            ans[s] = {}
            for d in dlist:
                ans[s][d] = {}

    ### fill the ans
    for d in dlist:
        for s in slist:
            if mdict[d].has_key(s):
                ans[s][d] = {'has': True, 'version':mdict[d][s]['version'], 'suffix':mdict[d][s]['suffix']}
            else:
                ans[s][d] = {'has': False, 'version':'', 'suffix':''}

    return ans



if __name__ == '__main__':
    filename = './data/Monitoring.csv'
    tmp = parse_input(filename)
    #print software_dict
    #split_software_string('10.0.40219')
    #split_software_string('Microsoft Visual C++ 2012 Redistributable (x64) - 11.0.60610')
    #split_software_string('Dotfuscator and Analytics Community Edition 5.22.0')
    #split_software_string('MSBuild/NuGet Integration 14.0 (x86)')
    #split_software_string('Microsoft SQL Server 2016 T-SQL Language Service ')

    device_list = get_device_list()
    software_list, software_dict = generate_expected_data(tmp)
    ans = final_process(software_dict, software_list, device_list)

    print ans



    #print software_dict
