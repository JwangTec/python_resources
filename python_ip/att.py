import paramiko
import socket
from concurrent.futures import ThreadPoolExecutor
import threading
from functools import partial

def connection(host_ip, host_port=22):
    # 实例化SSHClient
    client = paramiko.SSHClient()
    # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端，以用户名和密码进行认证
    client.connect(hostname=host_ip, port=host_port, username='rimi', password='123', timeout=5)
    # 打开一个Channel并执行命令
    stdin, stdout, stderr = client.exec_command('')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
    # 打印执行结果
    # print(stdout.read().decode('utf-8'))
    print('这台机器的ip可以用{}'.format(host_ip))
    # 关闭SSHClient
    client.close()


def try_conn(j,i):
    try:
        connection('10.2.{}.{}'.format(str(j),str(i)), 22)
    except Exception:
        pass


executor = ThreadPoolExecutor(max_workers=20)
# t.
all_task = [executor.submit(partial(try_conn,j), (i)) for j in range(3) for i in range(256)]
#all_task1 = [executor.submit(partial(try_conn1,j), (i)) for j in range(256) for i in range(256)]
