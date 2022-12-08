# HanFI
* 稳妥起见 刷机前请备份自己的基带4分区及firmware
* 也许你需要自行替换firmware及基带 详见 [大佬文章](https://www.coolapk.com/feed/38895153) 已验证
* tools都不带系统镜像 其中tool.7z已验证 其余需要自行验证 
* 需要将action生成的OpenWrt_firmware_Handsome_handsome-openstick-ufi001c_xxxx.zip 中的两个img放入你需要的tool解压后目录
* 重命名.bat=>双击.bat/刷入.bat=>刷入 
* 刷入前请自行删除旧版本boot.img及rootfs.img(tool.7z下为system.img)
* firmware 见 [openstick](https://github.com/OpenStick/OpenStick/releases)
# Scripts
* 短信转发pushdeer脚本msg.py op下测试可用 根据https://www.cnblogs.com/uwiu/p/16556855.html 修改修复 使用一致
* 依赖在及python源码前面注释
1. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
2. python get-pip.py
3. pip install pypushdeer
4. 查看脚本修改自己pushkey或自建服务器
* autoawitch.sh 先切换host模式 5秒后查找是否有 网卡USB 10 或 eth0 或 LAN等 自行修改target 若没grep到 切回gadget模式
* bark推送 自行修改
* pushdeer推送 自行修改
# 问题 
mac80211驱动有问题，要编译老网卡需要换，自己添加wcn36xx驱动进去 
还望大佬们指导编译方案 也不清楚是否可行

# 其他
* 打开主机模式，连接拓展坞 echo host > /sys/kernel/debug/usb/ci_hdrc.0/role
* 打开网络共享，关闭主机模式 echo gadget > /sys/kernel/debug/usb/ci_hdrc.0/role
