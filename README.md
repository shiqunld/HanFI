# HanFI
* 稳妥起见 刷机前请备份自己的基带4分区及firmware
* 也许你需要自行替换firmware及基带
* tools都不带系统镜像 其中tool.7z已验证 其余需要自行验证 
* 需要将action生成的OpenWrt_firmware_Handsome_handsome-openstick-ufi001c_xxxx.zip 中的两个img放入你需要的tool解压后目录
* 重命名.bat=>双击.bat/刷入.bat=>刷入 
* 刷入前请自行删除旧版本boot.img及rootfs.img(tool.7z下为system.img)
* firmware 见 [openstick](https://github.com/OpenStick/OpenStick/releases)
* 1202更新 短信转发pushdeer脚本 op下测试可用
# 问题 
mac80211驱动有问题，要编译老网卡需要换，自己添加wcn36xx驱动进去 
还望大佬们指导编译方案 也不清楚是否可行
