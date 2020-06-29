from math import log
import re
from datetime import date,time,datetime,timedelta
from operator import itemgetter
import sys
import glob

# =============================================================================
# x=1
# y=2
# z=3
# string1="this is a"
# string2="string"
# new_string=string1+string2
# =============================================================================

# =============================================================================
# print('ouput #1: {0},{1},{2}'.format(x,y,z))
# print("ouput #2: {0:s}".format('I\'m enjoying learning python.'))
# print("ouput #2: {0:s}".format("I'm enjoying learning\
#                                fdbhfsbjfdjsfpython\
#                                    njkjkjjjjknsnfdsnfjnsdjfnsd."))
# print("ouput #3: {0:s}".format('''I'm enjoying learning\
#                                fdbhfsbjfdjsfpython\
#                                    njkjkjjjjknsnfdsnfjnsdjfnsd.'''))   
# print("output #4:{0:.3f}".format(log(4)))                                   
# print("output #5:{0:s},{1:s}".format("she is","good girl"))
# =============================================================================
# =============================================================================
# string3="my delverable is due in may"
# string_list1=string3.split(" ",2)
# print("output #6: first piece {0}, second piece {1} third piece {2}"\
#       .format(string_list1[0], string_list1[1],string_list1[2]))
#     
# =============================================================================
# =============================================================================
# string4="my,delverable,is,due,in,may"
# string_list2=string4.split(',')
# print("output #7: {0},{1},{2}".format(string_list2[0],string_list2[5], string_list2[-1]))
# =============================================================================
# =============================================================================
# 
# string="The quick brown fox jumps over the lazy dog."
# string_list=string.split(" ")
# # =============================================================================
# # pattern=re.compile(r"The", re.I)
# # count=0
# # for word in string_list:
# #     if pattern.search(word):
# #         count+=1
# # print("output #8:{0:d}".format(count))
# # =============================================================================
# 
# pattern=re.compile(r"(?P<match_word>The)",re.I)
# print("output #9: ")
# 
# for word in string_list:
#     if pattern.search(word):
#         print("{0:s}".format(pattern.search(word).group("match_word")))
#         
# print("{0:s}".format(pattern.sub("a",string)))
# =============================================================================

#-----------------------------------------------------------------------------

# =============================================================================
# today=date.today()
# one_day=timedelta(days=-1)
# yesterday=today+one_day
# print("output #10: {0!s} ".format(yesterday))
# eight_hours=timedelta(hours=-8)
# print("output #11: {0!s},{1!s} ".format(eight_hours.days,eight_hours.seconds))
# 
# date_diff=today-yesterday
# print("output #12: {0!s} ".format(date_diff))
# print("output #13: {0!s} ".format(str(date_diff).split()[0]))
# 
# #----------------------------------------------------------------------------
# date1=today.strftime('%m-%d-%Y')
# print("output #14:{!s}".format(datetime.strptime(date1,'%m-%d-%Y')))
# 
# print("output #15:{!s}".format(datetime.date(datetime.strptime(date1,'%m-%d-%Y'))))
# #-----------------------------------------------------------------------------
# unordered_list=[4,8,9,11,0,1,2]
# list_copy=unordered_list[:]
# list_copy.sort()
# print("output #16:{}".format(list_copy))
# list_copy.reverse()
# print("output #16:{}".format(list_copy))
# 
# 
# my_lists=[[1,4,3,5],[4,7,5,8],[9,4,3,2]]
# my_lists_index_3=sorted(my_lists, key=lambda index_value:index_value[3])
# print(my_lists_index_3)
# my_lists_copy=my_lists[:]
# my_lists_index_3and0=sorted(my_lists_copy,key=itemgetter(3,0) )
# print(my_lists_copy)
# #----------------------------------------------------------------------------
# 
# a_dict={'four':4,'two':2,'three':3}
# order_dict1=sorted(a_dict.items(), key=lambda item:item[0], reverse=False)
# print("output #17(order by values by asc):{}".format(order_dict1))
# =============================================================================

# =============================================================================
# 
# def getMean(numericValues):
#     return sum(numericValues)/len(numericValues)
# mylist=[]
# 
# try:
#     result=getMean(mylist)
#    
# except ZeroDivisionError as detail:
#     print(("Output #19: {}".format(float('nan'))))
#     print(("Output #20: {}".format(detail)))
# else: 
#     print("Output #18: {}".format(getMean(mylist)))
# finally:
#     print("the finally block is executed every time")
# =============================================================================
   
# =============================================================================
# input_file=sys.argv[1]#在命令行输入文件名， [0]为本运行文件，1为读取文件
# print("output #21:")
# file_reader=open(input_file,'r')
# for rows in file_reader:
#     print (rows.strip())
# file_reader.close()
#     
# 
# input_file=sys.argv[1]#在命令行输入文件名， [0]为本运行文件，1为读取文件
# print("output #22:")
# with open(input_file,'r',newline='') as filereader:
#     for rows in filereader:
#         print("{}".format(rows.strip()))
# =============================================================================
    
