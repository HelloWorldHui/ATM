import os


# 普通用户
class Client:
    def __init__(self, data):
        print(data)
        self.id = data[0]  # id
        self.password = data[1]  # 密码
        self.level = data[2]  # 级别
        self.money = data[3]  # 金额
        self.stauts = data[4]  # 状态

    # 查询 金额
    def chaxun(self):
        print("账号'%s',余额为%.2f$" % (self.id, int(self.money)))
        return self.money

    # 取钱
    def qu(self):
        num = int(input("输入取走金额(以百为单位,最高5000):"))
        while num % 100 != 0 or num > int(self.money) or num < 100 or num > 5000:
            num = int(input("输入错误,请重试:"))
        data_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                data_list.append(line)
        with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
            for i in range(len(data_list)):
                detail_list = data_list[i].strip().split(',')
                if detail_list[0] == self.id:
                    # 取完后的钱
                    self.money = str(int(detail_list[3]) - num)
                    detail_list[3] = self.money
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                else:
                    info_str = ','.join(detail_list) + '\n'
                    f1.write(info_str)
        os.remove('user_info.txt')
        os.rename('user_info(副本).txt', 'user_info.txt')
        print("账号'%s',取走%.2f$,余额为%.2f$" % (self.id, int(num), int(self.money)))
        return self.money
     # 存钱
    def cun(self):
        num = int(input("输入存入金额(以百为单位):"))
        while num % 100 != 0 or num < 100:
            num = int(input("输入错误,请重试:"))
        data_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                data_list.append(line)
        with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
            for i in range(len(data_list)):
                detail_list = data_list[i].strip().split(',')
                if detail_list[0] == self.id:
                    # 存完之后的钱
                    self.money = str(int(detail_list[3]) + num)
                    detail_list[3] = self.money
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                else:
                    info_str = ','.join(detail_list) + '\n'
                    f1.write(info_str)
        os.remove('user_info.txt')
        os.rename('user_info(副本).txt', 'user_info.txt')
        print("账号'%s',取走%.2f$,余额为%.2f$" % (self.id, int(num), int(self.money)))
        return self.money

    # 转账
    def zhuan(self):
        id_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                info_list = line.strip().split(',')
                id_list.append(info_list[0])
        print("#ID列表", id_list, )
        id = input("输入转账ID:")
        while id not in id_list or id == self.id:
            id = input("ID输入错误,请重试:")
            if id.lower() == 'q':
                return

        num = int(input("输入转账金额(以百为单位,最高5000):"))
        while num % 100 != 0 or num > int(self.money) or num < 100 or num > 5000:
            num = int(input("金额输入错误,请重试:"))

        data_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                data_list.append(line)

        with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
            for i in range(len(data_list)):
                detail_list = data_list[i].strip().split(',')
                if detail_list[0] == self.id:  # 修改自己的 金额
                    self.money = str(int(detail_list[3]) - num)
                    detail_list[3] = self.money
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                elif detail_list[0] == id:  # 增加 接收人的金额
                    detail_list[3] = str(int(detail_list[3]) + num)
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                else:
                    info_str = ','.join(detail_list) + '\n'
                    f1.write(info_str)
        os.remove('user_info.txt')
        os.rename('user_info(副本).txt', 'user_info.txt')
        print("转账成功,剩余余额%.2f" % int(self.money))
        return self.money

    # 修改密码
    def xiugai(self, ):
        old_pwd = input("输入旧密码:")
        while old_pwd != self.password:
            old_pwd = input("密码错误,请重试:")

        new_pwd = input("输入新密码(q返回):")
        if new_pwd.lower() == 'q':
            print("取消修改密码")
            return

        while len(new_pwd) < 6 or len(set(new_pwd)) == 1:
            new_pwd = input("新密码不能小于6位或者6位完全相同,请重试:")

        new_pwd_2 = input("确认新密码:")
        while len(new_pwd_2) < 6 or len(set(new_pwd_2)) == 1:
            print("新密码不能小于6位或者6位完全相同,请重试:")
        if new_pwd == new_pwd_2:
            data_list = []
            with open("user_info.txt", 'r', encoding='utf8') as f:
                for line in f:
                    data_list.append(line)

            with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
                for i in range(len(data_list)):
                    detail_list = data_list[i].strip().split(',')
                    if detail_list[0] == self.id:  # 修改自己密码
                        self.password = new_pwd
                        detail_list[1] = self.password
                        info_str = ','.join(detail_list) + "\n"
                        f1.write(info_str)
                    else:
                        info_str = ','.join(detail_list) + '\n'
                        f1.write(info_str)
            os.remove('user_info.txt')
            os.rename('user_info(副本).txt', 'user_info.txt')
            print("密码修改成功,新密码为%s" % self.password)
            return self.password

        else:
            print("2次密码不一样,请重试")
            return

