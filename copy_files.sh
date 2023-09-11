#!/bin/bash

# 源目录和目标目录的路径
source_directory="cache/leetcode/editor/cn"
target_directory="leetcode"

# 使用`cp`命令将源目录中的文件复制到目标目录，并使用 `-u` 选项来进行覆盖
cp -r "$source_directory"/* "$target_directory"/

# 检查`cp`命令的退出状态来确定是否成功复制文件
if [ $? -eq 0 ]; then
  echo "Files copy successfully!"
else
  echo "Failed to copy files."
fi
