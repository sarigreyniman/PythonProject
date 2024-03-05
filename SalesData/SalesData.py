import datetime
import random
import platform
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

from FileOperation.FileOperation import FileOperation


class SalesData:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    # task2:4
    def eliminate_duplicates(self):
        """avoiding duplicate lines in the dataset """
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)

    # task2:5
    def calculate_total_sales(self):
        """calculate the total sales for each product"""
        total_sales = self.data.groupby('Product')['Total'].sum().reset_index()
        return total_sales

    # task2:6
    def _calculate_total_sales_per_month(self):
        """calculate the total sales for each month"""
        total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum()
        return total_sales_per_month

    # task2:7
    def _identify_best_selling_product(self):
        """find the product with the max total sales"""
        total_sales = self.calculate_total_sales().max()
        return total_sales['Product']

    # task2:8
    def _identify_month_with_highest_sales(self):
        """find the month with the max total sales"""
        total_sales = self._calculate_total_sales_per_month().idxmax()
        return total_sales

    # task2:9
    def analyze_sales_data(self):
        """do dictionary with the best-selling product and the month with highest sales"""
        d = {
            'best_selling_product': self._identify_best_selling_product(),
            'month_with_highest_sales': self._identify_month_with_highest_sales(),
        }
        return d

    # task2:10
    def add_values_to_the_dictionary(self):
        """return mean sum of sales for month for each product"""
        d = self.analyze_sales_data()
        d['minimest selling product'] = self.calculate_total_sales().min()['Product']
        d["average of the sales for monthes"] = self._calculate_total_sales_per_month().mean()
        return d

    # task3:11
    def calculate_cumulative_sales(self):
        monthly_sales = self.data.groupby(['Product', self.data['Date'].dt.month])['Total'].sum().groupby(
            'Product').cumsum().reset_index()
        return monthly_sales

    # task3:12
    def add_90_values_column(self):
        self.data['Discount'] = 0.9 * (self.data['Price'])

    # task3:13
    def bar_chart_category_sum(self):
        grouped_data = self.data.groupby('Product')['Quantity'].sum().reset_index()
        plt.bar(grouped_data['Product'], grouped_data['Quantity'])
        plt.xlabel('Product')
        plt.ylabel('Quantity Sold')
        plt.title('Sum of Quantities Sold for Each Product')
        plt.tight_layout()
        plt.show()

    # task3:14
    def calculate_mean_quantity(self):
        total_column = self.data['Total'].values
        mean = np.mean(total_column)
        median = np.median(total_column)
        max_total = np.max(total_column)
        max_index = np.where(total_column == max_total)
        total_column = np.delete(total_column, max_index)
        second_max = np.max(total_column)
        return mean, median, second_max

    # task3:15
    def filter_by_selling_or(self):
        sales_summary = self.data.groupby('Product').count().reset_index()
        return sales_summary[(sales_summary['Quantity'] > 5) | (sales_summary['Quantity'] == 0)]

    def filter_by_selling_and(self):
        sales = self.data
        sales['Count'] = sales.groupby('Product')['Product'].transform('count')
        return sales[(sales['Price'] > 300) & (sales['Count'] < 2)]

    # task3:16
    def divide_by_2(self):
        self.data['Black_Friday'] = self.data['Price'] / 2

    # task3:17
    def calculate_stats(self, columns=None):
        try:
            # Select valid numeric columns
            numeric_columns = self.data.select_dtypes(include=[np.number]).columns

            if columns is None:
                # Find maximum, sum, absolute values, and cumulative maximum for all numeric columns
                all_stats = {
                    'Maximum': self.data[numeric_columns].max(),
                    'Sum': self.data[numeric_columns].sum(),
                    'Absolute Values': np.abs(self.data[numeric_columns]),
                    'Cumulative Maximum': self.data[numeric_columns].cummax()
                }
                print(all_stats)
            else:
                # Find maximum, sum, absolute values, and cumulative maximum for specified numeric columns
                selected_stats = {
                    'Maximum': self.data[columns].max(),
                    'Sum': self.data[columns].sum(),
                    'Absolute Values': np.abs(self.data[columns]),
                    'Cumulative Maximum': self.data[columns].cummax()
                }
                print(selected_stats)

                # Visualize the results using Seaborn
                plt.figure(figsize=(12, 8))
                sns.heatmap(self.data[columns].corr(), annot=True, cmap='coolwarm', fmt='.2f')
                plt.title('Correlation Heatmap for Selected Columns')
                plt.show()

        except Exception as e:
            print(f"Error calculating and visualizing stats: {e}")

    # task6
    def plot_total_sales(self):
        """bar plot for total sales """
        total_sales = self.calculate_total_sales()
        products = total_sales['Product']
        sales = total_sales['Total']
        plt.figure(figsize=(10, 6))
        plt.bar(products, sales, color='skyblue')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.title('Total Sales for Each Product')
        plt.tight_layout()
        plt.show()

    # task6
    def plot_total_sales_per_month_lineplot(self):
        """ linerplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Line Plot)')
        plt.show()

    # task6
    def plot_total_sales_per_month_scatterplot(self):
        """ scatterplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Scatter Plot)')
        plt.show()

    # task6
    def plot_total_sales_per_month_barplot(self):
        """ barplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=total_sales_per_month.index, y=total_sales_per_month.values)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Bar Plot)')
        plt.show()

    # task6
    def plot_total_sales_per_month_boxplot(self):
        """ boxplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=total_sales_per_month.values)
        plt.xlabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Box Plot)')
        plt.show()

    # task6
    def plot_total_sales_per_month_violinplot(self):
        """ violinplot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.violinplot(x=total_sales_per_month.values)
        plt.xlabel('Total Sales')
        plt.title('Total Sales per Month (Seaborn Violin Plot)')
        plt.show()

    # task6
    def plot_total_sales_per_month(self):
        """ simple plot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.plot(total_sales_per_month.index, total_sales_per_month.values, marker='o', linestyle='-')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        plt.tight_layout()
        plt.show()

    # task6
    def plot_total_sales_per_month_horizontal_bar(self):
        """ horizontal_bar for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        total_sales_per_month.plot(kind='barh', color='skyblue')
        plt.xlabel('Total Sales')
        plt.ylabel('Month')
        plt.title('Total Sales per Month (Horizontal Bar Plot)')
        plt.tight_layout()
        plt.show()

    # task6
    def plot_total_sales_per_month_pie(self):
        """ pie for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.figure(figsize=(8, 8))
        total_sales_per_month.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.tab20.colors)
        plt.ylabel('')
        plt.title('Total Sales Distribution per Month (Pie Chart)')
        plt.tight_layout()
        plt.show()
    # task6
    def plot_total_sales_per_month_step(self):
        """ step plot for total sales per month"""
        total_sales_per_month = self._calculate_total_sales_per_month()
        plt.step(total_sales_per_month.index, total_sales_per_month.values, color='skyblue', where='mid')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month (Step Plot)')
        plt.tight_layout()
        plt.show()

    # task6
    def plot_monthly_sales_histogram(self):
        monthly_sales = self.calculate_cumulative_sales()
        plt.figure(figsize=(10, 6))
        plt.hist(monthly_sales['Total'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Total Sales')
        plt.ylabel('Frequency')
        plt.title('Histogram of Total Sales per Product')
        plt.grid(True)
        plt.show()

        # task6
    # task6
    def plot_monthly_sales_boxplot(self):
        monthly_sales = self.calculate_cumulative_sales()
        plt.boxplot(monthly_sales['Total'], vert=False)
        plt.xlabel('Total Sales')
        plt.title('Box Plot of Total Sales per Product')
        plt.show()

    # task6
    def plot_pie_chart(self, total_sales):
        if total_sales is None:
            print("Error: No data available")
            return
        # Convert 'Total' column to numeric values
        total_sales['Total'] = pd.to_numeric(total_sales['Total'], errors='coerce')
        # Remove rows with NaN values
        total_sales = total_sales.dropna(subset=['Total'])
        # Create a pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(total_sales['Total'], labels=total_sales.index, autopct='%1.1f%%', startangle=140)
        plt.title('Total Sales Distribution by Product')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    # task6
    def plot_3d_graph(self):
        if self.data is None:
            print("Data is empty")
            return
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = self.data['Price'].values
        y = self.data['Quantity'].values
        z = self.data['Total'].values
        ax.scatter(x, y, z)
        ax.set_xlabel('Price')
        ax.set_ylabel('Quantity')
        ax.set_zlabel('Total')
        plt.show()

    # task6
    def calculate_customer_payment(self, customer_numbers):
        total_payment = 0
        for num in customer_numbers:
            if num % 8 == 0:
                total_payment += 200
            else:
                total_payment += 200 + (num % 8 - 1) * 50
        return total_payment

    # task7:1
    def treat_errors(self):
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        current_name = "Yudit&Ruti&Sari"
        try:
            x = 4 / 0
            print(x)
        except ZeroDivisionError:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> type error: divide by zero! <" + current_name + ">")
        try:
            year = 50
            month = 50
            day = 50
            if year < 2000 | year > 2024 | month < 1 | month > 12 | day < 1 | day > 31:
                raise ValueError("Invalid date")
            datetime.datetime(year, month, day)
        except ValueError:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> type error: you didnt enter correct date!!! <" + current_name + ">")
        try:
            y = "aaa"
            print(int(y))
        except BaseException:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> cannot convert type str to int <" + current_name + ">")
        try:
            s = {'o': 'f'}
            print(s['Price'])
        except BaseException:
            print("<" + current_name + "," + str(current_date) + "," + str(
                current_time) + "> cannot find 'Price' in s <" + current_name + ">")

    # task7:2

    # task7:3
    def rand_num(self, product_name):
        sum_sales = self.data.groupby('Product')['Quantity'].count()[product_name]
        max_sales_sum = self.data.groupby('Product')['Price'].max()[product_name]
        rand_num = random.randint(sum_sales, max_sales_sum)
        a = []
        a.append(product_name)
        a.append(sum_sales)
        a.append(max_sales_sum)
        a.append(rand_num)
        print(a)

    # task7:4
    def get_python_version(self):
        version = platform.python_version()
        return version

    # task7:5
    def process_parameters(*args):
        result = {}
        for param in args:
            if isinstance(param, str) and "=" in param:
                value, name = param.split("=", 1)
                result[name] = value
            elif isinstance(param, (int, float)):
                print(param)
        return result

    # task7:6
    def print_from_data(self):
        print(self.data.head(3))
        print("==================")
        print(self.data.tail(2))
        random_row = self.data.sample(n=1)
        print(random_row)

    # task7:7
    def read_on_time(self):
        for value in self.data.select_dtypes(include=[np.number]).values.flatten():
            print(value)

# 4
print("========4==========")
file_path = "C:\\Users\\user1\\Documents\\תיקיית תיכנות\\שנה ב'\\phyton\\project_YafeNof\\Files\\YafeNof.csv"
file = FileOperation()
data = file.read_csv(file_path)
sales = SalesData(data)
print(sales.data)
sales.eliminate_duplicates()
print(sales.data)
# 5
print("========5==========")
total = sales.calculate_total_sales()
print(total)
# 6
print("========6==========")
total1 = sales._calculate_total_sales_per_month()
print(total1)
# 7
print("========7==========")
total = sales._identify_best_selling_product()
print("max product:", total)
# 8
print("========8==========")
total = sales._identify_month_with_highest_sales()
print("max month:", total)
# 9
print("========9==========")
data = sales.analyze_sales_data()
print(data)
# 10
print("========10==========")
data = sales.add_values_to_the_dictionary()
print(data)
# 11
print("========11==========")
monthly_sales = sales.calculate_cumulative_sales()
print(monthly_sales)
# 12
print("========12==========")
sales.add_90_values_column()
print(sales.data)
# 13
print("========13==========")
sales.bar_chart_category_sum()
# 14
print("========14==========")
tuple_calculated = sales.calculate_mean_quantity()
print(tuple_calculated)
# 15
print("========15A==========")
new_sales = sales.filter_by_selling_or()
print(new_sales[['Product', 'Quantity']])
print("========15B==========")
new2_sales = sales.filter_by_selling_and()
print(new2_sales[['Product', 'Quantity', 'Price']])
# 16
print("========16==========")
sales.divide_by_2()
print(sales.data)
print("========17==========")
stats = sales.calculate_stats(data)
print(stats)

# task 6
# matplotlib
# 1
sales.plot_total_sales()
# 2
sales.plot_total_sales_per_month()
# 3
sales.plot_total_sales_per_month_horizontal_bar()
# 4
sales.plot_total_sales_per_month_pie()
# 5
sales.plot_total_sales_per_month_step()
# 6
sales.plot_monthly_sales_histogram()
# 7
sales.plot_monthly_sales_boxplot()

# seaborn
# 1
sales.plot_total_sales_per_month_lineplot()
# 2
sales.plot_total_sales_per_month_scatterplot()
# 3
sales.plot_total_sales_per_month_barplot()
# 4
sales.plot_total_sales_per_month_boxplot()
# 5
sales.plot_total_sales_per_month_violinplot()

# task 7
print("**************task 7*****************")
# 1
sales.treat_errors()
print("task7-----1")

# 3
sales.rand_num('Chafetz Chaim')
print("task7-----3")
# 4
python_version = sales.get_python_version()
print(python_version)
print("task7-----4")
# 5
result1 = sales.process_parameters(10, "j=number", 3.14)
print("Result 1:", result1)
result2 = sales.process_parameters("Teilim=name", 20, "20=age", 25)
print("Result 2:", result2)
result3 = sales.process_parameters("d=key", 5, "o=value")
print("Result 3:", result3)
print("task7-----5")
# 6
sales.print_from_data()
print("task7-----6")
# 7
sales.read_on_time()
print("task7-----7")