# 管理员
class Admin:
    def __init__(self):
        self.id = 'a0001'
        self.password = '112233'

    # 添加 用户
    def tianjia(self):
        id_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                info_list = line.strip().split(',')
                id_list.append(info_list[0])

        new_id = input("输入新账号ID:")
        while new_id in id_list:
            new_id = input("ID已存在,请重试:")

        with open("user_info.txt", 'a', encoding='utf8') as f:
            f.write(new_id + ',' + '123456' + ',' + '1' + ',' + '10000' + ',' + '0' + '\n')
        print(new_id, '添加成功')

    # 冻结
    def dongjie(self):
        id_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                info_list = line.strip().split(',')
                id_list.append(info_list[0])

        dongjie_id = input("输入冻结账号ID:")
        while dongjie_id not in id_list:
            dongjie_id = input("ID不存在,请重试:")

        data_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                data_list.append(line)

        with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
            for i in range(len(data_list)):
                detail_list = data_list[i].strip().split(',')
                if detail_list[0] == dongjie_id:  # 修改自己密码
                    detail_list[-1] = '1'
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                else:
                    info_str = ','.join(detail_list) + '\n'
                    f1.write(info_str)
        os.remove('user_info.txt')
        os.rename('user_info(副本).txt', 'user_info.txt')
        print(dongjie_id, '以冻结')

    # 解冻
    def jiedong(self):
        id_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                info_list = line.strip().split(',')
                id_list.append(info_list[0])

        jiedong_id = input("输入解冻账号ID:")
        while jiedong_id not in id_list:
            jiedong_id = input("ID不存在,请重试:")

        data_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                data_list.append(line)

        with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
            for i in range(len(data_list)):
                detail_list = data_list[i].strip().split(',')
                if detail_list[0] == jiedong_id:  # 修改自己密码
                    detail_list[-1] = '0'
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                else:
                    info_str = ','.join(detail_list) + '\n'
                    f1.write(info_str)
        os.remove('user_info.txt')
        os.rename('user_info(副本).txt', 'user_info.txt')
        print(jiedong_id, '已解冻')

    # 查询用户信息
    def chaxun(self):
        id_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                info_list = line.strip().split(',')
                id_list.append(info_list[0])
        print('ID列表', id_list)
        chaxun_id = input("查询ID:")

        while chaxun_id not in id_list:
            print('ID列表', id_list)
            chaxun_id = input("ID不存在,请重试:")

        l = ['账号', '密码', '级别(0管理员,1普通)', '金额', '状态(0正常,1冻结)']

        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                info_list = line.strip().split(',')
                if chaxun_id == info_list[0]:
                    for i in range(len(info_list)):
                        print(l[i], ">>>", info_list[i])
                    return
            else:
                print("ID不存在,请重试:")


# ATM 系统
class ATM:

    def __init__(self):
        with open("user_info.txt", 'w', encoding='utf8') as f:
            f.write("a0001,112233,0,10000,0" + '\n')  # 管理员
            f.write("p0001,123456,0,10000,0" + '\n')  # 普通账号1
            f.write("p0002,123456,0,10000,0" + '\n')  # 普通账号2

    # 密码错三次冻结
    def dongjie(self, ID):
        data_list = []
        with open("user_info.txt", 'r', encoding='utf8') as f:
            for line in f:
                data_list.append(line)

        with open("user_info(副本).txt", 'w', encoding='utf8') as f1:
            for i in range(len(data_list)):
                detail_list = data_list[i].strip().split(',')
                if detail_list[0] == ID:  # 修改自己密码
                    detail_list[-1] = '1'
                    info_str = ','.join(detail_list) + "\n"
                    f1.write(info_str)
                else:
                    info_str = ','.join(detail_list) + '\n'
                    f1.write(info_str)
        os.remove('user_info.txt')
        os.rename('user_info(副本).txt', 'user_info.txt')

    # z主程序运行
    def run(self):
        ID = input("请输入卡号:")
        password = input("请输入密码:")
        client = None
        admin = None

        # 管理员登录
        if ID == 'a0001':
            while password != '112233':
                password = input("密码错误,联系管理员(q退出系统):")
                if password.lower() == 'q':
                    print('退出系统...')
                    return
            print("管理员登录成功")
            admin = Admin()

        if admin != None:
            task = {'1': admin.tianjia, '2': admin.dongjie, '3': admin.jiedong, '4': admin.chaxun}
            menu = {'1': "添加账号", '2': "冻结账号", '3': "解冻", '4': "查询信息", '5': '退出系统'}

            while 1:
                for k, v in menu.items():
                    print(k, v)

                choice = input("请输入你要执行的任务序号:")
                if choice == '5':
                    print('退出系统...')
                    return
                try:
                    task[choice]()
                except Exception as e:
                    print("出错,请重试....")
                print('\n')

        with open("user_info.txt", 'r', encoding='utf8') as f:
            data_list = []
            for line in f:
                data_list.append(line)

        for line in data_list:
            num = 1

            # 用户信息列表
            data = line.strip().split(",")
            if ID == data[0]:  # 判断 账号是否存在
                if data[-1] == "1":
                    print('该账号已冻结,请联系管理员解冻')
                    return

                # 密码错三次 账号冻结
                while password != data[1] and num < 3:
                    num += 1
                    password = input("密码错误,请重试(第%s次尝试):" % num)

                if ID == data[0] and password == data[1]:

                    print('"%s",登录成功\n' % ID)
                    client = Client(data)  # 实例化一个客户类 把用户信息传进去
                    break  # 跳出 for 循环

                else:
                    self.dongjie(ID)
                    print("该账号'%s'已冻结,联系管理员解冻" % ID)
                    break  # 跳出 for 循环
        else:
            print("账号'%s'不存在,请联系管理员" % ID)

        if client != None:
            task = {'1': client.chaxun, '2': client.qu, '3': client.cun, '4': client.zhuan, '5': client.xiugai}
            menu = {'1': "查询余额", '2': "取款", '3': "存款", '4': "转账", '5': "修改个人密码", '6': '退出系统'}
            while 1:
                for k, v in menu.items():
                    print(k, v)

                choice = input("请输入你要执行的任务序号(默认为1):")
                if choice == '6':
                    print('退出系统...')
                    return
                try:
                    task[choice]()
                except Exception as e:
                    print("出错,请重试...")
                print('\n')


if __name__ == '__main__':
    ATM().run()  # 程序的入口
