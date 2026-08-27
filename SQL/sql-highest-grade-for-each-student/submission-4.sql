-- Write your query below
SELECT DISTINCT ON (student_id) student_id, exam_id, score
FROM exam_results
GROUP BY student_id, score, exam_id
ORDER BY student_id ASC, score DESC, exam_id ASC;