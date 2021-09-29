-- Question 1: Write a SQL query to list ALL the users (including user_id and name) with the
-- number of orders they have done including users who haven’t ordered anything yet.

select 
	users.user_id, 
	users.name, 
	count(orders.order_id) as orders 
from 
	users 
full join 
	orders 
on 
	users.user_id=orders.user_id
group by users.user_id;

-- Question 2: Write a SQL query to list the users (including user_id and name) that haven’t got
-- any orders.

select 
	users.user_id, 
	users.name, 
	count(orders.order_id) as orders 
from 
	users 
full join 
	orders 
on 
	users.user_id=orders.user_id
group by users.user_id
having count(orders.order_id) = 0;


-- Question 3: Write a SQL query to list the users that have orders greater than £100. Include
-- user_id, name, and the total number of orders they have done including those less than £100.

select 
	users.user_id,
	users.name,
	count(orders.order_id) total_orders
from users 
right join 
	(select 
	 	distinct user_id
	 from orders 
	 where amount > 100) as users_with_orders_gt_100
on users_with_orders_gt_100.user_id = users.user_id
left join 
	orders
	on orders.user_id=users.user_id
group by users.user_id;
