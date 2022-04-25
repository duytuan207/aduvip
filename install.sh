#!/usr/bin/env bash
set -e
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#=================================================
#	System Requirements:
#   Debian 6+, Ubuntu 14.04+, CentOS 7+,
#	Blog: blog.lvcshu.com
#	Author: johnpoint
#   Maintain: BennyThink
#   Install Express Bot
#   Requires root privilege
#   This code is tested under Ubuntu 16.04/14.04, CentOS 7 and Debian 9.
#   Publish under GNU General Public License v3
#   USE AT YOUR OWN RISK!!!
#=================================================

sh_ver="0.0.0"
Green_font_prefix="\033[32m" && Red_font_prefix="\033[31m" && Green_background_prefix="\033[42;37m" && Red_background_prefix="\033[41;37m" && Font_color_suffix="\033[0m"
Info="${Green_font_prefix}[信息]${Font_color_suffix}"
Error="${Red_font_prefix}[错误]${Font_color_suffix}"
Tip="${Green_font_prefix}[注意]${Font_color_suffix}"
Separator_1="——————————————————————————————"

Get_Dist_Name()
{
    if grep -Eqi "CentOS" /etc/issue || grep -Eq "CentOS" /etc/*-release; then
        DISTRO='CentOS'
        PM='yum'
    elif grep -Eqi "Red Hat Enterprise Linux Server" /etc/issue || grep -Eq "Red Hat Enterprise Linux Server" /etc/*-release; then
        DISTRO='RHEL'
        PM='yum'
    elif grep -Eqi "Aliyun" /etc/issue || grep -Eq "Aliyun" /etc/*-release; then
        DISTRO='Aliyun'
        PM='yum'
    elif grep -Eqi "Fedora" /etc/issue || grep -Eq "Fedora" /etc/*-release; then
        DISTRO='Fedora'
        PM='yum'
    elif grep -Eqi "Amazon Linux AMI" /etc/issue || grep -Eq "Amazon Linux AMI" /etc/*-release; then
        DISTRO='Amazon'
        PM='yum'
    elif grep -Eqi "Debian" /etc/issue || grep -Eq "Debian" /etc/*-release; then
        DISTRO='Debian'
        PM='apt'
    elif grep -Eqi "Ubuntu" /etc/issue || grep -Eq "Ubuntu" /etc/*-release; then
        DISTRO='Ubuntu'
        PM='apt'
    elif grep -Eqi "Raspbian" /etc/issue || grep -Eq "Raspbian" /etc/*-release; then
        DISTRO='Raspbian'
        PM='apt'
    elif grep -Eqi "Deepin" /etc/issue || grep -Eq "Deepin" /etc/*-release; then
        DISTRO='Deepin'
        PM='apt'
    else
        DISTRO='unknow'
    fi

}


# Install_all
Install_all(){
dep_prepare
Install_pip
if [ $1 -eq 1 ];then
    Install_config 10
else
    Install_config 20
fi
install_service
Start_service
}


dep_prepare(){
if [ "$PM" = "yum" ]; then
	$PM install -y epel-release
	$PM update
    $PM install -y python-pip git

elif [ "$PM" = "apt" ]; then
	$PM update
    $PM install -y build-essential python-dev python-pip git
    pip install  setuptools
fi
}


Install_config(){

echo 'Input your Token (telegram bot)'
read p
TOKEN=$p

echo "TOKEN = '$TOKEN'">/home/tele-uptime-bot/bot/config.py

}


# Install_main
Install_pip(){
cd /home
git clone https://github.com/johnpoint/tele-uptime-bot.git
cd tele-uptime-bot
if [ "$PM" = "yum" ]; then
    echo 'CentOS:-)'
    # sed -i '$d' requirements.txt
fi
pip install -r requirements.txt
}

uninstall_all(){
pip uninstall -y -r /home/tele-uptime-bot/requirements.txt
rm -rf /home/tele-uptime-bot
}

menu(){
	echo -e "  Tele-uptime-bot一键管理脚本 ${Red_font_prefix}[v${sh_ver}]${Font_color_suffix}
  ---- 主程序：johmpoint  | 脚本：johnpoint ----
  ——————————————————————
  ${Green_font_prefix}1.${Font_color_suffix} 一键 安装（环境变量）
  ${Green_font_prefix}2.${Font_color_suffix} 一键 安装（配置文件）
  ——————————————————————
  ${Green_font_prefix}3.${Font_color_suffix} 一键 卸载
  ——————————————————————
  ${Green_font_prefix}4.${Font_color_suffix} 启动 服务（systemd）
  ${Green_font_prefix}5.${Font_color_suffix} 停止 服务（systemd）
  ${Green_font_prefix}6.${Font_color_suffix} 重启 服务（systemd）
  ${Green_font_prefix}7.${Font_color_suffix} 查看 服务状态（systemd）
  ——————————————————————
 "
	read -p "请输入数字 [1-7]：" num
case "$num" in
	1)
	Install_all 1
	;;
	2)
	Install_all 2
	;;
	3)
	uninstall_all
	;;
	4)
	Start_service
	;;
	5)
	Stop_service
	;;
	6)
	Restart_service
	;;
	7)
	Service_status
	;;
	*)
	echo -e "${Error} 请输入正确的数字 [1-7]"
	;;
esac
}


# main goes here...

# Check if user is root
if [ $(id -u) != "0" ]; then
    echo "Error: You must be root to run this script, please switch to root."
    exit 1
fi

Get_Dist_Name
# check distribution
if [ "${DISTRO}" = "unknow" ]; then
    echo -e "${Error} 无法获取发行版名称，或者不支持当前发行版"
    exit 1
fi

action=$1
if [[ ! -z $action ]]; then
	if [[ $action = "start" ]]; then
		Start_service
	elif [[ $action = "stop" ]]; then
		Stop_service
	fi
else
	menu
fi