# =============================================================================
# my_letters=['a','b','c','d','e','f','g','h','i','j']
# max_index=len(my_letters)
# outputfile=sys.argv[1]
# 
# try:
#     file_writer=open(outputfile,'w')
#     for index_value in range(max_index):
#         if index_value<(max_index-1):
#             file_writer.write(my_letters[index_value]+'\t')
#         else:
#             file_writer.write(my_letters[index_value]+'\n')
#     file_writer.close()
#     print("output written to the file")
# except SyntaxError as detail:
#     print("output #23: ", detail)
# =============================================================================

# =============================================================================
# input_file=sys.argv[1]#在命令行输入文件名， [0]为本运行文件，1为读取文件
# print("output #24:")
# with open(input_file,'r',newline='') as filereader:
#     for rows in filereader:
#         print("{}".format(rows.strip()))
# =============================================================================
# =============================================================================
# my_letters=[1,2,3,4,5,6,7]
# max_index=len(my_letters)
# inputfile=sys.argv[1]
# write_to_file=open(inputfile,'a')
# for index_value in range(max_index):
#     if index_value<(max_index-1):
#         write_to_file.write(str(my_letters[index_value])+',')
#     else:
#         write_to_file.write(str(my_letters[index_value])+'\n')
# write_to_file.close()
# 
# =============================================================================

#practice

# (1)=============================================================================
# list1=['hi','my','name']
# list2=['is','hcy','and','I']
# list3=['11,5,9,3','love','music']
# 
# list_add=list1+list2+list3
# 
# for index in range(len(list_add)):
#     print("output #25:{0:d},{1:s} ".format(index, list_add[index]))
#     
# =============================================================================
    
# (2)=============================================================================
# list4=['cat','dog','pig','rat','horse','person','crocodile']
# list5=['1','2','3','4','5','6','7']
# dict_1={}
# max_index=len(list5)
# 
# for index in range(max_index):
#     if list5[index] not in dict_1.keys():
#         dict_1[list5[index]]=list4[index]
# for a,b in dict_1.items():
#     print("output #26:{0:s},{1:s} ".format(a,b))
# =============================================================================
    
# =============================================================================
# list6=['142,332','234,676','898,333']
# list7=[]
# 
# for letter in range(len(list6)): 
#     list7+=list6[letter].split(",")
# 
# for letter_num in range(len(list7)):
#     if letter_num<(len(list7)-1):
#         print("output #27:{}".format(str(list7[letter_num])+','))
#     else:
#         print("output #28:{}".format(str(list7[letter_num])+'\n'))
# =============================================================================

# (3)=============================================================================
# list_of_lists=[['pig','dog','cate'],['bird','rat','giraff'],['snake','tiger','fish']]
# output=''
# for list_outside in list_of_lists:
#     index_list=len(list_outside)
# 
#     for list_inside in range(index_list):
#         if list_inside<(index_list-1):
#             output+=list_outside[list_inside]+','
#         else:
#             output+=list_outside[list_inside]+'\n'
# print(output)
# =============================================================================

# =============================================================================

#读写csv文件
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# 
# with open(input_file,'r',newline='') as filereader:
#     with open(output_file,'w',newline='') as filewriter:
#         header=filereader.readline()
#         header= header.strip()
#         header_list=header.split(',')
#         print(header_list)
#         filewriter.write(','.join(map(str,header_list))+'\n')
#         for rows in filereader:
#             rows=rows.strip()
#             row_list=rows.split(',')
#             print(row_list)
#             filewriter.write(','.join(map(str,row_list))+'\n')
# =============================================================================
# =============================================================================
#     
# import pandas as pd
# input_file=sys.argv[1]
# input_file=sys.argv[2]
# data_frame=pd.read_csv(input_file)
# data_frame.to_csv(input_file,index=False)
# =============================================================================


# 基础python=============================================================================
#行中的值满足某个条件
# =============================================================================
# import csv
# import sys
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#         header=next(filereader)
#         filewriter.writerow(header)
#         for rows in filereader:
#             supplier=str(rows[0]).strip()
#             cost=str(rows[3]).strip('$').replace(',','')
#             if supplier=='Supplizer Z'or float(cost)>600.00:
#                 filewriter.writerow(rows)
# =============================================================================
# pandas用法=============================================================================
# import pandas as pd
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# data_frame=pd.read_csv(input_file)
# data_frame['Cost']=data_frame['Cost'].str.strip('$').astype(float)
# data_frame_values_meet=data_frame.loc[(data_frame['Supplier Name']\
#                                       .str.contains('Z'))|(data_frame['Cost'])>600.00, :]
# data_frame_values_meet.to_csv(output_file,index=False)
# =============================================================================

