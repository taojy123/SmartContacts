主机地址 http://smartcontacts.sinaapp.com/

现设定了5请求：
1、add_contacts 添加通讯录记录
2、get_contacts 查询通讯录数据
3、add_send 添加发货记录
4、get_send 查询发货数据
5、get_user_info 查询用户信息



你可以依次在浏览器上输入以下网址模拟请求，在网页上查看返回数据结果

http://smartcontacts.sinaapp.com/add_contacts/?user_id=abc&_id=123&QQHaoMa=77888&ShouJi=13500001234
# 添加通讯录信息，请求 /add_contacts/ 加上参数
# 返回 ok

http://smartcontacts.sinaapp.com/get_contacts/123/
# 查询通讯录数据，请求 /get_contacts/(记录id)/
# 返回 json 格式的这一条通讯录的数据

http://smartcontacts.sinaapp.com/get_user_info/abc/
# 查询某个用户的信息（他拥有的所有通讯记录的id和所有发货记录的id），请求 /get_user_info/(用户id)/
# 返回 json 格式数据，其中有两个键，cids 为所有的通讯录记录id，每个id以逗号隔开；sids 为所有的发货记录的id，每个id以逗号隔开

# 发货记录的添加和查询方法与通讯录类似，就不赘述。