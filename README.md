<h1 align="center">

GDUF_autocheck

</h1>

**广东金融学院易广金健康打卡**
- [x] 支持多人打卡👨‍👩‍👧‍👧
- [x] 支持Server酱微信通知打卡结果💬
- [x] 目前仅支持固定内打卡🏫（默认地址是肇庆校区，本部的朋友需要到[index.py](index.py)自行改一下地址哈）
- [x] 基于Github Actions定时每日早上8:00自动打卡，完全解放你的设备和服务器✔
- [ ] 正在改1Secrets提交方法！

为防止查水表，暂不提供任何教程和帮助，自行解决！！！

## 使用方法
- Star并Fork此项。<br>
- 进入你的仓库，Settings → Secrets,
- 添加2个 Secrets（利用Secrets解决隐私问题）：

|Name |Value                                                        |
|:----|:------------------------------------------------------------|
|USERS|{"名字":["logintoken","学号"],"名字2":["logintoken2","学号2"]}|
|SCKEY|SCUxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      |

备注：<br>
①理论上USERS项的Value格式填写正确，可添加无限用户<br>
②如何获取[logintoken](如何获取logintoken.pdf) <br>
③如何获取[SCKEY](如何获取SCKEY.pdf)


## 许可
本项目以 MIT 协议开源，详情请见 [LICENSE](LICENSE) 文件。
