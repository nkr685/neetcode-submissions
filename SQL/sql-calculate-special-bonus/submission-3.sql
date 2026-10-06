-- Write your query below
SELECT * FROM (
    SELECT employee_id, 0 AS bonus FROM employees
    WHERE NOT MOD(employee_id, 2) = 1 OR name LIKE 'M%'
    UNION
    SELECT employee_id, salary AS bonus FROM employees
    WHERE MOD(employee_id, 2) = 1 AND name NOT LIKE 'M%'
) 
ORDER BY employee_id ASC;