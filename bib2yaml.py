# bib2yaml.py
import re

def bib2yaml(dict_of_files):
    list_output = []
    for bib_files, list_of_files in dict_of_files.items():
        for file in list_of_files:
            #print(file)
            with open(file, 'r') as fr:
                list_lines = fr.readlines()

            # go through the lines
            for str_line in list_lines:
                #print(str_line)
                
                # first line with id
                if str_line.startswith('@'):
                    sg_t1 = re.search('^@(.*){(.*),$', str_line)
                    str_id = re.sub(':','',sg_t1.group(2))
                    str_first = '\n-%s: &%s' % (sg_t1.group(1), str_id)
                    list_output.append(str_first)
                    #print(str_first)
            
                # for the other lines
                else:
                    sg_tn = re.search('(.*) = {(.*?)}', str_line)
                    #print(sg_tn)
                    try:
                        str_cat = sg_tn.group(1).lower()
                        str_val = sg_tn.group(2)
                    except AttributeError:
                        #print(str_line)
                        continue
            
                    # make a list of all the authors
                    if str_cat=='author':
                        #print('estou aqui')
                        list_authors = str_val.split(' and ')
                        str_auths = '\n    -'.join(list_authors)
                        str_aut_out = '  %s:\n    -%s' % (str_cat, str_auths)
                        list_output.append(str_aut_out)
            
                    # all the integer values
                    list_ints = ['number','volume','read','year']
                    if str_cat in list_ints:
                        str_jt_out = '  %s: %s' % (str_cat, str_val)
                        list_output.append(str_jt_out)
                        
                    # all the string values
                    else:
                        str_gen_out = '  %s: "%s"' % (str_cat, str_val)
                        list_output.append(str_gen_out)
                        #print(str_gen_out)
        #print(list_output)
        with open('test.yaml','w') as fw:
            fw.write('\n'.join(list_output))
