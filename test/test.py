from datetime import datetime
import generator
import alg

def ttest(funcName,Name):
    base, groundtruth = generator.make_data(15)  # 括号内输入需要生成的数据范围
    print("原始数据:", base)
    print("正确排序:", groundtruth, "\n")

    # 代码调用
    begin_time = datetime.now()
    base=funcName(base)  # 排序算法调用
    end_time = datetime.now()
    if base == groundtruth:
        print("排序正确")
        print("算法运行时间:", run_time, "\n")  # 由于时间精度，算法运行时间可能为零
        print("{}排序结果:".format(Name), base)
    else:
        print("排序错误")

    run_time = end_time - begin_time  # 由于时间精度，算法运行时间可能为零

    # 结果输出
    print("-------------------------------")

# ttest(alg.InsertSort,"插入")
# ttest(alg.bubbleSort,"冒泡")
ttest(alg.quick_sort,"快速")




# #在这下面测试quick_sort
#
# base, groundtruth = generator.make_data(15)  # 括号内输入需要生成的数据范围
# print("原始数据:", base)
# print("正确排序:", groundtruth, "\n")
#
# begin_time = datetime.now()
# alg.quick_sort(base,base[0],base[-1])  # 排序算法调用
# end_time = datetime.now()
# run_time = end_time - begin_time  # 由于时间精度，算法运行时间可能为零
#
# # 结果输出
# if base == groundtruth:
#     print("排序正确")
#     print("算法运行时间:", run_time, "\n")  # 由于时间精度，算法运行时间可能为零
#     print("快速排序结果:", base)
# else:
#     print("排序错误")
# print("-------------------------------")