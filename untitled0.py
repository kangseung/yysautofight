import y_functions2 as yf2
from settings import Settings

y_settings = Settings()
#导入准备模板
t_start, t_beforeend,t_end, t_ready, t_startzudui,n = yf2.begin()
#n为计划刷御魂次数，通过begin函数输入
for k in range(n):

    print('开始刷第{}次御魂'.format(k + 1))

    #检测挑战模板
    print ("start match start")
    # yf2.matchT(t_start, y_settings.start_x, y_settings.start_y)

    yf2.matchT(t_startzudui, y_settings.startzudui_x, y_settings.startzudui_y)
    print ("end match start")
    # print('点击准备')
    # # yf2.matchT(t_ready, y_settings.ready_x, y_settings.ready_y)
    # #等待战斗最后结尾点三下跳过动画
    # yf2.endclick(y_settings)
    # print('结尾点击三次')
    #finish war
    print ("start match before end")
    yf2.matchT(t_beforeend, y_settings.beforeend_x, y_settings.beforeend_y)
    print ("end match before end")
    #检测结束模板
    print ("start match end")
    yf2.matchT(t_end, y_settings.end_x, y_settings.end_y)
    print ("end match before end")
print('一共刷完了{}次御魂'.format(n))