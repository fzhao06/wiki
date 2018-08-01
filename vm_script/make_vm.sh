#!/bin/bash
virt-install --name=test$1 \
--vcpus 1 \
--ram 1025 \
--location=/var/lib/libvirt/images/CentOS-7-x86_64-DVD-1804.iso \
--disk size=70 \
--os-variant centos7.0 \
--initrd-inject=gen_ks1.cfg \
--extra-args "ks=file:gen_ks1.cfg console=tty0 console=ttyS0,115200"
#-x 'console=ttyS0,115200n8 serial' \
#-x "ks=file:~/gen_ks.cfg"
exit 0
