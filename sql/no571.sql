-- 571. Find Median Given Frequency of Numbers

-- The Numbers table keeps the value of number and its frequency.

-- +----------+-------------+
-- |  Number  |  Frequency  |
-- +----------+-------------|
-- |  0       |  7          |
-- |  1       |  1          |
-- |  2       |  3          |
-- |  3       |  1          |
-- +----------+-------------+
-- In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.

-- +--------+
-- | median |
-- +--------|
-- | 0.0000 |
-- +--------+
-- Write a query to find the median of all numbers and name the result as median.

select avg(number) as median from (
select 
number,frequency,
@st_range:=@end_range+1 as st_range,
@end_range:=@st_range+frequency-1 as end_range,
c.total_sum
from numbers a, (select @st_range:=0,@end_range:=0) b, (select sum(frequency) as total_sum from numbers )c
order by number
)a 
where (floor((total_sum+1)/2)>=st_range and floor((total_sum+1)/2)<=end_range) or 
(floor((total_sum+2)/2)>=st_range and floor((total_sum+2)/2)<=end_range) 
;

