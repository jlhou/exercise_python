# 1.输入苹果单价
price_str = input("输入单价")
# 2.输入苹果重量
weight_str = input("苹果的重量")
# 3.计算支付金额
price = float(price_str)
weight = float(weight_str)
money = price*weight
print(money)