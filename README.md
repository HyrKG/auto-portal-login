### 获取方式
````
你可以自行编译，也可以在release页中直接下载成品。
````
<a href="https://github.com/HyrKG/auto-portal-login/releases/">☞点此前往Release页</a>

### 使用流程

````
一、找到一个文件夹，并将 auto_portal_login.exe 丢入其中

二、首次使用双击打开软件，等待生成配置（同级目录下auto-pl-config.ini），
并编辑配置保存（账号密码不正确会登录失败），配置解释在下方板块。

三、右键软件【创建快捷方式】，将快捷方式复制到 
【C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp】 以实现开机启动。

四、完成，下次打开电脑将会自动进行验证登录
````

### 配置
````
[general]
#登录类型，0为以PC端登录，1为以移动端登录
term-type = 1 
#账号
account = 199xxxxxxxx
#密码
password = 20xxxxxx
````

### 注意事项
````
一、为确保自动连接有效性，若使用WIFI，请将电信WIFI设置为自动登录。

二、杀软会将所有登录目录中位置的软件报毒，信任此软件即可。若不放心，也可自行通过pyinstaller编译。
````