# ------------------------------------------------------------------------------
# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2025 Jayesh Badwaik <j.badwaik@fz-juelich.de>
# ------------------------------------------------------------------------------
FROM  rockylinux:9
RUN   yum install -y python3-pip
RUN   pip install easybuild
RUN   useradd -m testuser
RUN   yum update -y
RUN   yum install -y epel-release
RUN   yum install -y Lmod which perl tar bzip2
RUN   yum groupinstall -y "Development Tools"
RUN   ln -s /usr/share/lmod/8.7.55/libexec/lmod /usr/local/bin/lmod
USER  testuser
RUN   eb --robot --modules-tool Lmod /usr/local/easybuild/easyconfigs/g/GCCcore/GCCcore-15.1.0.eb
RUN   eb --robot --modules-tool Lmod  /usr/local/easybuild/easyconfigs/g/GCC/GCC-15.1.0.eb
USER  root
RUN   yum install -y python3-devel
USER  testuser
COPY  .bashrc /home/testuser/.bashrc