# =============================================================================
# 行中的值属于某个集合

#基础python
# import csv
# import sys
# input_file=sys.argv[1]
# output_file=sys.argv[2]

# important_dates=['1/20/2014','1/30/2014']
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#         header=next(filereader)
#         filewriter.writerow(header)
#         for rows in filereader:
#             a_date=rows[4]
#             if a_date in important_dates:
#                 filewriter.writerow(rows)
#                 
# # pandas
# import pandas as pd
# import sys

# input_file=sys.argv[1]
# output_file=sys.argv[2]
# important_dates=['1/20/2014','1/30/2014']
# data_frame=pd.read_csv(input_file)
# 
# data_frame_set_in_value=data_frame.loc[data_frame['Purchase Date'].isin(important_dates),:]
# data_frame_set_in_value.to_csv(output_file,index=False)                                       
# =============================================================================
         

# 行中的值匹配于某个模式/正则表达式
# 基础python=============================================================================
# import sys
# import csv
# import re
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# pattern=re.compile(r'(?p<my_pattern_group>^001-.*)',re.I)
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#         header=next(filereader)
#         filewriter.writerow(header)
#         for rows in filereader:
#             invoice_number=rows[1]
#             if pattern.search(invoice_number):
#                 filewriter.writerow(rows)
# ==========================================================================

# # pandas语法
# import pandas as pd
# import sys
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# data_frame=pd.read_csv(input_file)
# 
# data_frame_set_in_value=data_frame.loc[data_frame['Invoice Number'].str.startswith('001-'),:]
# data_frame_set_in_value.to_csv(output_file,index=False)   
# =============================================================================

# =============================================================================
# 列索引值， 选取特定的值


# #基础python=============================================================================
# 
# import sys
# import csv
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# my_columns=[0,3]
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#         for rows in filereader:
#             row_out_file=[]
#             for index_rows in my_columns:
#                 row_out_file.append(rows[index_rows])
#             filewriter.writerow(row_out_file)

# pandas=============================================================================
# import pandas as pd
# import sys
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# data_frame=pd.read_csv(input_file)
# data_frame_coloumn_by_index=data_frame.iloc[:,[0,3]]
# data_frame_coloumn_by_index.to_csv(output_file,index=False)
# =============================================================================

#列标题（想保留的标题很容易识别，而处理多个输入文件时，输入文件中的位置（索引）会发生改变，但标题不变。
# =============================================================================
# 基础python
# import sys
# import csv
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# my_columns=['Invoice Number','Purchase Date']
# my_columns_index=[]
# 
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#         header=next(filereader,None)
#         #print(len(header))
#         for header_lists_index in range(len(header)):
#             if header[header_lists_index] in my_columns:
#                 my_columns_index.append(header_lists_index)
#         filewriter.writerow(my_columns)
#         for rows in filereader:
#             row_list_output=[]
#             for row_index in my_columns_index:
#                 row_list_output.append(rows[row_index])
#         filewriter.writerow(row_list_output)
# =============================================================================

# pandas
# =============================================================================
# import pandas as pd
# import sys
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# data_frame=pd.read_csv(input_file)
# data_frame_coloumn_by_index=data_frame.loc[:,['Invoice Number','Purchase Date']]
# data_frame_coloumn_by_index.to_csv(output_file,index=False)
# =============================================================================

#选取连续的行（输入文件中包含了不需要的头部和尾部信息，修改python脚本，使他不读取这些行）


# #基础python=============================================================================
# =============================================================================
# import sys
# import csv
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# row_counter=0
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#        
#         for rows in filereader:
#             if row_counter>=2 and row_counter<=14:
#                 filewriter.writerow([values.strip() for values in rows])
#             row_counter+=1
# 
# =============================================================================


# pandas
# =============================================================================
# import pandas as pd
# import sys
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# data_frame=pd.read_csv(input_file, header=None)
# data_frame =data_frame.drop([0,1,15,16])
# data_frame.columns=data_frame.iloc[0]
# print(data_frame.columns)
# data_frame=data_frame.reindex(data_frame.index.drop(2))
# data_frame.to_csv(output_file,index=False)
# =============================================================================

# 添加标题行
# 基础python====================================================================
# import sys
# import csv
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# with open(input_file,'r',newline='') as csv_in_file:
#     with open(output_file,'w',newline='') as csv_out_file:
#         filereader=csv.reader(csv_in_file, delimiter=',')
#         filewriter=csv.writer(csv_out_file, delimiter=',')
#         header_list=['Supplier Name','Invoive Number','Part Number','Cost','Purchase Date']
#         filewriter.writerow(header_list)
#         for rows in filereader:
#             filewriter.writerow(rows)
# =============================================================================
            

