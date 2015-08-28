#youkuXBLock by wwj718<wuwenjie718@gmail.com>
优酷开发平台：http://open.youku.com/

#安装（平台级别的设置）
*  sudo su edxapp -s /bin/bash
*  cd ~
*  source edxapp_env
*  pip install -e git+https://github.com/wwj718/youkuXBLock
*  在/edx/app/edxapp/cms.envs.json 添加 `"ALLOW_ALL_ADVANCED_COMPONENTS": true,` 到FEATURES

#在studio中设置(课程级别的设置)
进入到"Settings" ⇒ "Advanced Settings",将"youku"添加到Advanced Module List

#使用方法（结合腾讯云）
参考我的文章:[]()
