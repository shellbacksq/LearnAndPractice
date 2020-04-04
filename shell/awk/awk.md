# awk

> awk定位是文本处理，名字来由为贝尔实验室 Alfred Aho，Peter Weinberger, 和 Brian Kernighan 的Family Name的首字符.

参考:
- https://www.cnblogs.com/ginvip/p/6352157.html
- https://coolshell.cn/articles/9070.html





---

## 基本语法和常识
![](https://www.runoob.com/wp-content/uploads/2018/10/20170719154838100.png)

- awk '{pattern + action}' {filenames}
- -F 用于指定分割符
- $1,$2..$n代表第n列
- NF表示当前的第N列, NR表示当前第R行
- 花括号（{}）不需要在程序中始终出现，但它们用于根据特定的模式对一系列指令进行分组.
- printf 可以控制输出格式
- ''内字符串用""
- $1 ~ /FIN/ 模式匹配
- awk 'NR!=1{print > $6}' netstat.txt 按第6类属性分组
- BEGIN{ 这里面放的是执行前的语句 } {这里面放的是处理每一行时要执行的语句}  END {这里面放的是处理完所有的行后要执行的语句 }
- 环境变量, 使用-v来传入外部变量 awk -v val=$x 


## 例子
例子1:
```
$ cat cal.awk
#!/bin/awk -f
#运行前
BEGIN {
    math = 0
    english = 0
    computer = 0
    printf "NAME    NO.   MATH  ENGLISH  COMPUTER   TOTAL\n"
    printf "---------------------------------------------\n"
}
#运行中
{
    math+=$3
    english+=$4
    computer+=$5
    printf "%-6s %-6s %4d %8d %8d %8d\n", $1, $2, $3,$4,$5, $3+$4+$5
}
#运行后
END {
    printf "---------------------------------------------\n"
    printf "  TOTAL:%10d %8d %8d \n", math, english, computer
    printf "AVERAGE:%10.2f %8.2f %8.2f\n", math/NR, english/NR, computer/NR

```




|||
|-|-|
|$0	|当前记录（这个变量中存放着整个行的内容）|
|$1~$n|	当前记录的第n个字段，字段间由FS分隔|
|FS	|输入字段分隔符 默认是空格或Tab|
|NF	|当前记录中的字段个数，就是有多少列|
|NR	|已经读出的记录数，就是行号，从1开始，如果有多个文件话，这个值也是不断累加中。|
|FNR|	当前记录数，与NR不同的是，这个值会是各个文件自己的行号|
|RS	|输入的记录分隔符， 默认为换行符|
|OFS|	输出字段分隔符， 默认也是空格|
|ORS|	输出的记录分隔符，默认为换行符|
|FILENAME|	当前输入文件的名字|