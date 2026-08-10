# Write your MySQL query statement below
select pt.product_name, sl.year, sl.price
from Sales sl
left join Product pt
on sl.product_id = pt.product_id 