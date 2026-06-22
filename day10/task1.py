# Author: bibberzz & Codex, GPT-5.5
# Created: 2026/6/4 20:13
# Project: day10
# File: task1.py
# Description: 数据指标概念考察

from pathlib import Path  # 导入 Path，用来处理文件路径

import pandas as pd  # 导入 pandas，并简写为 pd，后面用它读取 Excel 和处理表格数据


class Homework:
    def __init__(self, path):
        self.path = path

    def get_dau(self, date):
        df = pd.read_excel(self.path, sheet_name="新增及留存")  # 读取 Excel 中的“新增及留存”工作表
        target_date = pd.Timestamp(date)  # 指定要计算 DAU 的目标日期

        dau = 0  # 创建一个变量，用来累加 date 当天的活跃用户数
        details = []  # 创建一个列表，用来保存每一项参与计算的数据明细

        for _, row in df.iterrows():  # 逐行遍历表格；_ 是行号，这里用不到；row 是当前这一行的数据
            current_date = row["日期"]  # 取出当前行的日期，也就是这批用户的新增日期

            if current_date > target_date:  # 如果新增日期晚于 date，不可能对 date 当天 DAU 有贡献
                continue  # 跳过这一行，继续看下一行

            days_diff = (target_date - current_date).days  # 计算当前新增日期距离 date 相差多少天

            if days_diff == 0:  # 如果相差 0 天，说明这一行就是 date 当天新增的用户
                value = row["当日新增"]  # 当天新增用户在当天都算作活跃用户
                source = "当日新增"  # 记录这次取数来自“当日新增”这一列
            else:  # 如果不是当天新增，就要看这批老用户在 date 当天是否留存
                source = f"{days_diff}日留存"  # 根据相差天数，拼出要读取的留存列名，例如 6日留存
                value = row[source]  # 从对应的留存列中取出这批用户在 date 当天仍然活跃的人数

            dau += value  # 把当前这一项人数累加到 DAU 总数里
            details.append((current_date.strftime("%Y-%m-%d"), source, int(value)))  # 保存明细，方便最后打印检查

        return dau, details

    def answer1(self):
        """
        1. 1 月 7 日当天的 DAU 是多少？
        :return:
        """
        dau, details = self.get_dau("2018-01-07")

        print("1月7日 DAU 计算明细：")  # 打印说明文字
        for date, source, value in details:  # 遍历刚才保存的每一条计算明细
            print(f"{date} {source}: {value}")  # 打印这一天取了哪一列，以及取到的人数

        print(f"\n2018-01-07 DAU = {int(dau)}")  # 打印最终计算出来的 DAU 结果
        return int(dau)  # 返回 DAU 结果，方便后续代码继续使用这个数值

    def answer2(self):
        """
        2. 从留存角度来看，质量最高的新增用户来自哪一天？
        :return:
        """
        df = pd.read_excel(self.path, sheet_name="新增及留存")  # 读取 Excel 中的“新增及留存”工作表

        # 计算 1.1 - 1.30 每天的对应 1-30 日留存率
        for day in range(1, 31):  # 遍历 1 到 30，分别计算 1日留存率 到 30日留存率
            count_column = f"{day}日留存"  # 拼出留存人数列名，例如 1日留存、2日留存
            rate_column = f"{day}日留存率"  # 拼出留存率列名，例如 1日留存率、2日留存率
            df[rate_column] = df[count_column] / df["当日新增"]  # 留存率 = 留存人数 / 当日新增人数

        rate_columns = []  # 创建一个列表，用来保存 1日留存率 到 30日留存率 这些列名
        for day in range(1, 31):  # 再遍历一次 1 到 30
            rate_columns.append(f"{day}日留存率")  # 把每一天的留存率列名加入列表

        df["1-30日平均留存率"] = df[rate_columns].mean(axis=1, skipna=False)  # 计算每个新增日期的 1-30 日平均留存率
        # mean 取平均值，axis=1 按行求
        # skipna=False，这一行的 30 个留存率里有任何一个缺失值 NaN，那这一行的平均值也直接变成 NaN

        valid_df = df.dropna(subset=["1-30日平均留存率"]).copy()  # 只保留有完整 30 天留存数据的新增日期
        top_df = valid_df.sort_values("1-30日平均留存率", ascending=False).head(5)  # 按平均留存率从高到低排序，取前 5 名
        best_row = top_df.iloc[0]  # 取排序后的第一行，也就是整体留存质量最高的一天

        best_date = best_row["日期"].strftime("%Y-%m-%d")  # 取出最佳新增日期，并转成字符串格式
        best_rate = best_row["1-30日平均留存率"]  # 取出最佳新增日期对应的 1-30 日平均留存率

        print("第二问判断口径：")  # 打印说明文字
        print("质量高 = 后续 30 天整体留存率更高")  # 说明这里如何理解“质量高”
        print("1-30日平均留存率 = 1日留存率 到 30日留存率 的平均值\n")  # 说明具体计算方法

        print("1-30日平均留存率前 5 名：")  # 打印榜单标题
        for _, row in top_df.iterrows():  # 遍历前 5 名的每一行数据
            date = row["日期"].strftime("%Y-%m-%d")  # 取出当前行的日期
            new_users = int(row["当日新增"])  # 取出当前行的当日新增人数
            avg_rate = row["1-30日平均留存率"] * 100  # 把小数形式的留存率转成百分比
            print(f"{date} 当日新增: {new_users}, 1-30日平均留存率: {avg_rate:.2f}%")  # 打印当前日期的排名信息

        print(f"\n第二问答案：从整体留存角度看，质量最高的新增用户来自 {best_date}。")  # 打印第二问结论
        print(f"理由：这一天的 1-30 日平均留存率最高，为 {best_rate * 100:.2f}%。")  # 打印支持这个结论的理由
        return best_date, best_rate  # 返回最佳日期和对应留存率，方便后续代码继续使用

    def answer3(self):
        """
        3. SKU 数量是多少？在 2 月 5 日当天，SKU 销售激活率是多少？
        :return:
        """
        sku_df = pd.read_excel(self.path, sheet_name="商品信息")  # 读取 Excel 中的“商品信息”工作表
        sales_df = pd.read_excel(self.path, sheet_name="商品销售情况")  # 读取 Excel 中的“商品销售情况”工作表

        sku_count = len(sku_df)  # 统计商品信息表的行数，也就是 SKU 总数量

        target_date = pd.Timestamp("2018-02-05")  # 指定要计算 SKU 销售激活率的日期
        sales_on_target_date = sales_df[target_date]  # 取出 2018-02-05 这一天所有商品的销量

        active_sku_count = (sales_on_target_date > 0).sum()  # 统计当天销量大于 0 的商品数量
        activation_rate = active_sku_count / sku_count  # SKU 销售激活率 = 当天有销量的 SKU 数量 / SKU 总数量

        print("第三问计算结果：")
        print(f"SKU 数量 = {sku_count}")
        print(f"2018-02-05 当天有销量的 SKU 数量 = {active_sku_count}")
        print(f"2018-02-05 SKU 销售激活率 = {activation_rate * 100:.2f}%")

        return sku_count, active_sku_count, activation_rate  # 返回 SKU 总数、有销量 SKU 数、销售激活率

    def answer4(self):
        """
        详情页购买转化率 = 当日售卖件数/当日页面浏览次数
        4. 请问三星充电器商品详情页购买转化率哪天最高？
        :return:
        """
        sales_df = pd.read_excel(self.path, sheet_name="商品销售情况")  # 读取 Excel 中的“商品销售情况”工作表
        browse_df = pd.read_excel(self.path, sheet_name="商品浏览情况")  # 读取 Excel 中的“商品浏览情况”工作表

        product_name = "三星 充电器"  # 指定要分析的商品名称
        sales_row = sales_df[sales_df["商品名"] == product_name].iloc[0]  # 找到三星充电器在销售表中的那一行
        # sales_df[] 拿到的依旧是表格形式的数据，需要通过 iloc 定位到实际数据所在的第一行也就是 iloc[0]
        browse_row = browse_df[browse_df["商品名（单位：浏览次数）"] == product_name].iloc[0]  # 找到三星充电器在浏览表中的那一行

        result_list = []  # 创建一个列表，用来保存每天的销售件数、浏览次数和购买转化率

        for date_column in sales_df.columns[1:]:  # 遍历销售表中除“商品名”以外的每一个日期列
            sales_count = sales_row[date_column]  # 取出三星充电器在当前日期的销售件数
            browse_count = browse_row[date_column]  # 取出三星充电器在当前日期的浏览次数

            if browse_count == 0:  # 如果浏览次数为 0，就不能做除法
                continue  # 跳过这一天

            conversion_rate = sales_count / browse_count  # 详情页购买转化率 = 当日售卖件数 / 当日页面浏览次数
            result_list.append({
                "日期": pd.Timestamp(date_column),  # 保存当前日期
                "销售件数": int(sales_count),  # 保存当前日期的销售件数
                "浏览次数": int(browse_count),  # 保存当前日期的浏览次数
                "详情页购买转化率": conversion_rate,  # 保存当前日期的详情页购买转化率
            })

        result_df = pd.DataFrame(result_list)  # 把列表转换成 DataFrame，方便排序和筛选
        max_rate = result_df["详情页购买转化率"].max()  # 找到最高的详情页购买转化率
        best_df = result_df[result_df["详情页购买转化率"] == max_rate].copy()  # 筛选出所有并列最高的日期

        print("第四问计算结果：")
        print(f"{product_name} 详情页购买转化率最高为 {max_rate * 100:.2f}%")
        print("并列最高日期：")

        for _, row in best_df.iterrows():  # 遍历所有并列最高的日期
            date = row["日期"].strftime("%Y-%m-%d")  # 把日期转换成字符串格式
            sales_count = row["销售件数"]  # 取出销售件数
            browse_count = row["浏览次数"]  # 取出浏览次数
            print(f"{date}: {sales_count} / {browse_count} = {max_rate * 100:.2f}%")

        return best_df, max_rate  # 返回并列最高日期明细和最高转化率

    def answer5(self):
        """
        5. 从全站商品来看，这款电商产品，在春节期间的售卖情况与平时相比如何？
        :return:
        """
        sales_df = pd.read_excel(self.path, sheet_name="商品销售情况")  # 读取 Excel 中的“商品销售情况”工作表
        browse_df = pd.read_excel(self.path, sheet_name="商品浏览情况")  # 读取 Excel 中的“商品浏览情况”工作表

        result_list = []  # 创建一个列表，用来保存每天的全站销量、全站浏览量和全站购买转化率

        for date_column in sales_df.columns[1:]:  # 遍历销售表中除“商品名”以外的每一个日期列
            total_sales = sales_df[date_column].sum()  # 计算当前日期所有商品的总销售件数
            total_browse = browse_df[date_column].sum()  # 计算当前日期所有商品的总浏览次数
            conversion_rate = total_sales / total_browse  # 全站购买转化率 = 全站总销售件数 / 全站总浏览次数

            result_list.append({
                "日期": pd.Timestamp(date_column),  # 保存当前日期
                "全站售卖件数": total_sales,  # 保存当前日期全站售卖件数
                "全站浏览次数": total_browse,  # 保存当前日期全站浏览次数
                "全站购买转化率": conversion_rate,  # 保存当前日期全站购买转化率
            })

        result_df = pd.DataFrame(result_list)  # 把列表转换成 DataFrame，方便后续筛选和计算

        spring_start = pd.Timestamp("2018-02-15")  # 指定春节开始日期，这里按除夕处理
        spring_end = pd.Timestamp("2018-02-21")  # 指定春节结束日期，这里按初六处理

        is_spring_festival = (result_df["日期"] >= spring_start) & (result_df["日期"] <= spring_end)  # 判断每一天是否属于春节期间
        spring_df = result_df[is_spring_festival].copy()  # 筛选出春节期间的数据
        normal_df = result_df[~is_spring_festival].copy()  # 筛选出非春节期间的数据，作为平时数据

        spring_total_sales = spring_df["全站售卖件数"].sum()  # 计算春节期间全站总售卖件数
        spring_total_browse = spring_df["全站浏览次数"].sum()  # 计算春节期间全站总浏览次数
        spring_conversion_rate = spring_total_sales / spring_total_browse  # 计算春节期间整体购买转化率
        spring_daily_avg_rate = spring_df["全站购买转化率"].mean()  # 计算春节期间日均购买转化率

        normal_total_sales = normal_df["全站售卖件数"].sum()  # 计算平时全站总售卖件数
        normal_total_browse = normal_df["全站浏览次数"].sum()  # 计算平时全站总浏览次数
        normal_conversion_rate = normal_total_sales / normal_total_browse  # 计算平时整体购买转化率
        normal_daily_avg_rate = normal_df["全站购买转化率"].mean()  # 计算平时日均购买转化率

        print("第五问计算结果：")
        print("春节期间按 2018-02-15 到 2018-02-21 计算")
        print(f"春节期间总售卖件数 = {int(spring_total_sales)}")
        print(f"春节期间总浏览次数 = {int(spring_total_browse)}")
        print(f"春节期间整体购买转化率 = {spring_conversion_rate * 100:.2f}%")
        print(f"春节期间日均购买转化率 = {spring_daily_avg_rate * 100:.2f}%")
        print()
        print(f"平时总售卖件数 = {int(normal_total_sales)}")
        print(f"平时总浏览次数 = {int(normal_total_browse)}")
        print(f"平时整体购买转化率 = {normal_conversion_rate * 100:.2f}%")
        print(f"平时日均购买转化率 = {normal_daily_avg_rate * 100:.2f}%")
        print()
        print("春节期间逐日全站购买转化率：")

        for _, row in spring_df.iterrows():  # 遍历春节期间每天的数据
            date = row["日期"].strftime("%Y-%m-%d")  # 把日期转换成字符串格式
            total_sales = int(row["全站售卖件数"])  # 取出当天全站售卖件数
            total_browse = int(row["全站浏览次数"])  # 取出当天全站浏览次数
            conversion_rate = row["全站购买转化率"] * 100  # 把小数形式的转化率转换成百分比
            print(f"{date}: {total_sales} / {total_browse} = {conversion_rate:.2f}%")

        print()
        print("结论：春节期间浏览次数明显下降，但销量下降不明显，所以购买转化率略高于平时。")

        return spring_df, normal_df  # 返回春节期间和平时的数据，方便后续继续分析

    def answer6(self):
        """
        6. 试计算 1 月 9 日当天的 ARPU 值。
        :return:
        """
        sales_df = pd.read_excel(self.path, sheet_name="商品销售情况")  # 读取 Excel 中的“商品销售情况”工作表
        sku_df = pd.read_excel(self.path, sheet_name="商品信息")  # 读取 Excel 中的“商品信息”工作表

        target_date = pd.Timestamp("2018-01-09")  # 指定要计算 ARPU 的目标日期

        # 创建变量，用来累加 1 月 9 日当天的 DAU
        # 创建列表，用来保存 DAU 的计算明细
        dau, details = self.get_dau(target_date)

        merged_df = sales_df[["商品名", target_date]].merge(
            sku_df,
            left_on="商品名",
            right_on="商品名（单位：元）",
            how="left",
        )  # 把商品销售表和商品信息表合并，这样每个商品都有 1 月 9 日销量和单价

        merged_df["销售额"] = merged_df[target_date] * merged_df["单价"]  # 每个商品销售额 = 当天销售件数 * 商品单价
        total_revenue = merged_df["销售额"].sum()  # 1 月 9 日总销售额 = 所有商品销售额求和
        arpu = total_revenue / dau  # ARPU = 总收入 / 活跃用户数

        print("第六问计算结果：")
        print("ARPU = Average Revenue Per User，即每用户平均收入")
        print("ARPU = 当日总销售额 / 当日 DAU\n")

        print("2018-01-09 DAU 计算明细：")
        for date, source, value in details:  # 遍历 DAU 计算明细
            print(f"{date} {source}: {value}")  # 打印每一项 DAU 来源

        print(f"\n2018-01-09 DAU = {int(dau)}")
        print(f"2018-01-09 总销售额 = {int(total_revenue)}")
        print(f"2018-01-09 ARPU = {arpu:.2f} 元/人")

        return int(dau), total_revenue, arpu  # 返回 DAU、总销售额和 ARPU

    def answer7(self):
        print(f'选 D：')
        print(f'ARPPU = 总收入 / 付费用户数，表内无付费用户数信息，不能计算。A 排除。')
        print(f'消费人数占比 = 消费人数 / 活跃人数，表内无消费人数信息，不能计算。B 排除。')
        print(f'人均下单次数 = 订单数 / 用户数，不能简单用当天销售量和 DAU 进行计算，'
              f'计算标准无法界定。C 排除。')
        print(f'周留存率 = 7日留存 / 当日新增，表中存在数据，可计算。选 D。')


if __name__ == "__main__":  # 只有直接运行当前文件时，才执行下面这些代码
    current_dir = Path(__file__).resolve().parent  # 获取当前这个 Python 文件所在的文件夹路径
    excel_path = current_dir / "指标作业用数据.xls"  # 拼接出 Excel 数据文件的完整路径

    homework = Homework(excel_path)

    homework.answer1()  # 调用第一问函数，输出第一问答案
    print("\n" + "=" * 40 + "\n")
    homework.answer2()  # 调用第二问函数，输出第二问答案
    print("\n" + "=" * 40 + "\n")
    homework.answer3()  # 调用第三问函数，输出第三问答案
    print("\n" + "=" * 40 + "\n")
    homework.answer4()  # 调用第四问函数，输出第四问答案
    print("\n" + "=" * 40 + "\n")
    homework.answer5()  # 调用第五问函数，输出第五问答案
    print("\n" + "=" * 40 + "\n")
    homework.answer6()  # 调用第六问函数，输出第六问答案
    print("\n" + "=" * 40 + "\n")
    homework.answer7()  # 调用第七问函数，输出第七问答案
