# lottery-main

以下是如何使用此脚本的一些示例：

- 从`names.txt`文件中选择3个中奖者并将结果打印到控制台：

  ```bash
  python lottery.py names.txt 3 console
  ```

- 从`names.txt`文件中选择5个中奖者并将结果保存到`winners.txt`文件中：

  ```bash
  python lottery.py names.txt 5 file winners.txt
  ```

确保名单文件每行包含一个名称，且没有多余的空白字符。