# =============================================================================
# #pandas
# import pandas as pd
# import sys
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# header_list=['Supplier Name','Invoive Number','Part Number','Cost','Purchase Date']
# data_frame=pd.read_csv(input_file, header=None,names=header_list)
# data_frame.to_csv(output_file,index=False)
# =============================================================================


#文件计数与文件中的行列计数
# =============================================================================
# import sys
# import os
# import csv
# import glob
# 
# input_file=sys.argv[1]
# file_counter=0
# for input_file in glob.glob(os.path.join(input_file, 'sales_*')):
#     row_counter=1
#     with open(input_file,'r',newline='') as csv_in_file:
#         filereader=csv.reader(csv_in_file)
#         header=next(filereader)
#         for rows in filereader:
#             #print(rows)
#             row_counter+=1
#         print('{0:s},\t {1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter,len(header)))
#     file_counter+=1
# print('Number of files: {0:d} files'.format(file_counter))
# =============================================================================
            
#将多个文件中数据连接集中在同一个文件中
# =============================================================================
# 基础python
# import sys
# import csv
# import os
# import glob
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# first_file=True
# for input_file in glob.glob(os.path.join(input_file,'sales_*')):
#     print(os.path.basename(input_file))
#     with open(input_file,'r',newline='') as csv_in_file:
#         with open(output_file,'a',newline='') as csv_out_file:
#             filereader=csv.reader(csv_in_file, delimiter=',')
#             filewriter=csv.writer(csv_out_file, delimiter=',')
#             if first_file:
#                 for rows in filereader:
#                     filewriter.writerow(rows)
#                 first_file=False
#             else:
#                 header=next(filereader,None)
#                 for rows in filereader:
#                     filewriter.writerow(rows)
# =============================================================================

 
# =============================================================================
# pandas语法
# import pandas as pd
# import glob
# import sys
# import os
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# all_files=glob.glob(os.path.join(input_file,'sales_*'))
# all_data_frames=[]
# for file in all_files:
#     data_frame=pd.read_csv(file,index_col=None)
#     all_data_frames.append(data_frame)
# data_frame_concat=pd.concat(all_data_frames,axis=0,ignore_index=True)
# data_frame_concat.sort_values('Invoice Number',inplace=True)
# data_frame_concat.to_csv(output_file,index=False)
# =============================================================================


#计算每个文件中值的总和和均值
# 基础python=============================================================================
# import sys
# import os
# import csv
# import glob
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# header_list=["file_name","total_sales","average_sales"]
# csv_out_file=open(output_file,'w',newline='')
# file_writer=csv.writer(csv_out_file)
# file_writer.writerow(header_list)
# for files in glob.glob(os.path.join(input_file,'sales_*')):
#     with open(files,'r',newline='') as csv_in_file:
#         filereader=csv.reader(csv_in_file)
#         output_list=[]
#         output_list.append(os.path.basename(files))
#         total_sales=0
#         number_sales=0
#         average_sales=0
#         header=next(filereader)
#         for row in filereader:
#             sale_number=row[3]
#             total_sales+=float(str(sale_number.strip('$').replace(',','')))
#             number_sales+=1
#         average_sales='{0:.2f}'.format(total_sales/number_sales)
#         output_list.append(total_sales)
#         output_list.append(average_sales)
#         file_writer.writerow(output_list)

# csv_out_file.close()
# =============================================================================


# pandas语法
# =============================================================================
# import pandas as pd
# import sys
# import  os
# import csv
# import glob
# 
# input_file=sys.argv[1]
# output_file=sys.argv[2]
# all_files=glob.glob(os.path.join(input_file, 'sales_*'))
# all_data_frame=[]
# 
# for files in all_files:
#     data_frame=pd.read_csv(files)
#     total_cost=pd.DataFrame( [float(str(value).strip('$').replace(',', '')) \
#                                    for value in data_frame.loc[0:,'Sale Amount']]).sum()
#         
#     average_cost=pd.DataFrame( [float(str(value).strip('$').replace(',', '')) \
#                                    for value in data_frame.loc[0:,'Sale Amount']]).mean()
#         
#     data={'file name': os.path.basename(files),
#           'total cost':total_cost.map(lambda x:('%.2f')%x),
#           'average_cost': average_cost.map(lambda x:('%.2f')%x)} ##map精确保留2位数，而round是四舍五入保留2位小数，输出结果不一定是两位小数（如果小数点为0的话） 
#     
#     all_data_frame.append(pd.DataFrame(data,columns=['file name','total cost','average_cost']))
# 
# data_frame_concat=pd.concat(all_data_frame,axis=0,ignore_index=True)
# data_frame_concat.to_csv(output_file,index=False)
# =============================================================================
