# TD2: HADOOP and other Apache projects (Pig/Hive)
[toc]

## !!! Download & install before the course !!! : 
### 1. Download 
#### - Oracle VirtualBox: https://www.virtualbox.org/wiki/Downloads
#### - HDP Sandbox (**17GB**)
The download links of HDP Sandbox on VirtualBox:
- HDP 2.6.5 (https://archive.cloudera.com/hwx-sandbox/hdp/hdp-2.6.5/HDP_2.6.5_virtualbox_180626.ova)

### 2. Installation: 
  1. Install Oracle VirtualBox. (for Windows 11, following this tutorial: https://nerdschalk.com/how-to-install-and-use-virtualbox-on-windows-11/)
  2. Add    

## Prerequisites

- Familiarity with terminals, shell commands and fundamental knowledge in operating Systems (Linux)
- Basic knowledge in virtualization and managing virtual machines
- Basic knowledge in containerization and dealing with Docker images and containers
Objectives

##  Install a hypervisor or VM monitor such as VirtualBox
- Install Hortonworks Data Platform
- Access Hortonworks Data Platform via ssh
- Access HDFS and learn how to transfer files

## Introduction

Every business is now a data business. Data is the organizations’ future and most valuable asset. The Hortonworks Data Platform (HDP) is a security-rich, enterprise-ready open-source Hadoop distribution based on a centralized architecture (YARN). Hortonworks Sandbox is a single-node cluster and can be run as a Docker container installed on a virtual machine. HDP is a complete system to handle the processing and storage of big data. It is an open architecture used to store and process complex and large-scale data. It is composed of numerous Apache Software Foundation (ASF) projects including Apache Hadoop and is built specifically to meet enterprise demands. Hortonworks was a standalone company untill 2019 when it is merged to Cloudera and now Hortonworks is a subsidiary for Cloudera, Inc.

![!\[alt text\]("img/!\[Nel\](img/Nel8wxT.png)" "Hortonworks")](img/Nel8wxT.png)

## Hardware requirements

- Memory dedicated to the cluster (Minimum: 4 GiB, Recommended: 8+ GiB). More is better.
- CPU (Minimum: 4 Cores, Recommended: 6+ Cores)
- Virtualization should be enabled
(Check Virtualization on Windows, On Linux: lscpu). Sometimes it is disabled in BIOS.
- Storage
  - 25-35 GiB for HDP 2.5.0
  - 65-75 GiB for HDP 2.6.5
  - 80-100 GiB for HDP 3.0.1

HDP 2.5.0 is based on CentOS 6.8 which is EOL by 2021 and updating the packages via yum is kinda not possible. We recommend to install HDP 2.6.5 unless you have less resources.


## Installing Hortonworks Sandbox