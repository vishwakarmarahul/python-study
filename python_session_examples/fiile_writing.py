

file_o = open('d:/temp/sample.txt', 'w', encoding='utf-8')
'''
write('big string... any string \n... \n..')
writeLines
'''

file_o.write('A')
file_o.write('B')
file_o.writelines(['A','B'])
file_o.close()

