### 使用流程

````
一、找到一个文件夹，并将 auto_portal_login.exe 丢入其中

二、首次使用双击打开软件，等待生成配置，并编辑配置保存。配置解释在下方。

三、右键软件【创建快捷方式】，将快捷方式复制到 
【C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp】 

四、完成，下次打开电脑将会自动进行验证登录
````

### 配置
````
[general]
#登录类型，0为以PC端登录，1为以手机端登录
term-type = 1 
#账号
account = 199xxxxxxxx
#密码
password = 20xxxxxx
````